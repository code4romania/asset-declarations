from moonsheep.models import Task
from moonsheep.tasks import AbstractTask


class DigitalizationTask(AbstractTask):
    child_tasks = []

    def after_save(self, verified_data):
        for class_name in self.child_tasks:
            self.create_new_task(class_name)

    def average_subtasks_count(self):
        return len(self.child_tasks) or 1

    def create_new_task(self, class_name, extra_params=None):
        params = {**extra_params, **self.instance.params} if extra_params else self.instance.params

        # TODO: get current module name
        full_class_name = f"project_template.tasks.{class_name}"

        Task.objects.create(type=full_class_name, doc_id=self.instance.doc_id, parent=self.instance, params=params)


class RowEntryTask(DigitalizationTask):
    def save_verified_data(self, verified_data: dict):
        verified_data["row_number"] = self.params.get("row_number")
        verified_data["table_id"] = self.params.get("table_id")
        return verified_data


class CountTableRowsTask(DigitalizationTask):
    task_form = None
    storage_model = None
    template_name = "tasks/row_count_template.html"

    def save_verified_data(self, verified_data):
        # TODO: add declaration here
        table, _ = self.storage_model.objects.get_or_create(count=verified_data["count"])
        self.params["table_id"] = table.id

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        number_rows = int(verified_data["count"])

        for row_number in range(1, number_rows + 1):
            for child_class in self.child_tasks:
                self.create_new_task(
                    child_class.__name__, {"row_number": row_number, "table_id": self.params["table_id"]}
                )
