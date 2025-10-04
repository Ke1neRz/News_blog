from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import FeedbackForm
from .models import Feedback

def index_view(request):
    context = {'title': 'Новостной блог!'}
    return render(request, "main/index.html", context)

def about_view(request):
    context = {'title': 'О нас'}
    return render(request, "main/about.html", context)

def contact_view(request):
    context = {'title': 'Контакты'}
    return render(request, "main/contact.html", context)

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            Feedback.objects.create(
                name=name,
                email=email,
                message=message
            )
                        
            send_mail(
                subject=f'Обратная связь от {name}',
                message=f'Email: {email}\n\nСообщение: {message}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            
            messages.success(request, f'Спасибо {name}!\nВаше сообщение: "{message}".Успешно отправлено.')
            return redirect('/feedback')
    else:
        form = FeedbackForm()

    context = {
        'title': 'Обратная связь',
        'form': form,
    }

    return render(request, "main/feedback.html", context)
