"""
User authenticating related form.
"""


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from user_auth.models import UserInfo

class RegisterForm(forms.Form):
    """
    RegisterForm is a django form that is responsible for processing the 
    user register information. 
    """
    user_name = forms.CharField(label="User Name", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=50)
    first_name = forms.CharField(label="First_Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)
    email_address = forms.EmailField(label="Email", max_length=50, required=False)

    def register_form(self):
        """
        This memeber function **register_form()** registers the user info received
        from register page. It tries to reject if the username is already exists.
        """
        try:
            isvalid = User.objects.get(username=self.cleaned_data['user_name'])
        except:
            print "rerere"
            isvalid = None
        if not isvalid:
            user = User.objects.create_user(username=self.cleaned_data['user_name'],
                                            password=self.cleaned_data['password'],
                                            first_name=self.cleaned_data['first_name'],
                                            last_name=self.cleaned_data['last_name'],
                                            email=self.cleaned_data['email_address'])
        else:
            print "error here!"
            return False
        # create empty userinfo
        user_info = UserInfo.objects.create(user=user)
        user.save()
        user_info.save()
        print user_info.save
        return True


class LogInForm(forms.Form):
    """
    **LogInForm** is a django form that handles user login process. It is
    used for displaying user login input fields as well as processing the
    login process once it receives the neccessary information from user.
    """

    user_name = forms.CharField(max_length=50, label="User Name")
    password = forms.CharField(max_length=50,
                               label="Password",
                               widget=forms.PasswordInput())

    def login_process(self, request):
        """
        This function is responsible for log the user in into the site.
        """
        user_name = self.cleaned_data['user_name']
        password = self.cleaned_data['password']


        # instanciate the user object.
        user = authenticate(username=user_name, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return user
        return None


class EditForm(forms.Form):
    """
    **EditForm** is responsible for editing the user information. The assumption is that the user
    is already registered. We restrict non-registered user to access edit page from the profifle
    views function. The list of information that the user can edit is :

        - Password
        - Description
        - Picture
        - Name
    """
    picture = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    def process(self, user):
        """
        If an user tries to change their personal info, this function handles
        the work.
        """
        if self.cleaned_data['first_name']:
            user.first_name = self.cleaned_data['first_name']
        if self.cleaned_data['last_name']:
            user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data['picture']:
            user_info = UserInfo.objects.get(user=user)
            user_info.picture = self.cleaned_data['picture']
            user_info.save()
        user.save()
        return user
