from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def about(request):
	return render(request, 'main/about.html', {})

def projects(request):
	projects_list = Project.objects.all()
	return render(request, 'main/projects.html', {'projects_list': projects_list})

def project_detail(request, slug):
	project = get_object_or_404(Project, slug=slug)
	return render(request, 'main/project_detail.html', {'project':project, 'images': ProjectImages})	

def contact_form(request):
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			sender = form.cleaned_data['email']
			message = 'From: ' + name + '\n\nEmail: ' + sender + '\n\nMessage:' + form.cleaned_data['text']
			subject = form.cleaned_data['subject']
			form.save()
			recipient = ['shigewood@gmail.com']
			send_mail(subject,message,settings.EMAIL_HOST_USER,recipient,fail_silently=False)
			global thanks
			form = ContactForm()
			thanks = 'Thank you! We will get back to you shortly.'


	else:
		form = ContactForm()
		thanks = ''

	return render(request, 'main/contact.html', {'form':form, 'thanks':thanks,})