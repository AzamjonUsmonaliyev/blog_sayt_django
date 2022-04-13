from dataclasses import fields
from pickle import OBJ
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleUpdateView(LoginRequiredMixin , UserPassesTestMixin ,UpdateView):
    model = Article
    fields = ['title','summary', 'body','photo',]
    template_name = 'article_edit.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin , UserPassesTestMixin ,CreateView):
    model = Article
    fields = ['title','summary', 'body','photo',]
    template_name = 'article_new.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # new
        return self.request.user.is_superuser 