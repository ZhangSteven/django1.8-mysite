from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Book
from .forms import ContactForm

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



def search3(request):
	# An improved search view, where it can:
	# 1. Serve the search form if parameter 'q' is not there,
	# 2. Serve the search form with custom error messages if 'q' is empty,
	# 3. Serve the search result
	
	errors = []	# instead of using a Boolean, using a message list
	if 'q' in request.GET:
		q = request.GET['q']
		if q == '':
			errors.append('Search query cannot be empty.')
		elif len(q) > 20:
			errors.append('Search query must be less than 20 characters')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_result.html', {'books':books, 'query':q})

	return render(request, 'search_form3.html', {'errors': errors})



def contact(request):
	if request.method == 'GET':
		# give some default values to the form fields
		form = ContactForm(
				initial={'subject':'What a lovely site!'}
			)
		return render(request, 'contact_form.html', {'form':form})
		
	elif request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# do some processing here
			# cd = form.cleaned_data
			# send_mail(cd ...)
			return HttpResponseRedirect('/contact/thanks/')
		else:
			return HttpResponse('<html><body><h1>Ooops, something is wrong</h1></body></html>')
	else:
		raise Http404()



def contact_thankyou(request):
	return render(request, 'contact_thankyou.html', {})