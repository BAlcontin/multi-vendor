from django.shortcuts import render, redirect
from developers.forms import DeveloperForm

from .forms import UserForm
from developers.forms import DeveloperForm
from .models import User, UserProfile
from django.contrib import messages
from developers.models import Developer
from django.contrib import messages

from django.template.defaultfilters import slugify


def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(
                request, 'Your account has been created sucessfully!')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:

        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)


def registerDeveloper(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        dev_form = DeveloperForm(request.POST, request.FILES)
        if form.is_valid() and dev_form.is_valid:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.DEVELOPER
            user.save()
            developer = dev_form.save(commit=False)
            developer.user = user
            developer_name = dev_form.cleaned_data['developer_name']
            developer.developer_slug = slugify(developer_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            developer.user_profile = user_profile
            developer.save()

            # Send verification email
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(
            #     request, user, mail_subject, email_template)

            messages.success(
                request, 'Your account has been registered sucessfully! Please wait for the approval.')
            return redirect('registerDeveloper')
    else:
        form = UserForm()
        dev_form = DeveloperForm()

    context = {
        'form': form,
        'dev_form': dev_form,
    }

    return render(request, 'accounts/registerDeveloper.html', context)
