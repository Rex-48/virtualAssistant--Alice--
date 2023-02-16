from datetime import datetime, timedelta

# Get tasks and their durations from the user

def task_scheduler():
    tasks = []
    while True:
        task_name = input("Enter task name (or press Enter to finish): ")
        if not task_name:
            break
        duration = int(input("Enter time required for the task in minutes: "))
        tasks.append((task_name, duration))
    
    # Get task priorities from the user
    priorities = input("Enter task priorities (comma-separated list): ").split(",")
    
    # Initialize the current time to the start of the day
    
    print("diet routine")
    print("")
    
    current_time = datetime(2023, 2, 17, 8, 0, 0)
    print(f"{current_time:%H:%M} - 9:00: Breakfast")
    
    current_time = datetime(2023, 2, 17, 13, 0, 0)
    print(f"{current_time:%H:%M} - 14:00: Lunch")
    
    print("hobbies must get some time you know!!!!")
    print("")
    
    current_time = datetime(2023, 2, 17, 14, 0, 0)  
    print(f"{current_time:%H:%M} - 15:10: your hobbies")
    
    current_time = datetime(2023, 2, 17, 10, 0, 0)
    
    print(" your tasks are scheduled here,15 mins break is given after each task")
    print("")
    print("")
    # Schedule the tasks according to their priorities
    for priority in priorities:
        for task in tasks:
            if task[0] == priority:
                task_name, duration = task
                if current_time.time() >= datetime(2023, 2, 17, 13, 0, 0).time() and current_time.time() < datetime(2023, 2, 17, 15, 0, 0).time():
                      current_time = datetime(2023, 2, 18, 15, 15, 0) 
                
                start_time = current_time
                finish_time = start_time + timedelta(minutes=duration)
                print(f"{start_time:%H:%M} - {finish_time:%H:%M}: {task_name}")
                current_time = finish_time + timedelta(minutes=15)
    
    # Schedule remaining tasks if any
    if priorities:
        remaining_tasks = [task for task in tasks if task[0] not in priorities]
    else:
        remaining_tasks = tasks
    
    if remaining_tasks:
        print("Remaining tasks:")
        for task in remaining_tasks:
            task_name, duration = task
            start_time = current_time
            finish_time = start_time + timedelta(minutes=duration)
            print(f"{start_time:%H:%M} - {finish_time:%H:%M}: {task_name}")
            current_time = finish_time + timedelta(minutes=15)
    
    # Schedule dinner and free time
    print(f"{current_time:%H:%M} - {current_time + timedelta(minutes=15):%H:%M}: Refreshment")
    current_time += timedelta(minutes=15)
    
    
    print(f"{current_time:%H:%M} - {current_time + timedelta(minutes=45):%H:%M}: Dinner")
    current_time += timedelta(minutes=45)
    
    print(f"{current_time:%H:%M} - 24:00: Free time")
    

