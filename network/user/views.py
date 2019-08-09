from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from user.models import User


def render_register_user_form(request):
    template = 'user/register_user_form.html'
    return render(request, template)


def process_register_user_form(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            date_of_birth=request.POST['date_of_birth'],
            phone_number=request.POST['phone_number'],
            gender=request.POST['gender'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        new_user.save()

        return HttpResponseRedirect(reverse('user:login'))
    return HttpResponse('Error: method not allowed.')


def render_login_user_form(request):
    template = 'user/login_user_form.html'
    return render(request, template)


def process_login_user_form(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist.')

        return HttpResponseRedirect(reverse('social:index', kwargs={'user_id': user.pk}))
    return HttpResponse('Error:method not allowed.')
