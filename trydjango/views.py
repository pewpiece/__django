from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article
import random
from django.shortcuts import render




def home_view(request, *args, **kwargs):
    
    name = "Justin"
    random_id = random.randint(1,4)

    # from the database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    return render(request, "home_view.html", context)