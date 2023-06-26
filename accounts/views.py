from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CreateUserForm, ProfileUpdateForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    
    return render(request, 'registration/signup.html', {'form':form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('profile')
    fields = ['username','first_name','last_name','email']

    def get_object(self):
        return self.request.user


class PasswordUpdateView(LoginRequiredMixin , PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_update.html'
    success_url = reverse_lazy('index')

@login_required
def ProfileView(request):
    user_posts = Post.objects.filter(user = request.user).count()
    return render(request, 'accounts/profile.html', { 'user_posts' : user_posts})