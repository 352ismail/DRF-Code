from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255, null = True)
    price = models.DecimalField(max_digits=14 , decimal_places=3,default=0.000)

    @property
    def sale_price(self):
        return self.price-900
    
    @property
    def general_sales_tax(self):
        return self.price-(self.price//100) 
    
    @property
    def total_records(self):
        return None
    
    def get_discount(self):
        try:
            return self.price-(self.price//100) 
        except: 
            None
    
    def get_user_name(self):
        try:
            return f"Your userName is :{self.title} {self.content}"
        except:
            None


