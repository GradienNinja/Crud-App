from django.urls import path
from . import views 

urlpatterns = [
   path('',views.home,name="home"),
   path('create/',views.create_post,name='create'),
   path('edit/<int:post_id>',views.edit_post,name="edit"),
   path('delete/<int:post_id>',views.delete_post,name="delete")
]