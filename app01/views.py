from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app01.forms import BookForm
from app01 import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        user_obj = models.User.objects.filter(username=user, password=pwd).first()
        if not user_obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
        # 登录成功,添加session信息
        request.session['is_login'] = True
        return redirect(reverse('index'))

    return render(request, 'login.html')


def book_list(request):
    if request.method == 'POST':  # 这里只让按照书名进行查询
        book_title = request.POST.get('my_query')  # 输入的书名
        print(book_title)
        all_book = models.Book.objects.filter(title=book_title)
    else:
        all_book = models.Book.objects.all()
    return render(request, 'book_list.html', {'all_book': all_book})


def book_change(request, edit_id=None):
    obj = models.Book.objects.filter(pk=edit_id).first()  # 注意要加first
    form_obj = BookForm(instance=obj)
    if request.method == 'POST':
        form_obj = BookForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('book_list'))
    return render(request, 'book_change.html', {'form_obj': form_obj})


def book_del(request, del_id):
    models.Book.objects.filter(pk=del_id).delete()
    return redirect(reverse('book_list'))


def book_query(request, del_id):
    models.Book.objects.filter(pk=del_id).delete()
    return redirect(reverse('book_list'))
