from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=30)          # 실명
    id = models.TextField(primary_key=True)         # 아이디
    pw = models.TextField()                         # 비밀 번호
    phonenum = models.CharField(max_length=30)   # 전화 번호
    schoolssn = models.TextField(null=True)        # 학번

class Images(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가