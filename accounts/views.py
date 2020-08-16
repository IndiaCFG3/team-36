from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import UpdateView
from django.utils.http import is_safe_url
from .admin import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from accounts.models import *


def index(request):
    response = {}
    # response = {'message': info}
    return render(request, 'home.html', response)


# @csrf_exempt
# def checkuserifscrutinyuser(user):
#     if user.groups.filter(name="owner").exists() and user.is_superuser:
#         return True
#     else:
#         return False
#
#
@csrf_exempt
def user_logout(request):
    logout(request)
    messages.success(request, "you have been logged out.")
    return HttpResponseRedirect('/login/')

# @csrf_exempt
# def admin_login(request):
#     response = {}
#     if request.user.is_authenticated:
#         logout(request)
#     else:
#         response = {}
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     if user.groups.filter(name="owner").exists() and user.is_superuser:
#                         return HttpResponseRedirect('/content/')
#                     else:
#                         messages.success(request, 'You are successfully logged in.')
#                         return HttpResponseRedirect('/')
#                 else:
#                     messages.warning(request, 'User is not active yet')
#                     response['message'] = 'User is not active yet'
#             else:
#                 messages.warning(request, 'User is invalid')
#                 response['message'] = 'User is invalid'
#
#         return render(request, 'account/signin.html', response)
#
class UserFormView(generic.View):
    form_class = UserCreationForm
    template_name = 'accounts/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            messages.success(request, 'Your account has been successfully created.')
            return redirect('accounts:index')

        return render(request, self.template_name, {'form': form})

#
# class UserUpdateFormView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = CustomUser
#     fields = ['email', 'name', 'mobile', 'gender', 'registration_number', 'image']
#     template_name = 'account/registration_form.html'
#
#     def form_valid(self, form):
#         form.instance.by = str(self.request.user)
#         messages.success(self.request, f'Your account has been updated!')
#         return super().form_valid(form)
#
#     def test_func(self):
#         customUser = str(self.get_object())
#         user = str(self.request.user)
#         if user == customUser:
#             return True
#         return False
#
#
def user_login(request):
    response = {}
    # if request.user.is_authenticated:
    #     logout(request)
    # else:
    if request.method == 'POST':
        next_post = request.POST.get('next')
        redirect_path = next_post
        username = request.POST['username']
        try:
            username = CustomUser.objects.get(email=username).username
        except CustomUser.DoesNotExist:
            username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You are successfully logged in.')
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
                else:
                    return redirect('../')
            else:
                messages.warning(request, 'User is not active yet')
                response['message'] = 'User is not active yet'
        else:
            messages.warning(request, 'User is invalid')
            response['message'] = 'User is invalid'

    return render(request, 'accounts/signin.html', response)

