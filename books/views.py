from django.shortcuts import render
from django.views import View
from .models import Books
# Create your views here.


class ListView(View):
    def get(self, request):
        book = Books.objects.all()
        context = {
            'book': book
        }
        return render(request, 'book_list.html', context=context)
