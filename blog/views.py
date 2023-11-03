from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        for obj in queryset:
            if len(str(obj.image)) < 1:
                obj.is_image = False
            else:
                pass
        queryset = queryset.filter(is_image=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image', 'slug')

    def get_success_url(self):
        return reverse('blog:blog_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_details', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog:blog_list')
