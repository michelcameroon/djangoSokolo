from django.shortcuts import render

# Create your views here.



from django.views.generic import (TemplateView, ListView)




from .models import Table1





#class IndexView(TemplateView):
#    template_name = 'index.html'


#class AuthorCreateView(CreateView):
#    model = Author
#    template_name = 'my-author-create.html'
#    form_class = AuthorForm
#    success_url = '/my-books'



class Table1ListView(ListView):
    model = Table1
    template_name = 'table1_list.html'


