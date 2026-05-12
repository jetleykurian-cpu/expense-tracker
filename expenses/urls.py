from django.urls import path
from .views import ExpenseView, ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView
from . import auth_views
from .api_views import ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    # main views
    path('', ExpenseListView.as_view(), name='home'),
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('<int:pk>/edit/', ExpenseUpdateView.as_view(), name='expense-edit'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),

     # API endpoints
     path('api/expenses/', ExpenseListCreateView.as_view(), name ='api-expenses'),
          path('api/expenses/<int:pk>/', ExpenseDetailView.as_view(), name ='api-expenses-detail'),
]