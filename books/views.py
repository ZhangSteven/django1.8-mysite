from django.shortcuts import render

# Create your views here.
def book_list(request):
	"""
	Use the shortcut render() function to do template rendering.
	"""
	dt = datetime.now()
	return render(request, 'book_list.html',
					{'current_date':dt})