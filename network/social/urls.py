from django.urls import path
from social import views


app_name = 'social'
urlpatterns = [
    path('index/<int:user_id>', views.render_index, name='index'),
    path('activity/<int:user_id>', views.render_activity_form, name='activity'),
    path('add/', views.process_activity_form, name='add'),
    path('edit/<int:activity_id>', views.render_edit_activity_form, name='edit'),
    path('save_edit/<int:activity_id>', views.process_edit_activity_form, name='save_edit'),
    path('delete/<int:activity_id>', views.delete_activity, name='delete'),
    path('group/', views.render_group_form, name='group'),
    path('make/', views.process_group_form, name='make'),
    path('group_list/', views.GroupView.as_view(), name='group_list'),
    path('join_group/', views.GroupView.as_view(), name='join_group'),
    path('event/', views.render_event_form, name='event'),
    path('new_event/', views.process_event_form, name='new_event'),
    path('event_list/', views.EventView.as_view(), name='event_list'),
    path('assist_event/', views.EventView.as_view(), name='assist_event'),
]
