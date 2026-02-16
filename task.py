class Task:
    def __init__(self, title: str, due_date: str, status: str):
        """Initialize a Task instance.
        
        Args:
            title (str): The title of the task.
            due_date (str): The due date of the task.
            status (str): The current status of the task (e.g. "Pending", "Completed").
        """
        self.title = title
        self.due_date = due_date
        self.status = status

    def __repr__(self) -> str:
        return f"Task(title={self.title}, due_date={self.due_date}, status={self.status})"

    def is_completed(self) -> bool:
        """Check if the task is completed.
        
        Returns:
            bool: True if the task is completed, False otherwise.
        """
        return self.status == 'Completed'

    @staticmethod
    def filter_tasks(tasks: list["Task"], filter_type: str) -> list["Task"]:
        """Filter tasks based on status.
        
        Args:
            tasks (list[Task]): The list of Task instances.
            filter_type (str): The type of filter to apply (e.g. "Completed", "Pending").
        
        Returns:
            list[Task]: Filtered list of tasks based on the filter type.
        """
        if filter_type == 'Completed':
            return [task for task in tasks if task.is_completed()]
        elif filter_type == 'Pending':
            return [task for task in tasks if not task.is_completed()]
        return tasks
