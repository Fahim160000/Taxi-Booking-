from django.db import models

# Create your models here.
class TaxiDetails(models.Model):
    taxi_id = models.AutoField(primary_key = True)
    registration_number = models.CharField(max_length = 15, unique = True)
    model = models.CharField(max_length = 50) 
    capacity  = models.IntegerField(null=True)
    availability = models.BooleanField(default = True)
    
    def __str__(self):
        return f"{self.registration_number}-{self.model}"
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 15)
    
    def __str__(self):
        return self.name
    
class PaymentReciept(models.Model):
    reciept_id = models.AutoField(primary_key = True)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    taxi = models.ForeignKey(TaxiDetails,on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10,decimal_places = 2)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"Reciept {self.reciept_id} - {self.amount}"
    
    