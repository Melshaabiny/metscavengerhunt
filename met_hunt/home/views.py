from django.shortcuts import render_to_response
from django.contrib.auth.models import User
# Create your views here.
def main(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
	else:
		user = None
	args = {'user':user}
	return render_to_response('home/home.html', args)

def search(request, query):
	args = {'result':query}
	return render_to_response('home/search_template.html', args)
