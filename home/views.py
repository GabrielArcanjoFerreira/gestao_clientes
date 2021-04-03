from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensagem'] = 'Olá, Mundo'
        return context

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')
    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')
    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')