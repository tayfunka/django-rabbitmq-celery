from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import ReviewForm


class ReviewFormView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = 'Your review has been sent successfully'
        return HttpResponse(msg)
