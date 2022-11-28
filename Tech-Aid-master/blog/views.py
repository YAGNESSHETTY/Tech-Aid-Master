from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import postblog
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    Post={
        "posts":postblog.objects.all()
    }
    return render(request,'blog/home.html',context=Post);

class postblogListView(ListView):
    model = postblog
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by=10
    
    

class userpostblogListView(ListView):
    model = postblog
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by=10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return postblog.objects.filter(user=user).order_by('-date_posted')

class postblogDetailView(DetailView):
    model = postblog
    template_name = "blog/post_content.html"
    context_object_name = "post"

class postblogCreateView(LoginRequiredMixin, CreateView):
    model = postblog
    template_name = "blog/post_create.html"
    fields = (
        'title',
        'content',
    )
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class postblogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = postblog
    template_name = "blog/post_create.html"
    fields = (
        'title',
        'content',
    )
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.user:
            return True
        return False


class postblogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = postblog
    template_name = "blog/post_delete.html"
    context_object_name = "post"
    success_url="/"
    fields = (
        'title',
        'content',
    )
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.user:
            return True
        return False


def about(request):
    return render(request,'blog/about.html');