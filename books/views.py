from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
	"""
	Use the shortcut render() function to do template rendering.
	"""
	return render(request, 'book_list.html',
					{'books':Book.objects.all()})



def search(request):
	# if the user has submitted a search form ('q in request.GET') and
	# the search query is non-empty (request.GET['q'] != '')
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		return render(request, 'search_result.html', {'books':books, 'query':q})
	else:
		return render(request, 'search_form.html', {'error': True})



def search_form(request):
	# display the search form
	return render(request, 'search_form.html', {'error': False})




def search2(request):
	# An improved search view, where it can:
	# 1. Serve the search form if parameter 'q' is not there,
	# 2. Serve the search form with an error if 'q' is empty,
	# 3. Serve the search result
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if q != '':
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_result.html', {'books':books, 'query':q})
		else:
			error = True

	return render(request, 'search_form.html', {'error': error})