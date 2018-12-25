#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from news.models import Articles

# from django.contrib.auth.forms import UserCreationForm
# from mainApp.forms import UserRegisterForm
# from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'web/index.html', {'values': ['blablabla', '3578548']})
