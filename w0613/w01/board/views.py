from django.shortcuts import render
from board.models import Board
from comment.models import Comment


def view(request, bno):
    qs = Board.objects.get(bno=bno)
    c_qs = Comment.objects.filter(board=qs).order_by('-cno')
    context = {'board':qs, 'clist':c_qs}
    return render(request,'board/view.html', context)

def list(request):
    qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    context = {'list':qs}
    return render(request,'board/list.html', context)

