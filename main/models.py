from django.db import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import true
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class Covid(Base):
    __tablename__ = 'covid_data'
    idx = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    addr = Column(String)
    company = Column(String)
    reporter = Column(String)
    cate1 = Column(String)
    cate2 = Column(String)
    cate3 = Column(String)
    keyword = Column(String)

    def __repr__(self):
        return "<Covid(addr='%s', company='%s', reporter='%s', cate1='%s', cate2='%s', cate3='%s', keyword='%s')>" % (
            self.addr, self.company, self.reporter, self.cate1, self.cate2, self.cate3, self.keyword)