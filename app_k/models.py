from django.db import models
import uuid

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.core.validators import MinLengthValidator, RegexValidator

class MyUserManager(BaseUserManager):
    def create_user(self, username:str, nickname:str, email:str, password:str)-> 'CustomUser':
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            nickname = nickname,           
        )
        user.set_password(password)
        user.save(using=self._db)
        # Token.objects.create(user=user)
        return user

    def create_superuser(self, username:str, email:str, nickname:str, password:str) -> 'CustomUser':
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            nickname = nickname,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
  email = models.EmailField(verbose_name='Email', max_length=50, unique=True)
  nickname = models.CharField(verbose_name='ニックネーム', max_length=10, default=0, null=False)
  username = models.CharField(verbose_name='username', max_length=10, unique=True, validators=[MinLengthValidator(5,), RegexValidator(r'^[a-zA-Z0-9]*$',)])
  date_joined = models.DateTimeField('登録日', default=timezone.now) 

  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  
  objects = MyUserManager()
 
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email','nickname']

  def __str__(self):
      return self.username

  class Meta:
    db_table = 'Users'


class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL,to_field='username',verbose_name='投稿者', on_delete=models.CASCADE, related_name='when_created_post')
  content = models.TextField('今何してる？', max_length=128)
  created_at = models.DateTimeField('投稿日時', auto_now_add=True) 

  def __str__(self):
    return self.content
  
  class Meta:
    db_table = 'Posts'


class Notification(models.Model):
  post = models.OneToOneField(Post, verbose_name='ポスト', default=0, on_delete=models.SET_NULL, null=True, related_name='which_post')

  class Meta:
    db_table = 'Notifications'
    

class Friendlist(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
  reader = models.ForeignKey(settings.AUTH_USER_MODEL, default=0,verbose_name='読んだ人', on_delete=models.CASCADE,related_name='who_met_before',to_field='username')
  receiver = models.ForeignKey(settings.AUTH_USER_MODEL, default=0,verbose_name='読まれた人', on_delete=models.CASCADE,related_name='receiver',to_field='username')
  read_at = models.DateTimeField('友達になった日', auto_now_add=True) 
  
  def __str__(self):
    return f"{self.reader}&{self.receiver}"

  class Meta:
    db_table = 'Friendlists'