from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, BMIRecord
from django.urls import reverse_lazy
from .forms import BMIRecordForm

class HomePageView(TemplateView):
    template_name = 'apps/home.html'

class AboutPageView(TemplateView):
    template_name = 'apps/about.html'

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'apps/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'apps/blog_detail.html'

class BlogCreateView(CreateView):  
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'apps/blog_create.html'
    
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'apps/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'apps/blog_delete.html'
    success_url = reverse_lazy('blog')

class BMICalculatorView(CreateView):
    model = BMIRecord
    form_class = BMIRecordForm
    template_name = 'apps/bmi_calculator.html'

    def form_valid(self, form):
        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height'] / 100  
        bmi = weight / (height ** 2)
        form.instance.bmi = bmi

        if bmi < 18.5:
            bmi_category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            bmi_category = 'Normal weight'
        elif 25 <= bmi < 29.9:
            bmi_category = 'Overweight'
        else:
            bmi_category = 'Obesity'

        form.instance.bmi_category = bmi_category
        return super().form_valid(form)

class BMIRecordListView(ListView):
    model = BMIRecord
    context_object_name = 'bmi_records'
    template_name = 'apps/bmi_record_list.html'

class BMIRecordDetailView(DetailView):
    model = BMIRecord
    context_object_name = 'bmi_record'
    template_name = 'apps/bmi_record_detail.html'

class BMIRecordUpdateView(UpdateView):
    model = BMIRecord
    fields = ['weight', 'height']
    template_name = 'apps/bmi_record_update.html'

    def form_valid(self, form):
        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height'] / 100  
        bmi = weight / (height ** 2)
        form.instance.bmi = bmi

        if bmi < 18.5:
            bmi_category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            bmi_category = 'Normal weight'
        elif 25 <= bmi < 29.9:
            bmi_category = 'Overweight'
        else:
            bmi_category = 'Obesity'

        form.instance.bmi_category = bmi_category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bmi_record_list')

class BMIRecordDeleteView(DeleteView):
    model = BMIRecord
    template_name = 'apps/bmi_record_delete.html'
    success_url = reverse_lazy('bmi_record_list')