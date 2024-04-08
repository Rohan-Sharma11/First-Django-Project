from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.


posts = [
    {   'author': 'Rohan',
        'title': 'Python',
        'content': 'First Post Content',
        'date_posted': 'March 2004',
         
    },

       
    {   'author': 'Lakhi',
        'title': 'Biology',
        'content': 'Second Post Content',
        'date_posted': 'August 2005',
         
    }
]




# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

#def about(request):
    #return HttpResponse('<h1>Blog About</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})