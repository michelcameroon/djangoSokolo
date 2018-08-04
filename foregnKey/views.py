from django.shortcuts import render

# Create your views here.



from django.views.generic import (TemplateView, ListView)




from .models import Reporter, Article





#class IndexView(TemplateView):
#    template_name = 'index.html'


#class AuthorCreateView(CreateView):
#    model = Author
#    template_name = 'my-author-create.html'
#    form_class = AuthorForm
#    success_url = '/my-books'



class ReporterListView(ListView):
    model = Reporter
    template_name = 'reporter_list.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


