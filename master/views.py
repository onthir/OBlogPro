from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
from .forms import ContactForm
from .models import *
from django.contrib.sitemaps import Sitemap
import time
from django.core.mail import send_mail
import sendgrid
import os
from sendgrid.helpers.mail import *
from .models import Category
# create mailing list
def create_mailing_list(name, email):
    ml = MailingList(full_name=name, email=email)
    ml.save()

# home display
def home(request):
    # get mailing list
    full_name = request.GET.get('name')
    email = request.GET.get('email')
    if full_name and email:
        # create mailing list
        create_mailing_list(full_name, email)
        msg = 'Successfully added ' + str(full_name) + ' to the mailing list'
        return render(request, 'master/success.html', {'msg': msg})

    # get the search item
    query = request.GET.get('q')
    if query:
        categories = Category.objects.all()
        short_list = Blog.objects.all().filter(publish=True)
        blogs = short_list.filter(Q(title__icontains=query) | Q(category__cat__icontains=query) | Q(date__icontains=query))
        ct = blogs.count()

        notf = Notification.objects.filter(read=False).count()
        
        context = {
            'categories': categories,
            'blogs': blogs,
            'query': query,
            'ct': ct,
            'notf': notf,
            
        }
        return render(request, 'master/search.html', context)
    # get all categories
    categories = Category.objects.all()

    # creating the featured content
    """
        Initial phase of the featured will contain the first i.e the latest post but the later version will have
        featured content based on some certain criterias.

    """
    featured = Blog.objects.all().filter(publish=True).order_by('-date')[0]
    slg = featured.slug
    # side blog posts
    sides = Blog.objects.all().filter(publish=True).exclude(slug=slg).order_by('-date')[:2]
    
    # all posts
    all_posts = Blog.objects.all().filter(publish=True).order_by('-date')
    # count of posts in each category
    catcount = Category.objects.annotate(num_blog=Count('blog'))

    notf = Notification.objects.filter(read=False).count()
    context = {
        'categories': categories,
        'featured': featured,
        'sides':sides,
        'all_posts': all_posts,
        'catcount': catcount,
        'notf': notf,
    }
    return render(request, 'master/index.html', context)

# details page
def details(request, slug):
    # get mailing list
    full_name = request.GET.get('name')
    email = request.GET.get('email')
    if full_name and email:
        # create mailing list
        create_mailing_list(full_name, email)
        msg = 'Successfully added ' + str(full_name) + ' to the mailing list'
        return render(request, 'master/success.html', {'msg': msg})
    else:
        print("Error")

    # blog detials
    categories = Category.objects.all()
    post = Blog.objects.get(slug=slug)
    post.views = post.views + 1
    post.save()

    # recommended posts
    cat = post.category
    slg= post.slug

    notf = Notification.objects.filter(read=False).count()

    recommended = Blog.objects.filter(category=cat).filter(publish=True).exclude(slug=slg)[:5]
    context = {
        'post': post,
        'categories': categories,
        'recommended': recommended,
        'notf': notf
    }
    return render(request, 'master/details.html', context)  

# category filter
def filter(request, cat):
    # get mailing list
    full_name = request.GET.get('name')
    email = request.GET.get('email')
    if full_name and email:
        # create mailing list
        create_mailing_list(full_name, email)
        msg = 'Successfully added ' + str(full_name) + ' to the mailing list'
        return render(request, 'master/success.html', {'msg': msg})
    else:
        print("Error")

    categories = Category.objects.all()
    cate = Category.objects.get(cat=cat)
    posts = Blog.objects.filter(category=cate).filter(publish=True).order_by('-date')

    notf = Notification.objects.filter(read=False).count()
    context = {
        'posts': posts,
        'categories': categories,
        'cate': cate,
        'notf': notf,
    }
    return render(request, 'master/filter.html', context)

# archive
def archive(request, date):
    posts = Blog.objects.filter(date__year=date).filter(publish=True).order_by('date')
    categories = Category.objects.all()

    notf = Notification.objects.filter(read=False).count()
    context = {
        'posts': posts,
        'date': date,
        'categories': categories,
        'notf': notf,
    }
    return render(request, 'master/archive.html', context)
# send email


def contact(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            data = form.save()
            # also add to the notificaiton to be read by the admin
            formatted = data.email
            formatted2 = data.message
            final = str(formatted) + "\n\n-->" + str(data.message)
            Notification.objects.create(head=data.full_name, content=final)
            return render(request, 'master/thankyou.html', {'categories' : categories, 'data': data})
    else:
        form = ContactForm()
    
    return render(request, 'master/contact.html', {'form': form})


def admin_panel(request):
    if request.user.is_superuser:
        categories = Category.objects.all()
        notifications = Notification.objects.all()
        unread = Notification.objects.filter(read=False)
        read = Notification.objects.filter(read=True)
        contacts = Contact.objects.all()
        # notification count
        notf = Notification.objects.all().count()
        notfu = unread.count()
        notfr = read.count()

        # user message count
        userc = contacts.count()

        # top posts
        posts = Blog.objects.all().order_by("-views")[:5]
        pps = Blog.objects.all().order_by("views")[:5]
        recents = Blog.objects.all().order_by("-date")[:5]

        # drafts 
        drafts = Blog.objects.filter(publish=False)
        context = {
            'categories': categories,
            'notififcations': notifications,
            'unread': unread,
            'read': read,
            'contacts': contacts,
            'notf': notf,
            'notfu': notfu,
            'notfr': notfr,
            'userc': userc,
            'posts': posts,
            'pps': pps,
            'recents': recents,
            'drafts': drafts,
        }
        return render(request, 'master/adminpanel.html', context)
    else:
        return redirect("master:home")
    
def read_notification(request, id):
    if request.user.is_superuser:
        notf = Notification.objects.get(id=id)
        if not notf.read:
            notf.read = True
        notf.save()
        return redirect("master:panel")
    else:
        return redirect("master:home")

def remove_message(request, id):
    if request.user.is_superuser:
        msg = Contact.objects.get(id=id)
        msg.delete()
        return redirect("master:panel")
    else:
        return redirect("master:home")
def remove_notf(request, id):
    if request.user.is_superuser:
        nt = Notification.objects.get(id=id)
        nt.delete()
        return redirect("master:panel")
    else:
        return redirect("master:home")

# sitemap
class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.date
def google_verification(request):
    return render(request, 'master/google1178e9883bf5717c.html')