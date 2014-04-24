from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from models import Poll

def index(request):
    lastest_poll_list = Poll.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    #context = RequestContext(request, {
    #    'lastest_poll_list':lastest_poll_list,
    #})
    context = {"lastest_poll_list":lastest_poll_list}
    return render(request, "polls/index.html", context)
    #return HttpResponse(template.render(context))

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, "polls/detail.html", {"poll":poll})

def results(request, poll_id):
    return HttpResponse("result %s" %poll_id)

def vote(request, poll_id):
    return HttpResponse("vote %s" %poll_id)
