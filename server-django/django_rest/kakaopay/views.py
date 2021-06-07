from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "99a836422e698b27efd4eaec3c62fef7",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "german",    # 유저 아이디
            "item_name": "와퍼",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "5500",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/kakaopay/success",
            "cancel_url": "http://127.0.0.1:8000/kakaopay/cancel",
            "fail_url": "http://127.0.0.1:8000/kakaopay/fail",
        }

        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)
        print(res)

    return render(request, 'kakaopay/index.html')