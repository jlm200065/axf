from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from App.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow
from App.models import FoodType, Goods
from App.models import AXFUser

# Create your views here.
from App.views_constant import ALL_TYPE, ORDER_TOTAL, ORDER_PRICE_UP, ORDER_PRICE_DOWN, ORDER_SALE_UP, ORDER_SALE_DOWN, \
    HTTP_OK, HTTP_USER_EXIST, EMAIL_OK, EMAIL_EXIST
from App.views_helper import hash_str


def hello(request):
    return HttpResponse("hello!")


def home(request):
    main_wheels = MainWheel.objects.all()
    main_navs = MainNav.objects.all()
    main_mustbuys = MainMustBuy.objects.all()
    main_shops = MainShop.objects.all()
    main_shop0_1 = main_shops[0:1]
    main_shop1_3 = main_shops[1:3]
    main_shop3_7 = main_shops[3:7]
    main_shop7_11 = main_shops[7:11]
    main_shows = MainShow.objects.all()

    data = {
        'title': '首页',
        'main_wheels': main_wheels,
        'main_navs': main_navs,
        'main_mustbuys': main_mustbuys,
        'main_shop0_1': main_shop0_1,
        'main_shop1_3': main_shop1_3,
        'main_shop3_7': main_shop3_7,
        'main_shop7_11': main_shop7_11,
        'main_shows': main_shows,

    }
    return render(request, 'main/home.html', context=data)


def market(request):
    return redirect(reverse('axf:market_with_params', kwargs={
        "typeid": 103541,
        "childcid": 0,
        "order_rule": 0,
       
    }))


def market_with_params(request, typeid, childcid, order_rule, goods_list=None):
    foodtypes = FoodType.objects.all()
    good_list = Goods.objects.filter(categoryid=typeid)
    
    if childcid == ALL_TYPE:
        pass
    else:
        good_list = good_list.filter(childcid=childcid)
    print(typeid)


    if order_rule == ORDER_TOTAL:
        pass
    elif order_rule == ORDER_PRICE_UP:
        good_list = good_list.order_by("price")
    elif order_rule == ORDER_PRICE_DOWN:
        good_list = good_list.order_by("-price")
    elif order_rule == ORDER_SALE_UP:
        good_list = good_list.order_by("productnum")
    elif order_rule == ORDER_SALE_DOWN:
        good_list = good_list.order_by("-productnum")


    foodtype = foodtypes.get(typeid=typeid)

    """
        全部分类:0#进口水果:103534#国产水果:103533
        切割  #
            ['全部分类:0', '进口水果:103534', '国产水果:103533']
        切割  :
            [[全部分类, 0], [进口水果, 103534], [国产水果, 103533]]

    """
    foodtypechildnames = foodtype.childtypenames

    foodtypechildname_list = foodtypechildnames.split("#")

    foodtype_childname_list = []

    for foodtypechildname in foodtypechildname_list:
        foodtype_childname_list.append(foodtypechildname.split(":"))

    order_rule_list = [
        ['综合排序', ORDER_TOTAL],
        ['价格升序', ORDER_PRICE_UP],
        ['价格降序', ORDER_PRICE_DOWN],
        ['销量升序', ORDER_SALE_UP],
        ['销量降序', ORDER_SALE_DOWN],
    ]


    data = {
        'title': '闪购',
        'foodtypes': foodtypes,
        'good_list': good_list,
        'typeid': int(typeid),
        'foodtype_childname_list': foodtype_childname_list,
        'childcid': childcid,
        'order_rule_view': order_rule,
        'order_rule_list':order_rule_list

    }
    return render(request, 'main/market.html', context=data)


def cart(request):
    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')


def register(request):
    if request.method == "GET":
        data = {
            "title": "注册",
        }
        return render(request, 'user/register.html', context=data)
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        icon = request.FILES.get("icon")

        password = make_password(password)
        user = AXFUser()
        user.u_username = username
        user.u_email = email
        user.u_password = password
        user.u_icon = icon
        user.save()

        return redirect(reverse("axf:login"))



def check_user(request):

    username = request.GET.get("username")


    users = AXFUser.objects.filter(u_username=username)

    data = {
        "status": HTTP_OK,
        "msg": 'user can use'
    }


    if users.exists():
        data['status'] = HTTP_USER_EXIST
        data['msg'] = 'user already exist'
    else:
        pass

    return JsonResponse(data=data)


def check_email(request):
    email = request.GET.get("email")
    emails = AXFUser.objects.filter(u_email=email)
    data = {
        "status": EMAIL_OK,
        "msg": 'email can use'
    }

    if emails.exists():
        data['status'] = EMAIL_EXIST
        data['msg'] = 'email already exist'
    else:
        pass
    return JsonResponse(data=data)




def login(request):
    if request.method == "GET":

        error_message = request.session.get('error_message')

        data = {

            "title": "登录"
        }

        if error_message:
            del request.session['error_message']
            data['error_message'] = error_message

        return render(request, 'user/login.html', context=data)

    elif request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        users = AXFUser.objects.filter(u_username=username)

        if users.exists():
            user = users.first()

            if check_password(password, user.u_password):

                if user.is_active:

                    request.session['user_id'] = user.id

                    return redirect(reverse('axf:mine'))
                else:
                    print('not activate')
                    request.session['error_message'] = 'not activate'
                    return redirect(reverse('axf:login'))
            else:
                print('密码错误')
                request.session['error_message'] = 'password error'
                return redirect(reverse('axf:login'))
        print('用户不存在')
        request.session['error_message'] = 'user does not exist'
        return redirect(reverse('axf:login'))