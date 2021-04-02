#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/8/9 10:43
@Author  : jiangliming
@File    : urls.py
"""

from django.contrib import admin
from django.urls import path,include
from App import views

app_name = 'axf'
urlpatterns = [
    path('hello/', views.hello, name='hello' ),
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)', views.market_with_params, name='market_with_params'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.check_user, name='check_user'),
    path('checkemail/', views.check_email, name='check_email'),
]