from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField



# Category model
class Category(models.Model):
    cat = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.URLField(max_length=1000)
    
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.cat

class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField()
    author = models.CharField(default='Bibek Bhandari', max_length=50)
    image = models.URLField(max_length=1000)
    slug = models.SlugField(max_length=500, unique=True)
    views = models.IntegerField()
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Question.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    # for sitemaps
    def get_absolute_url(self):
        return '/blog/%s' %self.slug

class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.full_name
    
    def __unicode__(self):
        return self.full_name
    
class Notification(models.Model):
    head = models.CharField(max_length=150)
    content =  models.TextField(max_length=200)
    received = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.head


# table for mailing list
class MailingList(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name