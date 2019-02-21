from moonsheep.tasks import AbstractTask


# This class is temporary.
# It is used in the development stage. 
# All Task classes MUST inherit this class.
# Once Catpol-Declaratii moved into the deployment phase,
# all Task casses WILL inherit AbstractTask once more.
# The purpose of this class is to simulate child-parent relationships
# within Task classes. 
class DigitalizationTask(AbstractTask):
    
    def create_new_task(self, task, info):
        from moonsheep.register import base_task
        base_task.register(task)