from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . forms import ContactForm

@login_required
def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been received')
        else:
            form = ContactForm()
            messages.error(request,'Your message was not received. Check the input information')
        return redirect('blog:home')
    context ={
        'form':form
    }
    return render(request,'contact/contact.html',context)




