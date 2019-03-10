from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from .models import Post

post_list = ListView.as_view(model=Post)


def goldmembership_guide(request):
    return render(request, 'blog/goldmembership_guide.html', {} )

@login_required
@permission_required('blog.can_view_goldpage', login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

# post_detail = DetailView.as_view(model=Post)
