from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.urls import reverse #不导入，程序中的next无法用。
from .models import User

# Create your views here.
def user_register(request):
    if request.method == "GET":
        register_form = RegisterForm()
        return render(request, "register.html", context={"register_form": register_form})
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]
            email = register_form.cleaned_data.get("email", "")
            # 创建用户
            user = User.objects.create_user(username, email, password)
            next = request.GET.get("next", reverse("zlapp:index"))
            return redirect(next)
        else:
            return render(request, "register.html", {"register_form": register_form})

"""
def register(request):
    """  """
    if request.method != 'POST':
        #
        form = UserCreationForm()
    else:
        #
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #
            login(request, new_user)
            return redirect('xuexiaoapp:index')

    #
    context = {'form':form}
    return render(request, 'registration/register.html', context)
"""
