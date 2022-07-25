import sys
import json
#import xlsxwriter
import pandas as pd
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from debtapp.utils import getSPCall
from django.shortcuts import redirect
from django.utils.formats import date_format
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http.response import JsonResponse,HttpResponse

#from debtapp import models as debt

@login_required
def index(request):
    context = {'companies':getSPCall('company',['sjayaraman'])}
    return render(request, 'dashboard/dashboard.html',context)

@login_required
def changecompany(request,companyID):
    request.session['comp_id'] = companyID
    dsys = getSPCall('defaultsystem',[companyID])
    for sys in dsys:
        request.session['CurrentDate'] = sys[0]
        request.session['StartOfPrevMonth'] = sys[1]
        request.session['EndOfPrevMonth'] = sys[2]
        request.session['EndOfNextMonth'] = sys[3]
        request.session['CurrPeriodStartDt'] = date_format(sys[4])
        request.session['CurrPeriodEndDt'] = date_format(sys[5])
        request.session['EndOfLastQtr'] = sys[6]
        request.session['FYFirstDay'] = sys[7]
        request.session['FYLastDay'] = sys[8]
        request.session['HOSupplierID'] = sys[9]
        request.session['SMSFrom'] = sys[10]
        request.session['VaultServices'] = sys[11]
        request.session['VaultPercentage'] = "{:.2f}".format(sys[12])
        request.session['CompanyName_Short'] = sys[13]
        request.session['ABA_BankCode'] = sys[14]
        request.session['CurrencyID'] = sys[15]
    return redirect('/')

@login_required
def agingdetail(request):
    if(request.GET.get('debtor')):
        context = {
            'companies':getSPCall('company',['sjayaraman']),
            'members':getSPCall('memberlist',['[ALL]',False,'IJC']),
            'memberdetail':getSPCall('memberdetail',[request.GET.get('debtor'),request.session['comp_id']]),
            'agingsummary':getSPCall('agingsummary',[request.GET.get('debtor'),request.session['comp_id']]),
            'latestdetail':getSPCall('latestdetail',[request.GET.get('debtor'),request.session['comp_id']]),
            'systemparam':getSPCall('systemparam',['AdtnlFilter_Coll_AR',request.session['comp_id']]),
            'supplier':getSPCall('supplier',[request.GET.get('debtor'),False,request.session['comp_id']]),
            'transaction_open':getSPCall('transaction_open',[request.GET.get('debtor'),False,False,'ALL',request.session['comp_id']])
        }
        print(context)
    else:
        context = {'members':getSPCall('memberlist',['[ALL]',False,'IJC'])}
    #context = {'members':getSPCall('memberlist',['[ALL]',False,'IJC'])}
    return render(request, 'dashboard/agingdetail.html',context)

@login_required
def users(request):
    context = {'users':User.objects.values()}
    #print (context)
    return render(request, 'dashboard/users.html',context)

@login_required
def getfile(request):
    import csv
    debtor = request.POST.get('exp_debtor')
    trans_status = request.POST.get('exp_trans')
    translist = getSPCall('transaction_open',[debtor,False,True,trans_status,request.session['comp_id']])
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['Document#','Doc Type',	'Description',	'Supplier Name',	'Doc Dt',	'Due Dt',	'Overdue Days',	'Ex GST',	'GST',	'Inc GST',	'Curr Amt',	'Disputed/Voided',	'Posted Dt',	'Batch #'])    
    print(request.POST.getlist('expfil[]'))
    for ts in translist:
        for array_obj in request.POST.getlist('expfil[]'):
            if(array_obj.startswith('[')):
                if(array_obj == '[Exclude $0.00]' and ts[11] > 0):
                    writer.writerow([ts[0], ts[1], ts[2], ts[4], ts[5], ts[6], ts[7], ts[8], ts[9], ts[10], ts[11], ts[12], ts[13], ts[14], ts[15]])

                if(array_obj == '[Load Overdue]' and ts[7] > 0):
                    writer.writerow([ts[0], ts[1], ts[2], ts[4], ts[5], ts[6], ts[7], ts[8], ts[9], ts[10], ts[11], ts[12], ts[13], ts[14], ts[15]])

                if(array_obj == '[Load Invoices]' and ts[1] == 'Invoice'):
                    writer.writerow([ts[0], ts[1], ts[2], ts[4], ts[5], ts[6], ts[7], ts[8], ts[9], ts[10], ts[11], ts[12], ts[13], ts[14], ts[15]])
                if(array_obj == '[Load Credits/Payments]' and (ts[1] == 'Credit' or ts[1]=='Payment')):
                    writer.writerow([ts[0], ts[1], ts[2], ts[4], ts[5], ts[6], ts[7], ts[8], ts[9], ts[10], ts[11], ts[12], ts[13], ts[14], ts[15]])
            else:
                if(array_obj == ts[3]):
                    writer.writerow([ts[0], ts[1], ts[2], ts[4], ts[5], ts[6], ts[7], ts[8], ts[9], ts[10], ts[11], ts[12], ts[13], ts[14], ts[15]])
    return response
    #return HttpResponse(request.POST.get('exp_debtor'))
    #response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
    #response['Content-Disposition'] = 'attachment; filename="demo.xlsx"'  
    #workbook = xlsxwriter.Workbook('demo.xlsx')
    #writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
    #writer.save()
    #pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
    #worksheet = workbook.add_worksheet()

    #worksheet.write(0, 0, 1234)     # Writes an int
    #worksheet.write(1, 0, 1234.56)  # Writes a float
    #worksheet.write(2, 0, 'Hello')  # Writes a string
    #worksheet.write(3, 0, None)     # Writes None
    #worksheet.write(4, 0, True)     # Writes a bool

    #workbook.close()
    #import csv
    #response = HttpResponse(content_type='text/csv')  
    #response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    #writer = csv.writer(response)  
    #writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    #writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    #return response  

@login_required
def sm(request):
   res = send_mail("test email from debtor app", "comment tu vas?", "phpexpert2021@gmail.com", ['dileep@ennomail.com'])
   return HttpResponse('%s'%res)
   
@login_required
def ajaxreq(request):
    if(request.GET.get('type') == 'setdebtor'):
        dt = request.GET.get('info')
        context = {
            'memberdetail':getSPCall('memberdetail',[request.GET.get('info'),request.session['comp_id']]),
            'agingsummary':getSPCall('agingsummary',[request.GET.get('info'),request.session['comp_id']]),
            'latestdetail':getSPCall('latestdetail',[request.GET.get('info'),request.session['comp_id']]),
            'systemparam':getSPCall('systemparam',['AdtnlFilter_Coll_AR',request.session['comp_id']]),
            'vaultdropdown':getSPCall('systemparam',['AmountLabel_AR_Detail',request.session['comp_id']]),
            'supplier':getSPCall('supplier',[request.GET.get('info'),False,request.session['comp_id']]),
            'transaction_open':getSPCall('transaction_open',[request.GET.get('info'),False,False,'ALL',request.session['comp_id']])
        }
        
        return JsonResponse({'success':True, 'data':context})
    if(request.GET.get('type') == 'transtype'):
        context = {
                'transaction_list':getSPCall('transaction_open',[request.GET.get('debtor'),False,True,request.GET.get('trans'),request.session['comp_id']])
            }
        #if(request.GET.get('trans') == 'history'):
         #   context = {
          #      'transaction_list':getSPCall('transaction_open',[request.GET.get('debtor'),False,True,'HIST',request.session['comp_id']])
           # }
        #if(request.GET.get('trans') == 'open'):
         #   context = {
          #      'transaction_list':getSPCall('transaction_open',[request.GET.get('debtor'),False,False,'ALL',request.session['comp_id']])
           # }
        return JsonResponse({'success':True, 'data':context})
    if(request.GET.get('type') == 'requestcopy'):
        emailtemp = getSPCall('selecttemplate',['Email', 'InvoiceCopy', 'Supplier', request.session['comp_id']])
        if(len(emailtemp) == 0):
            msg = "The email template for 'InvoiceCopy' doessn't exist and can't proceed further"
            return JsonResponse({'success':False, 'data':'noexist'})
        else:
            mname = request.GET.get('memname').split(" - ")
            subject = emailtemp[0][1]
            subject = subject.replace("~memberid~", request.GET.get('info'))
            subject = subject.replace("~membername~", mname[1])

            body = emailtemp[0][3]
            senderinfo = getSPCall('systemparam',['email_ar',request.session['comp_id']])
            sup = getSPCall('suppliercontact',[request.GET.get('chdata'),request.session['comp_id']])
            body = body.replace("~firstname~",sup[0][0])
            cp = 'copy'
            body = body.replace("~singularplural~",cp)
            finalAr = []

            transdata = request.GET.get('sopt').split('___')
            transtbl = "<table border='1'><tr><th>Document#</th><th>Doc Type</th><th>Description</th><th>Supplier Name</th><th>Doc Dt</th><th>Due Dt</th><th>Overdue Days</th><th>Ex GST</th><th>GST</th><th>Inc GST</th><th>Curr Amt</th><th>Disputed/ Voided</th><th>Posted Dt</th><th>Batch #</th></tr>"
            #Some error in split array
            for trs in transdata:
                trsd = trs.split('++++')
                transtbl = transtbl+"<tr><td>"+trsd[0]+"</td><td>"+trsd[1]+"</td><td>"+trsd[2]+"</td><td>"+trsd[3]+"</td><td>"+trsd[4]+"</td><td>"+trsd[5]+"</td><td>"+trsd[6]+"</td><td>"+trsd[7]+"</td><td>"+trsd[8]+"</td><td>"+trsd[9]+"</td><td>"+trsd[10]+"</td><td>"+trsd[11]+"</td><td>"+trsd[12]+"</td><td>"+trsd[13]+"</td></tr>"

            transtbl = transtbl+"</table>"
            body = body.replace("~transtable~",transtbl)

            #Get Receiver of email
            
            res = send_mail(subject, body, senderinfo[0][0], ['dileep@ennomail.com'],auth_user=senderinfo[0][0], auth_password=senderinfo[0][1], html_message=body)
            #return HttpResponse('%s'%res)
            return JsonResponse({'success':True, 'data':res})

        