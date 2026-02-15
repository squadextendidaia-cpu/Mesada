class Task:
    """
    Classe para representar uma tarefa.
    """
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.status = "pending"  # statuses: pending, completed, canceled

    def complete(self) -> None:
        """
        Marca a tarefa como completa.
        """
        self.status = "completed"

    def cancel(self) -> None:
        """
        Cancela a tarefa.
        """
        self.status = "canceled"

    def __str__(self) -> str:
        return f"Task(title={self.title}, description={self.description}, status={self.status})"