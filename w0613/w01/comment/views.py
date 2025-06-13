from django.shortcuts import render
from django.http import JsonResponse
from comment.models import Comment
from member.models import Member
from board.models import Board

# 하단 댓글 수정저장
def cupdate(request):
    cno = request.POST.get('cno')
    ccontent = request.POST.get('ccontent')
    print('넘어온 데이터: ', cno)
    
    # db 수정
    qs = Comment.objects.get(cno=cno)
    qs.ccontent = ccontent
    qs.save()
    # Json 타입으로 변경
    json_qs = list(Comment.objects.filter(cno=cno).values())
    context = {'result':'success', 'comment':json_qs}
    return JsonResponse(context)

# 하단 댓글 삭제
def cdelete(request):
    cno = request.POST.get('cno')
    print('넘어온 데이터: ', cno)
    
    # db 삭제
    qs = Comment.objects.get(cno=cno).delete()
    context = {'result':'success'}
    return JsonResponse(context)

# 하단 댓글 등록
def cwrite(request):
    id = request.POST.get('id')
    bno = request.POST.get('bno')
    cpw = request.POST.get('cpw')
    ccontent = request.POST.get('ccontent')
    print('넘어온 데이터: ', id, cpw, ccontent)
    member = Member.objects.get(id=id)
    board = Board.objects.get(bno=bno)
    # db 저장
    qs = Comment.objects.create(member=member, board=board, cpw=cpw, ccontent=ccontent)
    # Json type 변경
    json_qs = list(Comment.objects.filter(cno=qs.cno).values())
    # json_qs = list(Comment.objects.filter(cno=5,ctitle='제목').values())
    print(json_qs)
    context = {'result':'success', 'comment':json_qs}
    return JsonResponse(context)


# 하단 댓글: Json type
def clist(request):
    context = {'result':'success'}
    return JsonResponse(context)
