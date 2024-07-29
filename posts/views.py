from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from pytils.translit import slugify
from .models import Post


# Create your views here.


class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostCreateView(generic.CreateView):
    model = Post
    fields = ('title', 'text', 'preview', 'is_published',)
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        if form.is_valid():
            form.instance.slug = slugify(form.instance.title)
            form.save()
            return super().form_valid(form)


class PostDetailView(generic.DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj_ = super().get_object(queryset)
        obj_.views_count += 1
        obj_.save()
        return obj_


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ('title', 'text', 'preview', 'is_published',)

    # def get_success_url(self) -> str:
    #     return reverse('posts:post_detail', kwargs={'pk': self.object.pk})
    def get_success_url(self) -> str:
        return reverse('posts:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')
