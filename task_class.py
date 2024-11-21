from task import Task

task = Task("Finished OOP exercises")
task.mark_done()

print(f"Task Name is: {task.description}")
print(f"Task Status is: {task.get_status()}")
