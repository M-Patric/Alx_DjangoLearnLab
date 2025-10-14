from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Type your message here..."}),
        label="Message",
    )
