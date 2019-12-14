from moonsheep.tasks import AbstractTask

EXAMPLE_URL = 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf'


class DigitalizationTask(AbstractTask):

    def create_new_task(self, task, info):
        from moonsheep.registry import register
        register(task)

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
        })

        return task_data

    def get_presenter(self):
        return super(DigitalizationTask, self).get_presenter()


class CountTableRowsTask(DigitalizationTask):
    task_form = None
    storage_model = None
    child_class = None
    template_name = 'tasks/row_count_template.html'

    def save_verified_data(self, verified_data):
        model_instance, created = self.storage_model.objects.get_or_create(
            count=verified_data['count'])

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        number_rows = int(verified_data['count'])
        for row_number in list(range(1, number_rows)):
            self.create_new_task(self.child_class, {'row_number': row_number})
