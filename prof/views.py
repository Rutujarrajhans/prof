from django.shortcuts import render,get_object_or_404
from prof.forms import contactformemail

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def emailsending(request):
    if request.method=="GET":
        form=contactformemail()
    else:
        form=contactformemail(request.POST)
        if form.is_valid():
            fromemail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,fromemail,['2018.rutuja.rajhans@ves.ac.in',fromemail])
           

    return render(request,'index.html',{'form':form})

