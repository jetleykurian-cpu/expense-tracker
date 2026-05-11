from django.urls import path
from . import views
from . import auth_views
from .api_views import ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('login/', auth_views.logout_view, name='logout'),

     # API endpoints
     path('api/expenses/', ExpenseListCreateView.as_view(), name ='api-expenses'),
          path('api/expenses/<int:pk>/', ExpenseDetailView.as_view(), name ='api-expenses-detail'),
]