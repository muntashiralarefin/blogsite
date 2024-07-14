from django.shortcuts import get_object_or_404, redirect, render

from .forms import blogForm
from .models import blog


# Create your views here.
def index(request):
  return render(request, 'blog/index.html')

def blog_list(request):
  blogs = blog.objects.all().order_by('-created_at')
  return render(request, 'blog/blog_list.html', {'blogs' : blogs})

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

def blog_delete(request, blog_id):
  #blog=None
  blogs = get_object_or_404(blog, pk=blog_id, user=request.user)
  if request.method == "POST":
    blogs.delete()
    return redirect('blog_list')
  return render(request, 'blog/blog_delete.html', {'blogs' : blogs})

