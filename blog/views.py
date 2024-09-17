import datetime

from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.services import send_post_email


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "post", "image",)
    success_url = reverse_lazy('blog:blog_list',)

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.slug = f'{slugify(self.object.title)} {datetime.datetime.now()}'
            self.object.save()

        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "post", "image")
    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.slug = f'{slugify(self.object.title)} {datetime.datetime.now()}'
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        # return reverse('blog:blog_detail', args=[self.kwargs.get('slug')])
        return reverse('blog:blog_detail', args=[self.object.slug])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        # if self.object.views_count >= 20:
        #     obj = self.object
        #     send_post_email(obj)
        return self.object

