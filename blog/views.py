from django.shortcuts import render
from django.views.generic import ListView,DetailView # CBV로 페이지 만들기 위해 import 
from .models import Post, Category


'''
CBV로 페이지 만들기 
'''

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html' # 지정하지 않으면 자동으로 인식
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context
    
    def category_page(request, slug) :
        if slug == 'no_category' :
            category = '미분류'
            post_list = Post.objects.filter(category=None)
        else :
            category = Category.objects.get(slug=slug)
            post_list = Post.objects.filter(category=category)

        category = Category.objects.get(slug=slug)

        return render(
            request,
            'blog/post_list.html',
            {
                'post_list': post_list,
                'categories': Category.objects.all(),
                'no_category_post_count': Post.objects.filter(category=None).count(),
                'category' : category,
            }
        )
    
    

class PostDetail(DetailView) :
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

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