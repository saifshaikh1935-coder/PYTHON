tasks = []

def add_task():
    task = input("Enter task: ")
    tags = set(input("Enter tags: ").split())
    
    tasks.append({
        "task": task,
        "tags": tags
    })

def display_all():
    for item in tasks:
        print(item)

def find_by_tag():
    tag = input("Enter tag: ")
    
    for item in tasks:
        if tag in item["tags"]:
            print(item)

add_task()
add_task()

display_all()
find_by_tag()