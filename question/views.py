from django.shortcuts import render
from django.http import HttpResponse
from question.models import User
from question.forms import UserForm

# Create your views here.


def index(request):
    user_list = User.objects.all()
    context = {"user_list": user_list}
    return render(request, 'question/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): # 这一行不能少,cleaned_data必须跟在is_valid()后面
            cur_account = form.cleaned_data['account']
            exist_account = User.objects.filter(account=cur_account)
            if exist_account:
                return register_fail(request)
            form.save(commit=True)
            return index(request)
    else:
        form = UserForm()
    return render(request, 'question/register.html', {'form': form})


def register_fail(request):
    form = UserForm(request.POST)
    if form.is_valid():
        cur_account = form.cleaned_data['account']
        return render(request, 'question/register_fail.html', {'account': cur_account})


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): # 这一行不能少,cleaned_data必须跟在is_valid()后面
            cur_account = form.cleaned_data['account']
            cur_passwd = form.cleaned_data['passwd']

            exist_account = User.objects.filter(account=cur_account, passwd=cur_passwd)
            if exist_account:
                return index(request)
            return login_fail(request)
    else:
        form = UserForm()
    return render(request, 'question/login.html', {'form': form})


def login_fail(request):
    form = UserForm(request.POST)
    if form.is_valid():
        cur_account = form.cleaned_data['account']
        return render(request, 'question/login_fail.html', {'account': cur_account})
