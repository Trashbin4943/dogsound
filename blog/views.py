from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from .forms import PostForm, SignupForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def create_post(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_list')
    else:
        form=PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_list(request):
    posts = Blog.objects.all()
    return render (request, 'post_list.html', {'posts': posts})

def view_post(request, pk=int):
    post=get_object_or_404(Blog,pk=pk)
    comments=post.comments.all()

    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form=CommentForm()

    return render (request, 'view_post.html', {'post': post, 'comments': comments, 'form':form})


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post= get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, {'post': post})

def delete_comment(request,comment_id):
    comment= get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST" and request.user == comment.author:
        post_pk= comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    return redirect('post_detail', pk=comment.post.pk)
    

def signup_view(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('post_list')
    else:
        form=AuthenticationForm()
    return render(request, 'login.html', {'form':form})