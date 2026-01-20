from django.shortcuts import render,redirect 
from .models import Post 
from .forms import PostForm 
# Create your views here.

def home(request):
	post = Post.objects.all()
	return render(request,'index.html',{"posts" : post})

def create_post(request):
	form = PostForm(request.POST or None)
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request,'create.html',{'form' : form})


def edit_post(request,post_id):
	posts = Post.objects.get(id=post_id)
	if request.method != "POST":
		form = PostForm(instance=posts)
	else:
		form = PostForm(instance=posts,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
	    'form' : form,
	    'posts' : posts 
	}
	return render(request,'edit.html',context)

def delete_post(request,post_id=None):
	post = Post.objects.get(id=post_id)
	post.delete()
	return redirect('/')

