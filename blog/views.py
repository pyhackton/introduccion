from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import View

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_list.html', context)

