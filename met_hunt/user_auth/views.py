"""
user_auth.views

    This views.py is responsible for all user authenticating related jobs such as login a user,
    register a visitor...
"""
from django.shortcuts import render_to_response
from user_auth.auth_forms import RegisterForm, LogInForm, EditForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf # for Cross Site Request Forgery.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def edit(request):
    """
    The user can edit their information from the profile page.
    """
    form = None
    title = "Edit User Information"
    if request.method == 'POST':
        # make changes.
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.process(request.user)
            args = {'editted':True, 'user':user}
            args.update(csrf(request))
            return render_to_response('user_auth/edit.html', args)
    else:
        # provide edit form.
        form = EditForm()
    args = {'form':form, 'user':request.user, 'title':title, 'editted':False}
    args.update(csrf(request))
    return render_to_response('user_auth/edit.html', args)

@login_required
def profile(request):
    user = None
    if request.user.is_authenticated():
        user = request.user

    args = {'user':user}
    args.update(csrf(request))
    return render_to_response('user_auth/profile.html', args)

# Create your views here.
def login_user(request):
    """
    login a user into the website.
    """
    title = "LogIn"
    args = {}
    user = None

    if request.method == "POST":
        # The method should be post since it does not expose the user imformation on url.
        # it should be get method since login does not change state of any user data.
        form = LogInForm(request.POST)
        # check the form validation.
        if form.is_valid():

            user = form.login_process(request)
            if user is not None:
                args = {'user':user}
                args.update(csrf(request))
                return render_to_response('home/home.html', args)
            else:
                args = {'title':'Username does not exist.'}
                args.update(csrf(request))
                return render_to_response('user_auth/login.html', args)
    else:
        form = LogInForm()


    args = {'form':form, 'title':title}
    args.update(csrf(request))
    return render_to_response('user_auth/login.html', args)

@login_required
def logout_user(request):
    logout(request)
    return render_to_response('home/home.html', {})

def register(request):
    """
    Register new user. If the request method is not POST, then return the register page template.
    Otherwise, register the user with given data.
    """
    user = None
    # handles registering.
    title = 'Register'
    args = {}
    if request.method == 'POST':
        # it means that we received inputs from the user.
        # Then, fill them out.
        form = RegisterForm(request.POST)
        # check if all inputs are valid.
        if form.is_valid():
            if_error = form.register_form()
            if not if_error:
                args = {'title':'Username Exists', 'valid':False}
                return render_to_response('user_auth/register.html', args)
            return HttpResponseRedirect('/')
        else:
            # form is not valid.
            args = {'title':'Data is not valid', 'valid':False}
            return render_to_response('user_auth/register.html', args)
    else:
        form = RegisterForm()

    args = {'form' : form,
            'title' : title,
            'valid':True}
    args.update(csrf(request)) # Guess passing csrf token to the template.
    return render_to_response('user_auth/register.html', args)

