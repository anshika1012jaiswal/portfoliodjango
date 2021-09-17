from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


from portfolioproject.models import Contact


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        messages = request.POST.get('message')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        ins = Contact(cname=name , cmessage=messages , cemail=email,csubject=subject)
        ins.save()


        mail_subject = 'anshika.codes'
        mail_message = f"Name: {name} \n email: {email} \n subject: {subject} \n message: {messages} \n"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['anshika1012jaiswal@gmail.com', ]
        send_mail(mail_subject,mail_message, email_from, recipient_list)
       


    return render(request, 'index.html')



