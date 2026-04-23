# ########## const #################
tasks = [
    {"id": 1, "title": "Learn Flask",       "completed": False},
    {"id": 2, "title": "Build API",         "completed": False},
    {"id": 3, "title": "Test with Postman", "completed": True},
]


def get_all_tasks():
    return (tasks)


def get_task_by_id(int: task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
