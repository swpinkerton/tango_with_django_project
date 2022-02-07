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
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/'} ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'} ]

    other_pages = [
    {'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/'},
    {'title':'Flask',
    'url':'http://flask.pocoo.org'} ]

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
        print (cat)
        # for cat_name, cat_views, cat_likes, cat_pages in cat.items():
        c = add_cat(cat['name'],cat['views'],cat['likes'])
        for p in cat['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
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

    #     cats = [
    #     {'name': 'Python',
    #         'views': 'pages',
    #         'likes': python_pages,},
    #     {'name': 'Django',
    #         'views': 'pages',
    #         'likes': django_pages,},
    #     {'name': 'Other Frameworks',
    #         'views': 'pages',
    #         'likes': other_pages,} ]

    # # If you want to add more categories or pages,
    # # add them to the dictionaries above.

    # # The code below goes through the cats dictionary, then adds each category,
    # # and then adds all the associated pages for that category.
    # for cat in cats:
    #     for (cat_name, cat_views, cat_likes) in catt.items():
    #         c = add_cat(cat_name,cat_views,cat_likes)
    #         for p in cat_likes:
    #             add_page(c, p['title'], p['url'])

    # # Print out the categories we have added.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print(f'- {c}: {p}')



    # cats = {'Python': {'pages': python_pages},
    #         'Django': {'pages': django_pages},
    #         'Other Frameworks': {'pages': other_pages} }

    # # If you want to add more categories or pages,
    # # add them to the dictionaries above.

    # # The code below goes through the cats dictionary, then adds each category,
    # # and then adds all the associated pages for that category.
    # for cat, cat_data in cats.items():
    #     c = add_cat(cat)
    #     for p in cat_data['pages']:
    #         add_page(c, p['title'], p['url'])

    # # Print out the categories we have added.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print(f'- {c}: {p}')


    # for cat in cats:
    #     for (cat_name, cat_stuff) in cat.items():
    #         c = add_cat(cat_name,cat_stuff['views'],cat_stuff['likes'])
    #         for p in cat_stuff['likes']:
    #             add_page(c, p['title'], p['url'])