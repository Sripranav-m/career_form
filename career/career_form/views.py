from django.shortcuts import render,redirect 
from .models import information
import datetime

def career_form(request):
	if request.method=="POST":
		x=datetime.datetime.now()
		x=x.strftime("%c")
		f_name=request.POST.get("firstname")
		l_name=request.POST.get("lastname")
		gender=request.POST.get("gender")
		dob=request.POST.get("dateofbirth")
		education=xstr(request.POST.get("degree"))+"  at  "+xstr(request.POST.get("college"))+"  with apercentage of  "+xstr(request.POST.get("percentage"))
		email=request.POST.get("email")
		p_num=request.POST.get("phonenumber") 
		address=xstr(request.POST.get("addressline1"))+"  ,  "+xstr(request.POST.get("addressline2"))+"  . CITY :  "+xstr(request.POST.get("city"))+" . STATE:  "+xstr(request.POST.get("state"))+"  . COUNTRY:  "+xstr(request.POST.get("country"))+" . POSTALCODE:  "+xstr(request.POST.get("postalcode"))
		skills=request.POST.get("skill1")+"  ,  "+xstr(request.POST.get("skill2"))+"  ,  "+xstr(request.POST.get("skill3"))+"  ,   "+xstr(request.POST.get("otherskills"))
		texp=xstr(request.POST.get("tey"))+" YEARS , "+xstr(request.POST.get("tem"))+" MONTHS ."
		if xstr(request.POST.get("tey"))==" " and xstr(request.POST.get("tem"))==" ":
			texp="----------"
		rtexp=xstr(request.POST.get("rtey"))+" YEARS , "+xstr(request.POST.get("rtem"))+" MONTHS ."
		if xstr(request.POST.get("rtey"))==" " and xstr(request.POST.get("rtem"))==" ":
			rtexp="----------"
		cctc=xstr(request.POST.get("cctc"))
		ectc=xstr(request.POST.get("ectc"))
		np=xstr(request.POST.get("noticeperiod"))
		reason=xstr(request.POST.get("reason"))
		resume=request.FILES.get("resume")
		object=information(date=x,firstname=f_name,lastname=l_name,gender=gender,dateofbirth=dob,education=education,email=email,phonenumber=p_num,address=address,skills=skills,total_experience=texp,realtime_experience=rtexp,current_ctc=cctc,expected_ctc=ectc,noticeperiod=np,reason=reason,resume=resume)
		object.save()
		return redirect(career_form)
	else:
		return render(request,"form1.html",{})

def xstr(s):
    if s is None:
        return ' '
    return str(s)