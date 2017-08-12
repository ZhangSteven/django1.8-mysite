# My first view

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from datetime import datetime, timedelta



def hello(request):
	return HttpResponse('<h1>Hello, World</h1>')



def current_datetime(request):
	dt = datetime.now()
	html = '<html><body><h1>It is now {0}</h1></body></html>'.format(dt)
	return HttpResponse(html)



def current_datetime2(request):
	"""
	Serve the same purpose as current_datetime(), but it uses template
	rendering instead of generating HTML text inside the function.
	"""
	dt = datetime.now()
	t = get_template('current_datetime.html')
	ctx = Context({'current_date':dt})	# a variable 'current_date' is needed
										# by the template, so the key name is
										# 'current_date'
	html = t.render(ctx)
	return HttpResponse(html)



def current_datetime3(request):
	"""
	Use the shortcut render() function to do template rendering.
	"""
	dt = datetime.now()
	return render(request, 'current_datetime.html',
					{'current_date':dt})



def current_datetime4(request):
	"""
	Use the shortcut render() function to do template rendering.
	"""
	dt = datetime.now()
	return render(request, 'current_datetime_inherit.html',
					{'current_date':dt})



def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except:
		raise Http404()

	dt = datetime.now()
	# assert False
	html = '<html><body><h1>It is now {0}</h1></body></html>' \
			.format(dt+timedelta(hours=offset))
	return HttpResponse(html)



def hours_ahead2(request, offset):
	"""
	Use template rendering to display the page.
	"""
	try:
		offset = int(offset)
	except:
		raise Http404()

	dt = datetime.now()
	# assert False
	return render(request, 'hours_ahead.html',
				{'hours':offset, 'future_date':dt+timedelta(hours=offset)})


		
