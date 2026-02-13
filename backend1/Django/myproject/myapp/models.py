from django.db import models

class Invoice(models.Model):

    seller_gstin = models.CharField(max_length=20)
    buyer_gstin = models.CharField(max_length=20)

    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()

    taxable_value = models.DecimalField(max_digits=12, decimal_places=2)
    gst_value = models.DecimalField(max_digits=12, decimal_places=2)

    total_value = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(max_length=20, default="CREATED")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number


