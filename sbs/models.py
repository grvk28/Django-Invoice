import uuid
from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse
#from .views  import index

User=settings.AUTH_USER_MODEL

class Category(models.Model):
    name=models.CharField(max_length=70)


    def __str__(self):
        return self.name

class Items(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    Item=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=50)
    slug=models.SlugField()
    status=models.CharField(max_length=500)
    date = models.DateField(default=datetime.now)

    def get_absolute_url(self):
        return reverse('home')
    
    def __str__(self):
        return self.Item

#business_code,cust_number,name_customer,clear_date,buisness_year,doc_id,posting_date,document_create_date,
#document_create_date,due_in_date,invoice_currency,document_type,posting_id,area_business,total_open_amount,
#baseline_create_date,cust_payment_terms,invoice_id,isOpen
class t1(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    id=models.AutoField(primary_key=True)
    business_code=models.CharField(max_length=50)
    cust_number=models.CharField(max_length=50)
    name_customer=models.CharField(max_length=50)
    clear_date=models.CharField(max_length=50)
    buisness_year=models.CharField(max_length=50)
    doc_id=models.CharField(max_length=50)
    posting_date=models.CharField(max_length=50)
    document_create_date=models.CharField(max_length=50)
    document_create_date1=models.CharField(max_length=50)
    due_in_date=models.CharField(max_length=50)
    invoice_currency=models.CharField(max_length=50)
    document_type=models.CharField(max_length=50)
    posting_id=models.CharField(max_length=50)
    area_business=models.CharField(max_length=50)
    total_open_amount=models.CharField(max_length=50)
    baseline_create_date=models.CharField(max_length=50)
    cust_payment_terms=models.CharField(max_length=50)
    invoice_id=models.CharField(max_length=50)
    isOpen=models.CharField(max_length=50)

    def __str__(self):
        return self.name_customer

    def get_absolute_url(self):
        return reverse('home1')


