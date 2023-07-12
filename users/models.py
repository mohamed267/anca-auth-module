from django.db import models

from django.contrib.auth.models import  BaseUserManager, PermissionsMixin,  AbstractUser




# Create your models here.




class CustomUserManager(BaseUserManager):
  
    def create_user(self,email , first_name , last_name ,  password=None ):
        # if not email:
        #     raise ValueError("Users must have email addess")
        # if not username:
        #     raise ValueError("Users must have username")



        # email  = self.normalize_email(email)

        user =  self.model(
            email =  email,
            first_name=first_name,
            last_name=last_name
        )

       

        user.set_password(password)

        user.save(using=self._db)
        return user
    # def create_superuser(self, email , password=None):
    #     user = self.create_user(
    #         email,
    #         password=password
    #     )
        
    #     user.is_admin = True
    #     user.is_staff = True
    #     user.is_superuser = True

    #     user.save(using=self._db)
    #     return user
    



class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=120 , unique =True)
    # username =  models.CharField(max_length=20)
    phone =  models.CharField(max_length=15 , null=True)
    first_name = models.CharField(max_length=25 )
    last_name = models.CharField(max_length=25 )
    password = models.CharField(max_length=200 )
    is_active = models.BooleanField(default=True)

    is_stuff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS= ["password"]

    objects = CustomUserManager()



    # def get_full_name(self) -> str:
    #     return super().get_full_name()f'{self.first_name} {self.last_name}'

   


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


