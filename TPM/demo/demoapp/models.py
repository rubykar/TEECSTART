from django.db import models
from django.contrib import auth
from datetime import date
from django.contrib.auth.models import User

class Admin(models.Model):
    First_Name=models.CharField(max_length=45,blank=False)
    Middle_Name=models.CharField(max_length=45,null=True,default='-')
    Last_Name=models.CharField(max_length=67,blank=False)
    Name=models.CharField(max_length=50,blank=False)
    Designation=models.CharField(max_length=600,null=True,default='-')
    Email=models.EmailField(blank=False,null=True,default='-')
    Mobile_No=models.CharField(max_length=10,blank=False,default='-')
    Permanent_Add = models.CharField(max_length=100,blank=False)
    City = models.CharField(max_length=30,default='Siliguri')
    state_choices=(
        (  'Andhra Pradesh' ,  'Andhra Pradesh'),
        (  'state' ,'Arunachal Pradesh(Itanagar)'),
        (  'state' , 'Assam(Dispur)'),
        (  'state' , 'Bihar(Patna)'),
        (  'state' ,'Chhattisgarh(Raipur)'),
        (  'state' ,   'Goa(Panaji)'),
        (  'state' ,    'Gujarat(Gandhinagar)'),
        (  'state' ,        'Haryana(Chandigarh))'),
        (  'state' ,     'Himachal Pradesh(Shimla)'),
        (  'state' , 'Jharkhand(Ranchi)'),
        (  'state' ,  'Karnataka(Bangalore)'),
        (  'state' , 'Kerala(Thiruvananthapuram)'),
        (  'state' ,  'Madhya Pradesh(Bhopal)'),
        (  'state' ,   'Maharashtra(Mumbai)'),
        (  'state' , 'Manipur(Imphal)'),
        (  'state' ,    'Meghalaya(Shillong)'),
        (  'state' ,    'Mizoram(Aizawl)'),
        (  'state' ,   'Nagaland(Kohima)'),
        (  'state' ,  'Odisha(Bhubaneshwar)'),
        (  'state' ,  'Punjab(Chandigarh)'),
        (  'state' ,    'Rajasthan(Jaipur)'),
        (  'state' ,  'Sikkim(Gangtok)'),
        (  'state' ,  'Tamil Nadu(Chennai)'),
        (  'state' ,   'Telangana(Hyderabad)'),
        (  'state' ,   'Tripura(Agartala)'),
        (  'state' ,   'Uttarakhand(Dehradun)'),
        (  'state' ,   'Uttar Pradesh(Lucknow)'),
        (  'state' ,   'West Bengal(Kolkata)'),

        ( 'union territories'  , ' Andaman and Nicobar Islands(Port Blair)'),
        ( 'union territories'  , ' Chandigarh(Chandigarh)' ),
        ( 'union territories'  , 'Dadra and Nagar Haveli and Daman & Diu' ),
        ( 'union territories'  , 'The Government of NCT of Delhi(Delhi)'),
        ( 'union territories'  ,' Jammu & Kashmir(Srinagar-S*, Jammu-W*)'),
        ( 'union territories'  , 'Ladakh(Leh)'),
        ( 'union territories'  , 'Lakshadweep(Kavaratti)'),
        ( 'union territories'  ,' Puducherry(Puducherry)'),

 )
    States = models.CharField(choices=state_choices,max_length=30,default='West Bengal(Kolkata)')
    Country = models.CharField(max_length =30,default='India')
    Photo = models.ImageField(editable=True,default='-')



class Organisation(models.Model):
    Name=models.CharField(max_length=50,blank=False,default='-')
    Industry=models.CharField(max_length=45,null=True,default='-')
    Email = models.EmailField(blank=False,default='-')
    Phone = models.CharField(max_length=10,blank=False,default='-')
    Admin = models.OneToOneField(Admin,on_delete=models.CASCADE,default='-')
    Type = models.CharField(max_length=70,null=True,default='-')
    Permanent_Add = models.CharField(max_length=30,null=True)
    City = models.CharField(max_length=30,default='Siliguri')
    state_choices=(
        (  'Andhra Pradesh' ,  'Andhra Pradesh'),
        (  'state' ,'Arunachal Pradesh(Itanagar)'),
        (  'state' , 'Assam(Dispur)'),
        (  'state' , 'Bihar(Patna)'),
        (  'state' ,'Chhattisgarh(Raipur)'),
        (  'state' ,   'Goa(Panaji)'),
        (  'state' ,    'Gujarat(Gandhinagar)'),
        (  'state' ,        'Haryana(Chandigarh))'),
        (  'state' ,     'Himachal Pradesh(Shimla)'),
        (  'state' , 'Jharkhand(Ranchi)'),
        (  'state' ,  'Karnataka(Bangalore)'),
        (  'state' , 'Kerala(Thiruvananthapuram)'),
        (  'state' ,  'Madhya Pradesh(Bhopal)'),
        (  'state' ,   'Maharashtra(Mumbai)'),
        (  'state' , 'Manipur(Imphal)'),
        (  'state' ,    'Meghalaya(Shillong)'),
        (  'state' ,    'Mizoram(Aizawl)'),
        (  'state' ,   'Nagaland(Kohima)'),
        (  'state' ,  'Odisha(Bhubaneshwar)'),
        (  'state' ,  'Punjab(Chandigarh)'),
        (  'state' ,    'Rajasthan(Jaipur)'),
        (  'state' ,  'Sikkim(Gangtok)'),
        (  'state' ,  'Tamil Nadu(Chennai)'),
        (  'state' ,   'Telangana(Hyderabad)'),
        (  'state' ,   'Tripura(Agartala)'),
        (  'state' ,   'Uttarakhand(Dehradun)'),
        (  'state' ,   'Uttar Pradesh(Lucknow)'),
        (  'state' ,   'West Bengal(Kolkata)'),

        ( 'union territories'  , ' Andaman and Nicobar Islands(Port Blair)'),
        ( 'union territories'  , ' Chandigarh(Chandigarh)' ),
        ( 'union territories'  , 'Dadra and Nagar Haveli and Daman & Diu' ),
        ( 'union territories'  , 'The Government of NCT of Delhi(Delhi)'),
        ( 'union territories'  ,' Jammu & Kashmir(Srinagar-S*, Jammu-W*)'),
        ( 'union territories'  , 'Ladakh(Leh)'),
        ( 'union territories'  , 'Lakshadweep(Kavaratti)'),
        ( 'union territories'  ,' Puducherry(Puducherry)'),

 )
    States = models.CharField(choices=state_choices,max_length=30,default='West Bengal(Kolkata)')
    Country = models.CharField(max_length =30,default='India')
    Logo = models.ImageField(editable=True,null=True,default='-')
    Cover = models.ImageField(editable=True,default='Null') 



class Manager(models.Model):
    First_Name=models.CharField(max_length=45,blank=False,null=True,default='-')
    Middle_Name=models.CharField(max_length=45,null=True,default='-')
    Last_Name=models.CharField(max_length=67,blank=False,null=True,default='-')
    Name=models.CharField(max_length=50,null=True,default='-')
    Designation=models.CharField(max_length=600,null=True,default='-')
    Email=models.EmailField(blank=False,null=True,default='-')
    Mobile_No=models.CharField(max_length=10,blank=False,null=True,default='-')
    City = models.CharField(max_length=30)
    state_choices=(
        (  'Andhra Pradesh' ,  'Andhra Pradesh'),
        (  'state' ,'Arunachal Pradesh(Itanagar)'),
        (  'state' , 'Assam(Dispur)'),
        (  'state' , 'Bihar(Patna)'),
        (  'state' ,'Chhattisgarh(Raipur)'),
        (  'state' ,   'Goa(Panaji)'),
        (  'state' ,    'Gujarat(Gandhinagar)'),
        (  'state' ,        'Haryana(Chandigarh))'),
        (  'state' ,     'Himachal Pradesh(Shimla)'),
        (  'state' , 'Jharkhand(Ranchi)'),
        (  'state' ,  'Karnataka(Bangalore)'),
        (  'state' , 'Kerala(Thiruvananthapuram)'),
        (  'state' ,  'Madhya Pradesh(Bhopal)'),
        (  'state' ,   'Maharashtra(Mumbai)'),
        (  'state' , 'Manipur(Imphal)'),
        (  'state' ,    'Meghalaya(Shillong)'),
        (  'state' ,    'Mizoram(Aizawl)'),
        (  'state' ,   'Nagaland(Kohima)'),
        (  'state' ,  'Odisha(Bhubaneshwar)'),
        (  'state' ,  'Punjab(Chandigarh)'),
        (  'state' ,    'Rajasthan(Jaipur)'),
        (  'state' ,  'Sikkim(Gangtok)'),
        (  'state' ,  'Tamil Nadu(Chennai)'),
        (  'state' ,   'Telangana(Hyderabad)'),
        (  'state' ,   'Tripura(Agartala)'),
        (  'state' ,   'Uttarakhand(Dehradun)'),
        (  'state' ,   'Uttar Pradesh(Lucknow)'),
        (  'state' ,   'West Bengal(Kolkata)'),

        ( 'union territories'  , ' Andaman and Nicobar Islands(Port Blair)'),
        ( 'union territories'  , ' Chandigarh(Chandigarh)' ),
        ( 'union territories'  , 'Dadra and Nagar Haveli and Daman & Diu' ),
        ( 'union territories'  , 'The Government of NCT of Delhi(Delhi)'),
        ( 'union territories'  ,' Jammu & Kashmir(Srinagar-S*, Jammu-W*)'),
        ( 'union territories'  , 'Ladakh(Leh)'),
        ( 'union territories'  , 'Lakshadweep(Kavaratti)'),
        ( 'union territories'  ,' Puducherry(Puducherry)'),

 )
    States = models.CharField(choices=state_choices,max_length=30,default='West Bengal(Kolkata)')
    Country = models.CharField(max_length =30,default='India')
    Photo = models.ImageField(editable=True,default='Null')



class Department(models.Model):
    Name=models.CharField(max_length=30,blank=False,null=True,default='-')
    Description = models.CharField(max_length=60,null=True)



class Employee(models.Model):
    Name=models.CharField(max_length=30,blank=False,default='-')
    Designation=models.CharField(max_length=600,null=True,default='-')
    Mobile_No=models.CharField(max_length=10,blank=False,default='-')
    Department=models.ManyToManyField(Department)
    Join_In=models.DateField(blank=False, null=False)
    Till = models.DateField(blank=False,null=False)
    College = models.CharField(max_length=20,null=True,default='-')
    Degree = models.CharField(max_length = 30,null=True,default='-')
    Specialization = models.CharField(max_length=90,null=True,default='-')
    City = models.CharField(max_length=30,default='Siliguri')
    state_choices=(
        (  'Andhra Pradesh' ,  'Andhra Pradesh'),
        (  'state' ,'Arunachal Pradesh(Itanagar)'),
        (  'state' , 'Assam(Dispur)'),
        (  'state' , 'Bihar(Patna)'),
        (  'state' ,'Chhattisgarh(Raipur)'),
        (  'state' ,   'Goa(Panaji)'),
        (  'state' ,    'Gujarat(Gandhinagar)'),
        (  'state' ,        'Haryana(Chandigarh))'),
        (  'state' ,     'Himachal Pradesh(Shimla)'),
        (  'state' , 'Jharkhand(Ranchi)'),
        (  'state' ,  'Karnataka(Bangalore)'),
        (  'state' , 'Kerala(Thiruvananthapuram)'),
        (  'state' ,  'Madhya Pradesh(Bhopal)'),
        (  'state' ,   'Maharashtra(Mumbai)'),
        (  'state' , 'Manipur(Imphal)'),
        (  'state' ,    'Meghalaya(Shillong)'),
        (  'state' ,    'Mizoram(Aizawl)'),
        (  'state' ,   'Nagaland(Kohima)'),
        (  'state' ,  'Odisha(Bhubaneshwar)'),
        (  'state' ,  'Punjab(Chandigarh)'),
        (  'state' ,    'Rajasthan(Jaipur)'),
        (  'state' ,  'Sikkim(Gangtok)'),
        (  'state' ,  'Tamil Nadu(Chennai)'),
        (  'state' ,   'Telangana(Hyderabad)'),
        (  'state' ,   'Tripura(Agartala)'),
        (  'state' ,   'Uttarakhand(Dehradun)'),
        (  'state' ,   'Uttar Pradesh(Lucknow)'),
        (  'state' ,   'West Bengal(Kolkata)'),

        ( 'union territories'  , ' Andaman and Nicobar Islands(Port Blair)'),
        ( 'union territories'  , ' Chandigarh(Chandigarh)' ),
        ( 'union territories'  , 'Dadra and Nagar Haveli and Daman & Diu' ),
        ( 'union territories'  , 'The Government of NCT of Delhi(Delhi)'),
        ( 'union territories'  ,' Jammu & Kashmir(Srinagar-S*, Jammu-W*)'),
        ( 'union territories'  , 'Ladakh(Leh)'),
        ( 'union territories'  , 'Lakshadweep(Kavaratti)'),
        ( 'union territories'  ,' Puducherry(Puducherry)'),

 )
    States = models.CharField(choices=state_choices,max_length=30,default='West Bengal(Kolkata)')
    Country = models.CharField(max_length =30,default='India')



class Work(models.Model):
    Name=models.CharField(max_length=90,blank=False,default='-')
    Duration=models.DurationField(blank=False)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,default='-')
    Specify_Due_Date=models.DateField(blank=False, null=False, default='2020-01-01')
    Set_Reminder_From=models.DurationField(blank=False)
    




class Client(models.Model):
    status_choices = (
        ('individual','individual'),
        ('HUF','HUF'),
        ('Company','Company'),
        ('Firm','Firm'),
        ('AOP',"AOP"),
        ('Local authority','Local authority'),
        ('Artificial juridicial person','Artificial juridicial person'),
        ('Others','Others')
    )
    Status = models.CharField(max_length=30,choices=status_choices)
    Title= models.CharField(max_length=30,null=True,default='-')
    Name= models.CharField(max_length=30,blank=False,default='-')
    Pan=models.CharField(max_length=10,blank=False,default='-')
    First_Name = models.CharField(max_length=20,blank=False,default='-')
    Last_Name = models.CharField(max_length=20,blank=False,default='-')
    Date_of_Birth=models.DateField(null=False, default='2020-01-01')
    Flat_no= models.CharField(max_length=10,null=True,default='-')
    Name_of_Premises= models.CharField(max_length=20,null=True,default='-')
    Road  = models.CharField(max_length=30,null=True,default='-')
    Area = models.CharField(max_length=40,null=True,default='-')
    City = models.CharField(max_length=50,default='Siliguri')
    state_choices=(
        (  'Andhra Pradesh' ,  'Andhra Pradesh'),
        (  'state' ,'Arunachal Pradesh(Itanagar)'),
        (  'state' , 'Assam(Dispur)'),
        (  'state' , 'Bihar(Patna)'),
        (  'state' ,'Chhattisgarh(Raipur)'),
        (  'state' ,   'Goa(Panaji)'),
        (  'state' ,    'Gujarat(Gandhinagar)'),
        (  'state' ,        'Haryana(Chandigarh))'),
        (  'state' ,     'Himachal Pradesh(Shimla)'),
        (  'state' , 'Jharkhand(Ranchi)'),
        (  'state' ,  'Karnataka(Bangalore)'),
        (  'state' , 'Kerala(Thiruvananthapuram)'),
        (  'state' ,  'Madhya Pradesh(Bhopal)'),
        (  'state' ,   'Maharashtra(Mumbai)'),
        (  'state' , 'Manipur(Imphal)'),
        (  'state' ,    'Meghalaya(Shillong)'),
        (  'state' ,    'Mizoram(Aizawl)'),
        (  'state' ,   'Nagaland(Kohima)'),
        (  'state' ,  'Odisha(Bhubaneshwar)'),
        (  'state' ,  'Punjab(Chandigarh)'),
        (  'state' ,    'Rajasthan(Jaipur)'),
        (  'state' ,  'Sikkim(Gangtok)'),
        (  'state' ,  'Tamil Nadu(Chennai)'),
        (  'state' ,   'Telangana(Hyderabad)'),
        (  'state' ,   'Tripura(Agartala)'),
        (  'state' ,   'Uttarakhand(Dehradun)'),
        (  'state' ,   'Uttar Pradesh(Lucknow)'),
        (  'state' ,   'West Bengal(Kolkata)'),

        ( 'union territories'  , ' Andaman and Nicobar Islands(Port Blair)'),
        ( 'union territories'  , ' Chandigarh(Chandigarh)' ),
        ( 'union territories'  , 'Dadra and Nagar Haveli and Daman & Diu' ),
        ( 'union territories'  , 'The Government of NCT of Delhi(Delhi)'),
        ( 'union territories'  ,' Jammu & Kashmir(Srinagar-S*, Jammu-W*)'),
        ( 'union territories'  , 'Ladakh(Leh)'),
        ( 'union territories'  , 'Lakshadweep(Kavaratti)'),
        ( 'union territories'  ,' Puducherry(Puducherry)'),

 )
    States = models.CharField(choices=state_choices,max_length=30,default='West Bengal(Kolkata)')
    Country = models.CharField(max_length=20,default='India')
    Pin_Code = models.CharField(max_length=6,null=True,default='-')
    Email_Address = models.EmailField(blank=False,null=True,default='-')
    Mobile_no = models.CharField(max_length=10,blank=False,default='-')
    GST = models.CharField(max_length=15,null=True,default='-')
    Aadhar_no = models.CharField(max_length=12,null=True,default='-')
    TDS_no = models.CharField(max_length = 10,null=True,default='-')
        

    def __str__(self):
        return self.Name

class Task(models.Model):
    Name = models.CharField(max_length=60,blank=False,default='-')
    Work=models.ForeignKey(Work,on_delete=models.CASCADE,default='-')
    Stage=models.CharField(max_length=70,null=True,default='-')
    Assign_to = models.CharField(max_length=90,blank=False,default='-')
    Group_Member = models.CharField(max_length=90,blank=False,default='-')
    Team_lead = models.CharField(max_length=40,null=True,default='-')
    Create_date=models.DateField(blank=False, null=False, default='2020-01-01')
    Est_finish_date=models.DateField(blank=False, null=False, default='2020-01-01')
    Actual_Start=models.DurationField(blank=False, default='2020-01-01')
    Actual_Complete = models.DurationField(blank=False, default='2020-01-01')
    Comments =models.CharField(max_length=800,null=True,default='-')
    worklog = models.CharField(max_length=40,null=True,default='-')
    Description = models.CharField(max_length=600,null=True,default='-')
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE,default='-')



class UserProfileInfo(models.Model):



    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='_customer_profile')
    portfolio_site = models.URLField( blank = True)
    profile_pic = models.ImageField( upload_to= 'profile_pics',blank=True)
    

    
