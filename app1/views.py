from django.shortcuts import render
from django.http import HttpResponse
from project1 import forms
from app1.forms import NewUserForm

# Create your views here.

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'app1/index.html',context=my_dict)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            # Do Something Code
            print("Validation Success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Name: "+form.cleaned_data['text'])

    return render(request,'app1/form_page.html',{'form':form})   


def form_home(request):
    return render(request,'app1/form_home.html')


def signup_home(request):
    return render(request,'app1/signup_home.html')


def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return signup_home(request)
        else:
            print("ERROR! Form Invalid")
    
    return render(request, 'app1/users.html', {'form':form})


def relative(request):
    return render(request, 'app1/relative_url_templates.html')

def other(request):
    return render(request, 'app1/other.html')
    