from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib.auth.decorators import login_required

# from .forms import PatientRegistrationForm, PatientLoginForm



def index(request):
    obj = CarouselItem.objects.all()
    about_content = AboutContent.objects.first()  
    opening_hours = OpeningHours.objects.all()
    appointments = Appoint_contact.objects.all()
    home_content = ApointmentContent.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    team_members = TeamMember.objects.all()
    
    
    context = {
        'obj': obj,
        'about_content': about_content,
        'opening_hours': opening_hours,
        'appointments': appointments,
        'home_content': home_content,
        'services': services,
        'testimonials': testimonials,
        'team_members': team_members 
    }
    return render(request, 'index.html', context)
    

def about(request):
    about_content = AboutContent.objects.first()  
   
    context = {
        'about_content': about_content,

    }
    return render(request, 'about.html', context)


def appointment(request):
    appointment = appointment.object.all()
    context={appointment: appointment}
    return render(request, 'appointment.html', context )

def success():
    return  HttpResponse("thank...! You will get a feedback from you soon")



def service(request):
    services = Service.objects.all()
    appointments = Appoint_contact.objects.all()
   
    context = {
        'services': services,
        'appointments': appointments
    }
    return render(request, 'service.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index') 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def patient_reg_view(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            
            # Create a user with the admission_number as username and password
            user = User.objects.create_user(
                username=admission_number,
                password=password
            )
            
            patient = form.save(commit=False)
            patient.user = user
            patient.save()
            
            messages.success(request, 'Registration successful. Please log in using your credentials.')
            return redirect('loginpage')
        else:
            print("Form has errors:", form.errors)
    else:
        form = PatientRegistrationForm()

    return render(request, 'patient_reg.html', {'form': form})

def patient_login_view(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission_number, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')  # Redirect to your patient dashboard URL
            else:
                messages.error(request, 'Invalid admission number or password.')

    else:
        form = PatientLoginForm()

    # To display the current year
    current_year = datetime.datetime.now().year

    context = {
        'form': form,
        'current_year': current_year,
    }

    return render(request, 'loginpage.html', context)

def patient_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('loginpage')  # Redirect to your login page URL

def staff_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('staff_login')  # Redirect to your login page URL



# def staff_reg_view(request):
#     if request.method == 'POST':
#         form = StaffRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Form is valid. Data saved.")
#             return redirect('index')
#         else:
#             print("Form has errors:", form.errors)
#     else:
#         form = StaffRegistrationForm()

#     return render(request, 'staff_reg.html', {'form': form})



from django.contrib.auth.models import User
from .models import StaffRegistration
from .forms import StaffRegistrationForm  # Make sure to import your form

def staff_reg_view(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']

            # Create a user with the admission_number as username and password
            user = User.objects.create_user(
                username=admission_number,
                password=password,
                is_staff=True  # Set is_staff to True for staff members
            )

            staff = form.save(commit=False)
            staff.user = user
            staff.save()

            messages.success(request, 'Registration successful. Please log in using your credentials.')
            return redirect('staff_login')
        else:
            print("Form has errors:", form.errors)
    else:
        form = StaffRegistrationForm()

    return render(request, 'staff_reg.html', {'form': form})




    
def staff(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission_number, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')  # Redirect to your patient dashboard URL
            else:
                messages.error(request, 'Invalid admission number or password.')

    else:
        form = StaffLoginForm()

    # To display the current year
    current_year = datetime.datetime.now().year

    context = {
        'form': form,
        'current_year': current_year,
    }

    return render(request, 'staff.html', context)



def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber = form.save()

            # Send welcome email
            subject = 'Welcome to our Newsletter'
            message = 'Thank you for subscribing to our newsletter!'
            from_email = 'your_email@example.com'
            to_email = [email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            return redirect('index') 
    else:
        form = NewsletterForm()

    return render(request, 'index.html', {'form': form})



@login_required  # Ensure the user is logged in
def profile(request):
    # Assuming there's a one-to-one relationship between User and PatientRegistration
    try:
        patient_registration = PatientRegistration.objects.get(user=request.user)
    except PatientRegistration.DoesNotExist:
        # Handle the case where the patient registration doesn't exist
        patient_registration = None

    context = {'profiles': patient_registration}
    return render(request, 'profile.html', context)



@login_required  # Ensure the user is logged in
def staff(request):
    # Assuming there's a one-to-one relationship between User and PatientRegistration
    try:
        staff_registrationt = StaffRegistration.objects.get(user=request.user)
    except StaffRegistration.DoesNotExist:
        # Handle the case where the patient registration doesn't exist
        staff_registrationt = None

    context = {'staffs': staff_registrationt}
    return render(request, 'staff.html', context)



def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission_number, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')  # Redirect to your patient dashboard URL
            else:
                messages.error(request, 'Invalid admission number or password.')

    else:
        form = StaffLoginForm()

    # To display the current year
    current_year = datetime.datetime.now().year

    context = {
        'form': form,
        'current_year': current_year,
    }

    return render(request, 'staff_login.html', context)





def register(request):
    context = {}
    return render(request, 'register.html', context)


def login_page(request):
    context = {}
    return render(request, 'login_page.html', context)

def password_reset(request):
    context = {}
    return render(request, 'password_reset.html', context)


# @login_required
# def videocall(request):
#     return render(request, 'WEB_UIKITS.html', {"name" : request.user})

def videocall(request):
    user = request.user
    if user.is_authenticated:
        first_name = user.first_name
        last_name = user.last_name
        full_name = f"{first_name} {last_name}" if first_name and last_name else user.username
    else:
        full_name = "Guest"

    return render(request, 'WEB_UIKITS.html', {"name": full_name})

# views.py
# from django.shortcuts import render

# def join_video_call(request, room_id):
#     return render(request, 'join_video_call.html', {'room_id': room_id})

from django.shortcuts import render

def join_meeting(request):
    if request.method == 'POST':
        # Handle the form submission for joining a meeting
        room_id = request.POST.get('roomID')
        # Perform any necessary actions for joining a meeting

    return render(request, 'join_meeting.html')


