User Authentication
*******************

The application that handles all of the user related tasks is named **user_auth** app in our system. The tasks it handles are

	1. User Login

		- The view that handles this task is **user_auth.views.login_user**. It handles user login process, rendering template with appropriate forms. If user login information is invalid, it renders correct template with error messages. 
	2. User Logout
	   
		- **user_auth.views.logout_user** handles this task. It simply let the user logout.

	3. User Profile
		
		- **user_auth.views.profile** function handles user profile related tasks. It renders neccessary templates and display logged in user information in the profile page.

	4. Register

		- **user_auth.views.register** function is responsible for registering the
		  new user. It also renders template with correct form.

	6. Edit User Information

		- **user_auth.views.edit** handles editting the logged in user information if
		  the user wants. 
	   
This includes all the form validation processes, and error handlings. Our **user_auth/views.py** is written as light as possible which means that many 
of the works such as user information processings, and form validations are 
taken care by **user_auth/auth_forms.py**. 

.. include:: ./user_auth/doc_user_auth.rst

