from django.db.models import Count
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import *

# https://docs.djangoproject.com/en/1.11/topics/signals/
from django.core.signals import request_finished
from django.dispatch import receiver

# https://django-mssql.readthedocs.io/en/latest/usage.html
# https://dev.mysql.com/doc/connector-net/en/connector-net-tutorials-stored-procedures.html
from django.db import connection

# https://docs.djangoproject.com/en/1.11/topics/db/transactions/
from django.db import transaction


# Create your views here.
def index(request):
    title = "My Blog Page"

    menu = get_menu()

    # slider
    link = 'http://localhost:8000/'
    slide = get_slider()



    # feature
    features = get_feature()
    # ---------------------------------------



    # post
    post = get_post()
    # prev next ?????
    # recent post new get_recent or this
    # ---------------------------------------


    # user
    user = get_user()
    # ---------------------------------------


    # categories
    category = get_category()
    # ---------------------------------------


    # tags
    tag = get_tag()
    # ---------------------------------------


    # ref: http://books.agiliq.com/projects/django-orm-cookbook/en/latest/database_view.html
    #view -->  python manage.py shell
    #view_user_table = Users_View.objects.all().values()

    return render_to_response('main/index.html', locals())


def detail(request, content_id):
    tag=get_tag()
    content = get_object_or_404(Content, pk=content_id)

    return render_to_response('main/detail.html', locals())


def get_menu():
    menu = Menu.objects.filter(parent=None).order_by("order")
    return menu


def get_slider():
    slide = Slider.objects.all().order_by("order")

    return slide


def get_feature():
    # last 5 feature
    # features = Feature.objects.order_by('-create_at')[:5]
    features = Feature.objects.all().order_by('created')

    return features


def get_post():
    post = Post.objects.all().order_by('published')[:5]

    return post


def get_post_detail():
    # template tarafından kullanılırken {{ post.content|safe }} html olarak yazar
    pass


def get_user():
    user = Author.objects.all().get()  # order_by if multiple users

    return user


def get_category():
    category = Category.objects.all()

    return category

# atomicity transaction update tag and view tag
def get_tag():
    tag = Tag.objects.all()

    with transaction.atomic():
        Tag.objects.filter(pk=1).update(title='python3')

    return tag


# Django trigger methods/ signals
# https://docs.djangoproject.com/en/1.11/topics/signals/
# The 'Request Finished' commandline is printed when the connection is established.
@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


# https://docs.djangoproject.com/en/dev/topics/db/sql/#django.db.models.CursorWrapper.callproc
with connection.cursor() as cursor:
    result = cursor.callproc('train_proc', ['ali'])
    print(result)