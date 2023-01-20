from django.shortcuts import render
from django.http import HttpResponse
from .models import Painting, PaintingInstance, Genre , Language, Artist
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

def index(request):
 
    num_painting = Painting.objects.all().count()
    num_instance = PaintingInstance.objects.all().count()
    
    num_instance_avail = PaintingInstance.objects.filter(status__exact='a').count()
    
    context = {
        'num_painting':num_painting,
        'num_instance':num_instance,
        'num_instance_avail':num_instance_avail
    }
    
    return render(request,'index.html',context=context)

class PaintingCreateView(LoginRequiredMixin, CreateView):
    model = Painting
    fields = '__all__'
    template_name = "painting_form.html"

class PaintingDetailView(DetailView):
    model = Painting
    template_name = "painting_detail.html"

@login_required
def sonic(request):
    return render(request, 'paintings/sonic.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'paintings/signup.html'

class CheckedOutBooksByUserView(LoginRequiredMixin,ListView):
    model = PaintingInstance
    template_name = 'paintings/profile.html'
    paginate_by = 5
    
    def get_queryset(self):
        return PaintingInstance.objects.filter(borrower=self.request.user).all()
    