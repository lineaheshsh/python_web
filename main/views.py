from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from django.shortcuts import redirect, render
from .models import Covid, Post

# Create your views here.
def index(request):
    return render(request,'main/index.html')

## blog 페이지
def blog(request):

    postlist = Post.objects.all()

    return render(request,'main/blog.html', {'postlist': postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'main/posting.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

def covid(request):
    id = "root"
    password = "1q2w3e4r5t"
    host = "localhost"
    db_name = "covid"
    
    engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4".format(id, password, host, db_name), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    print(session)

    query_request = session.query(Covid).all()

    return render(request,'main/covid.html', {'covidList': query_request})

def covidAdd(request):
    if request.method == 'POST':
            id = "root"
            password = "1q2w3e4r5t"
            host = "localhost"
            db_name = "covid"
            
            engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4".format(id, password, host, db_name), pool_pre_ping=True)
    
            Session = sessionmaker(bind=engine)
            session = Session()
            print(session)

            covid = Covid(addr=request.POST['addr'], company=request.POST['company'], reporter=request.POST['reporter'], cate1=request.POST['cate1'], cate2=request.POST['cate2'], cate3=request.POST['cate3'], keyword=request.POST['keyword'])
            session.add(covid)
            session.commit()

            return redirect('/covid/')
    return render(request, 'main/covidAdd.html')