from django.shortcuts import render,redirect
from .models import Member,History,Referral,Site
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    site = Site.objects.get(site='site')


    his_d = History.objects.filter(type='Deposit').order_by('-pk')[:10]
    his_w = History.objects.filter(type='Withdraw').order_by('-pk')[:10]
    cont = {'dep':his_d, 'wit':his_w,'site':site}

    if request.GET.get('ref'):
        viewer = request.GET.get('ref')
        request.session['ref'] = viewer
        return render(request,'home/index.html',cont)

    return render(request, 'home/index.html', cont)

def about(request):
    return render(request,'home/about.html')

def livepay(request):
    his_w = History.objects.filter(type='Withdraw').order_by('-pk')[:20]
    cont = {'wit':his_w}
    return render(request,'home/livepay.html',cont)

def terms(request):
    return render(request,'home/terms.html')

def faq(request):
    return render(request,'home/faq.html')

def signup(request):

    if 'name' in request.POST:
        name = request.POST['name']
        s_user = request.POST['user']
        user = s_user.strip()
        email = request.POST['email']
        password = request.POST['password']
        wallet = request.POST['wallet']

        request.session['mail']=email
        request.session['name'] = user

        if 'ref' in request.session:
            ref = request.session['ref']
        else:
            ref='none'

        new = Member(name=name, user=user, email=email,password=password,wallet=wallet, ref=ref)
        new.save()

        refs = Referral(user=ref, invited=user)
        refs.save()

        htm_msg = render_to_string('mail/welcome.html', {} , request)
        send_mail(
            subject='SURECOIN LTD WELCOME YOU',
            message='',
            from_email='support@surecoin.uk',
            recipient_list=[ request.session['mail'] ],
            html_message=htm_msg,
            fail_silently=True
        )

        info = 'A new user' +' '+ name
        htm_msg = render_to_string('mail/mail.html', {'msg':info} , request)
        send_mail(
            subject='NEW MEMBER',
            message='',
            from_email='support@surecoin.uk',
            recipient_list=['ssurecoin@gmail.com'],
            html_message=htm_msg,
            fail_silently=False
        )



        refh = Member.objects.get(user= request.session['name'])
        try:
            refm = Member.objects.get(user=refh.ref)


            info = 'you have added a new member' + ' ' + request.session[
                'name'] + ' via your referral link and will be rewarded %5 of payment of every active deposit made'
            htm_msg = render_to_string('mail/mail.html', {'msg': info}, request)
            send_mail(
                subject='You have a new direct signup on',
                message='',
                from_email='support@surecoin.uk',
                recipient_list=[refm.email],
                html_message=htm_msg,
                fail_silently=True
            )
        except ObjectDoesNotExist:
            return render(request, 'auth/success.html')

        if 'ref' in request.session:
            del request.session['ref']

        return render(request, 'auth/success.html')


    if 'ref' in request.session:
        ref = request.session['ref']
        rd = "you were referred by " + ref
        cont = {'ref': rd}

        # refm = Member.objects.get(user= request.session['ref'])
        # print(refm.email)
        # info='you have added a new member'+' '+ request.session['name'] +' via your referral link and will be rewarded %5 of payment of every active deposit made'
        # htm_msg = render_to_string('mail/mail.html', {'msg': info}, request)
        # send_mail(
        #     subject='You have a new direct signup on',
        #     message='',
        #     from_email='support@surecoin.uk',
        #     recipient_list=[refm.email],
        #     html_message=htm_msg,
        #     fail_silently=True
        # )
        return render(request,'auth/signup.html', cont)

        del request.session['ref']


    return render(request,'auth/signup.html')

def login(request):
    if request.method =='POST':
        l_user = request.POST['user']
        user = l_user.strip()
        password = request.POST['pword']

        try:

            luser = Member.objects.get(user=user)
            if password == luser.password:
                request.session['user']=user

                return redirect('/account/')
            else:
                cont = {'error': 'Password not correct'}
                return render(request, 'auth/login.html', cont)


        except ObjectDoesNotExist:
            cont={'error':'Account Not Found'}
            return render(request, 'auth/login.html', cont)

    if request.session.get('user'):
        try:
            if Member.objects.get(user=request.session['user']):
                user = Member.objects.get(user=request.session['user'])
                if user.pin:
                    return redirect('/pin/')
                else:
                    return redirect('/account/')
        except ObjectDoesNotExist:
            del request.session['user']
            return render(request, 'auth/login.html')

    return render(request,'auth/login.html')

def pin(request):
    if request.session['user']:
        user = Member.objects.get(user=request.session['user'])
        if request.method =='POST':
            pin = request.POST['pin']

            if user.pin == pin:
                return redirect('/account/')
        return render(request, 'auth/pin.html')


def account(request):

    if request.session['user']:
        user = Member.objects.get(user= request.session['user'])

        bal=user.balance + user.ref_bal +0.0
        act = user.active_deposit + 0.0
        t_dep = user.t_deposit + user.active_deposit

        if user.ref =='admins':
            admin='block'
        else:
            admin='none'
          # the auto pay command

        paynow = datetime.datetime.now()

        if user.payday.day == paynow.day:
            if int(user.pay_approve) > 5:
                user.balance = user.balance + user.profit
                user.t_profit =user.balance - user.active_deposit
                user.active_deposit = 0
                user.pay_approve =0
                user.profit = 0
                user.save()

        if user.pin == None:
            hid ='block'
            msg=''
        else:
            hid ='none'
            msg='TWO FACTOR PIN AUTHENTICATION IS SET ON'
        cont ={'user':user, 'bal':bal, 'act':act,'hid':hid, 'msg':msg, 'admin':admin,'t_dep':t_dep}
        return render(request,'user/account.html', cont)


def ref(request):
    if request.session['user']:
        ref = Referral.objects.filter(user=request.session['user'])
        user = Member.objects.get(user=request.session['user'])

        cont ={'refs':ref,'user':user}
        return render(request,'user/get.html',cont)

def deposit(request):
    if request.session['user']:
        if request.method =="POST":
            update =Member.objects.get(user=request.session['user'])
            site = Site.objects.get(site='site')

            update.active_deposit = request.POST['amt']
            update.duration = datetime.datetime.now()
            update.plan = request.POST['plan']


            if update.plan =='BEGINNER PLAN' or update.plan =='GROWTH PLAN' or update.plan=='VIP PLAN' :
                update.payday = datetime.datetime.now() + datetime.timedelta(days=1)
                du="24hrs Duration"
            elif update.plan =='CLASSIC PLAN' or update.plan =='ACTIVE PLAN':
                update.payday = datetime.datetime.now() + datetime.timedelta(days=2)
                du = "48hrs Duration"

            else:
                du=''

            if update.plan == 'BEGINNER PLAN':
                update.profit=(0.15 * int(update.active_deposit)) + int(update.active_deposit)
            if update.plan == 'ACTIVE PLAN':
                update.profit=(0.35 * int(update.active_deposit)) + int(update.active_deposit)
            if update.plan == 'GROWTH PLAN':
                update.profit=(0.60 * int(update.active_deposit)) + int(update.active_deposit)
            if update.plan == 'CLASSIC PLAN':
                update.profit=(0.90 * int(update.active_deposit)) + int(update.active_deposit)
            if update.plan == 'VIP PLAN':
                update.profit=(1.20 * int(update.active_deposit)) + int(update.active_deposit)

            update.deposit = int(update.deposit) + int(update.active_deposit)
            update.save()

            his = History(user=update.user, type='Deposit', his_date=datetime.datetime.now(), amount=update.active_deposit)
            his.save()

            try:
                ref = Member.objects.get(user=update.ref)
                ref.ref_bal=0.05* int(update.active_deposit)
                ref.save()
            except ObjectDoesNotExist:
                print('ref not found')

            cont = {'user':update,'du':du, 'site':site}
            return render(request, 'user/summary.html', cont)

        return render(request,'user/deposit.html')

def withdraw(request):
    if request.session['user']:
        user = Member.objects.get(user = request.session['user'])

        cont={'user':user}
        if request.method =="POST":
            amt = request.POST['amt']

            user.balance=int(user.balance) - float(amt)
            user.ref_bal = 0
            user.l_withraw = amt
            user.t_withdraw = int(user.t_withdraw) + float(amt)

            if user.balance < 0 :
                return render(request, 'user/failed.html')
            else:
                user.save()

                his = History(user=user.user, type='Withdraw', his_date=datetime.datetime.now(),
                              amount=amt, status='pending..')
                his.save()
                return render(request, 'user/success.html')

        return render(request,'user/withdraw.html',cont)

def history(request):
    if request.session['user']:
        his = History.objects.filter(user= request.session['user'])
        cont ={'His':his}
        return render(request,'user/history.html',cont)

def settings(request):
    if request.session['user']:
        user=Member.objects.get( user=request.session['user'] )

        if 'email' in request.POST:
            user.email = request.POST['update']
            user.save()
            msg = 'UPDATE WAS SUCCESSFUL'

            cont = {'user': user, 'msg': msg}
            return render(request, 'user/settings.html', cont)

        if 'user_name' in request.POST:
            user.user = request.POST['update']
            user.save()
            msg = 'UPDATE WAS SUCCESSFUL'
            cont = {'user': user, 'msg': msg}
            return render(request, 'user/settings.html', cont)

        if 'wallet' in request.POST:
            user.wallet = request.POST['update']
            user.save()
            msg = 'UPDATE WAS SUCCESSFUL'

            cont = {'user': user, 'msg': msg}
            return render(request, 'user/settings.html', cont)

        if 'pword' in request.POST:
            user.pword = request.POST['update']
            user.save()
            msg='UPDATE WAS SUCCESSFUL'

            cont = {'user': user, 'msg': msg}
            return render(request, 'user/settings.html', cont)

        cont= {'user':user}
        return render(request,'user/settings.html',cont)

def security(request):
    if request.session['user']:
        if request.method =='POST':
            user = Member.objects.get(user = request.session['user'])
            user.pin = request.POST['pin']
            user.save()
        return render(request, 'user/security.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('/')
    return redirect('/')

def admin(request):
    if request.session['user']:
        luser = Member.objects.get(user=request.session['user'])
        if luser.ref =='admins':
            mem = Member.objects.all().order_by('user')
            cont= {'mems':mem,}


            if 'title' in request.POST:
                user = request.GET.get('user')
                e_user = Member.objects.get(user=user)
                e_user.title = request.POST['title']
                e_user.message = request.POST['msg']
                e_user.save()

            if 'status' in request.POST:
                trans = request.POST['status']
                his = History.objects.get(pk=trans)
                his.status = 'successful'
                his.save()
                amt=his.amount

                user = request.GET.get('user')
                e_user = Member.objects.get(user=user)

                info='your payment has been successfully sent to your bitcoin wallet account :' +'\n'+ e_user.wallet + '\n' + 'Amount: $'+amt
                htm_msg = render_to_string('mail/mail.html', {'msg': info,'name':'Dear'+ e_user.name +' '+ e_user.user,'pp':'Thanks for your partnership'}, request)
                send_mail(
                    subject='WITHDRAW SUCCESSFUL',
                    message='',
                    from_email='support@surecoin.uk',
                    recipient_list=[e_user.email],
                    html_message=htm_msg,
                    fail_silently=True
                )


            if 'bal' in request.POST:
                user = request.GET.get('user')
                e_user = Member.objects.get(user=user)
                e_user.balance = e_user.balance + int(request.POST['update'])
                e_user.save()

            if 'a_deposit' in request.POST:
                user = request.GET.get('user')
                e_user = Member.objects.get(user=user)
                e_user.active_deposit = e_user.active_deposit + int(request.POST['update'])
                e_user.save()

            if 'subject' in request.POST:
                user = request.GET.get('user')
                e_user = Member.objects.get(user=user)

                sub = request.POST['subject']
                msgs = request.POST['msg']

                info = 'Hello' + ' ' + e_user.user + '\n' + msgs
                htm_msg = render_to_string('mail/mail.html', {'msg': info}, request)
                send_mail(
                    subject=sub,
                    message='',
                    from_email='support@surecoin.uk',
                    recipient_list=[e_user.email],
                    html_message=htm_msg,
                    fail_silently=True
                )

            if 'approve' in request.POST:
                luser = request.POST['memb']
                approve = request.POST['approve']

                e_user = Member.objects.get(user=luser)

                e_user.pay_approve = approve
                e_user.save()

                try:
                    pref = Member.objects.get(user=e_user.ref)
                    if e_user.ref:
                        sub='Referral Commission'
                        com=0.05 * int(approve)
                        name = 'Dear' + ' ' + pref.name + ' '+'('+pref.name+')'
                        msg = 'You have received a (5%) referral commission of $'+str(com)+' Bitcoin from '+e_user.name+' deposit.'
                        htm_msg = render_to_string('mail/mail.html', {'name': name, 'msg':msg}, request)
                        send_mail(
                            subject=sub,
                            message='',
                            from_email='support@surecoin.uk',
                            recipient_list=[pref.email],
                            html_message=htm_msg,
                            fail_silently=True
                        )
                except ObjectDoesNotExist:
                    print('next')


                his = History.objects.get(amount=approve, user=luser, status='pending..')
                his.status = 'successful'
                his.save()

                cont = {'mem': e_user}
                return render(request, 'admin/edit.html', cont)

            if request.GET.get('delete'):
                cont = {'mems': mem, 'error': 'user not found'}
                user = request.GET.get('delete')
                try:
                    del_user = Member.objects.get(user=user)
                    del_user.delete()

                    return redirect('/admin/', )

                except ObjectDoesNotExist:

                    return redirect('/admin/', )

            # if request.GET.get('approve'):
            #     try:
            #         user = request.GET.get('user')
            #         approve = request.GET.get('approve')
            #         e_user = Member.objects.get(user = user)
            #
            #         e_user.pay_approve = approve
            #         e_user.save()
            #
            #         his = History.objects.get(amount =approve, user=user, status='pending..')
            #         his.status = 'successful'
            #         his.save()
            #
            #         cont = {'mem':e_user}
            #         return render(request, 'admin/edit.html', cont)
            #
            #     except ObjectDoesNotExist:
            #         cont={'msg':'user not found'}
            #
            #         return render(request, 'admin/edit.html', cont)

            if request.GET.get('user'):
                try:
                    user = request.GET.get('user')
                    e_user = Member.objects.get(user = user)
                    his = History.objects.filter(user=user).order_by('-date')
                    cont = {'mem':e_user,'His':his}
                    return render(request, 'admin/edit.html', cont)

                except ObjectDoesNotExist:
                    cont={'msg':'user not found'}

                return render(request, 'admin/edit.html', cont)

            return render(request,'admin/admin.html',cont)

def site(request):
    if request.session['user']:
        user = Member.objects.get(user=request.session['user'])
        if user.ref == 'admins':
            site = Site.objects.get(site='site')
            cont={'site':site}

            if 'wallet' in request.POST:
                site.wallet = request.POST['update']
                site.save()

            if 'fb' in request.POST:
                site.fb = request.POST['update']
                site.save()

            if 'wh' in request.POST:
                site.wh = request.POST['update']
                site.save()

            if 'tel' in request.POST:
                site.tele = request.POST['update']
                site.save()
            if 'phone' in request.POST:
                site.phone = request.POST['update']
                site.save()

            if 'gmail' in request.POST:
                site.mail = request.POST['update']
                site.save()

            if 'adm' in request.POST:
                site.adm_access = request.POST['update']
                site.save()


            return render(request,'admin/site.html', cont)
