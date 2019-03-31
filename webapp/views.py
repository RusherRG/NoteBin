from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    context = {'login_status':'Login'}
    return render(request, 'index.html',context)

def login(request):
    context = {'login_status':'Login'}
    if context['login_status'] == "Login":
        return render(request, 'login.html',context)
    else:
        return render(request, 'signup.html')

def submit(request):
    print(request.GET['username'],request.GET['password'])
    return redirect(home)