from django.db import models

# Create your models here.

class AddVendors(models.Model):
    vendorname = models.CharField(max_length=30)
    
    def __str__(self): 
        return str(self.vendorname)
    

class AddProducts(models.Model):
    SKU = models.CharField(max_length=10, null=True)
    Vendor = models.ForeignKey(AddVendors ,on_delete=models.SET_NULL, null=True)
    Category = models.CharField(max_length=50, null=True)
    Sub_category = models.CharField(max_length=50, null=True)
    Product_Name = models.CharField(max_length=50, null=True)
    MRP = models.IntegerField(null=True)
    Vendor_Price = models.FloatField(null=True)
    Transport1 = models.FloatField(null=True)
    Transport2 = models.FloatField(null=True)
    Branding = models.FloatField(null=True)
    Packing = models.FloatField(null=True)
    Profit_in_precentage = models.FloatField(null=True)
    Profit_amount = models.FloatField(null=True)
    GF_Price = models.FloatField(null=True)
    Tax_in_precentage = models.FloatField(null=True)
    Tax_amount = models.FloatField(null=True)
    Total_GF_price = models.FloatField(null=True)
    product_image = models.ImageField(upload_to="product_images", null=True)
    
    def __str__(self): 
        return str(self.Product_Name)
    
class ManualComboTemp(models.Model):
    product = models.ForeignKey(AddProducts ,on_delete=models.SET_NULL, null=True)