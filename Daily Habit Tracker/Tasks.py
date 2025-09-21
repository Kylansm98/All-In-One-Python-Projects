def Tasks:
    def __init__(self, name )
    self.name = name
    self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        
    def remove_task(self, task):
        self.tasks.remove(task)