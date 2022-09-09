from django.shortcuts import render,redirect
from .models import *
from .forms import TodoForm, RegisterForm,UserProfileForm,UserUpdateForm
from django.contrib import messages
from .filters import TodoFilter
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
    
def register(request):
  form = RegisterForm()
  if request.method == "POST":
    form = RegisterForm(request.POST)
    username_check = request.POST['username']
    if User.objects.filter(username=username_check).exists():
      messages.error(request,'Username already exists,Try a new one')
    elif form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request,f'Account has been created for {username} successfully')
      return redirect('login')
    else:
      messages.error(request,'An unknown error occurred during registration')
  context = {'form':form}
  return render(request,'Todo/register.html',context)
  
  
  
def loginUser(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.error(request,'User does not exist or wrong password')
  return render(request,'Todo/login.html')
  
  
def logoutUser(request):
  logout(request)
  return redirect('login')
  
  
@login_required(login_url='login')
def home(request):
    todos = Todo.objects.filter(user=request.user)
    myFilter = TodoFilter(request.GET,queryset=todos)
    todos = myFilter.qs
    return render(request,'Todo/home.html',{'todos':todos,'myFilter':myFilter})
    
    
@login_required(login_url='login')
def profile(request):
  form = UserProfileForm(instance=request.user.profile)
  update_form = UserUpdateForm(instance=request.user)
  if request.method == "POST":
    form = UserProfileForm(request.POST,request.FILES,instance=request.user.profile)
    update_form = UserUpdateForm(request.POST,instance=request.user)
    if form.is_valid() and update_form.is_valid():
      form.save()
      update_form.save()
      messages.success(request,'Profile was updated successfully!')
  context = {'form':form,'update_form':update_form}
  return render(request,'Todo/profile.html',context)
  
  
def newTodo(request):
  form = TodoForm()
  context = {'form':form}
  if request.method == "POST":
    form = TodoForm(request.POST)
    if form.is_valid():
      form = form.save(commit=False)
      form.user = request.user
      form.save()
      messages.success(request,'Task was created successfully!')
      return redirect('home')
  return render(request,'Todo/new_todo.html',context)
    
    
def updateTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    form =TodoForm(instance=todo)
    context = {'form':form}
    if request.method == "POST":
        form =TodoForm(request.POST,instance=todo)
    if form.is_valid():
            form.save()
            messages.success(request,'Task was updated successfully!') 
            return redirect('/')
    return render(request,'Todo/update.html',context)
    
        
def deleteTodo(request,pk):
    todo = Todo.objects.get(id=pk)
    context = {'todo':todo}
    if request.method == "POST":
        todo.delete()
        messages.error(request,'Task was successfully deleted!')
        return redirect('/')
    return render(request,'Todo/delete.html',context)
    
 
def report(request):
     todos = Todo.objects.filter(user=request.user)
     done = Todo.objects.filter(completed=True,user=request.user).count()
     incomplete = Todo.objects.filter(completed=False,user=request.user).count()
     context = {'todos':todos,'done':done,'incomplete':incomplete}
     return render(request,'Todo/my_report.html',context)                                           