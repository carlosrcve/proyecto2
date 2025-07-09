from django import forms
from .models import Book,Post

'''
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']



class PostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['mes', 'indice', 'variacion']

'''


class BookForm1(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mes', 'indice', 'variacion']