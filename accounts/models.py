from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#
# class User(AbstractUser):
#     is_manager = models.BooleanField(default=False)
#     is_salesrep = models.BooleanField(default=False)
#     is_buyer = models.BooleanField(default=False)


class SalesRep(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='SalesRep')
    # # company = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True)
    # name = models.CharField(max_length=250)
    # email = models.EmailField(max_length=254)
    # phone = models.IntegerField()
    # sales_rep_pic = models.ImageField(upload_to=f"accounts/{name}/sales_rep",blank=True)
    #
    # # def get_absolute_url(self):
    # #     return reverse('classroom:teacher_detail',kwargs={'pk':self.pk})
    #
    # def __str__(self):
    #     return self.name
    pass

class Company(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Company')
    # name = models.CharField(max_length=250)
    # email = models.EmailField(max_length=254)
    # phone = models.IntegerField()
    # is_workshop = models.BooleanField()
    # company_logo = models.ImageField(upload_to=f"accounts/{name}/company_logo", blank=True)
    # date_joined = models.DateTimeField(auto_now=True)
    # members = models.ManyToManyField(
    #     SalesRep,
    #     through='Membership',
    #     through_fields=('Company', 'SalesRep'),
    # )
    # # def get_absolute_url(self):
    # #     return reverse('classroom:student_detail', kwargs={'pk': self.pk})
    #
    # def __str__(self):
    #     return self.name
    #
    # class Meta:
    #     ordering = ['-date_joined']
    pass


class Membership(models.Model):
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # salesrep = models.ForeignKey(SalesRep, on_delete=models.CASCADE)
    # inviter = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="membership_invites",
    # )
    # invite_reason = models.CharField(max_length=64)
    #
    # def __str__(self):
    #         return self.salesrep.name
    #
    # class Meta:
    #     unique_together = ('company','salesrep')
    pass




class Buyer(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    # name = models.CharField(max_length=250)
    # email = models.EmailField(max_length=254)
    # phone = models.IntegerField()
    # buyer_pic = models.ImageField(upload_to=f"accounts/{name}/sales_rep",blank=True)
    #
    # # def get_absolute_url(self):
    # #     return reverse('classroom:teacher_detail',kwargs={'pk':self.pk})
    #
    # def __str__(self):
    #     return self.name
    pass

# class StudentsInClass(models.Model):
#     teacher = models.ForeignKey(Teacher,related_name="class_teacher",on_delete=models.CASCADE)
#     student = models.ForeignKey(Student,related_name="user_student_name",on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.student.name
#
#     class Meta:
#         unique_together = ('teacher','student')