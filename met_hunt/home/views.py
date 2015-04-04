from django.shortcuts import render_to_response
from django.contrib.auth.models import User
# Create your views here.
def main(request):
	user = None
	if request.user:
		user = User.objects.get(username=request.user)
	args = {'user':user}
	return render_to_response('home/home.html', args)
