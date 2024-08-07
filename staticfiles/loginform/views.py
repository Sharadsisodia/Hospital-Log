from django.http import HttpResponse
from django.shortcuts import render, redirect
from formlogin.models import patient,doctor,imagePost,Category,draft
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def logIn(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request,"signupForm.html")



def loginpage(request):
    if request.method == 'POST':
        r_role = request.POST.get('role')
        client_username = request.POST.get('username')
        client_password = request.POST.get('password')
        print("fffffffff",r_role,client_password,client_username)
        
        user = authenticate(request, username=client_username, password=client_password)
        print('uss',user)
        
        if user is not None:

            login(request, user)
            print('login done')
            if r_role == 'patient':
                try:
                    pat = patient.objects.get(user=user)
                    context = {
                        'logged_in': "Patient",
                        'first_name': pat.p_Firstname,
                        'last_name': pat.p_Lastname,
                        'profile_picture': pat.p_Picture.url,
                        'username': pat.p_Username,
                        'email': pat.p_EmailId,
                        'address_line1': pat.p_AddressLi,
                        'city': pat.p_City,
                        'state': pat.p_State,
                        'pincode': pat.p_Pincode
                    }
                    print(context)
                    return redirect('/home/')
                except patient.DoesNotExist:
                    context = {'error': 'No matching patient found.'}
                    return render(request, 'index.html', context)
            elif r_role == 'doctor':
                try:
                    doc = doctor.objects.get(user=user)
                    context = {
                        'logged_in': "Doctor",
                        'first_name': doc.d_Firstname,
                        'last_name': doc.d_Lastname,
                        'profile_picture': doc.d_Picture.url,
                        'username': doc.d_Username,
                        'email': doc.d_EmailId,
                        'address_line1': doc.d_AddressLi,
                        'city': doc.d_City,
                        'state': doc.d_State,
                        'pincode': doc.d_Pincode
                    }
                    return redirect('/home/')
                except doctor.DoesNotExist:
                    context = {'error': 'No matching doctor found.'}
                    return render(request, 'index.html', context)
        else:
            context = {'error': 'Incorrect username or password'}
            return render(request, 'index.html', context)

    elif request.method == 'GET' and request.user.is_authenticated:
        try:
            if hasattr(request.user, 'patient'):
                pat = patient.objects.get(user=request.user)
                context = {
                    'logged_in': "Patient",
                    'first_name': pat.p_Firstname,
                    'last_name': pat.p_Lastnae,
                    'profile_picture': pat.p_Picture.url,
                    'username': pat.p_Username,
                    'email': pat.p_EmailId,
                    'address_line1': pat.p_AddressLi,
                    'city': pat.p_City,
                    'state': pat.p_State,
                    'pincode': pat.p_Pincode
                }
                return render(request, 'patientLogin.html', context)
            elif hasattr(request.user, 'doctor'):
                doc = doctor.objects.get(user=request.user)
                context = {
                    'logged_in': "Doctor",
                    'first_name': doc.d_Firstname,
                    'last_name': doc.d_Lastname,
                    'profile_picture': doc.d_Picture.url,
                    'username': doc.d_Username,
                    'email': doc.d_EmailId,
                    'address_line1': doc.d_AddressLi,
                    'city': doc.d_City,
                    'state': doc.d_State,
                    'pincode': doc.d_Pincode
                }
                return render(request, 'loginPage.html', context)
        except (patient.DoesNotExist, doctor.DoesNotExist):
            context = {'error': 'Profile details could not be found'}
            return render(request, 'index.html', context)

    return render(request, 'loginPage.html')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def signupComp(request):
    if request.method == 'POST':
        f_name = request.POST.get('firstName')
        l_name = request.POST.get('lastName')
        picture = request.FILES.get('profilePicture')
        userName = request.POST.get('username')
        eMail = request.POST.get('email')
        password = request.POST.get('password')
        addr1 = request.POST.get('addressLine1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        role = request.POST.get('role')

        if User.objects.filter(username=userName).exists():
            context = {'usernameExist': 'Username already exists, try using a different username'}
            return render(request, 'signupForm.html', context)

        user = User.objects.create_user(username=userName, password=password, email=eMail, first_name=f_name, last_name=l_name)

        if role == 'patient':
            pat = patient(user=user, p_Firstname=f_name, p_Lastname=l_name, p_Picture=picture, p_Username=userName, p_EmailId=eMail, p_AddressLi=addr1, p_City=city, p_State=state, p_Pincode=pincode)
            pat.save()
        else:
            doc = doctor(user=user, d_Firstname=f_name, d_Lastname=l_name, d_Picture=picture, d_Username=userName, d_EmailId=eMail, d_AddressLi=addr1, d_City=city, d_State=state, d_Pincode=pincode)
            doc.save()

        return render(request, "signupComp.html")

    return render(request, 'signupForm.html')
    
def base(request):
    return render(request,"base.html")

def myPost(request):
    if request.method=='POST':
        print('hihi')

        title=request.POST.get('title')
        image=request.FILES.get('image')
        category=request.POST.get('category')
        summary=request.POST.get('summary')
        content=request.POST.get('content')
        checkbox=request.POST.get('checkbox')
        user=request.user

        if checkbox=='True':
            entryData=imagePost(user=user,iTitle=title, iImage=image, iCategory=category, iSummary=summary, iContent=content,is_draft=True)
            entryData.save()
            return redirect('/mypost/')
        else:
            entryData=imagePost(user=user,iTitle=title, iImage=image, iCategory=category, iSummary=summary, iContent=content,is_draft=False)
            entryData.save()
            return redirect('/mypost/')
    user=request.user
    post=imagePost.objects.filter(user=user)
    context={
        'posts':post
    }
    print(context)
    return render(request,"my_posts.html",context)

def postList(request):
    return render(request,"post_list.html")

def createPost(request):

    return render(request,"create_post.html")

from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = request.user
    print(user, 'jeej')

    if user.is_authenticated:
        print('auth')
        try:
            # Try to get the patient profile first
            pat = patient.objects.get(user=user)
            context = {
                'logged_in': "Patient",
                'first_name': pat.p_Firstname,
                'last_name': pat.p_Lastname,
                'profile_picture': pat.p_Picture.url,
                'username': pat.p_Username,
                'email': pat.p_EmailId,
                'address_line1': pat.p_AddressLi,
                'city': pat.p_City,
                'state': pat.p_State,
                'pincode': pat.p_Pincode
            }
        except patient.DoesNotExist:
            try:
                # If patient profile does not exist, try to get the doctor profile
                doc = doctor.objects.get(user=user)
                context = {
                    'logged_in': "Doctor",
                    'first_name': doc.d_Firstname,
                    'last_name': doc.d_Lastname,
                    'profile_picture': doc.d_Picture.url,
                    'username': doc.d_Username,
                    'email': doc.d_EmailId,
                    'address_line1': doc.d_AddressLi,
                    'city': doc.d_City,
                    'state': doc.d_State,
                    'pincode': doc.d_Pincode
                }
            except doctor.DoesNotExist:
                context = {'error': 'No profile details found for the user.'}
    else:
        context = {'error': 'User is not authenticated.'}
    print(context)

    return render(request, 'loginPage.html', context)

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('/')


def mentalhealth(request):
    posts=imagePost.objects.filter(is_draft=False,iCategory="Mental Health")
    context={
        "catog":"Mental Health Blogs",
        "posts":posts
    }
    return render(request,'patient_post.html',context)

def immune(request):
    posts=imagePost.objects.filter(is_draft=False ,  iCategory="Immunization")
    context={
        "catog":"Immunization Blogs",
        "posts":posts
    }
    return render(request,'patient_post.html',context)

def heart(request):
    posts=imagePost.objects.filter(is_draft=False,iCategory='Heart Disease')
    context={
        "catog":"Heart Disease Blogs",
        "posts":posts
    }
    return render(request,'patient_post.html',context)

def covid(request):
    posts=imagePost.objects.filter(is_draft=False,iCategory='Covid19')
    context={
        "catog":"Covid19 Blogs",
        "posts":posts
    }
    return render(request,'patient_post.html',context)