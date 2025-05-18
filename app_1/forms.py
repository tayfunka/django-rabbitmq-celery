from django import forms

from .tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=4, label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your name', 'id': 'form-name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Enter your email', 'id': 'form-email'}
    ))
    review = forms.CharField(label='Review', widget=forms.TextInput(
        attrs={'class': 'form-control', 'rows': '5'}
    ))

    # send this task to celery to run
    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['review'])
