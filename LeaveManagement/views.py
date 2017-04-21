from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from .forms import *

@login_required
def index(request):
    return render(request,'lm/base.html')

@login_required
def applying_for_leave(request):
    if request.method == "GET":
        form = LeaveApplicationForm()
        leave_record = LeaveRecordDetail.objects.get(employee = request.user)
        approver = leave_record.reporting_manager
        return render(request, "lm/user/leave_application_form.html", {"form":form,"applicant":request.user, "approver":approver})

    if request.method == "POST":
        print(request.POST)
        return HttpResponse('skjfdnkjsdnkjsd')

