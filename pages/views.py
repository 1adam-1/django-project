from django.shortcuts import render, redirect

def home(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    
    return render(request, 'pages/homepage.html')



