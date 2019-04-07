from django.shortcuts import render,redirect
from .models import Note, User
from datetime import datetime
from django.http import JsonResponse, HttpResponse
import random
import string
from pprint import pprint
s = string.ascii_letters
# Create your views here.
def home(request):
    #populate()
    search("Feature")
    try:
        if request.session['name']:
            context = {'username':request.session['name'], 'login_status':0}
        else:
            context = {'username':'public','login_status':1}
    except:
        context = {'username':'public','login_status':1}
        request.session['name'] = 'public'
    notes = fetch_notes()
    context['user_notes'] = []
    context['public_notes'] = []
    for note in notes:
        if note['user']==context['username']:
            context['user_notes'].append(note)
        else:
            context['public_notes'].append(note)
    context['notes'] = notes
    #pprint(context)
    return render(request, 'index.html',context)

def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        user = User.objects.filter(email = email)
        if not user.count():
            user = User()
            user.email = email
            user.password = password
            user.save()
            request.session['name'] = email
            return redirect(home)
        else:
            user = user[0]
            if user.password == password:
                request.session['name'] = email
                return redirect(home)
            else:
                return render(request, 'login.html',context={'verify':'Wrong Password :/'})

def logout(request):
    if request.method=='GET':
        request.session['name'] = ''
        return redirect(home)


def fetch_notes():
    notes = Note.objects.all()
    NOTES = []
    for note in notes:
        NOTE = {}
        NOTE['user'] = note.user
        NOTE['name'] = note.name
        NOTE['note'] = note.note
        NOTE['time_modified'] = note.time_modified
        #print(note.user)
        NOTES.append(NOTE)
    NOTES = sorted(NOTES, key=lambda x: x['time_modified'], reverse=True)
    return NOTES

def delete_note(request,name):
    if request.method=='GET':
        print('deleting')
        Note.objects.filter(name=name).delete()
        print('deleted')
    return redirect(home) 

def save_note(request):
    if request.method=='GET':
        user = request.session['name']
        name = request.GET.get("name",None)
        note = request.GET.get("note",None)
        time_modified = datetime.now()
        NOTE = Note.objects.filter(name = name, user = user)
        if not NOTE:
            print("create and save")
            NOTE = Note()
            NOTE.user = user
            NOTE.name = name
            NOTE.note = note
            NOTE.time_modified = datetime.now()
            NOTE.save()
        else:
            print("saving")
            NOTE.update(note = note, time_modified = time_modified)
        print("Saved")
        return JsonResponse({'status':'success'})

def populate():
    user = "Public"
    for i in range(10):
        note = Note()
        note.note = "".join([random.choice(s+'\t\n') for j in range(random.randint(200,500))])
        note.user = user
        note.name = "".join([random.choice(s) for j in range(random.randint(20,50))])
        note.time_modified = datetime.now()
        note.save()

def signup(request):
    user = User()
    user.email = ""
    user.password = "" 
    user.save()

def new_note(request):
    return redirect('/'+''.join([random.choice(s) for i in range(10)]))

def note(request, name):
    note = Note.objects.filter(name = name)
    if note.count():
        context = {'note': note[0]}
        if note[0].user=='Public' or note[0].user==request.session['name']:
            return render(request, "note.html", context)
        else:
            return redirect(home)
    else:
        context = {'note': {'name':name}}
        return render(request, 'note.html', context)
    
def search(text):
    stext=".*"+text+".*"
    print(stext)
    x = Note.objects.filter(note__iregex=stext)
    for i in x:
        print(i.__dict__)   
    print("Here", x, type(x))
    for i in x:
        print(x)
    return HttpResponse("Done")

