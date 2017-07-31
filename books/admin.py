from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher



class AuthorAdmin(admin.ModelAdmin):
	# display the below attributes for a Book object
	list_display = ('first_name', 'last_name', 'email')

	# add a search box
	search_fields = ('first_name', 'last_name')



class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date', )
	date_hierarchy = 'publication_date'

	# display the newest published book first.
	ordering = ('-publication_date',)

	# Control what attributes to let a user input via admin page.
	# Below prevents a user from inputing publication_date, in that
	# case, the publication_date will be populated by some other process. 
	fields = ('title', 'authors', 'publisher')



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)