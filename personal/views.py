from django.shortcuts import render, render_to_response, redirect
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
from django.shortcuts import redirect, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Count,Avg,Aggregate,IntegerField, F
import math

def template_three(request):
    return render_to_response('login.html')


class articles(View):
    def get(self, request):
        articles = Article.objects.annotate(comments_count=Count('comments')).all()
        return render_to_response('articles.html', {'articles': articles, 'username': auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike (request, article_id):
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


