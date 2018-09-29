from django.template import Context
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.http.response import HttpResponse,Http404
from django.template.loader import get_template
from django.contrib import auth
from personal.models import Article, Comments
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from personal.models import Article, Comments
from personal.forms import CommentForm
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, render_to_response, render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Count,Avg,Aggregate,IntegerField, F
import math


def template_three(request):
    return render(request, 'login.html')


class articles(View):
    def get(self, request):
        articles = Article.objects.annotate(comments_count=Count('comments')).all()
        return render(request, 'articles.html', {'articles': articles})


def article(request, article_id=1):
    comment_form = CommentForm
    article = Article.objects.get(id=article_id)
    comments = Comments.objects.filter(comments_article_id=article_id)

    return render(request, 'article.html', {'form': comment_form, "comments": comments, "article": article})


def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
    return redirect('/articles/get/%s/' % article_id)


