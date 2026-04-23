"""can delete it - as now use MongoDB - used at past when all store in memory only"""
import uuid

# ########## const #################

# initizlize data for start - static id for easier postman testing (the 4th task with uuid - as it should be):
tasks = [
    {"id": "1", "title": "Learn Flask",       "completed": False},
    {"id": "2", "title": "Build API",         "completed": False},
    {"id": "3", "title": "Test with Postman", "completed": True},
    {
        "id":  str(uuid.uuid4()),
        "title": "4th taks - with uuid4",
        "completed": True
    }
]


def get_tasks():
    # return all tasks.
    return tasks


def get_task(task_id):
    # return task obj from id .
    for task in tasks:
        if task_id == task["id"]:
            return task


def create_task(task_data):
    # we create TO-DO, so always default start as incomplete.
    new_task = {
        "id": str(uuid.uuid4()),
        "title": task_data["title"].strip(),
        "completed": False
    }
    tasks.append(new_task)
