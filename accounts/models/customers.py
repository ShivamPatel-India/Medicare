from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=13)
    # profile_picture = models.ImageField(upload_to='Accounts/profile_img', max_length=500, default='default.jpg',null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    @staticmethod
    def verify_customer(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def rgstr(self):
        self.save()

    def ifAlreadyExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False


    def validateCustomer(self):
        err_msg=None
        if not self.first_name:
            err_msg = "Fist Name Required!"
        elif len(self.contact_no)!=10 :
            err_msg = "Phone number must be of 10 digits!"
        elif self.ifAlreadyExist():
            err_msg = "User Already Registered!"
        return err_msg

    def __str__(self):
        return self.first_name