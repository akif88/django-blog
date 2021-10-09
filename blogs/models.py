from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Users(models.Model):
    #user = models.ForeignKey(User)#admin user
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class Blog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    published = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    url = models.CharField(max_length=255)
    user_id = models.ForeignKey(Users)

    def __str__(self):
        return self.name


class Templates(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Pages(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    url = models.CharField(max_length=255)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    templates_id = models.ForeignKey(Templates, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey("self", null=True, blank=True)
    order = models.IntegerField(default=0)
    url = models.CharField(max_length=255)
    target = models.CharField(max_length=10, default="_self")
    page_id = models.ForeignKey(Pages)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=50)

    def __str__(self):
        return  self.title


class Images(models.Model):
    url = models.ImageField(upload_to='thumb')

    def __str__(self):
        return self.url.name



class Feature(models.Model):
    created = models.DateField(auto_now=True)
    category_id = models.ManyToManyField(Category)
    image_id = models.ManyToManyField(Images)

    def __str__(self):
        return str(self.category_id.get())

    def get_images(self):
        return self.image_id.get()


class Tag(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(default=None)
    content = RichTextField()

    def __str__(self):
        return self.title



class Slider(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    created = models.DateField(auto_now=True)
    order = models.IntegerField(default=1)
    category_id = models.ManyToManyField(Category)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Images)

    def __str__(self):
        return self.title

    def get_images(self):
        return self.image_id.url.name

    def get_category(self):
        ctr = Category.objects.filter(slider__category_id=self.category_id.get())
        return ctr.get()

    def get_content(self):
        return self.content_id.content


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(Users)

    def __str__(self):
        return self.username


class Author(models.Model):
    user_id = models.ForeignKey(Users)
    blog_id = models.ForeignKey(Blog)
    about = models.TextField(null=True, blank=True)
    image_id = models.ForeignKey(Images)

    def __str__(self):
        return self.user_id.firstname

    def get_images(self):
        return self.image_id.url.name


class Reader(models.Model):
    user_id = models.ForeignKey(Users)
    image_id = models.ForeignKey(Images)


class Post(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    published = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    content_id = models.ForeignKey(Content, default=1)
    category_id = models.ForeignKey(Category, default=1)
    blog_id = models.ForeignKey(Blog, default=1)
    tag = models.ManyToManyField(Tag, default=1)
    image_id = models.ForeignKey(Images, default=1)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True)
    content_id = models.ForeignKey(Content)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


    #def __str__(self):
    #return '{} -> {}'.format(self.user_name, self.post.title)


class IPLog(models.Model):
    ip_address = models.CharField(max_length=15)


class Hit(models.Model):
    post_id = models.ForeignKey(Post)
    ip_address_id = models.ForeignKey(IPLog, on_delete=models.CASCADE)

#for view tables
class Users_View(models.Model):

    class Meta:
        managed=False
        db_table="view_users"

