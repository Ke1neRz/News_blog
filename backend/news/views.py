from django.shortcuts import render

from news.models import Article


def show_news_view(request):
    all_news = Article.objects.all()
    
    context = {
        'tetle': 'Новости',
        'all_news': all_news,
    }
    return render(request, "news/news.html", context)

def news_detail_view(request, news_id):
    news = Article.objects.get(id=news_id)

    context = {
        'tetle': 'Новости',
        'news': news,
    }
    return render(request, "news/news_detail.html", context)
