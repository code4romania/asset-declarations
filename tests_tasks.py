from django.test import TestCase

import project_template.tasks as tasks
import project_template.models as models
import project_template.forms as forms


class InitialInformationTestCase(TestCase):
    pass

class TableTestCase(TestCase):
    def setUp(self):
        self.task_table_classes = [x for x in dir(tasks) if x.endswith('Table')]

    def test_form_class_exist(self):
        passed = True

        for klass in self.task_table_classes:
            klass_instance  = getattr(tasks, klass)()

            try:
                klass_instance_in_froms = klass_instance.task_form()
            except NameError as e:
                self.assertTrue(False, f'{e}')

            name = klass_instance_in_froms.__class__.__name__
            if not name.endswith('Table'):
                print(f'{name} should end with Table.')
                passed = False

        self.assertTrue(passed, 'Not all Form classes end in Table.')

    def test_model_class_exists(self):
        passed = True

        for klass in self.task_table_classes:
            klass_instance = getattr(tasks, klass)()

            try:
                klass_instance_in_models = klass_instance.storage_model()
            except NameError as e:
                self.assertTrue(False, f'{e}')

            name = klass_instance_in_models.__class__.__name__
            if not name.endswith('Table'):
                print(f'{name} should end with Table.')
                passed = False

            self.assertTrue(passed, 'Not all Form classes end in Table.')


class RowEntryTestCase(TestCase):
    pass