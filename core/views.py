from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'core/home.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials. Please try again")
    return render(request, 'core/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully")
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'core/edit_post.html', {'form':form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You do not have permission to delete this post.")
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')
    
    return render(request, 'core/confirm_delete.html', {'post': post})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'core/post_detail.html', {'post': post, 'comments': comments, 'form': form})



@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        messages.error(request, "You do not have permission to edit this comment.")
        return redirect('post_detail', post_id=comment.post.id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully")
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'core/edit_comment.html', {'form':form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('post_detail', post_id=comment.post.id)

    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('post_detail', post_id=post_id)
    
    return render(request, 'core/delete_comment.html', {'comment': comment})