from django.shortcuts import render
from django.http import HttpResponse
from signalwire.relay.task import Task

def testing_signalwire_messages(request):
    project = 'Enter Your Project id Here'
    token = 'Enter Your Token Here'
    task = Task(project=project, token=token)
    success = task.deliver('office', {
        'uuid': 'unique id',
        'data': 'data for your job'
    })
    if success:
        return HttpResponse('Task delivered')
    else:
        return HttpResponse('Error delivering task..')

# Create your views here.
