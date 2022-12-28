from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
import re
# Create your views here.


def admin_home(request):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
   
    return render(request,'admin_home.html')

def add_movie(request):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    if request.method == "POST":
        image=request.FILES.get('image')
        name=request.POST['name']
       
        director=request.POST['director']
        description=request.POST['description']
        actor=request.POST['actor']
        rlz=request.POST['date']
        gen_id=request.POST['genre']
        genre=Genres.objects.get(id=gen_id)
        
        
        new_movie=Movies.objects.create(title=name,genre=genre,director=director,lead_actor=actor,release_date=rlz,movie_images=image,description=description)
        new_movie.save()
        messages.info(request,'movie added')
        return redirect('http://127.0.0.1:8000/movie_list')
        pass
    else:
        genere=Genres.objects.all()
        context={'genre':genere}
        return render(request,'add_movie.html',context)

def admin_movie_list(request):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    movie=Movies.objects.all()
    context={'movie_list':movie}
    return render(request,'admin_movie_list.html',context)

def edit_movie(request,pk):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    if request.method == "POST":
        image=request.FILES.get('image')
        name=request.POST['name']
       
        director=request.POST['director']
        description=request.POST['description']
        actor=request.POST['actor']
        rlz=request.POST['date']
        gen_id=request.POST['genre']
        genre=Genres.objects.get(id=gen_id)
        movie=Movies.objects.get(id=pk)
        if rlz is None:
            rlz=movie.release_date
        movie.title=name
        movie.genre=genre
        movie.director=director
        movie.lead_actor=actor
        movie.release_date=rlz
        movie.movie_images=image
        movie.description=description
        
        
       
        movie.save()
        return redirect('http://127.0.0.1:8000/movie_list')
    else:
        movie=Movies.objects.get(id=pk)
        genere=Genres.objects.all()
   
        context={'movie':movie,'genre':genere}
        return render(request,'movie_edit.html',context)

 
 


def delete_movie(request,pk):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    movie=Movies.objects.filter(id=pk)
    movie.delete()
    messages.info(request,'movie deleted')
    return redirect("http://127.0.0.1:8000/movie_list")

#genre

def add_genre(request):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    if request.method == "POST":
        image=request.FILES.get('image')
        name=request.POST['name']
       
        
        
        
        new_genre=Genres.objects.create(name=name,genre_image=image)
        new_genre.save()
        messages.info(request,'genre added')
        return redirect('http://127.0.0.1:8000/genre_list')
        
    else:
        
        return render(request,'add_genre.html')

def admin_genre_list(request):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    genre=Genres.objects.all()
    context={'genre_list':genre}
    return render(request,'admin_genre_list.html',context)

def edit_genre(request,pk):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    if request.method == "POST":
        image=request.FILES.get('image')
        name=request.POST['name']
       
        
        genre=Genres.objects.get(id=pk)
        genre.name=name
        genre.genre_image=image
        genre.save()
        
        
       
        
        return redirect('http://127.0.0.1:8000/genre_list')
    else:
       
        genere=Genres.objects.get(id=pk)
   
        context={'genre':genere}
        return render(request,'genre_edit.html',context)

 
 


def delete_genre(request,pk):
    try:
        uname = request.session['username']
        
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    genre=Genres.objects.filter(id=pk)
    genre.delete()
    messages.info(request,'genre deleted')
    return redirect("http://127.0.0.1:8000/genre_list")


def admin_signin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        log=admin_login.objects.filter(username=username,password=password)
        if log:
            request.session['username']=username
            return redirect("http://127.0.0.1:8000/admin_sec")
        else:
            msg = '<h1> Invalid Uname or Password!!!</h1>'
            context ={ 'msg1':msg }
            return render(request,'admin_login.html',context)
        
    else:
        
       return render(request,'admin_login.html')
   

def admin_logout(request):
    try:
        del request.session['username']
      
    except:
        return redirect("http://127.0.0.1:8000/admin_login")
    else:
        return redirect("http://127.0.0.1:8000/admin_login")
   
   

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        elif admin_login.objects.filter(username=username,password=password):
            request.session['username']=username
            return redirect("http://127.0.0.1:8000/admin_sec")
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect("http://127.0.0.1:8000/login")
    else:
        return render(request,'user_login.html')


def register(request):
    if request.method == "POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['pwd']
        password2=request.POST['confpwd']
        mobile=request.POST['mobile']
        validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
        st=re.match(validate_phone_number_pattern,str(mobile))
        print(st)
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if(re.search(regex,email)):
            em=True 
        else:
            em=False
        print(em)
        
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request,"Username already exist please choose another")
                return redirect("http://127.0.0.1:8000/register")
            elif User.objects.filter(email=email):
                messages.info(request,"Email Taken Please choose another")
                return redirect("http://127.0.0.1:8000/register")
            elif st==None:
                messages.info(request,"Invalid Mobile Number.Must start with 6-9")
                return redirect("http://127.0.0.1:8000/register")
            elif em==False:
                messages.info(request,"Your Gmail is wrong Please Check")
                return redirect("http://127.0.0.1:8000/register")
            
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                
                user_model=User.objects.get(username=username)
                id_usr=user_model.id
                new_profile=profile.objects.create(user=user_model,id_user=id_usr,fname=fname,lname=lname,mobile=mobile)
                new_profile.save()
                return redirect("http://127.0.0.1:8000/login")
        else:
            messages.info(request,"password not matching")
            return redirect("http://127.0.0.1:8000/register")
    
    else:
        return render(request,'register.html')
    
    
#user

def index(request):
    if request.method == "POST":
        search=request.POST["search"]
        movies=Movies.objects.filter(title__icontains=search)
        no=len(movies)
        return render(request,'searchresult.html',{'result': movies,'no':no})
     
    else:
        genre=Genres.objects.all()[:3]
        movies=Movies.objects.all()[:5]
        context={'genre':genre,'movies':movies}
        return render(request,"index.html",context)


def allgenre(request):
    genre=Genres.objects.all()
    return render(request,'all_genre_user.html',{'genre':genre})


def selectgenre(request):
    genre_id =request.GET.get('genre_id')
    genre=Genres.objects.get(id=genre_id)
    movies=Movies.objects.filter(genre=genre)
    context={'movies':movies}
    return render(request,'allmovies.html',context)

def searchresult(request):
    if request.method == "POST":
        search=request.POST["search"]
        movies=Movies.objects.filter(title__icontains=search)
        no=len(movies)
        return render(request,'searchresult.html',{'result': movies,'no':no})
def allmovies(request):
    movies=Movies.objects.all()
   
   
    context={'movies':movies}
    return render(request,'allmovies.html',context)


@login_required(login_url="http://127.0.0.1:8000/login")
def moviedetail(request,pk):
    no=pk
    movie=Movies.objects.get(id=pk)
    reviews=Review.objects.filter(Movie=movie)
    user=request.user
    rating=Rating.objects.filter(Movie=movie)
    rating_avg=rating.aggregate(Avg('rate'))
    avg=rating_avg['rate__avg']
    avg1=str(avg)
    avg2=round(avg, 2)
    print(avg2)
    rating_count=rating.count()
    rate_filter = Rating.objects.filter(Movie=movie,author=user).first()
    watchlist_filter = Watchlist.objects.filter(Movie=movie,author=user).first()
    if watchlist_filter == None:
        watch=0
    else:
        watch=1

    if rate_filter == None:
        status=0
        rate=0
        
    else:
        rate=rate_filter.rate
        status=1

    context={'movie':movie,'reviews' : reviews,'profile':user ,'status' : status,'rate':rate,'avg': avg2,'rating_count':rating_count,'watch' : watch}
    
    if request.method == "POST" and 'btnform2' in request.POST:
        description=request.POST['description']
        
       
        author=request.user
        new_comment=Review.objects.create(description=description,Movie=movie,author=author)
        new_comment.save()
        return render(request,'mov-det.html',context)
    elif  request.method == "POST" and 'btnform1' in request.POST:
        rate=request.POST["rate"]
        user_rate = Rating.objects.filter(Movie=movie,author=user).first()
        if user_rate == None:
            new_rate=Rating.objects.create(Movie=movie,author=user,rate=rate)
            new_rate.save()
            
            print(status)
        
            return redirect("/movie-detail/"+ str(no))
        #add
    elif  request.method == "POST" and 'unrate' in request.POST:
        the_rate= Rating.objects.filter(Movie=movie,author=user).first()
        the_rate.delete()
        
        
        return redirect("/movie-detail/"+ str(no))
          
    else:
            
       return render(request,'mov-det.html',context)

def logout(request):
    auth.logout(request)
    return redirect("http://127.0.0.1:8000/login")



def watchlist(request):
    user=request.user
    watch=Watchlist.objects.filter(author=user)
    no=len(watch)
    if request.method == "POST":
        movie_id=request.POST["movie"]
        watch_id=request.POST["watchlist"]
       
        watch=Watchlist.objects.get(id=watch_id)
        watch.delete()
        messages.info(request,"Please Add Your Review")
        return redirect("/movie-detail/"+ str(movie_id))

    else:
        return render(request,'watchlist.html',{'w': watch,'no':no})

def add_watchlist(request,pk):
    movie=Movies.objects.get(id=pk)
    user=request.user
    add=Watchlist.objects.create(Movie=movie,author=user)
    add.save()
    messages.info(request,"Movie Added To watchlist")
    return redirect("/movie-detail/"+ str(pk))