from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
	"""
	Use the shortcut render() function to do template rendering.
	"""
	return render(request, 'book_list.html',
					{'books':Book.objects.all()})