# Generated by Django 4.2 on 2023-04-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridfokuzapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addproducts',
            old_name='vendorname',
            new_name='Vendor',
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='product_customer_price',
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='product_holesale_price',
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='product_retail_price',
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Branding',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='GF_Price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='MRP',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Packing',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Profit',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Profit_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='SKU',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Sub_category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Tax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Tax_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Total_GF_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Transport1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Transport2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Vendor_Price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='Product_Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
