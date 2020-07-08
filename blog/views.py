from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(created_date__icontains=query) |
            Q(published_date__icontains=query)
        )
    paginator = Paginator(posts, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    paginator = Paginator(posts, 5)  # Show 5 contacts per page

    return render(request, "post.html", {'posts': posts})
