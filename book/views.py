from django.shortcuts import render
from .forms import BoardForm
from .models import Board
# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST) 
        if form.is_valid(): 
            form = form.save(commit = False) 
            form.date = timezone.now()
            form.save()
            return redirect('home') 
    else:
        form = BoardForm() #forms.py의 PostForm 클래스의 인스턴스
    return render(request, 'home.html', {'form' : form}) 

def all_books(request):
    boards = Board.objects.all()
    return render(request, 'all_books.html', {'boards':boards})
