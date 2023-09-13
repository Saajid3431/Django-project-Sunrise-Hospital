from django.db import models

# Create your models here.
# class About (models.Model):
#     dep_name = models.CharField(max_length=100)
#     dep_description = models.TextField()

#     def __str__(self):
#         return self.dep_name
    
class Departments (models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
    

class Doctors (models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name 

class Booking (models.Model):
    Patient_name = models.CharField (max_length=255)
    Patient_phone =models.CharField(max_length=10)
    Patient_email = models.EmailField()
    Doctor_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_date = models.DateField()
    Booked_on = models.DateField(auto_now=True)