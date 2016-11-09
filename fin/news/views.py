from django.shortcuts import render_to_response
from news.models import Blog,Tag,Author
from django.http import Http404
from django.http import HttpResponseRedirect
from django.template import RequestContext
## from news.forms import NewsForm,TagForm





# Create your views here.

def news_list(request):
    username=request.session.get('username',)
    news = Blog.objects.all()
    tags = Tag.objects.all()
    return render_to_response("new_list.html", {"username":username,"news": news,"tags":tags})


def news_show(request, id=''):
    username=request.session.get('username',)
    try:
        new = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("new_show.html", {"new": new,"username":username})


def news_filter(request, id=''):
    username=request.session.get('username',)
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    news = tag.blog_set.all()
    return render_to_response("new_filter.html",
        {"news": news, "tag": tag, "tags": tags,"username":username})
