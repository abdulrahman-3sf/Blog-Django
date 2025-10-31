from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Abdulrahman',
        'title': 'Blog Post 1',
        'content': 'This is my first post!',
        'date_posted': 'October 29, 2025'
    },
    {
        'author': 'Khaled',
        'title': 'Blog Post 2',
        'content': 'I\'m trying this blog webiste!',
        'date_posted': 'October 31, 2025'
    },
]

def home(request):
    context = {
        'posts': posts,
        'title': 'HOMEEEE'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Blog'})