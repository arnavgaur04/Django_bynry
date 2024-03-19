from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Request

def home(request):
  print(request.user.id)
  return render(request, 'home.html')

def newrequest(request):
  if request.user.id == None:
    return render(request, 'myfirst.html')
  
  if request.method=="POST":
    requestBy = request.user.id
    print("this is post")
    requestType = request.POST['type']
    text = request.POST['text']
    Request_instance = Request.objects.create(requestBy = requestBy, requestType = requestType, requestDetails=text)

  return render(request, 'new-request.html')

def viewrequest(request):
  if request.user.id == None:
    return render(request, 'myfirst.html')
  
  requestBy = request.user.id
  data = Request.objects.filter(requestBy = requestBy).values()
  template = loader.get_template('view-request.html')
  context = {
    'data': data,
  }

  return HttpResponse(template.render(context, request))


