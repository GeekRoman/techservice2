from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from client_office.forms import FeedbackForm
from master_office.forms import CommentForm
from master_office.models import Order, Comment, Master, OrderLine


def client_page(request):
    args = {}
    args['user'] = request.user
    return render(request, 'client_office/client_page.html', args)


def current_orders(request):
    user = request.user
    args = {}
    args['user'] = user
    args['orders'] = Order.objects.filter(client_id=user.pk).filter(status=0)
    args['title'] = "Текущие заказы"
    return render(request, 'client_office/current_orders.html', args)


def order(request, pk=1):
    comment_form = CommentForm()
    args = {}
    # args.update(csrf(request))
    order = Order.objects.get(id=pk)
    args['order'] = order
    args['comments'] = Comment.objects.filter(order=args['order'])
    args['username'] = request.user
    if order.status == 1:
        fb_form = FeedbackForm()
        args['fb_form'] = fb_form
    else:
        args['form'] = comment_form

    return render(request, 'client_office/order_detail.html', args)


def closed_orders(request):
    user = request.user
    args = {}
    args['user'] = user
    args['orders'] = Order.objects.filter(client_id=user.pk).filter(status=1)
    args['title'] = "Закрытые заказы"

    return render(request, 'client_office/current_orders.html', args)


def add_feedback(request, pk):
    args = {}
    # args.update(csrf(request))
    args['order'] = Order.objects.get(id=pk)
    args['comments'] = Comment.objects.filter(order=args['order'])
    args['username'] = request.user

    fb_form = FeedbackForm()
    args['fb_form'] = fb_form
    if request.POST:
        fb_form = FeedbackForm(request.POST)
        args['fb_form'] = fb_form
        if fb_form.is_valid():
            form_res = fb_form.save(False)
            cur_order = Order.objects.get(id=pk)
            cur_order.feedback = form_res.feedback
            cur_order.rating = form_res.rating
            cur_order.save()
            args['ready'] = 'Спасибо за вашу оценку! Вы помогаете нам стать лучше!'
            args['fb_form'] = FeedbackForm()
            lines = OrderLine.objects.filter(order=cur_order)
            for l in lines:
                masters_line = OrderLine.objects.filter(master=l.master).filter(status=1)
                m_rating = 0
                m_qty = 0
                for ml in masters_line:
                    m_rating += ml.order.rating
                    m_qty += 1
                l.master.rating = m_rating / m_qty
                l.master.save()
                print(l.master)
                print(m_rating / m_qty)
            return render(request, 'client_office/order_detail.html', args)

    return render(request, 'client_office/order_detail.html', args)


def addcomment(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rating = 0
            comment.author = request.user
            comment.order = Order.objects.get(id=pk)
            form.save()
            return redirect('client_office-detail', pk=pk)
            # return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return render(request, 'registration/register.html', {'form': form})
