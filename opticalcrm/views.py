from django.shortcuts import render,redirect,HttpResponseRedirect
from opticalcrm import models , forms
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth.models import auth, User


# Create your views here.
# ====================================================
# ====================== Login =======================
# ====================================================
def index(request):
    return render(request,'index.html')
    
def sbologin(request):
    if request.method == "POST":
        fm=forms.LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return redirect('AfterLogin')
    else:
        fm=forms.LoginForm()
    return render(request, 'login.html', {'form': fm})

def AfterLogin(request):
    if request.user.is_superuser == True:
        return redirect('main')


def sbologout(request):
    logout(request)
    return HttpResponseRedirect('/')

# ====================================================
# ==================== Dashboard =====================
# ====================================================
def fun(request):
    if request.user.is_authenticated:
        customers_count = models.customer_details.objects.all().count()
        pbarcode_count = models.barcode_list.objects.filter(status='no').count()
        sales_count = models.invoice.objects.all().count()
        pcount = models.invoice_products.objects.all().count()
        revenue = models.invoice.objects.all()
        revrange = sales_count + 1
        pd = pcount + 1
        total_payable_amount = 0
        total_profit = 0
        total_pending = 0
        pamount = 0
        for i in range(1,revrange):
            j = models.invoice.objects.get(id=i)
            total_payable_amount += j.paybleamount
            profit = (j.paybleamount) - (j.totalpurch)
            total_profit += profit
            total_pending += j.pendingamount

     
        context = {
            'data':customers_count,
            'pb':pbarcode_count,
            'payamount':total_payable_amount,
            'pamount':pamount,
            'profit':total_profit,
            'total_pending':total_pending,
            'sales_count':sales_count,
            'pcount':pcount,
            
            
        }
        return render(request, 'main.html',context)
    else:
        return redirect('login')







# ====================================================
# ================ Customer function =================
# ====================================================

def add_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fname=request.POST['fname']
            mname=request.POST['mname']
            lname=request.POST['lname']
            mobno=request.POST['mobno']
            emailid=request.POST['emailid']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            bdate=request.POST['bdate']
            age=request.POST['age']
            reg=modelscustomer_details(
                first_name=fname,middle_name=mname,
                last_name=lname,mobileno=mobno,email_id=emailid,address=address,
                city=city,state=state,birthdate=bdate,age=age
                )
            reg.save()
            messages.success(request, 'Customer Added Successfully...')
        return render(request, 'invoice/invoice_generate.html')
    else:
        return redirect('login')

def customer_list(request):
    if request.user.is_authenticated:
        customer_data = models.customer_details.objects.all()
        return render(request , 'customer/customer_list.html',{'data':customer_data})
    else:
        return redirect('login')

def customer_details_view(request,id):
    if request.user.is_authenticated:
        customer_data = models.customer_details.objects.get(pk=id)
        prescription_data = models.prescription.objects.filter(customer_info=customer_data.id)
        bill_data = models.invoice.objects.filter(custid=customer_data.id)
        return render(request , 'customer/customer_view.html',{'data':customer_data,'dt':prescription_data,'bill':bill_data})
    else:
        return redirect('login')

def customer_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fname=request.POST['fname']
            mname=request.POST['mname']
            lname=request.POST['lname']
            mobno=request.POST['mobno']
            emailid=request.POST['emailid']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            bdate=request.POST['bdate']
            age=request.POST['age']
            reg=models.customer_details(
                first_name=fname,middle_name=mname,
                last_name=lname,mobileno=mobno,email_id=emailid,address=address,
                city=city,state=state,birthdate=bdate,age=age
                )
            reg.save()
            messages.success(request, 'Customer Added Successfully...')
        return render(request, 'customer/customer_add.html')
    else:
        return redirect('login')

def customer_update(request,id):
    if request.user.is_authenticated:
        customer_data = models.customer_details.objects.get(pk=id)
        if request.method == 'POST':
            custid=request.POST['custid']
            fname=request.POST['fname']
            mname=request.POST['mname']
            lname=request.POST['lname']
            mobno=request.POST['mobno']
            emailid=request.POST['emailid']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            bdate=request.POST['bdate']
            age=request.POST['age']
            gdata = models.customer_details.objects.get(id=custid)
            gdata.first_name=fname
            gdata.middle_name=mname
            gdata.last_name=lname
            gdata.mobileno=mobno
            gdata.email_id=emailid
            gdata.address=address
            gdata.city=city
            gdata.state=state
            gdata.birthdate=bdate
            gdata.age=age
            gdata.save()
            messages.success(request, 'Customer Updated Successfully...')

        return render(request , 'customer/customer_update.html',{'data':customer_data})
    else:
        return redirect('login')
# ========================================================
# ====================products============================
# ========================================================

def frame_add(request):
    if request.user.is_authenticated:
        fm = forms.frameForm()
        dt = models.frame.objects.all()
        if request.method == 'POST':
            fm = forms.frameForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Frame Added Successfully...')
        else:
            fm = forms.frameForm()
        return render(request, 'products/frame_add.html',{'fm':fm,'data':dt})
    else:
        return redirect('login')

def glass_add(request):
    if request.user.is_authenticated:
        fm = forms.glassForm()
        dt = models.glass.objects.all()
        if request.method == 'POST':
            fm = forms.glassForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Frame Added Successfully...')
        else:
            fm = forms.glassForm()
        return render(request, 'products/glasses_add.html',{'fm':fm,'data':dt})
    else:
        return redirect('login')

def goggles_add(request):
    if request.user.is_authenticated:
        fm = forms.gogglesForm()
        dt = models.goggles.objects.all()
        if request.method == 'POST':
            fm = forms.gogglesForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Goggle Added Successfully...')
        else:
            fm = forms.gogglesForm()
        return render(request , 'products/goggles_add.html',{'fm':fm,'data':dt})
    else:
        return redirect('login')

# =======================================================
# =============== purchase functions ====================
# =======================================================
def supplier_add(request):
    if request.user.is_authenticated:
        fm = forms.supplierForm()
        if request.method == 'POST':
            fm=forms.supplierForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Supplier added successfully...!!!')
                fm = forms.supplierForm()
        else:
            fm = forms.supplierForm()
        return render(request, 'purchase/supplier_add.html',{'fm':fm})
    else:
        return redirect('login')

def supplier_list(request):
    if request.user.is_authenticated:
        data = models.supplier_details.objects.all()
        return render(request , 'purchase/supplier_list.html', {'data':data})
    else:
        return redirect('login')

def supplier_update(request,id):
    if request.user.is_authenticated:
        data = models.supplier_details.objects.get(pk=id)
        if request.method == 'POST':
            fm = forms.supplierForm(request.POST,instance=data)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Supplier Update Successfully...!!!')
        else:
            data = models.supplier_details.objects.get(pk=id)
            fm = forms.supplierForm(instance=data)
        return render(request , 'purchase/supplier_update.html', {'data':data,'fm':fm})
    else:
        return redirect('login')
    
def purchase_add(request):
    if request.user.is_authenticated:
        dt = models.supplier_details.objects.all()
        if request.method == 'POST':
            length = request.POST['totallength']
            supplier = request.POST['supplier']
            date = request.POST['date']
            pbn = request.POST['pbn']
            ta = request.POST['tprs']
            # data = models.purchase(supplier=supplier,date=date,bill_no=pbn,total_amount=ta)
            # data.save()
            i = 0
            for index in range(i,int(length)):
                product_id = ""
                description = ""
                quantity = ""
                prs = ""
                tprs = ""
                rp = ""
                flag = 0
                if 'product_id'+str(index) in request.POST:
                        product_id= request.POST['product_id'+str(index)]
                        flag = 1
                if 'productcode'+str(index) in request.POST:
                        description= request.POST['productcode'+str(index)]
                        flag = 1
                if 'quantity'+str(index) in request.POST:
                        quantity= request.POST['quantity'+str(index)]
                        flag = 1
                if 'purchase'+str(index) in request.POST:
                        prs= request.POST['purchase'+str(index)]
                        flag = 1
                if 'tpurchase'+str(index) in request.POST:
                        tprs= request.POST['tpurchase'+str(index)]
                        flag = 1
                if 'mrp'+str(index) in request.POST:
                        rp= request.POST['mrp'+str(index)]
                        flag = 1
                if flag == 1:
                    product_code = description[slice(0,5)]
                    des = description[slice(6,200)]
                    abc = int(quantity) + 1
                    for i in range(1,int(abc)):
                        x = models.barcode_list(date=date,product=product_id,description=des,product_code=product_code)
                        x.save()
                    
                    if models.inventory.objects.filter(product_code=product_code).exists():
                        a = models.inventory.objects.get(product_code=product_code)
                        a.available_stock += int(quantity)
                        a.save()
                    else:
                        s = models.inventory(product=product_id,product_code=product_code,description=des,available_stock=quantity)
                        s.save()

                    p_product = models.purchase_details(supplier=supplier,date=date,bill_no=pbn,product=product_id,description=des,quantity=quantity,purchase_rs=prs,total_purchase_rs=tprs,mrp=rp,total_amount=ta,product_code=product_code)
                    p_product.save()
                    
                    messages.success(request, 'Purchase Added Successfully')
        dt = models.supplier_details.objects.all()
        return render(request, 'purchase/purchase_add.html', {'data':dt})
    else:
        return redirect('login')

# frame autocomplete
def pautocomplete(request):
    if request.user.is_authenticated:
        qo = request.GET.get('product_code')
        payload = []
        
        if qo:
            qs = models.frame.objects.filter(product_code__icontains=qo)
            for i in qs:
                
                data = [i.product_code,i.company_name,i.frame_name,i.size,i.color,i.gender,i.type,i.shape,i.material]
                payload.append(data)
        return JsonResponse({'data':payload})
    else:
        return redirect('login')


def purchaseajax(request):
    if request.user.is_authenticated:
        qo = request.GET.get('i')
        pprice = []
        mrp = []
        if qo:
            qs = models.frame.objects.filter(product_code=qo)
            for i in qs:
                
                pprice1 = i.purchase_price
                mrp1 = i.retail_price
                
                pprice.append(pprice1)
                mrp.append(mrp1)
        return JsonResponse({'d2':pprice,'d1':mrp})
    else:
        return redirect('login')

# glass autocomplete
def gautocomplete(request):
    if request.user.is_authenticated:
        qo = request.GET.get('product_code')
        payload = []
        
        if qo:
            qs = models.glass.objects.filter(Q(product_code__icontains=qo) | Q(company_name__icontains=qo))
            for i in qs:
                data = [i.product_code,i.company_name,i.color,i.glass_details,i.coting,i.design,i.index]
                payload.append(data)
        return JsonResponse({'data':payload})
    else:
        return redirect('login')

def purchasegajax(request):
    if request.user.is_authenticated:
        qo = request.GET.get('i')
        pprice = []
        mrp = []
        if qo:
            qs = models.glass.objects.filter(product_code__icontains=qo)
            for i in qs:
                pprice1 = i.purchase_price
                mrp1 = i.retail_price
                
                pprice.append(pprice1)
                mrp.append(mrp1)
        return JsonResponse({'d2':pprice,'d1':mrp})
    else:
        return redirect('login')

# goggles autocomplete
def ggautocomplete(request):
    if request.user.is_authenticated:
        qo = request.GET.get('product_code')
        payload = []
        
        if qo:
            qs = models.goggles.objects.filter(Q(product_code__icontains=qo) | Q(company_name__icontains=qo))
            for i in qs:
                data = [i.product_code,i.company_name,i.color,i.gender,i.material,i.shape,i.size]
                payload.append(data)
        return JsonResponse({'data':payload})
    else:
        return redirect('login')

def purchaseggajax(request):
    if request.user.is_authenticated:
        qo = request.GET.get('i')
        pprice = []
        mrp = []
        if qo:
            qs = models.goggles.objects.filter(product_code__icontains=qo)
            for i in qs:
                pprice1 = i.purchase_price
                mrp1 = i.retail_price
                pprice.append(pprice1)
                mrp.append(mrp1)
        return JsonResponse({'d2':pprice,'d1':mrp})
    else:
        return redirect('login')

def purchase_history(request):
    if request.user.is_authenticated:
        data = models.purchase_details.objects.all()
    
        return render(request , 'purchase/purchase_history.html',{'data':data})
    else:
        return redirect('login')

# ======================================================
# ========================barcode=======================
# ======================================================
def confirm_barcode(request):
    if request.user.is_authenticated:
        dt = models.barcode_list.objects.all()
        return render(request , 'purchase/confirm_barcode.html',{'data':dt})
    else:
        return redirect('login')

def confirm_barcodeid(request,id):
    if request.user.is_authenticated:
        data = models.barcode_list.objects.get(pk=id)
        fm = forms.barcode_listForm()
        if request.method == 'POST':
            fm = forms.barcode_listForm(request.POST)
            if fm.is_valid():
                barcode1 = request.POST['barcode']
                data = models.barcode_list.objects.get(pk=id)
                data.barcode = barcode1
                if data.barcode:
                    data.status = "yes"
                    data.save()
                    messages.success(request, 'Barcode Updated successfully...')
        else:
            fm = forms.barcode_listForm()
        return render(request , 'purchase/barcode.html',{'data':data,'fm':fm})
    else:
        return redirect('login')

def inventory_details(request):
    if request.user.is_authenticated:
        data = models.inventory.objects.all()
        return render(request , 'inventory/inventory.html',{'data':data})
    else:
        return redirect('login')


# ======================================================
# ===================prescription=======================
# ======================================================

def prescription_add(request):
    if request.user.is_authenticated:
        dt = models.customer_details.objects.all()
        fm = forms.customer_detailsForm()
        if request.method == 'POST':
            customer_id = request.POST['customer_name'] 
            first_name = request.POST['fname']
            middle_name = request.POST['mname']
            last_name = request.POST['lname']
            mobileno = request.POST['mobno']
            email = request.POST['emailid']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            bdate=request.POST['bdate']
            age=request.POST['age']
            optometrist_name = request.POST['oname']
            RDSPH = request.POST['RDSPH']
            RDCYL = request.POST['RDCYL']
            RDAXIS = request.POST['RDAXIS']
            RDVISION = request.POST['RDVISION']
            RADD = request.POST['RADD']
            LDSPH = request.POST['LDSPH']
            LDCYL = request.POST['LDCYL']
            LDAXIS = request.POST['LDAXIS']
            LDVISION = request.POST['LDVISION']
            LADD = request.POST['LADD']
            RNSPH = request.POST['RNSPH']
            RNCYL = request.POST['RNCYL']
            RNAXIS = request.POST['RNAXIS']
            RNVISION = request.POST['RNVISION']
            LNSPH = request.POST['LNSPH']
            LNCYL = request.POST['LNCYL']
            LNAXIS = request.POST['LNAXIS']
            LNVISION = request.POST['LNVISION']
            wear = request.POST['wear']
            prescription_notes = request.POST['pnotes']
            if customer_id:
                qs = models.customer_details.objects.get(id=customer_id)
                qs.first_name=first_name 
                qs.middle_name = middle_name  
                qs.last_name = last_name 
                qs.mobileno = mobileno
                qs.email_id = email
                qs.address = address 
                qs.city = city
                qs.state = state
                qs.birthdate =bdate
                qs.age = age
                qs.save()
                data = models.prescription(
                    customer_info=customer_id,first_name=first_name,
                    middle_name=middle_name,last_name=last_name,mobileno=mobileno,
                    optometrist_name=optometrist_name,RDSPH=RDSPH,RDCYL=RDCYL,
                    RDAXIS=RDAXIS,RDVISION=RDVISION,RADD=RADD,LDSPH=LDSPH,LDCYL=LDCYL,
                    LDAXIS=LDAXIS,LDVISION=LDVISION,LADD=LADD,RNSPH=RNSPH,RNCYL=RNCYL,
                    RNAXIS=RNAXIS,RNVISION=RNVISION,LNSPH=LNSPH,LNCYL=LNCYL,
                    LNAXIS=LNAXIS,LNVISION=LNVISION,wear=wear,
                    prescription_notes=prescription_notes
                    )
                data.save()
                data=models.prescription.objects.all().last()
                cust=models.customer_details.objects.get(id=data.customer_info)
                return render_to_pdf('prescription/prescription_print.html',{'i':data,'j':cust})
            else:
                getid = models.customer_details.objects.last().id
                newid = getid + 1
                qs1 = models.customer_details(first_name=first_name,middle_name=middle_name,last_name=last_name,mobileno=mobileno,email_id=email,address=address,city=city,state=state,birthdate=bdate,age=age)
                data = models.prescription(customer_info=newid,first_name=first_name,middle_name=middle_name,last_name=last_name,mobileno=mobileno,optometrist_name=optometrist_name,RDSPH=RDSPH,RDCYL=RDCYL,RDAXIS=RDAXIS,RDVISION=RDVISION,RADD=RADD,LDSPH=LDSPH,LDCYL=LDCYL,LDAXIS=LDAXIS,LDVISION=LDVISION,LADD=LADD,RNSPH=RNSPH,RNCYL=RNCYL,RNAXIS=RNAXIS,RNVISION=RNVISION,LNSPH=LNSPH,LNCYL=LNCYL,LNAXIS=LNAXIS,LNVISION=LNVISION,wear=wear,prescription_notes=prescription_notes)
                qs1.save()
                data.save()
                data=models.prescription.objects.all().last()
                cust=models.customer_details.objects.get(id=data.customer_info)
                return render_to_pdf('prescription/prescription_print.html',{'i':data,'j':cust})
        return render(request , 'prescription/prescription_add.html',{'data':dt})
    else:
        return redirect('login')

def prescription_ajax(request):
    if request.user.is_authenticated:
        qo = request.GET.get('i')
        fname = []
        lname = []
        mname = []
        mobile = []
        email = []
        address = []
        city = []
        state = []
        bdate = []
        age = []
        if qo:
            qs = models.customer_details.objects.filter(id=qo)
            for i in qs:
                pfname = i.first_name
                pmname = i.middle_name
                plname = i.last_name
                pmobile = i.mobileno
                pemail = i.email_id
                paddress = i.address
                pcity = i.city
                pstate = i.state
                pdate = i.birthdate
                page = i.age
                fname.append(pfname)
                lname.append(plname)
                mname.append(pmname)
                mobile.append(pmobile) 
                email.append(pemail)
                address.append(paddress)
                city.append(pcity)
                state.append(pstate)
                bdate.append(pdate)
                age.append(page)
        context = {
            'fn':fname,'mn':mname,'ln':lname,
            'mb':mobile,'em':email,'add':address,
            'ct':city,'st':state,'bd':bdate,'ag':age
        }   
        return JsonResponse(context)
    else:
        return redirect('login')

def prescription_data(request):
    if request.user.is_authenticated:
        data = models.prescription.objects.all()
        return render(request , 'prescription/prescription_list.html',{'data':data})
    else:
        return redirect('login')

# ======================================================================
# ============================Generate print Pdf========================
# ======================================================================


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def download_pdf_view(request,id):
    data=models.prescription.objects.get(pk=id)
    cust=models.customer_details.objects.get(id=data.customer_info)
    return render_to_pdf('prescription/prescription_print.html',{'i':data,'j':cust})



def download_invoice_view(request,id):
    data=models.invoice.objects.get(pk=id)
    custdata = models.customer_details.objects.get(id=data.custid)
    product = models.invoice_products.objects.filter(invoice_no=data.billno)
    p = models.prescription.objects.filter(customer_info=data.custid).last()
   
    return render_to_pdf('sales/invoice_print.html',{'d':data,'j':custdata,'data':product,'i':p})

def download_invoice_print(request):
    data=models.invoice.objects.all().last()
    custdata = models.customer_details.objects.get(id=data.custid)
    product = models.invoice_products.objects.filter(invoice_no=data.billno)
    p = models.prescription.objects.filter(customer_info=data.custid).last()
    return render_to_pdf('sales/invoice_print.html',{'d':data,'j':custdata,'data':product,'i':p}) 

                      
# ======================================================
# ======================== Sales =======================
# ======================================================




def invoice_ajax(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cid = request.POST['i']
            data = models.customer_details.objects.get(pk=cid)
            p = models.prescription.objects.filter(customer_info=cid).last()
            customer_data = {
                'id':data.id,'fn':data.first_name,'mn':data.middle_name,'ln':data.last_name,
                'mb':data.mobileno,'em':data.email_id,'add':data.address,'ct':data.city,'st':data.state
                ,'age':data.age,'bd':data.birthdate,
            }
            if p:
                prescription_data = {
                    'id':p.id,'date':p.date,'RDSPH':p.RDSPH,'RDCYL':p.RDCYL,'RDAXIS':p.RDAXIS,'RDVISION':p.RDVISION,
                    'RADD':p.RADD,'LDSPH':p.LDSPH,'LDCYL':p.LDCYL,'LDAXIS':p.LDAXIS,'LDVISION':p.LDVISION,'LADD':p.LADD,
                    'RNSPH':p.RNSPH,'RNCYL':p.RNCYL,'RNAXIS':p.RNAXIS,'RNVISION':p.RNVISION,'LNSPH':p.LNSPH,'LNCYL':p.LNCYL,
                    'LNAXIS':p.LNAXIS,'LNVISION':p.LNVISION
                }
                return JsonResponse({'c':customer_data,'p':prescription_data})
            else:
                return JsonResponse({'c':customer_data})
    else:
        return redirect('login')

def invoice_product_ajax(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            bcode = request.POST['b']
            
            i = models.barcode_list.objects.get(barcode=bcode)
            data = {
                'type':i.product,
                'desc':i.description,
                'pcode':i.product_code
            }
        
            if i.product == 'Frame':
                j = models.frame.objects.get(product_code=i.product_code)
            
                product_details={
                    'name':j.product_name,
                    'purchase_price':j.purchase_price,'retail_price':j.retail_price
                }
            elif i.product == 'Goggles':
                j = models.goggles.objects.get(product_code=i.product_code)
                product_details={
                    'name':j.product_name,'purchase_price':j.purchase_price,'retail_price':j.retail_price
                }
            
            
            return JsonResponse({'p':product_details,'i':data})
    else:
        return redirect('login')

def invoice_productg_ajax(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            bcode = request.POST['b']
            payload = []
        
            glass = models.glass.objects.get(barcode=bcode)
            glassd={
                    'name':glass.product_name,
                    'purchase_price':glass.purchase_price,'retail_price':glass.retail_price
                }
            if bcode:
                qs = models.glass.objects.filter(barcode=bcode)
                for i in qs:
                    data = [i.product_code,i.company_name,i.color,i.glass_details,i.coting,i.design]
                    payload.append(data)
            
            return JsonResponse({'g':glassd,'x':payload})
    else:
        return redirect('login')

def invoice_generate(request):
    if request.user.is_authenticated:
        customer_data = models.customer_details.objects.all()
        if request.method == 'POST':
            length = request.POST['getid']
            custid = request.POST['customer_name']
            billno = request.POST['billno']
            bdate = request.POST['date']
            ddate = request.POST['ddate']
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            mobno = request.POST['mobno']
            emailid = request.POST['emailid']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            bidate=request.POST['bdate']
            age=request.POST['age']
            tprs = request.POST['tprs']
            pp = request.POST['getamf']
            discountp = request.POST['discount']
            damount = request.POST['damount']
            pamount = request.POST['pamount']
            adamount = request.POST['adamount']
            pdamount = request.POST['pdamount']
            pmode = request.POST['pmode']
            # ===================
            RDSPH = request.POST['RDSPH']
            RDCYL = request.POST['RDCYL']
            RDAXIS = request.POST['RDAXIS']
            RDVISION = request.POST['RDVISION']
            RADD = request.POST['RADD']
            LDSPH = request.POST['LDSPH']
            LDCYL = request.POST['LDCYL']
            LDAXIS = request.POST['LDAXIS']
            LDVISION = request.POST['LDVISION']
            LADD = request.POST['LADD']
            RNSPH = request.POST['RNSPH']
            RNCYL = request.POST['RNCYL']
            RNAXIS = request.POST['RNAXIS']
            RNVISION = request.POST['RNVISION']
            LNSPH = request.POST['LNSPH']
            LNCYL = request.POST['LNCYL']
            LNAXIS = request.POST['LNAXIS']
            LNVISION = request.POST['LNVISION']
            # =================================
            print(discountp)
            name = fname+' '+mname+' '+lname
            gbname = request.user.first_name+" "+request.user.last_name
            if custid:
                qs = models.customer_details.objects.get(id=custid)
                qs.first_name=fname 
                qs.middle_name = mname  
                qs.last_name = lname 
                qs.mobileno = mobno
                qs.email_id = emailid
                qs.address = address 
                qs.city = city
                qs.state = state
                qs.birthdate =bidate
                qs.age = age
                qs.save()
                if pdamount:
                    data = models.invoice(custid=custid,billno=billno,billdate=bdate,deliverydate=ddate,name=name,
                    mobno=mobno,totalrs=tprs,discountper=discountp,discountamount=damount,paybleamount=pamount,
                    advanceamount=adamount,pendingamount=pdamount,paymentmode=pmode,generatedby=gbname,totalpurch=pp)
                    data.save()
                else:
                    data = models.invoice(custid=custid,billno=billno,billdate=bdate,deliverydate=ddate,name=name,
                    mobno=mobno,totalrs=tprs,discountper=discountp,discountamount=damount,paybleamount=pamount,
                    advanceamount=adamount,paymentmode=pmode,generatedby=gbname,totalpurch=pp,pendingamount=0)
                    data.save()
                qo = models.prescription.objects.filter(customer_info=custid).last()
                qq = models.prescription.objects.filter(customer_info=custid)
                if qq:
                    if qo.RDSPH != RDSPH:
                        m = models.prescription(
                        customer_info=custid,first_name=fname,
                        middle_name=mname,last_name=lname,mobileno=mobno,
                        RDSPH=RDSPH,RDCYL=RDCYL,
                        RDAXIS=RDAXIS,RDVISION=RDVISION,RADD=RADD,LDSPH=LDSPH,LDCYL=LDCYL,
                        LDAXIS=LDAXIS,LDVISION=LDVISION,LADD=LADD,RNSPH=RNSPH,RNCYL=RNCYL,
                        RNAXIS=RNAXIS,RNVISION=RNVISION,LNSPH=LNSPH,LNCYL=LNCYL,
                        LNAXIS=LNAXIS,LNVISION=LNVISION,
                        )
                        m.save()
                        
                else:
                    m = models.prescription(
                    customer_info=custid,first_name=fname,
                    middle_name=mname,last_name=lname,mobileno=mobno,
                    RDSPH=RDSPH,RDCYL=RDCYL,
                    RDAXIS=RDAXIS,RDVISION=RDVISION,RADD=RADD,LDSPH=LDSPH,LDCYL=LDCYL,
                    LDAXIS=LDAXIS,LDVISION=LDVISION,LADD=LADD,RNSPH=RNSPH,RNCYL=RNCYL,
                    RNAXIS=RNAXIS,RNVISION=RNVISION,LNSPH=LNSPH,LNCYL=LNCYL,
                    LNAXIS=LNAXIS,LNVISION=LNVISION,
                    )
                    m.save()
                    
            else:
                getid = models.customer_details.objects.last().id
                newid = getid + 1
                qs1 = models.customer_details(first_name=fname,middle_name=mname,last_name=lname,mobileno=mobno,email_id=emailid,address=address,city=city,state=state,birthdate=bidate,age=age)
                if pdamount:
                    data = models.invoice(custid=newid,billno=billno,billdate=bdate,deliverydate=ddate,name=name,
                    mobno=mobno,totalrs=tprs,discountper=discountp,discountamount=damount,paybleamount=pamount,
                    advanceamount=adamount,pendingamount=pdamount,paymentmode=pmode,generatedby=gbname,totalpurch=pp)
                    data.save()
                else:
                    data = models.invoice(custid=newid,billno=billno,billdate=bdate,deliverydate=ddate,name=name,
                    mobno=mobno,totalrs=tprs,discountper=discountp,discountamount=damount,paybleamount=pamount,
                    advanceamount=adamount,paymentmode=pmode,generatedby=gbname,totalpurch=pp,pendingamount=0)
                    data.save()
                m = models.prescription(
                    customer_info=newid,first_name=fname,
                    middle_name=mname,last_name=lname,mobileno=mobno,
                    RDSPH=RDSPH,RDCYL=RDCYL,
                    RDAXIS=RDAXIS,RDVISION=RDVISION,RADD=RADD,LDSPH=LDSPH,LDCYL=LDCYL,
                    LDAXIS=LDAXIS,LDVISION=LDVISION,LADD=LADD,RNSPH=RNSPH,RNCYL=RNCYL,
                    RNAXIS=RNAXIS,RNVISION=RNVISION,LNSPH=LNSPH,LNCYL=LNCYL,
                    LNAXIS=LNAXIS,LNVISION=LNVISION,
                    )
                qs1.save()
                
                m.save()
                
            i = 0
            for index in range(i,int(length)):
                barcode = ""
                product = ""
                description = ""
                mrp = ""
                
                flag = 0
                if 'barcode'+str(index) in request.POST:
                        barcode= request.POST['barcode'+str(index)]
                        flag = 1
                if 'product'+str(index) in request.POST:
                        product= request.POST['product'+str(index)]
                        flag = 1
                if 'desc'+str(index) in request.POST:
                        description= request.POST['desc'+str(index)]
                        flag = 1
                if 'mrp'+str(index) in request.POST:
                        mrp= request.POST['mrp'+str(index)]
                        flag = 1
                
                if flag == 1:
                    if product == 'Frame' or product == 'Goggles':
                        x = models.barcode_list.objects.get(barcode=barcode)
                        i = x.product_code
                        print(i)
                        if models.inventory.objects.filter(product_code = i).exists():
                            a = models.inventory.objects.get(product_code = i)
                            a.available_stock -= 1
                            a.save()
                        x.delete()
                    v = models.invoice_products(invoice_no=billno,barcode=barcode,product=product,description=description,mrp=mrp)
                    v.save()
                    
            return redirect('download_invoice_print')
        return render(request, 'sales/invoice_generate.html',{'data':customer_data})
    else:
        return redirect('login')

def confirm_invoice(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = models.invoice.objects.last()
            dt = {
                'id':data.billno
            }
            
        return JsonResponse(dt)
    else:
        return redirect('login')

def getbillno(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = models.invoice.objects.last()
            dt = {
                'id':data.billno
            }
            
        return JsonResponse(dt)
    else:
        return redirect('login')

def invoicelist(request):
    if request.user.is_authenticated:
        data = models.invoice.objects.all()
        return render(request, 'sales/invoice_list.html',{'data':data})
    else:
        return redirect('login')

def pending_amount(request):
    if request.user.is_authenticated:
        data = models.invoice.objects.all()
        context = {
            'data':data
        }
        return render(request , 'sales/pending_amount_list.html',context)
    else:
        return redirect('login')

def pending_order(request):
    if request.user.is_authenticated:
        data = models.invoice.objects.all()
        data1 = models.invoice.objects.filter(order_status = 'no').count()
        context = {
            'data':data,
            'count':data1,
        }
        return render(request , 'sales/pending_order.html',context)
    else:
        return redirect('login')

def update_order(request,id):
    if request.user.is_authenticated:
        data = models.invoice.objects.get(pk=id)
        data.order_status = "yes"
        data.save()
        messages.success(request, "Order Completed")
        return redirect('pending_order')
    else:
        return redirect('login')

def update_order1(request,id):
    if request.user.is_authenticated:
        data = models.invoice.objects.get(pk=id)
        if (data.pendingamount == "") or (data.pendingamount == 0):
            data.deliver_status = "yes"
            data.save()
            messages.success(request, "Order Delivered")
            return redirect('complete_order')
        else:
            messages.warning(request, 'Customer have pending amount, please update it')
            return redirect('complete_order')
    else:
        return redirect('login')

def deliver_option(request,id):
    if request.user.is_authenticated:
        data = models.invoice.objects.get(pk=id)
        if request.method == 'POST':
            am = request.POST['amount']
            if am:
                data.pendingamount=am
                data.save()
            else:
                data.pendingamount = 0
                data.save()
            messages.success(request, 'amount updated')
        return render(request, 'sales/update_amount.html',{'data':data})
    else:
        return redirect('login')

def deliver_anyway(request,id):
    if request.user.is_authenticated:
        data = models.invoice.objects.get(pk=id)
        data.deliver_status = "yes"
        data.save()
        messages.success(request, "Order Delivered")
        return redirect('complete_order')
    else:
        return redirect('login')

def complete_order(request):
    if request.user.is_authenticated:
        data = models.invoice.objects.all()
        data1 = models.invoice.objects.filter(order_status = 'yes' , deliver_status = 'no').count()
        context = {
            'data':data,
            'count':data1,
        }
        return render(request , 'sales/complete_order.html',context)
    else:
        return redirect('login')

