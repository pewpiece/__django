from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login_view(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/")
    else:
        form = AuthenticationForm(request)
        context = {
            "form": form
        }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    return render(request, "accounts/logout.html")


# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         password_confirm = request.POST.get("password_confirm")

#         # Basic validation
#         if not username or not email or not password:
#             messages.error(request, "All fields are required.")
#             return render(request, "accounts/register.html")

#         if password != password_confirm:
#             messages.error(request, "Passwords do not match.")
#             return render(request, "accounts/register.html")

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#             return render(request, "accounts/register.html")

#         # Check if email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#             return render(request, "accounts/register.html")

#         # Create user
#         try:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             messages.success(request, "Account created successfully! Please log in.")
#             return redirect("login")
#         except Exception as e:
#             messages.error(request, "Error creating account. Please try again.")
#             return render(request, "accounts/register.html")

#     return render(request, "accounts/register.html")
