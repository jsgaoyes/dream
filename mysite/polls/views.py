from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from models import Poll, Choice
from django.views import generic
#def index(request):
#    lastest_poll_list = Poll.objects.order_by("-pub_date")[:5]
#    #template = loader.get_template("polls/index.html")
#    #context = RequestContext(request, {
#    #    'lastest_poll_list':lastest_poll_list,
#    #})
#    context = {"lastest_poll_list":lastest_poll_list}
#    return render(request, "polls/index.html", context)
#    #return HttpResponse(template.render(context))
#
#def detail(request, poll_id):
#    try:
#        poll = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
#    return render(request, "polls/detail.html", {"poll":poll})
#
#def results(request, poll_id):
#    poll = get_object_or_404(Poll, pk=poll_id)
#    return render(request, "polls/result.html", {"poll":poll})
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lastest_poll_list"

    def get_queryset(self):
        return Poll.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/results.html"

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST.get("choice"))
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "poll": p,
            "error_message":"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(p.id,)))
