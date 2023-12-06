from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse 

from django.views.generic import ListView, DetailView
from .models import Question, Choice

# Create your views here.
class IndexView(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_question_list'] = Question.objects.order_by('-pub_date')[:5]
        return context


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else : 
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))