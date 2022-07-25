from asyncio.windows_events import NULL
import sys
import json
#import xlsxwriter
import xlwt
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
    debtor = request.POST.get('exp_debtor')
    trans_status = request.POST.get('exp_trans')
    #translist = getSPCall('transaction_open',[debtor,False,True,trans_status,request.session['comp_id']])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="debtreport.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Transactions') # this will make a sheet named Users Data

    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Document#','Doc Type',	'Description',	'Supplier Name',	'Doc Dt',	'Due Dt',	'Overdue Days',	'Ex GST',	'GST',	'Inc GST',	'Curr Amt',	'Disputed/Voided',	'Posted Dt',	'Batch #',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = getSPCall('transaction_open',[debtor,False,True,trans_status,request.session['comp_id']])
    for row in rows:
        row_num += 1
        if(row[7] is None):
            ox = 0
        else:
            ox = row[7]

        ws.write(row_num, 0, row[0], font_style)
        ws.write(row_num, 1, row[1], font_style)
        ws.write(row_num, 2, row[2], font_style)
        ws.write(row_num, 3, row[4], font_style)
        ws.write(row_num, 4, row[5], date_format)
        ws.write(row_num, 5, row[6], date_format)
        ws.write(row_num, 6, ox, font_style)
        ws.write(row_num, 7, row[8], font_style)
        ws.write(row_num, 8, row[9], font_style)
        ws.write(row_num, 9, row[10], font_style)
        ws.write(row_num, 10, row[11], font_style)
        ws.write(row_num, 11, row[12], font_style)
        ws.write(row_num, 12, row[14], date_format)
        ws.write(row_num, 13, row[15], font_style)
       
    wb.save(response)

    return response  
    
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
            mynew = []

            transdata = request.GET.get('sopt').split('___')
            
            for trs in transdata:
                trsd = trs.split('++++')
                finalAr.append(trsd[1])
                arx = []
                for tx in trsd:
                    arx.append(tx)
                mynew.append(arx)

            print(mynew)
            transtbl = "<table border='1'><tr><th>Invoice#</th></tr>"
            #Some error in split array
            for fr in finalAr:
                transtbl = transtbl+"<tr><td>"+fr+"</td></tr>"    
            
            transtbl = transtbl+"</table>"
            body = body.replace("~transtable~",transtbl)
            #res = send_mail(subject, body, senderinfo[0][0], ['dileep@ennomail.com'],auth_user=senderinfo[0][0], auth_password=senderinfo[0][1], html_message=body)
            return JsonResponse({'success':True, 'data':'hi'})

    if(request.GET.get('type') == 'overdue'):
        emailtemp = getSPCall('selecttemplate',['Email', 'OverdueInvoices', 'Member', request.session['comp_id']])
        if(len(emailtemp) == 0):
            msg = "The email template for 'overdue' doessn't exist and can't proceed further"
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
            #finalAr = []

            transdata = request.GET.get('sopt').split('___')
            
            #for trs in transdata:
                #trsd = trs.split('++++')
                #finalAr.append(trsd[1])
                #arx = []
                #for tx in trsd:
                 #   arx.append(tx)
                #finalAr.append(arx)

            transtbl = "<table border='1'><tr><th>Invoice#</th><th>Invoice Dt</th><th>Supplier</th><th>Duedate</th></tr>"
            #Some error in split array
            for trs in transdata:
                trsd = trs.split('++++')
                transtbl = transtbl+"<tr><td>"+trsd[0]+"</td><td>"+trsd[3]+"</td><td>"+trsd[2]+"</td><td>"+trsd[4]+"</td></tr>"    
            
            transtbl = transtbl+"</table>"
            body = body.replace("~transtable~",transtbl)

            #Get Receiver of email
            
            #res = body
            res = send_mail(subject, body, senderinfo[0][0], ['dileep@ennomail.com'],auth_user=senderinfo[0][0], auth_password=senderinfo[0][1], html_message=body)
            #return HttpResponse('%s'%res)
            return JsonResponse({'success':True, 'data':res})

        