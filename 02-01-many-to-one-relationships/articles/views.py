from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ArticleForm, CommentForm
from .models import Article, Comment


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글인지 알려면 게시글 먼저 조회
    article = Article.objects.get(pk=article_pk)
    # CommentForm을 활용한 댓글 생성
    comment_form = CommentForm(request.POST)
    # 유효성검사
    if comment_form.is_valid():
        # 외래키 데이터 넣으려면 댓글 인스턴스 필요
        # 댓글은 save() 호출이 완료되어야 반환
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 첫번째 방법 : 삭제 전 게시글 번호 저장하기
    # article_id = comment.article.pk # 첫번째
    # return redirect('articles:detail', article_id)
    comment.delete()
    
    # 두번째 방법 : url에서 가져오기
    return redirect('articles:detail', article_pk)