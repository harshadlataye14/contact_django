from django.urls import path
from . import views

urlpatterns=[
    # path('',views.home, name='home'),
    path('',views.Homepage.as_view(), name='home'),
    path('detail/<int:pk>/' , views.DetailView.as_view(), name='detail'),
    path('search/',views.Search,name='search' ),
    path('contacts/create',views.ContactCreateView.as_view(),name='create'),
    path('contacts/update/<int:pk>',views.ContactUpdateView.as_view(),name='update'),
    path('contacts/delete/<int:pk>',views.ContactDeleteView.as_view(),name='delete'),
    path('signup',views.SignUpView.as_view(),name='signup'),
    
]