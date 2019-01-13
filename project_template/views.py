from django.shortcuts import render
from django.urls import reverse
from moonsheep.views import TaskView


class TranscriptionView(TaskView):
    def get_success_url(self):
        """
        Where to return after successful form submission?
        :return:
        """

        # Serve next task!
        return reverse('task')
