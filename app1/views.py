from django.shortcuts import render
from django.http import HttpResponse
from project1 import forms
from app1.forms import NewUserForm, UserForm, UserProfileInfoForm

# Create your views here.

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'app1/index.html',context=my_dict)


def index2(request):
    return render(request,'app1/index2.html')


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



def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'app1/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
