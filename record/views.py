from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from record.models import Entry
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

indexmap = {}

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        db = Entry.objects.filter(user=request.user).order_by('-name')
        Entryname = {
            "Entry": db
        }
        return render(request, template_name='record/index.html', context=Entryname)
    else:
        return render(request, template_name='record/homepage.html')


@login_required
def newentry(request):
    i = 0
    if request.method == 'POST':
        i+=1
        name = request.POST["username"]
        email = request.POST["email"]
        phoneno = request.POST["phone"]
        newEntry = Entry(name=name, email=email, phone_number=phoneno)
        newEntry.user = request.user
        newEntry.save()
        HttpResponse('New Entry Added!')
        messages.success(request, f'New Entry Added')
        # indexmap[newEntry.name] = newEntry
    return render(request, 'record/newentry.html')

#
# class CreateNewEntry(LoginRequiredMixin, CreateView):
#     model = Entry
#     fields = ['name', 'email', 'phone_number']
#     template_name = 'record/newentry.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(CreateNewEntry, self).form_valid(form=form)


@login_required
def delete_entry(request, entryid):
    entry = Entry.objects.get(id=entryid)
    entry.delete()
    messages.success(request, f'Entry Deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def update_entry(request, entryid):
    databaseentry = Entry.objects.get(id=entryid)
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
        "username": databaseentry.name,
        "email": databaseentry.email,
        "pinhone": databaseentry.phone_number,
    }
    return render(request, template_name='record/updateentry.html', context=context)


@login_required
def searchresult(request):
    try:
        searchkey = request.POST['searchkey']
    except KeyError:
        searchkey = "Nothing"
    indexentries(request)
    results = indexmap.get(searchkey)
    context = {
        "searchkey": searchkey,
        "results": results,
    }
    return render(request, template_name='record/searchresult.html', context=context)


@login_required
def indexentries(request):
    if request.user.is_authenticated:
        db = Entry.objects.filter(user=request.user).order_by('-name')
        Entryname = {
            "Entry": db,
        }
        i = 0
        for x in db:
            indexmap[x.name] = x
            i += 1
        messages.success(request, f'Indexing Complete')
        return render(request, template_name='record/index.html', context=Entryname)
    else:
        return render(request, template_name='record/homepage.html')
