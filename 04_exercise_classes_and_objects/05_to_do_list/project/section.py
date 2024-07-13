from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {new_task}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        # for task in self.tasks:
        #     if task.name == task_name:
        #         task.complete = True
        #         return f'Task {task_name} marked as completed'
        t = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.complete = True
            return f'Completed task {t.name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        total_tasks = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f'Cleared {total_tasks - len(self.tasks)} tasks.'

    def view_section(self):
        task_details = '\n'.join(t.details() for t in self.tasks)
        return f'Section {self.name}:\n{task_details}'
