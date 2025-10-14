from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)
