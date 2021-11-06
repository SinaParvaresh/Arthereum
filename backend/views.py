from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .models import User

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

class Login(View):
    template = "backend/login.html"

    def get(self, request):
        return render(request, self.template)

    def post(self, request, address):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if not user is None:
            if user.address is address:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, self.template, {
                    'message': "Your ethereum account is not synced, please use a different address with MetaMask"
                })

        return render(request, self.template, {
            'message': "Invalid username or password",
        })

@csrf_exempt
def Register(request):
    pass

def check_account(request, address):
    try:
        user = User.objects.get(address=address)
    except User.DoesNotExist:
        return False

    return True

@login_required(login_url='/accounts/login')
def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, "backend/profile.html", {
        'user': user,
    })
