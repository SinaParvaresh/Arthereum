from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .models import User, Auction

global address

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

class Login(View):
    template = "backend/login.html"

    def get(self, request):
        if request.is_ajax():
            print('connected')
            data = {'address': request.GET.get('address', None)}
            address = data[address]
            print(address)
        else:
            return render(request, self.template, {
                'message': "MetaMask not onnected"
            })

        return render(request, self.template)

    def post(self, request):#, address):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

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

class Register(View):
    template = 'backend/login.html'
    success_url = 'backend:auctions'

    def post(self, request):
        username = request.POST('username')
        first_name = request.POST('first_name')
        last_name = request.POST('last_name')
        email = request.POST('email')
        p1 = request.POST('p1')
        p2 = request.POST('p2')

        if not p1 == p2:
            return render(request, self.template, {
                'message': "passwords don't match",
            })

        user = User.objects.create_user(username, first_name=first_name, last_name=last_name, email=email, password=p1)
        user.save()

        return HttpResponseRedirect(reverse(success_url))

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

@login_required(login_url='/accounts/login')
def auction(request):
    list = Auction.objects.all()
    return render(request, "backend/auction_list.html", {
        'list': list,
    })

@login_required(login_url='/accounts/login')
def  detail(request, pk):
    item = Auction.objects.get(id=pk)
    return render(request, "backend/nft.html", {
        'item': item,
    })

@login_required(login_url='/accounts/login')
def make_offer(request, pk, num):
    item = Auction.objects.get(id=pk)
    item.cur_bid = num
    item.save()
    return HttpResponseRedirect(reverse("backend:NFT", args=(item.id,)))

class Transaction(View):
    template = "backend/eth.html"
    success_url = "backend:transaction"

    def get(self, request, address):
        #user = User.objects.get(address=address)
        return render(request, self.template, {
            'user': request.user,
        })

    def post(self, request, address):
        return HttpResponseRedirect(reverse(self.success_url, args=(address,)))

class Upload(View):
    template = "backend/form.html"
    success_url = "backend:auction"

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        return HttpResponseRedirect(reverse(self.success_url))
