from rest_framework import generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer

# GET all expenses / POST new expense
class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
         # only return logged-in user's expenses
        return Expense.objects.filter(user=self.request.user).order_by('-date')
    def perform_create(self, serializer):
        # automatically attach logged-in user when creating
        serializer.save(user=self.request.user)

# GET / PUT / DELETE a single expense
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)     