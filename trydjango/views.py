from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article
import random




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
        "id": article_obj.id,
        "content": article_obj.content,
    }


    # Django templates

    HTML_STRING = render_to_string("home_view.html", context=context)
   
   
    # HTML_STRING = f"""
    # <h1>{title} (id: {id})</h1>
    # <p>{content}!</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)