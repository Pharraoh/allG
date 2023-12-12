from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import MyCustomForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout



# def register(request):
#     if request.method == 'POST':
#         # Handle form submission
#         form = MyCustomForm(request.POST)
#         if form.is_valid():
#             return redirect("accounts:signin")
#             # Process valid form data
#             # ...
#     else:
#         # Display a blank form
#         form = MyCustomForm()
#
#     return render(request, 'accounts/create_account.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:signin")
    else:
        form = UserCreationForm()
    return render(request, "accounts/create_account.html", {"form": form})


def sign_in(request):
    if request.method == 'POST':
        form = MyCustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home
                return redirect('profiles:account_status')  # Replace 'home' with the name of your home URL
            else:
                # Invalid login
                form.add_error(None, 'Invalid username or password')
                print(f"Failed login attempt. Username: {username}, Password: {password}")
    else:
        form = MyCustomForm()

    return render(request, 'accounts/sign_in.html', {'form': form})



# def sign_in(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("profiles:account_status")
#     else:
#         form = AuthenticationForm()
#         return render(request, "accounts/sign_in.html", {"form": form})


# def about(request):
#     return render(request, "accounts/about.html")

def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:signin")




# def my_view(request):
#     if request.method == 'POST':
#         # Handle form submission
#         form = MyCustomForm(request.POST)
#         if form.is_valid():
#             # Process valid form data
#             # ...
#     else:
#         # Display a blank form
#         form = MyCustomForm()
#
#     return render(request, 'my_template.html', {'form': form})



# accounts/views.py


def signin_view(request):
    if request.method == 'POST':
        form = MyCustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home
                return redirect('home')  # Replace 'home' with the name of your home URL
            else:
                # Invalid login
                form.add_error(None, 'Invalid username or password')
    else:
        form = MyCustomForm()

    return render(request, 'signin.html', {'form': form})
