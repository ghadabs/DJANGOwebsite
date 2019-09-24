from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from .form import ContactForm
from .models import NewsletterUser
from .form import NewsletterUserForm
from django.contrib import admin,messages

def contact(request):
    
    if request.method == 'POST':
        if request.POST['form-type'] == "contact-form":   # test the form type
            form = ContactForm(request.POST) 
            if form.is_valid():
                name = form.cleaned_data['name']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
              
                try:
                    send_mail(name, message, from_email, ['commercial@grouptelili.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
        else:
            form = NewsletterUserForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False) #we dont want to save just yet
                if NewsletterUser.objects.filter(email=instance.email).exists():
                    print( "your Email Already exists in our database")
                else:
                    instance = form.save() 
                    messages.success(request,"You are subscribed !")
                    subject='confirmation subsription!'
                    msg='Thank you for your subsription!'
                    from_email=settings.EMAIL_HOST_USER
                    to_list=[ instance.email]
                    send_mail(subject,msg,from_email,to_list,fail_silently=True)
                    print( "your Email has been submitted to our database") 
                    
    return render(request,'contact.html',{
            'contact_form': ContactForm(),
            'NewsletterUser_form': NewsletterUserForm(),
    })

















