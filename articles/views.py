from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article
from .forms import ArticleForm



def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("query")  # Changed from "q" to "query" to match the form

    article_obj = None
    if query is not None and query.strip():
        try:
            # Try to search by ID first, then by title
            if query.isdigit():
                article_obj = Article.objects.get(id=int(query))
            else:
                # Search by title containing the query
                articles = Article.objects.filter(title__icontains=query)
                if articles.exists():
                    article_obj = articles.first()
        except Article.DoesNotExist:
            article_obj = None

    context = {
        'object': article_obj,
        'query': query
    }
    return render(request, "articles/search.html", context=context)


# Create your views here.
@login_required
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'Article created successfully!')
            return redirect('article_detail', id=article.id)
    else:
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = Article.objects.get(id=id)
        except Article.DoesNotExist:
            article_obj = None

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)