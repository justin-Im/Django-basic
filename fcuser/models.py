from django.db import models

# Create your models here.
class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                vervose_name='사용자명')
    password = models.CharFiedl(max_length=64,
                                verbose='비밀번호')
    registered_dttm = models.DataTimeField(auto_now_add=True,
                                            verbose_name='등록시간')
    class Meta:
        db_table = 'fastcampus_fcuser'
