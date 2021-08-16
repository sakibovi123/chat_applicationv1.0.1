from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.



def get_home_page_url(request):
    users = User.objects.all()
    
    args = {
        'users': users
    }
    
    return render(request, 'home.html', args)

def chat_with_user(request, id):
    user = User.objects.get(pk=id)
    
    msg_form = MessageForm(request.POST)
    if request.method == 'POST':
        
        if msg_form.is_valid():
            msg_form.save()
            return redirect('/')
    reply_form = ReplyForm(request.POST)
    if request.method == 'POST':
        if reply_form.is_valid():
            reply_form.save()
            
            return redirect('/')
    
    msgs = ChatRoom.objects.filter(Q(user=user) | Q(user=user))
    replies = ReplyModel.objects.all()
    
    args = {
        'user': user,
        'msg_form': msg_form,
        'msgs': msgs,
        'reply_form': reply_form,
        'replies': replies,
    }
    return render(request, 'chat.html', args)