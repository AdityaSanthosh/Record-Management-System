from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from record.models import Person
from django.contrib import messages


# Create your views here.
def index(request):
    db = Person.objects.all()
    personname = {
        "person": db
    }
    return render(request, template_name='record/index.html', context=personname)


def newentry(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        phoneno = request.POST["phone"]
        newperson = Person(name=name, email=email, phone_number=phoneno)
        newperson.save()
        HttpResponse('New Entry Added!')
    return render(request, 'record/newentry.html')


def delete_entry(request, entryid):
    entry = Person.objects.get(id=entryid)
    entry.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_entry(request, entryid):
    databaseentry = Person.objects.get(id=entryid)
    username0 = databaseentry.name
    email0 = databaseentry.email
    phone0 = databaseentry.phone_number
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        databaseentry.name = username
        databaseentry.email = email
        databaseentry.phone_number = phone
        databaseentry.save()
    context = {
        "id": entryid,
        "username": username0,
        "email": email0,
        "phone": phone0,
    }
    return render(request, template_name='record/updateentry.html', context=context)
