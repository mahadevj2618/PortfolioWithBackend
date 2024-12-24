from django.shortcuts import render
from .models import Project, BlogPost
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    blog_posts = BlogPost.objects.order_by('-date_posted')[:3]
    return render(request, 'portfolio/home.html', {'projects': projects, 'blog_posts': blog_posts})

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'portfolio/blog.html', {'blog_posts': blog_posts})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolio/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
