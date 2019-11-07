from django.shortcuts import render

from .forms import ContactForm

from .models import Project, Student,Supervisor,Contact_us

# def contactus(request):
#     my_form = ContactweForm()
#     if request.method == "POST":
#         my_form =ContactweForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Contact_us.objects.create(** my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, 'contactus.html', context)





def contactus(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()


#    form = ContactForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = ContactForm()
#
#
#    context = {
#        'form':form
#     }
#
    return render(request, 'contactus.html',{'form':form})

def home(request):
    x = Project.objects.all().order_by('-id')[:3]
    context = {
        'x':x
    }

    return render(request, 'home.html', context)

def aboutus(request):

    return render(request, 'aboutus.html')

def portofolio_detail(request,id):
    project = Project.objects.get(pk=id)


    return render(request, 'portofolio_detail.html', {'project':project})


def team(request):
    cor = Supervisor.objects.all().filter(post='coordinator')
    teams = Supervisor.objects.all().exclude(post='coordinator')
    tea = Project.objects.all



    return render(request, 'team.html', {'cor':cor, 'teams':teams, 'tea':tea})

def student_detail(request, id):
    projet = Student.objects.get(pk=id)

    return render(request, 'student_detail.html', {'projet':projet})

def supervisor_detail(request, id):
    proje = Supervisor.objects.get(pk=id)
    return render(request, 'supervisor_detail.html', {'proje':proje})

def portofolio(request):
    pro = Project.objects.all().order_by('-id')

    return render(request, 'portofolio.html', {'pro':pro})


