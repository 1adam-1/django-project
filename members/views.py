from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def member_login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('homepage')
        else:
            messages.success(request,"Erreur : mot de passe ou username incorrecte !")
            return render(request, 'authentification/login.html')
        
    else:
        return render(request,'authentification/login.html')

def member_register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname  = request.POST["lastname"]
        email     = request.POST["email"]
        username  = request.POST["username"]
        password  = request.POST["password"]
        
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "L'utilisateur existe déja !")
            return render(request, 'authentification/register.html')
 
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        messages.success(request, "Utilisateur créé ")
        return render(request, 'authentification/register.html')
    
    else:
        return render(request, 'authentification/register.html')
    
def member_profile(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('loginpage')  

    # Fetch user data
    user_data = {
        'user_id': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email
    }

    # Pass user data to the template context
    context = {'user_data': user_data}

    return render(request, 'authentification/profil.html', context)


def member_edit(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    if request.method == "POST":
        # Update user information based on form data
        request.user.username = request.POST.get('username')
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('editpage')

    return render(request, 'authentification/edit.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('homepage')