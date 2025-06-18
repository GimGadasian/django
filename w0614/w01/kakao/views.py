from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json

def oauth(request):
    code = request.GET.get('code')
    Content_Type = 'application/x-www-form-urlencoded;charset=utf-8'
    grant_type = 'authorization_code' 
    client_id = '3297ffd1c2ad18f8b58e15c4ffea1d1c'
    redirect_uri = 'http://localhost:8000/kakao/oauth'
    kakao_token_url = 'https://kauth.kakao.com/oauth/token'
    
    request_data = {
        'grant_type' : grant_type,
        'client_id' : client_id,
        'redirect_uri' : redirect_uri,
        'code' : code
    }
    
    token_headers = {
        'Content-Type':Content_Type
    }
    
    token_data = requests.post(kakao_token_url,data=request_data,headers=token_headers)
    token_json = token_data.json()
    access_token = token_json.get('access_token')
    
    kakao_profile_url = 'https://kapi.kakao.com/v2/user/me'
    auth_headers = {
        'Authorization':f'Bearer ${access_token}',
        'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
    }
     # 개인정보 요청
    user_info = requests.get(kakao_profile_url,headers=auth_headers)
    # json타입으로 변경
    user_info_json = user_info.json()
    kakao_account = user_info_json.get('kakao_account')
    kakao_profile = kakao_account.get('profile')
    kakao_nickname = kakao_profile.get('nickname')
    kakao_thumbnail_image_url = kakao_profile.get('thumbnail_image_url')
    kakao_profile_image_url = kakao_profile.get('profile_image_url')
    
    return HttpResponse(f'code : {code},<br>token json:{token_json}<br>닉네임:{kakao_nickname},<br>프로필 사진:{kakao_thumbnail_image_url}')
