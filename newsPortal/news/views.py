from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm

# Существующие представления

def news_list(request):
    """Представление для отображения списка новостей и статей."""
    articles = Article.objects.all()
    return render(request, 'news_list1.html', {'articles': articles})

def news_detail(request, article_id):
    """Представление для отображения деталей конкретной статьи или новости."""
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news_detail.html', {'article': article})

# Новые представления для создания, редактирования и удаления новостей и статей

class NewsCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'news'  # Устанавливаем тип "новость"
        return super().form_valid(form)

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'article'  # Устанавливаем тип "статья"
        return super().form_valid(form)

class NewsUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('news_list')
