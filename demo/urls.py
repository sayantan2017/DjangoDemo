from django.urls import path
from . import views
from django.conf import settings
 
urlpatterns = [
    path('create/', views.add_items),
    path('get/',views.view_items),
    path('item/<int:id>/delete/',views.delete_items),
    path('update/<int:id>',views.update_items)
     
]