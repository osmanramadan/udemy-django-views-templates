from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BlogForm
from .models import Blog
from django.http import Http404 , HttpResponse




# Create your views here.



def list(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    
    return render(request, 'blog/list.html',context)



@staff_member_required
def create(request):
    form = BlogForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogForm()
        return redirect('blog')

    return render(request, 'blog/create.html', {'form': form})




def details(request,slug):
    
    r = Blog.objects.filter(slug=slug)
    if r.count() == 0:
       return HttpResponse("<h1>Blog Not Found</h1>")

    #obj= get_object_or_404(Blog,slug=slug)
    
    #obj = r.first()
    context = {"object":r}
    return render(request,"blog/details.html",context)



@staff_member_required
def update(request, slug):

    #obj = get_object_or_404(Blog,slug=slug)
    obj = Blog.objects.filter(slug=slug).first()

    if not obj:
        return redirect('/')

    form = BlogForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('blog')

    return render(request, 'blog/update.html', {'form': form,'object': obj})

@staff_member_required
def delete(request,slug):
    #obj = get_object_or_404(Blog,slug=slug)
    obj = Blog.objects.filter(slug=slug).first()
    if not obj:
        return redirect('/')

    if request.method == "POST":
        obj.delete()
        return redirect('blog')
    return render(request, 'blog/delete.html', {'object': obj})