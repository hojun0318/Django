from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    chattings = Chat.objects.all()
    context = {
        'chattings': chattings,
    }
    return render(request, 'chattings/index.html', context)


def create(request):
    if request.method == 'POST':
        # create
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            return redirect('chattings:detail', chat.pk)
    else:
        # new
        form = ChatForm()
    context = {
        'form': form,
    }
    return render(request, 'chattings/create.html', context)

def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    chat = Chat.objects.get(pk=pk)
    context = {
        'chat': chat
    }
    return render(request, 'chattings/detail.html', context)