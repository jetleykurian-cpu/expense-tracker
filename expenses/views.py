from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Expense
from .forms import ExpenseForm

class UserOwnerMixin:
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ExpenseView(View):
    template_name = 'expenses/home.html'

    def get(self, request):
        expenses = Expense.objects.filter(user=request.user).order_by('-date')
        total = sum(e.amount for e in expenses)
        form = ExpenseForm()
        return render(request, self.template_name, {
            'expenses': expenses,
            'total': total, 
            'form': form
        })
    
    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit = False)
            expense.user = request.user
            expense.save()
            return redirect('home')
        expenses = Expense.objects.filter(user=request.user).order_by('-date')
        total = sum(e.amount for e in expenses)
        form = ExpenseForm()
        return render(request, self.template_name, {
            'expenses': expenses,
            'total': total, 
            'form': form
        })

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses/home.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = sum(e.amount for e in self.get_queryset())
        context['form'] = ExpenseForm()
        return context
    
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/home.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/edit.html'
    success_url = reverse_lazy('home')

    
    
class ExpenseDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Expense
    template_name = 'expenses/delete.html'
    success_url = reverse_lazy('home')

    