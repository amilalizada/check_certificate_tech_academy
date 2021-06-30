from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from main.forms import HomeForm
from main.models import Certificate

def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            request.session['certificate_number'] = form.cleaned_data.get('verification')
            return redirect(reverse_lazy('info'))
    else:
        form = HomeForm()
    context = {
        'form': form
    }
    return render(request,'index.html', context)


def info(request):
    certificate_number = request.session.get('certificate_number')
    if not certificate_number:
        return redirect(reverse_lazy('home'))
    certificate = Certificate.objects.get(certificade_number=certificate_number)
    del request.session['certificate_number']
    print(request.session)
    context = {
        'certificate' : certificate
    }
    return render(request,'info.html', context)

    

