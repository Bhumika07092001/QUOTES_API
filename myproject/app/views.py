from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
import requests
from .forms import signUpForm
from .models import Quotes


# Create your views here.

class QuotesList(View):
    def fetch_data(request):
        category = 'happiness'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': 'xRU2fDlW1OEsaY+L/Yk+XA==jrY2agsm8ox2Z8Q8'})
        if response.status_code == requests.codes.ok:
         print(response.text)
         data= response.json()
         template_name= 'index.html'
         context={'quotes':data}
         return render(request,template_name,context)

        else:
         print("Error:", response.status_code, response.text)

class Forms(View):
   def signUp(request):
      if request.method == 'POST':
         form = signUpForm(request.POST)

         if form.is_valid():
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save()
            login(request,user)

            return render(request,'response.html',{'name':name,'email':email})
      else:
         form = signUpForm()
      return render(request, 'register.html',{'form':form})
   
   def reponseView(request):
      return render(request,'response.html')
   
class userData(View):
    def get(request):
        user_list = User.objects.all()
        print(user_list)
        return render(request,'user_list.html',{'users':user_list})

