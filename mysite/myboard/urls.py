from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    #view시스템이 아닌, 함수베이스로 이용
    path('', views.page),
    path('ajaxdel', views.ajaxdel),
    #get은 페이지번호를 요청했을때, 해당하는 페이지데이터를 한꺼번에 가져오는것
    path('ajaxget', views.ajaxget),

    path('<category>/<int:pk>/<mode>/', views.BoardView.as_view(), name="myboard"),
    #path('', lambda request: redirect('myboard', 'common', 0, 'list')),

]