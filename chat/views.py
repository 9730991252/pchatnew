from django.shortcuts import render, redirect, HttpResponseRedirect
from chat.models import *
from django.http import JsonResponse

# Create your views here.


def index(request):
    # My_group.objects.all().delete()
    group_name = Group_names.objects.filter(category='politic')
    return render(request, 'index.html', {'group_name': group_name, })


def my_group(request):
    if request.session.has_key('participants_mobile'):
        mobile = request.session['participants_mobile']
        p = Participants.objects.get(mobile=mobile)
        g = My_group.objects.filter(participant_id=p.id)
        return render(request, 'my_group.html', {'g': g})
    else:
        return redirect('participants_login')


def education_ssc(request):
    if request.session.has_key('participants_mobile'):
        mobile = request.session['participants_mobile']
        school = School.objects.all()
        return render(request, 'education_ssc.html', {'school': school})
    else:
        return redirect('participants_login')


def hsc_college(request):
    if request.session.has_key('participants_mobile'):
        mobile = request.session['participants_mobile']
        college = College.objects.all()
        return render(request, 'hsc_college.html', {'college': college})
    else:
        return redirect('participants_login')


def join_group(request):
    group_name = Group_names.objects.all()
    if request.session.has_key('participants_mobile'):
        mobile = request.session['participants_mobile']
        print(mobile)
        return render(request, 'all_group.html', {'group_name': group_name})
    else:
        return redirect('participants_login')


def participants_login(request):
    if request.method == "POST":
        number = request.POST.get("number")
        s = Participants.objects.filter(mobile=number)
        if s:
            request.session['participants_mobile'] = number
            return redirect('/')
        else:
            return redirect('participants_add')
    return render(request, 'participants_login.html')


def participants_add(request):
    village = Group_names.objects.filter(category='village')
    if request.method == "POST":
        name = request.POST.get("name")
        address_id = request.POST.get("address_id")
        mobile = request.POST.get("mobile")
        address = Group_names.objects.get(id=address_id)
        address = address.name
        Participants(name=name, address=address, mobile=mobile,
                     village_id=address_id).save()
        return redirect('join_group')
    return render(request, 'participants_add.html', {'village': village})


def group_name(request, group_name):
    if request.session.has_key('participants_mobile'):
        mobile = request.session['participants_mobile']
        participant = Participants.objects.get(mobile=mobile)
        group = Group_names.objects.get(id=group_name)
        chat = []
        chat = Chat.objects.filter(group_id=group_name)
        mg = My_group(group_id=group.id, participant_id=participant.id)
        data = {
            'g_name': group.name,
            'participant_name': participant.name,
            'participant_address': participant.address,
            'participant_id': participant.id,
            'village_id': participant.village_id,
            'ssc_year': group.ssc_year
        }
        m = My_group.objects.filter(
            group_id=group.id, participant_id=participant.id).exists()
        if m == False:
            mg.save()
        return render(request, 'group_name.html', {'groupname': group_name, 'data': data, 'chat': chat})
    else:
        return redirect('participants_login')


def select_year_group(request):
    mobile = request.session['participants_mobile']
    p = Participants.objects.get(mobile=mobile)
    p_id = p.id
    # print(p.id)
    if request.method == 'GET':
        school_id = request.GET['school_id']
        ss_year = request.GET['ss_year']
        # print(ss_year)
        school = School.objects.get(id=school_id)
        name = school.name
        sg = Group_names.objects.filter(
            ssc_school_id=school_id, ssc_year=ss_year).exists()
        # print(sg)
        if sg == False:
            Group_names(name=name, category='education',
                        ssc_school_id=school_id, ssc_year=ss_year).save()
            g = Group_names.objects.get(
                ssc_school_id=school_id, ssc_year=ss_year)
            gid = g.id
            My_group(group_id=gid, participant_id=p_id).save()
        else:
            sg = Group_names.objects.filter(
                ssc_school_id=school_id, ssc_year=ss_year).exists()
            if sg == True:
                g = Group_names.objects.get(
                    ssc_school_id=school_id, ssc_year=ss_year)
                gid = g.id
                mg = My_group.objects.filter(
                    group_id=gid, participant_id=p_id).exists()
                if mg == False:
                    g = Group_names.objects.get(
                        ssc_school_id=school_id, ssc_year=ss_year)
                    gid = g.id
                    print(gid)
                    My_group(group_id=gid, participant_id=p_id).save()

        return JsonResponse({'status': 1, })
    else:
        return JsonResponse({'status': 0, })


def select_year_hsc(request):
    mobile = request.session['participants_mobile']
    p = Participants.objects.get(mobile=mobile)
    p_id = p.id
    # print(p.id)
    if request.method == 'GET':
        college_id = request.GET['college_id']
        hsc_year = request.GET['hsc_year']
        # print(ss_year)
        college = College.objects.get(id=college_id)
        name = college.name
        sg = Group_names.objects.filter(hsc_id=college_id, ssc_year=hsc_year).exists()
        # print(sg)
        if sg == False:
            Group_names(name=name, category='education',hsc_id=college_id, ssc_year=hsc_year).save()
            g = Group_names.objects.get(hsc_id=college_id, ssc_year=hsc_year)
            gid = g.id
            My_group(group_id=gid, participant_id=p_id).save()
        else:
            sg = Group_names.objects.filter(hsc_id=college_id, ssc_year=hsc_year).exists()
            if sg == True:
                g = Group_names.objects.get(hsc_id=college_id, ssc_year=hsc_year)
                gid = g.id
                mg = My_group.objects.filter(group_id=gid, participant_id=p_id).exists()
                if mg == False:
                    g = Group_names.objects.get(hsc_id=college_id, ssc_year=hsc_year)
                    gid = g.id
                    print(gid)
                    My_group(group_id=gid, participant_id=p_id).save()

        return JsonResponse({'status': 1, })
    else:
        return JsonResponse({'status': 0, })


def add_new_school(request):
    mobile = request.session['participants_mobile']
    p = Participants.objects.get(mobile=mobile)
    a_name = p.name
    if request.method == "GET":
        name = request.GET['name']
        address = request.GET['address']
        School(name=name, address=address, added_by=a_name).save()
        return JsonResponse({'status': 1, })
    else:
        return JsonResponse({'status': 0})


def add_new_college(request):
    mobile = request.session['participants_mobile']
    p = Participants.objects.get(mobile=mobile)
    a_name = p.name
    if request.method == "GET":
        name = request.GET['name']
        address = request.GET['address']
        College(name=name, address=address, added_by=a_name).save()
        return JsonResponse({'status': 1, })
    else:
        return JsonResponse({'status': 0})
