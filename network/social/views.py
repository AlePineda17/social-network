from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect, redirect
from social.models import Activity, Group, Event, EventUser, GroupUser
from user.models import User
from django.views.generic import ListView


def render_index(request, user_id):
    template = 'social/index.html'
    context = {
        'index': Activity.objects.all,
        'user': user_id
    }
    return render(request, template, context)


def render_activity_form(request, user_id):
    template = 'social/activity_form.html'
    context = {
        'user': user_id
    }
    return render(request, template, context)


def process_activity_form(request):
    if request.method == 'POST':
        owner = User.objects.get(pk=request.POST['owner_id'])
        new_activity = Activity(
            picture=request.FILES['picture'],
            text=request.POST['text'],
            owner=owner,
        )
        new_activity.save()

        return HttpResponseRedirect(reverse('social:index', kwargs={'user_id': new_activity.owner.id}))
    return HttpResponse('Error: method not allowed.')


def render_edit_activity_form(request, activity_id):
    template = 'social/edit_activity_form.html'
    context = {
        'activity': Activity.objects.get(id=activity_id)
    }
    return render(request, template, context)


def process_edit_activity_form(request, activity_id):
    if request.method == 'POST':
        updated_activity = Activity.objects.get(id=activity_id)
        updated_activity.picture = request.FILES['picture']
        updated_activity.text = request.POST['text']
        updated_activity.save()

        return HttpResponseRedirect(reverse('social:index', kwargs={'user_id': updated_activity.user.id}))
    return HttpResponse('Error: method not allowed.')


def delete_activity(request, activity_id):
    deleted_activity = Activity.objects.get(id=activity_id)
    deleted_activity.delete()

    return HttpResponseRedirect(reverse('social:index', kwargs={'user_id': deleted_activity.owner.id}))


def render_group_form(request):
    template = 'social/group_form.html'
    return render(request, template)


def process_group_form(request):
    if request.method == 'POST':
        new_group = Group(
            name=request.POST['name'],
            description=request.POST['description'],
        )
        new_group.save()

        return HttpResponseRedirect(reverse('social:index', kwargs={'group_id': new_group.id}))
    return HttpResponse('Error: method not allowed.')


class GroupView(ListView):
    model = Group
    fields = '__all__'
    context_object_name = 'group_list'


def join_group(request, group_id, user_id):
    joined_group = Group.objects.get(id=group_id)
    user_joined = User.objects.get(id=user_id)
    GroupUser.add(joined_group, user_joined)

    return HttpResponseRedirect(reverse('social:group_list'))


def render_event_form(request):
    template = 'social/event_form.html'
    return render(request, template)


def process_event_form(request, user_id):
    if request.method == 'POST':
        user = EventUser.request.POST(id=user_id)
        new_event = Event(
            name=request.POST['name'],
            description=request.POST['description'],
            date=request.POST['date'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
            user=request.POST['user'],
        )
        new_event.save()
        return HttpResponseRedirect(reverse('social:index', kwargs={'user_id': new_event.user.id}))
    return HttpResponse('Error: method not allowed.')


class EventView(ListView):
    model = Event
    fields = '__all__'
    context_object_name = 'event_list'


def assist_event(request, user_id, event_id):
    chosen_event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)
    EventUser.add(chosen_event, user)
