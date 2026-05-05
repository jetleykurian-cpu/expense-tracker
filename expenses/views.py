from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm
@login_required(login_url ='login')
def home(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total = sum(e.amount for e in expenses)

    context = {
        "expenses": expenses,
        "total": total,
        'form': form,
    }
    return render(request, "expenses/home.html", context)

