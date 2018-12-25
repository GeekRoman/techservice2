import datetime
from django.shortcuts import render, redirect
from .models import Comment, Master
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from mainApp.models import Area, Service
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from master_office.models import Order, OrderLine


@login_required
def orders(request):
    pass


class OrderList(ListView):
    model = Order


class OrderDetailView(DetailView):
    model = Order


def order(request, pk=1):
    comment_form = CommentForm()
    args = {}
    args['order'] = Order.objects.get(id=pk)
    args['comments'] = Comment.objects.filter(order=args['order'])
    args['form'] = comment_form
    args['username'] = request.user
    return render(request, 'master_office/order_detail.html', args)


def show_orderlines(request):
    args = {}
    # args.update(csrf(request))

    master = Master.objects.get(user_id=request.user.id)
    args['serveces'] = Service.objects.filter(area__in=master.areas.all)
    args['orderlines'] = OrderLine.objects.filter(service__in=args['serveces'].all).exclude(master__isnull=False)
    args['page'] = 'all_orderlines'
    return render(request, 'master_office/orderline_list.html', args)


# module.workflow_set.filter(trigger_roles__in=[self.role], allowed=True)
# eventgroups__in=u.groups.all())
def masters_orders(request):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)
    master = Master.objects.get(user_id=request.user.id)
    args['orderlines'] = OrderLine.objects.filter(master=master).filter(
        status=0)  # Order.objects.get(master.id = request.user.id)
    args['page'] = 'masters_orderlines'
    return render(request, 'master_office/orderline_list.html', args)


def masters_closed_orders(request):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)
    master = Master.objects.get(user_id=request.user.id)
    args['orderlines'] = OrderLine.objects.filter(master=master).filter(
        status=1)  # Order.objects.get(master.id = request.user.id)
    args['page'] = 'closed'
    return render(request, 'master_office/orderline_list.html', args)


def master_page(request, pk):
    args = {}
    master = Master.objects.get(user_id=request.user.id)
    args['master'] = master
    return render(request, 'master_office/master_page.html', args)


def take_order(request, pk):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)

    master = Master.objects.get(user_id=request.user.id)
    args['serveces'] = Service.objects.filter(area__in=master.areas.all)
    args['orderlines'] = OrderLine.objects.filter(service__in=args['serveces'].all).exclude(master__isnull=False)
    args['page'] = 'all_orderlines'
    line = OrderLine.objects.get(id=pk)
    area = Area.objects.get(id=line.service.area.id)
    current_orders = OrderLine.objects.filter(master=master).filter(status=0)
    current_orders_number = len(current_orders)
    if current_orders_number > 4:
        args['many_orders'] = "Вы не можете взяться за этот заказ! Сначала выполните предыдущие!!"
    else:
        line.master = master
    line.save()
    return render(request, 'master_office/orderline_list.html', args)


def close_order(request, pk):
    args = {}
    # args.update(csrf(request))
    # args['master'] = Master.objects.get(user=request.user)
    line = OrderLine.objects.get(id=pk)
    line.status = 1
    line.save()
    order = Order.objects.get(id = line.order_id)
    order_lines = OrderLine.objects.filter(order=order)
    is_closed = True

    for l in order_lines:
        if l.status == 0:
            is_closed = False
            print("not closed")

    if is_closed:
        order.status = 1
        order.end_date = datetime.datetime.now()
    order.save()
    # area = Area.objects.get(id = line.service.area.id)
    # line.master = master
    return masters_orders(request)
    # return render(request, 'master_office/orderline_list.html', args)


def addcomment(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rating = 0
            comment.author = request.user
            comment.order = Order.objects.get(id=pk)
            form.save()
            return redirect('master_orders-detail', pk=pk)
            # return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return render(request, 'registration/register.html', {'form': form})
