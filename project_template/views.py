from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from moonsheep.views import TaskView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class TranscriptionView(TaskView):
    def get_success_url(self):
        """
        Where to return after successful form submission?
        :return:
        """

        # Serve next task!
        return reverse('task')

