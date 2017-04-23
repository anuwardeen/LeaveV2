from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from .forms import *

@login_required
def index(request):
    return render(request,'lm/base.html')

@login_required
def applying_for_leave(request):
    leave_record = LeaveRecordDetail.objects.get(employee=request.user)
    applicant = request.user
    approver = leave_record.reporting_manager
    if request.user.is_superuser:
        status = 'SA'
    elif request.user.is_staff :
        status = 'A'
    else:
        status = 'U'
    if request.method == "GET":
        form = LeaveApplicationForm()
        return render(request, "lm/leave_application_form.html", {"form":form,"applicant":applicant, "approver":approver,"status":status})

    if request.method == "POST":
        leave_type = request.POST.get('leave_type')
        num_of_days = int(request.POST.get('num_of_days'))
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        msg = request.POST.get('msg') or None
        try:
            LeaveApplication.objects.create(applicant = applicant, leave_type = leave_type, approver = approver,  number_of_days = num_of_days,from_date = from_date, to_date = to_date, additional_message = msg)
        except Exception as e:
            return HttpResponse("Error Occurred")
        else:
            if leave_type == "EL":
                leave_record.earned_leaves -= num_of_days
                leave_record.save()
            elif leave_type == "PL":
                leave_record.personal_leaves -= num_of_days
                leave_record.save()
            else:
                leave_record.sick_leaves -= num_of_days
                leave_record.save()
            return HttpResponse('skjfdnkjsdnkjsd')


@login_required
def responding_to_leave_application(request):

    if request.method == "GET":
        applications = LeaveApplication.objects.filter(approver = request.user)
        print(applications)
        return render(request, "lm/responding_to_application.html", {"applications":applications})