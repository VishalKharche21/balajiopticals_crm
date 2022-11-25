from django.db import models

# Create your models here.
class customer_details(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)

    def get_name(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name

class supplier_details(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

# ==================products=====================
class frame(models.Model):
    genderlist=[
        ('','-----select gender-----'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    product_name = models.CharField(max_length=100,default='Frame')
    product_code = models.CharField(max_length=5)
    frame_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50,choices=genderlist,blank=True,null=True)
    color = models.CharField(max_length=100,blank=True,null=True)
    size = models.IntegerField(blank=True,null=True)
    type = models.CharField(max_length=100,blank=True,null=True)
    shape = models.CharField(max_length=100,blank=True,null=True)
    material = models.CharField(max_length=100,blank=True,null=True)
    purchase_price = models.IntegerField(blank=True,null=True)
    retail_price = models.IntegerField(blank=True,null=True)


class glass(models.Model):
    product_name = models.CharField(max_length=100,default='Glass')
    product_code = models.CharField(max_length=5)
    glass_details = models.CharField(max_length=300)
    company_name = models.CharField(max_length=100)
    coting = models.CharField(max_length=100,blank=True,null=True)
    color = models.CharField(max_length=100,blank=True,null=True)
    material = models.CharField(max_length=100,blank=True,null=True)
    design = models.CharField(max_length=100,blank=True,null=True)
    index = models.CharField(max_length=100,blank=True,null=True)    
    purchase_price = models.IntegerField(blank=True,null=True)
    retail_price = models.IntegerField(blank=True,null=True)
    barcode = models.CharField(max_length=100)


class goggles(models.Model):
    genderlist=[
        ('','-----select gender-----'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    product_name = models.CharField(max_length=100,default='Goggles')
    product_code = models.CharField(max_length=5)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    color = models.CharField(max_length=100,blank=True,null=True)
    size = models.IntegerField(blank=True,null=True)
    type = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=50,choices=genderlist,blank=True,null=True)
    shape = models.CharField(max_length=100,blank=True,null=True)
    material = models.CharField(max_length=100,blank=True,null=True)
    purchase_price = models.IntegerField(blank=True,null=True)
    retail_price = models.IntegerField(blank=True,null=True)


# ==========================purchase==========================
# class purchase(models.Model):
#     supplier = models.IntegerField()
#     date = models.DateField()
#     bill_no = models.CharField(max_length=100)
#     total_amount = models.CharField(max_length=100)


# class purchase_products(models.Model):
#     purchase = models.ManyToManyField(purchase)
#     product = models.CharField(max_length=100)
#     description = models.CharField(max_length=300)
#     quantity = models.IntegerField()
#     purchase_rs = models.CharField(max_length=100)
#     mrp = models.CharField(max_length=100)
#     total_purchase_rs = models.CharField(max_length=100)

class purchase_details(models.Model):
    supplier = models.CharField(max_length=100)
    date = models.DateField()
    bill_no = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    product_code = models.CharField(max_length=5)
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
    purchase_rs = models.CharField(max_length=100)
    mrp = models.CharField(max_length=100)
    total_purchase_rs = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100)

    

class barcode_list(models.Model):
    date = models.DateField()
    product = models.CharField(max_length=100)
    product_code = models.CharField(max_length=5)
    description = models.CharField(max_length=300)
    barcode = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=10,default='no')

class inventory(models.Model):
    product = models.CharField(max_length=100)
    product_code = models.CharField(max_length=5)
    description = models.CharField(max_length=300)
    available_stock = models.IntegerField()

class prescription(models.Model):
    date = models.DateField(auto_now_add=True)
    customer_info = models.IntegerField(blank=True,null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=10)
    optometrist_name = models.CharField(max_length=100,blank=True,null=True)
    RDSPH = models.CharField(max_length=10)
    RDCYL = models.CharField(max_length=10)
    RDAXIS = models.CharField(max_length=10)
    RDVISION = models.CharField(max_length=10)
    RADD = models.CharField(max_length=10,blank=True,null=True)
    LDSPH = models.CharField(max_length=10)
    LDCYL = models.CharField(max_length=10)
    LDAXIS = models.CharField(max_length=10)
    LDVISION = models.CharField(max_length=10)
    LADD = models.CharField(max_length=10,blank=True,null=True)
    RNSPH = models.CharField(max_length=10,blank=True,null=True)
    RNCYL = models.CharField(max_length=10,blank=True,null=True)
    RNAXIS = models.CharField(max_length=10,blank=True,null=True)
    RNVISION = models.CharField(max_length=10,blank=True,null=True)
    LNSPH = models.CharField(max_length=10,blank=True,null=True)
    LNCYL = models.CharField(max_length=10,blank=True,null=True)
    LNAXIS = models.CharField(max_length=10,blank=True,null=True)
    LNVISION = models.CharField(max_length=10,blank=True,null=True)
    wear = models.CharField(max_length=200,blank=True,null=True)
    prescription_notes = models.CharField(max_length=300,blank=True,null=True)

    def get_name(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name

class invoice(models.Model):
    custid = models.IntegerField(blank=True,null=True)
    billno = models.IntegerField()
    billdate = models.DateTimeField()
    deliverydate= models.DateTimeField()
    name = models.CharField(max_length=200)
    mobno = models.CharField(max_length=10)
    totalrs = models.IntegerField()
    totalpurch = models.IntegerField(blank=True,null=True)
    discountper = models.CharField(max_length=10,blank=True,null=True)
    discountamount = models.CharField(max_length=10,blank=True,null=True)
    paybleamount = models.IntegerField()
    advanceamount = models.CharField(max_length=10,blank=True,null=True)
    pendingamount = models.IntegerField(blank=True,null=True)
    paymentmode = models.CharField(max_length=100,blank=True,null=True)
    order_status = models.CharField(max_length=10,default='no')
    deliver_status = models.CharField(max_length=10,default='no')
    generatedby = models.CharField(max_length=100)


class invoice_products(models.Model):
    invoice_no = models.IntegerField()
    barcode = models.CharField(max_length=100)
    product = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    mrp = models.IntegerField()
    



