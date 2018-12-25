from django import forms
from .models import Comment, Order, OrderLine
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="Ваш комментарий",required=True)

    class Meta:
        model = Comment
        fields = ('content',)

    def save(self, commit=True):
        comment = super(forms.ModelForm, self).save(commit=False)
        comment.content = self.cleaned_data["content"]
        # comment. = self.cleaned_data["first_name"]
        # user.last_name = self.cleaned_data["last_name"]
        if commit:
            comment.save()
        return comment


    # def save(self, commit=True):
    #     comment = super(forms.ModelForm, self).save(commit=False)
    #     comment.content = self.cleaned_data["content"]
    #     # comment. = self.cleaned_data["first_name"]
    #     # user.last_name = self.cleaned_data["last_name"]
    #     if commit:
    #         comment.save()
    #     return comment

    # order = models.ForeignKey('Order', on_delete=models.CASCADE)
    # brand_name = models.CharField(max_length = 20)
    # device_name = models.CharField(max_length = 20)
    # serial_id = models.CharField(max_length = 20)
    # feedback = models.TextField(blank=True)
    # trouble_description = models.TextField()
    # status = models.IntegerField(default = 0)








    # def save(self, commit=True):
    #     comment = super(ModelForm, self).save(commit=False)
    #     comment.content = self.cleaned_data["content"]
    #     comment.author = auth.get_user(request)

    #     if commit:
    #         comment.save()
    #     return comment


    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(label='first_name', max_length=100)
    # last_name = forms.CharField(label='last_name', max_length=100)

    # class Meta:
    #     model = User
    #     fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    # def save(self, commit=True):
    #     user = super(UserRegisterForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     if commit:
    #         user.save()
    #     return user




# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']

#         #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))

#         #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

#         # Помните, что всегда надо возвращать "очищенные" данные.
#         return data
