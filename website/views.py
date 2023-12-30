from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Record
# Create your views here.
def home(request):
    records=Record.objects.all()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #authenticater
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.warning(request, 'Error logging in, Please type the proper credentials, if correct, please try again later')
            return redirect('home')
    else:

        return render (request, 'home.html', {'records':records})


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been successfully logged out! Thank You")
    return redirect('home')

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(sno=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.warning(request, 'Must be logged in to view the page')
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(sno=pk)
        delete_it.delete()
        messages.success(request,"Record deleted, Redirected to Homepage")
        return redirect('home')
    else:
        messages.warning(request, 'Must be logged in to view the page')
        return redirect('home')

def add_record(request):
    form=RecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                print(add_record.sno)
                number=add_record.sno
                messages.success(request,"Record Added, Redirected to that Record")
                return redirect("record",number)
        return render(request, 'addrecord.html', {'form':form})
    else:
        messages.warning(request, 'Must be logged in to add records')
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(sno=pk)
        form=RecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated, Redirecting to the Updated form")
            return redirect("record",pk)
        return render(request, 'update_record.html', {'form':form,'pk':pk})
    else:
        messages.warning(request, 'Must be logged in to update records')
        return redirect('home')
        
