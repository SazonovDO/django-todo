from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import toDoList, company
from .serializers import toDoListSerializers, companySerializers
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class toDoListView(viewsets.ModelViewSet):
    serializer_class = toDoListSerializers
    queryset = toDoList.objects.all()

    def get_queryset(self):
        try:
            idd = self.request.session['company_id']
        except KeyError:
            idd = 0
        try:
            c = company.objects.get(id=idd)
        except company.DoesNotExist:
            c = None
        return toDoList.objects.filter(company=c)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(toDoListView,self).dispatch(request, *args, **kwargs)


class companyView(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companySerializers

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(companyView,self).dispatch(request, *args, **kwargs)


def login(request):
    form_auth = AuthenticationForm()
    companys = company.objects.all()
    if request.method == 'POST':
        form_auth = AuthenticationForm(request=request, data=request.POST)
        if form_auth.is_valid():
            user = form_auth.get_user()
            c = company.objects.get(pk=int(form_auth.data['company_id']))
            if len(c.users.filter(username=user)) == 0:
                msg = 'Error. You can\'t access to this company'
                context = {'form': form_auth, 'companys': companys, 'msg': msg}
                return render(request, "registration/login.html", context)
            else:
                auth.login(request, user)
                request.session['company_id'] = int(form_auth.data['company_id'])
                return redirect("/")
        else:
            msg = 'Error login or password'
            context = {'form': form_auth, 'companys':companys, 'msg':msg}
            return render(request, "registration/login.html", context)
    else:
        msg = ''
        context = {'form': form_auth, 'companys': companys, 'msg': msg}
        return render(request, "registration/login.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm
        context = {'form': form}
    return render(request, 'registration/register.html', context)

def index(request):
    name = ''
    if request.user.is_authenticated:
        name = auth.get_user(request).username + ' (' + auth.get_user(request).email + ')'
    try:
        info = company.objects.get(pk=request.session['company_id'])
    except KeyError:
        info = ''
    context = {'name': name, 'company': info}
    return render(request, 'index.html', context)


