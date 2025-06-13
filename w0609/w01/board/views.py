from django.shortcuts import render, redirect
from board.models import Board
from django.core.paginator import Paginator
from member.models import Member
from django.db.models import F, Q
from comment.models import Comment

def view(request, bno):
    print("넘어온 데이터 : ", bno)
    qs = Board.objects.filter(bno=bno)
    if not qs.exists():
        return render(request, 'board/view.html', {'error': '해당 게시글이 존재하지 않습니다.'})

    board = qs[0]
    pre_qs = Board.objects.filter(
        Q(notice__lte=board.notice, bgroup__lt=board.bgroup, bstep__lte=board.bstep) |
        Q(notice=board.notice, bgroup=board.bgroup, bstep__gt=board.bstep)
    ).order_by('-notice', '-bgroup', 'bstep').first()
    next_qs = Board.objects.filter(
        Q(notice__gte=board.notice, bgroup__gt=board.bgroup, bstep__gte=board.bstep) |
        Q(notice=board.notice, bgroup=board.bgroup, bstep__lt=board.bstep)
    ).order_by('notice', 'bgroup', '-bstep').first()

    print('현재글 : ', board.bno)
    print('이전글 : ', pre_qs.bno if pre_qs else None)
    print('다음글 : ', next_qs.bno if next_qs else None)
    
    # 하단댓글
    c_qs = Comment.objects.filter(board=qs[0]).order_by('-cno')
    print("하단댓글 데이터 : ",c_qs)
    
    context = {'board':qs[0],'pre_board':pre_qs,'next_board':next_qs,'comment':c_qs}
    return render(request,'board/view.html',context)

def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        # id = request.session.get('session_id') # session에서 가져오기
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        notice = request.POST.get('notice',0)
        notice_value = 1 if notice == 'on' else 0
        print("넘어온 데이터 : ",id,btitle,bcontent,bfile,notice)
        ### db저장
        qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile,notice=notice_value)
        # 답글달기할때 필요
        qs.bgroup = qs.bno
        qs.save()        
        return redirect('/board/list/')

def list(request):
    # 페이지번호가 있어야 함.
    page = int(request.GET.get('page',1))
    qs = Board.objects.all().order_by('-notice','-bgroup','bstep')
    paginator = Paginator(qs,10)    # 10개씩 분리해서 가져옴. 1,2,...10페이지생성
    list = paginator.get_page(page) # 1페이지 가져오기 -> 10개 게시글
    context = {'list':list,'page':page}
    return render(request,'board/list.html',context)