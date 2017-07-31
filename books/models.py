from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	# Create a string representation of the Publisher object
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

		

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	# email = models.EmailField()
	email = models.EmailField(blank=True)

	# Create a string representation of the Author object
	def __str__(self):
		return '{0} {1}'.format(self.last_name, self.first_name)



class Book(models.Model):
	title = models.CharField(max_length=100)

	# Unlike other fields, 'authors' is not a data column, it
	# represents a many-to-many relationship among books and 
	# authors: a books has one more authors, an author writes
	# one or many books.
	# 
	# Actually a joint table is created to handle the mapping
	# from books to authors.
	authors = models.ManyToManyField(Author)

	# Since a book has one and only one publisher, to express
	# this one-to-one relationship, use 'ForeignKey'.
	publisher = models.ForeignKey(Publisher)

	publication_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.title