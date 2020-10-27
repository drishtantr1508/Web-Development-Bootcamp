from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from blog.forms import PostForm,CommentForm
from blog.models import Post, Comment
from django.utils import timezone
# Create your views here.
class AboutView(TemplateView):
    template_name='blog/about.html'
class PostListView(ListView):
    model=Post #contextname is post_list
    template_name='blog/post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html'
    def get_context_data(self, **kwargs):

        context = super(PostDetailView, self).get_context_data(**kwargs)
        #context['post'] = Post.objects.all()
        context['comments'] = Comment.objects.all()

        # And so on for more models
        return context

class CreatePostView(LoginRequiredMixin,CreateView):
    model=Post
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model=Post
class UpdatePostView(LoginRequiredMixin,UpdateView):
    model=Post
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model=Post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url= reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_draft_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

######################################
######################################
             #COMMENT#
######################################
######################################

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)


@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)#post is an instance of Post class and we can use methods attached to it.
    post.publish()
    return redirect('post_detail',pk=pk)
