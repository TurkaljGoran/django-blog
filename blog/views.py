from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class BlogHome(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title']  = 'Home',
        context['date_shape'] = 'l, F dS, Y'

        return context
    


class AuthorBlogHome(ListView):
    """
    Displays only the posts of a single author, when user clicks an author link

    """

    model = Post
    template_name = 'blog/home.html'
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Any]:


        author_id = self.kwargs.get('author_id')
        
       
        return super().get_queryset().filter(author=author_id).order_by('-published_at')
       

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title']  = 'Home',
        context['date_shape'] = 'l, F dS, Y'

        return context





    
class BlogAbout(View):

    def get(self, request):

        return render(request, 'blog/about.html', {'title': 'About'})



#-------------CRUD OPERATIONS FOR THE BLOG POSTS-------------------------#


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['title', 'content']
   
    def form_valid(self, form):
        #set the author field to the currently logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/detail.html'




class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'content']

    #Ensure only author can edit a particular post
    def test_func(self):
       post = self.get_object()
       return self.request.user == post.author






class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name='blog/delete.html'
    success_url= reverse_lazy('blog:home')

    
    #Ensure only author can delete a particular post
    def test_func(self):
       post = self.get_object()
       return self.request.user == post.author


