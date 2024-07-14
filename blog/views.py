from django.shortcuts import get_object_or_404, redirect, render

from .forms import blogForm, UserRegistrationForm
from .models import blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
  return render(request, 'blog/index.html')

def blog_list(request):
  blogs = blog.objects.all().order_by('-created_at')
  return render(request, 'blog/blog_list.html', {'blogs' : blogs})

@login_required
def blog_create(request):
  if request.method == "POST":
    form = blogForm(request.POST, request.FILES)
    if form.is_valid():
      blog = form.save(commit=False)
      blog.user = request.user
      blog.save()
      return redirect('blog_list')
  else:
    form = blogForm()
  return render(request, 'blog/blog_create.html', {'form': form})

@login_required
def blog_edit(request, blog_id):
  blogs = get_object_or_404(blog, pk=blog_id, user=request.user)
  if request.method == "POST":
    form = blogForm(request.POST, request.FILES, instance=blogs)
    if form.is_valid():
      blogs = form.save(commit=False)
      blog.user = request.user
      blogs.save()
      return redirect('blog_list')
  else:
    form = blogForm(instance=blogs)
  return render(request, 'blog/blog_create.html', {'form': form})

@login_required
def blog_delete(request, blog_id):
  #blog=None
  blogs = get_object_or_404(blog, pk=blog_id, user=request.user)
  if request.method == "POST":
    blogs.delete()
    return redirect('blog_list')
  return render(request, 'blog/blog_delete.html', {'blogs' : blogs})

def register(request):
  if request.method == "POST":
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('blog_list')
  else:
    form = UserRegistrationForm()
  return render(request, 'registration/register.html', {'form': form})