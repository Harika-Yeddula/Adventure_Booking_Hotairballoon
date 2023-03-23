from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import adventureplaces,bookings
from .forms import BookingForm
import datetime

# Create your views here.

# homepage
def homepage(request):
   #Using visits in session to maintain the visits of the user on the page
   request.session['visits']= int(request.session.get('visits',0))+1
   all_countries = adventureplaces.objects.values('country').distinct()
   return render(request, 'index.html',{'all_countries': all_countries,'visits':request.session['visits']})

def userlogin(request):
   # user login and signup page
      if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         password = request.POST['pswd']
         #Authenticating the user
         user = auth.authenticate(username=username, password=password)
         # Checking the user is present or not
         if user is not None:
            # Attaching the authenticated user to the current session by using login() method
            auth.login(request,user)
            messages.success(request, "successful logged in")
            print("Login successful")
            return redirect('homepage')
         else:
            messages.warning(request, "Incorrect username or password")
            return redirect('userlogin')
      return render(request, 'userlogin.html')

def usersignup(request):

   if request.method == "POST":
      user_name = request.POST['username']
      email=request.POST['email']
      password1 = request.POST['password1']
      password2 = request.POST['password2']

      # to check whether the two passwords are matched
      if password1 != password2:
         messages.warning(request, "Password didn't match, Please try again")
         return redirect('usersignup')

      # To check whether the username is already taken
      try:
         if User.objects.all().get(username=user_name):
            messages.warning(request, "Username Not Available, try with other user names")
            return redirect('usersignup')
      except:
         pass

      new_user = User.objects.create_user(username=user_name, password=password1, email=email)
      new_user.save()
      print('User created')
      messages.success(request, "Registration Successful, Please login")
      return redirect("userlogin")
   return render(request, 'usersignup.html')

@login_required
def logoutuser(request):
   if request.method == 'GET':
      logout(request)
      messages.success(request, "Logged out successfully")
      print("Logged out successfully")
      return redirect('homepage')
   else:
      print("logout unsuccessfull")
      return redirect('userloginpage')

@login_required
def mybookings(request):
      booking_list = bookings.objects.filter(guest=request.user)
      return render(request,'mybookings.html',{'booking_list':booking_list})

def searchlocation(request):
   if request.method == "POST":
      location_selected=request.POST['search_location']
      loc_list=adventureplaces.objects.filter(country=location_selected)
      return render(request,'searchlocation.html',{'location_selected':location_selected,'loc_list':loc_list})

@login_required
def booking(request):
   if request.method == "POST":
      form = BookingForm(request.POST)
      # ap_location=request.POST['ap_location']
      if form.is_valid():
         form = form.save(commit=False)
         form.guest = request.user  # The logged-in user
         form.save()
         booking_list=bookings.objects.filter(guest=request.user)
         return render(request,'mybookings.html',{'booking_list':booking_list})
   ap_location=request.POST['ap_location']
   return render(request,'booking.html',{'form':BookingForm(),'ap_loc':ap_location,'user':request.user})


def contact(request):
   return render(request,'contact.html')

def about(request):
   return render(request,'#')

def test(request):
   return render(request,'test.html')

@login_required
#view for editing the booking
def editbooking(request, id):
   booking = bookings.objects.get(pk=id)
   form = BookingForm(instance=booking)
   if request.method == 'POST':
      form = BookingForm(request.POST)
      if form.is_valid():
         form = form.save(commit=False)
         form.guest = request.user  # The logged-in user
         form.save()
         booking_list = bookings.objects.filter(guest=request.user)
         return render(request, 'mybookings.html', {'booking_list': booking_list})
   return render(request, 'editbooking.html', {'form': form})

@login_required
#View for deleting the booking
def deletebooking(request, id):
    bookings.objects.get(pk=id).delete()
    return redirect('mybookings')