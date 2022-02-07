import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'count':1},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'count':2},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'count':3} ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'count':4},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'count':5},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'count':6} ]

    other_pages = [
    {'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/',
    'count':7},
    {'title':'Flask',
    'url':'http://flask.pocoo.org',
    'count':8} ]

    cats = [
        {'name': 'Python',
        'views': 128,
        'likes': 64,
        'pages': python_pages},
        {'name': 'Django',
        'views': 64,
        'likes': 32,
        'pages': django_pages},
        {'name': 'Other Frameworks',
        'views': 32,
        'likes': 16,
        'pages': other_pages} ]

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat in cats:
        # for cat_name, cat_views, cat_likes, cat_pages in cat.items():
        c = add_cat(cat['name'],cat['views'],cat['likes'])
        for p in cat['pages']:
            add_page(c, p['title'], p['url'], p['count'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate() 