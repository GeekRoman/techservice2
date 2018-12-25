from django import forms
from django.contrib.auth.models import User

from master_office.models import Order


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(label="Отзыв о качестве работы", required=True)
    rating = forms.IntegerField(label="Оценка", required=True, max_value=5, min_value=0)

    class Meta:
        model = Order
        fields = ('feedback', 'rating')

    def save(self, commit=True):
        order = super(forms.ModelForm, self).save(commit=False)
        order.feedback = self.cleaned_data["feedback"]
        order.rating = self.cleaned_data["rating"]
        # comment. = self.cleaned_data["first_name"]
        # user.last_name = self.cleaned_data["last_name"]
        if commit:
            order.save()
        return order
