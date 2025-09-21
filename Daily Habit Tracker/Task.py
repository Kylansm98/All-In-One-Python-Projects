def Task:
    def__init(self, name, description, frequency, priority):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.priority = priority
        self.compleated = False

    def mark_as_compleated(self):
        self.compleated = True
    def mark_as_incompleated(self):
        self.compleated = False