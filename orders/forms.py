from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}))
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Total Amount', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter total amount'}))

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':'Write your message'}))
