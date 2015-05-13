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
from user_auth.models import get_huntprog, get_createdhunts


@login_required
def edit(request):
    """

    :param: HttpRequest
    :rtype: HttpResponse

    The user can edit their information from the edit page. From the edit page, 
    the information that the user wants to modify will be taken and passed to
    the class **EditForm**. The class **EditForm** has class method called
    **process()** which is responsible for processing the edit information.
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
    """
    :param: HttpRequest
    :rtype: HttpResponse

    This function is responsible for checking if a user is authenticated when
    the user is try to access profile page.
    """

    user = None
    if request.user.is_authenticated():
        user = request.user
        uname = request.user.username
        lst_of_hunts = get_huntprog(uname)
        lst_of_crhunts = get_createdhunts(uname)

    args = {'user':user, 'lst_of_hunts': lst_of_hunts, 'lst_of_crhunts':lst_of_crhunts}
    args.update(csrf(request))
    return render_to_response('user_auth/profile.html', args)

# Create your views here.
def login_user(request):
    """

    :param: HttpRequest
    :rtype: HttpResponse
    

    log a user into the website. This function takes the login information
    such as the username and password from the user and pass the information
    to **LogInForm**. The **LogInForm** has class method called **login_process()**
    and this class method handles processing the login information.
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
    """

    :param: HttpRequest
    :rtype: HttpResponse

    This function handles log the user out from the website. 
    """

    logout(request)
    return render_to_response('home/home.html', {})

def register(request):
    """

    :param: HttpRequest
    :rtype: HttpResponse

    This method handles registering new users. All neccessary information is
    taken from **register.html** page, and those information is passed into
    **RegisterForm** and the class method **register_form()** will process 
    the information.
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

