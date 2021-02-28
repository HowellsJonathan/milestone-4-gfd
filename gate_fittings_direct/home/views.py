from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

def index(request):
    """ A View to return Index page """

    user_agent = get_user_agent(request)
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, 'home/mobile_index.html')
    elif user_agent.is_pc:
        return render(request, 'home/index.html')
