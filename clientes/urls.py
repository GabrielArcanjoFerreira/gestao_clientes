from django.urls import path
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import PersonListView, PersonDetail, PersonCreate, PersonUpdate, PersonDelete


urlpatterns = [
    path('list/', PersonListView.as_view(), name="person_list"),
    path('detail/<int:pk>/', PersonDetail.as_view(), name="person_detail"),
    path('create/', PersonCreate.as_view(), name="person_create"),
    path('update/<int:pk>/', PersonUpdate.as_view(), name="person_update"),
    path('delete/<int:pk>/', PersonDelete.as_view(), name="person_delete"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]