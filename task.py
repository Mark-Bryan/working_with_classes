class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def get_status(self):
        if self.is_done == True:
            return "Completed"

        else:
            return "Incomplete"
