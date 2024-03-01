from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .forms import UserRastirationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.
from django.views.generic import CreateView
from post.models import Article

from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string


def user_transaction_email(user,subject,template):
     
        message=render_to_string(template, {
        'user' : user,
    
        })
        send_mail=EmailMultiAlternatives(subject, '',  to= [user.email])
        send_mail.attach_alternative(message, 'text/html')
        send_mail.send()



class UsercreationView(CreateView):
    form_class=UserRastirationForm
    template_name='register.html'
    success_url=reverse_lazy('register')
    def form_valid(self, form):
        user=form.save()
        # login( self.request, user)
        messages.success(
            self.request,
            f'Your ragistartion request successful please confirm your registration form your email'
        )

        user_transaction_email(self.request.user, "registration Massage","login_email.html" )
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        messages.success(
            self.request,
            f'login successfull'
        )
        return reverse_lazy('profile')

def user_logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))

def profile(request):
    data=Article.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data':data})