from django.shortcuts import render
from .forms import RegistrationForm

def index(request):
    form = RegistrationForm()
    context = {
        'myregistrationform': form
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        bound_form = RegistrationForm(request.POST)
        print(bound_form.is_valid())
        print(bound_form.errors)
        return render(request, 'sucess.html')
