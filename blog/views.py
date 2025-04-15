from django.shortcuts import render
from django.views.generic import ListView,DetailView # CBV로 페이지 만들기 위해 import 
from .models import Post


'''
CBV로 페이지 만들기 
'''

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html' # 지정하지 않으면 자동으로 인식
    ordering = '-pk'

class PostDetail(DetailView) :
    model = Post
    template_name = 'blog/post_detail.html'

'''
FBV로 페이지 만들기 
'''
# def index(request) :
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )


def single_post_page(request, pk) :
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )