from django.shortcuts import render
from .models import Post, Comment, Reply
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    num_posts = Post.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    num_users = User.objects.all().count()
    request.session['num_visits'] = num_visits+1
    context={'num_posts':num_posts , 'num_visits' : num_visits , 'num_users' : num_users ,}
    return render(request, 'index.html' , context )


class PostlistView(generic.ListView):
    model = Post
    paginate_by = 10
    ordering = ['-date']

class PostDetailView(generic.DetailView):
    model = Post


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'body',]
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title', 'body',]


class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('posts')



class CommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = Comment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.post=get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})





class ReplyCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = Reply
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(ReplyCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['comment'] = get_object_or_404(Comment, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.comment=get_object_or_404(Comment, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(ReplyCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('comment-detail', kwargs={'pk': self.kwargs['pk'],})




class CommentDetailView(LoginRequiredMixin,generic.DetailView):
    model = Comment