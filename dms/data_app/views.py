from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.
from .models import FileDetails
# def get_upload_path()

def uploadfile(request):
	c= {}
	c.update(csrf(request))
	t = loader.get_template('uploadfile.html')
	r = RequestContext(request, {})
	return HttpResponse(t.render(r), content_type=c)

def fileupload(request):
	c= {}
	c.update(csrf(request))
	if request.method == 'POST':
		fd = FileDetails()
		fd.docid = request.user
		fd.fileName = request.POST['filename']
		fd.typeOfFIle = request.POST['typeOfFIle']
		fd.docfile = request.FILES['docfile']
		fd.save();
		return HttpResponse("File upload Successfully")
	else:
		return HttpResponse("File upload Problem")
def list(request):
	files = FileDetails.objects.filter(docid=request.user)
	return render_to_response(
		'list.html',
		{'files': files},
		context_instance=RequestContext(request)
	)

# Create your views here.
