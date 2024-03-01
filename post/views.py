from django.shortcuts import render, redirect
from django.urls import reverse
from .import forms
from .import models
from django.views.generic import CreateView, DeleteView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

from .forms import ArticleForm






class CreatePostView(CreateView):
    model = forms.Article
    form_class = ArticleForm
    template_name = "post.html"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            return super().form_valid(form)
        except Exception as e:
            print(e)  # Print out any exceptions for debugging
            return self.form_invalid(form)
class UserDetailView(DetailView):
    model = models.Article
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        form = forms.RatingForm(data=request.POST)
        article = self.get_object(self.get_queryset())
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.article = article  # Assign the current article to the rating
            new_rating.save()
            return redirect('home')  # Redirect to a success URL
        else:
            # Handle invalid form data
            # You can render the form again with errors or return an error response
            return redirect(reverse('post', kwargs={'pk': article.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        comments = article.ratings.all()
        form = forms.RatingForm()  # Rating form for the template
        context['ratings'] = comments
        context['rating_form'] = form
       
        return context




#edit podt view using classbase view
@method_decorator(login_required, name='dispatch')
class EditpostView(UpdateView):
    model = models.Article
    form_class = forms.ArticleForm
    template_name = 'post.html'
    pk_url_kwarg = 'id'  # Correct attribute name
    success_url = reverse_lazy('profile')

def deleteView(request,id):
    data=models.Article.objects.get(pk=id)
    data.delete()
    return redirect('home_page')

# class base deleteView
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Article
    template_name='delete.html'
    success_url =reverse_lazy('profile')
    pk_url_kwarg= 'id'