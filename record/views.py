from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from record.models import Person
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        db = Person.objects.all().order_by('-name')
        personname = {
            "person": db
        }
        return render(request, template_name='record/index.html', context=personname)
    else:
        return render(request, template_name='record/homepage.html')


@login_required
def newentry(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        phoneno = request.POST["phone"]
        newperson = Person(name=name, email=email, phone_number=phoneno)
        newperson.save()
        HttpResponse('New Entry Added!')
        messages.success(request, f'New Entry Added')
    return render(request, 'record/newentry.html')


class CreateNewEntry(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['name', 'email', 'phone_number']
    template_name = 'record/newentry.html'
    success_url = '/'


@login_required
def delete_entry(request, entryid):
    entry = Person.objects.get(id=entryid)
    entry.delete()
    messages.success(request, f'Entry Deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
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
        messages.success(request, f'Entry Updated')
    context = {
        "id": entryid,
        "username": username0,
        "email": email0,
        "phone": phone0,
    }
    return render(request, template_name='record/updateentry.html', context=context)