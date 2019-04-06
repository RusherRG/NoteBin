from django.shortcuts import render,redirect
from .models import Note, User
from datetime import datetime
from django.http import JsonResponse
import random
import string
s = string.ascii_letters
# Create your views here.
def home(request):
    #populate()
    try:
        context = {'username':request.session['name']}
    except:
        context = {'username':'public'}
        request.session['name'] = 'public'
    notes = fetch_notes()
    context['notes'] = notes
    return render(request, 'index.html',context)

def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        if not User.objects.filter(email = email).count():
            user = User()
            user.email = email
            user.password = password
            user.save()
            request.session['name'] = email
            return redirect(home)
        context = {'verify':'Email already used'}
        return render(request, 'login.html', context)

def fetch_notes():
    notes = Note.objects.all()
    NOTES = []
    for note in notes:
        NOTE = {}
        NOTE['user'] = note.user
        NOTE['name'] = note.name
        NOTE['note'] = note.note
        NOTE['time_modified'] = note.time_modified
        print(note.user)
        NOTES.append(NOTE)
    NOTES = sorted(NOTES, key=lambda x: x['time_modified'], reverse=True)
    return NOTES

def add_note(request):
    note = Note()
    note.user = request.session['name']
    note.name = request.POST.get("name",None)
    note.note = request.POST.get("note",None)
    note.time_modified = datetime.now()
    note.save()
    return 

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
    return render(request, "new_note.html")

def note(request, name):
    print(request, name)
    note = Note.objects.filter(name = name)
    print(note)
    if note.count():
        context = {'note': note[0]}
        return render(request, "note.html", context)
    else:
        context = {'note': ''}
        return render(request, 'note.html', context)