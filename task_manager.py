
# importing libraries
import datetime
from datetime import date


# creating new empty lists for later...
usernames_list = []
passwords_list = []


# defining new functions...

# function that checks username (user or admin) and displays appropriate menu
def username_fun():
    if username != "admin": 
        m_menu = ("\nPlease select one of the following options:\nr - register user\na - add task\nva - view "
        "all tasks\nvm - view my tasks\ngr - generate reports\ne - exit\n")
    else: 
        m_menu = ("\nPlease select one of the following options:\nr - register user\na - add task\nva - view "
        "all tasks\nvm - view my tasks\nvs - view statistics\ngr - generate reports\nds - display statistics\ne - exit\n")
    return(m_menu)


# function that allows to register new user, checks if in user.txt file username exists already and checks if passwords match
# writes information back to txt file
def admin_reg():
    user_temp1 = open("user.txt", "a")
    username_r = input("Enter a new username:")
    while username_r in usernames_list:
        username_r = input("Username exists already. Enter a new username:")
    else:
        password_r = input("Enter a new password:")
        pass_r_confirm = input("Confirm the password:")
        while pass_r_confirm != password_r:
            pass_r_confirm = input("Passwords don't match. Confirm the password:")
        else:
            user_temp1.write(f"\n{username_r}, {password_r}")
            print("New user registered succesfully.")
        user_temp1.close()

# function that adds a new task to tasks.txt file from user input
def new_task():
        with open("tasks.txt", "a+") as tasks_temp1:
            user_assign = input("Enter username of person taking the task:")
            title_task = input("Enter title of task:")
            description = input("Enter a description of task:")
            today = date.today()
            while True:
                try:
                    day_task = int(input("Enter due day as number (dd): "))
                    month_task = int(input("Enter due month as number (mm): "))
                    year_task = int(input("Enter due year as number (yyyy): "))
                    date_task = (f"{day_task} {month_task} {year_task}")
                    print("You have succesfully added a new task.")
                    return tasks_temp1.write(f"\n{user_assign}, {title_task}, {description}, {today}, {date_task}, No")
                except Exception:
                    print("Not valid dates entered. Try again: ")


# function that displays all tasks in tasks.txt file on screen
def view_all():
     with open("tasks.txt", "r") as tasks_temp2:
        line_va = tasks_temp2.readlines()
        for line in line_va:
            taskl = line.split(", ")
            print("\t\t\t\t\t\tTask information")
            print("~" * 120)
            print(f'''\nTask:\t\t\t{taskl[1]}\nAssigned to:\t\t{taskl[0]}\nDate assigned:\t\t{taskl[3]}\nDue date:   \
            {taskl[4]}\nTask complete?\t\t{taskl[5]}\nTask description:\t{taskl[2]}\n''')
            print("~" * 120)


# function that displays only registered user's tasks on screen
def view_mine():
        for (i, line) in enumerate(line_vm, start=0):
            taskv = line.split(", ")
            if taskv[0] == username:
                print("\t\t\t\t\t\tMy tasks")
                print("~" * 120)
                print(f'''\nTask:\t\t\t{taskv[1]}\nDate assigned:\t\t{taskv[3]}\nDue date:\
               {taskv[4]}\nTask complete?\t\t{taskv[5]}\nTask description:\t{taskv[2]}\nTask number:\t\t{i}''')


# function that allows to edit user's tasks, first the username can be changed from opened txt file and new data is written to file
# then the due date can be edited the same way
# if user selects other than 'us' or 'dd' prints error message
def edit_vm(lines_vm):
    if name_date_edit == "us":
        new_user = input("Enter new username for task:")
        line_task[0] = new_user
        line_str = ", ".join(line_task)
        line_vm[edit_menu] = line_str
        lines_vm.close()
        lines_vm = open("tasks.txt", "w")
        lines_vm.write("".join(i for i in line_vm))
        lines_vm.close()
        print(f"Username changed to {new_user}")
    elif name_date_edit == "dd":
        new_day = int(input("Enter new due day as number (dd):"))
        new_month = int(input("Enter new due month as number (mm):"))
        new_year = int(input("Enter new due year as number (yyyy):"))
        new_dd = (f"{new_day} {new_month} {new_year}")
        line_task[4] = new_dd
        line_str = ", ".join(line_task)
        line_vm[edit_menu] = line_str
        lines_vm.close()
        lines_vm = open("tasks.txt", "w")
        lines_vm.write("".join(i for i in line_vm))
        lines_vm.close()
        print(f"Due date changed to {new_dd}")
    else:
        print("Wrong input.")
    return(lines_vm)


# function that edits user's task from incomplete to complete and writes new data back to file
def edit_compl(lines_vm):
    line_task[5] = "Yes\n"
    line_str = ", ".join(line_task)
    line_vm[edit_menu] = line_str
    lines_vm.close()
    lines_vm = open("tasks.txt", "w")
    lines_vm.write("".join(i for i in line_vm))
    lines_vm.close()
    print("Task marked as complete.")
    return(lines_vm)


# function that opens tasks.txt and calculates tasks' reports information, then saves new data to new file
def tasks_overview():
    counter_user = 0
    counter_compl = 0
    counter_inc = 0
    counter_overd = 0
    tasks_tempf = open("tasks.txt", "r", encoding="utf-8")
    tasks_temp6 = tasks_tempf.readlines()
    totalof_tasks = len(tasks_temp6)
    for line in tasks_temp6:
        task_line = line.split(", ")
        task_over_us = open ("task_overview.txt", "w", encoding= "utf-8")
        if task_line[5] == "Yes\n":
            counter_compl += 1
        else:
            counter_inc += 1
            due_date = datetime.datetime.strptime(task_line[4], "%d %m %Y")
            if due_date > datetime.datetime.now():
                counter_overd += 1
    perc_inc_tasks = "{:.2f}".format(float(100 / totalof_tasks) * counter_inc)
    perc_over_tasks = "{:.2f}".format(float(100 / totalof_tasks) * counter_overd)
    tasks_tempf.close()
    task_over_us.write(f'''User {username} task reports\n\nTotal of tasks generated: {totalof_tasks}
Total of completed tasks: {str(counter_compl)}\nTotal of incomplete tasks: {str(counter_inc)}\nTotal of overdue tasks: {str(counter_overd)}
Percentage of incomplete tasks: {perc_inc_tasks}%\nPercentage of overdue tasks: {perc_over_tasks}%''')
    task_over_us.close()


# function that opens user.txt and tasks.txt and produces report information both general and for the user from those files
# saves reports to new txt file
def user_overview():
    user_tempf= open("user.txt", "r", encoding="utf-8")
    user_temp5 = user_tempf.readlines()
    totalof_users = len(user_temp5)
    user_tempf.close()
    tasksf_temp = open("tasks.txt", "r", encoding="utf-8")
    tasks_temp5 = tasksf_temp.readlines()
    totalof_tasks = len(tasks_temp5)
    counter_user = 0
    counter_compl = 0
    counter_inc = 0
    counter_overd = 0
    for line in tasks_temp5:
        task_line = line.split(", ")
        if task_line[0] == username:
            counter_user += 1
            user_over_us = open ("user_overview.txt", "w", encoding= "utf-8")
            if task_line[5] == "Yes\n":
                counter_compl += 1
            else:
                counter_inc += 1
                due_date = datetime.datetime.strptime(task_line[4], "%d %m %Y")
                if due_date > datetime.datetime.now():
                    counter_overd += 1
    perc_inc_tasks = "{:.2f}".format(float(100 / counter_user) * counter_inc)
    perc_over_tasks = "{:.2f}".format(float(100 / counter_user) * counter_overd)
    percent_user = "{:.2f}".format(float(100 / totalof_tasks) * counter_user)
    percent_comp = "{:.2f}".format(float(100 / counter_user) * counter_compl)
    tasksf_temp.close()
    user_over_us.write(f'''{username} user reports\n\nTotal of users registered: {totalof_users}\nTotal of tasks generated: {str(totalof_tasks)}
Total of tasks assigned to {username}: {str(counter_user)}\nPercentage of tasks assigned to {username}: {percent_user}%
Percentage of {username}'s completed tasks: {percent_comp}%\nPercentage of {username}'s incomplete tasks: {perc_inc_tasks}%
Percentage of {username}'s overdue tasks: {perc_over_tasks}%''')
    user_over_us.close()     

# function that displays task reports on screen
def display_task():
    for line in display_tasks:
        line = line.strip("\n")
        print(line)

# function that displays user reports on screen
def display_use():
    for line in display_user:
        line = line.strip("\n")
        print(line)




# asking for username input
username = input("Enter your username:").lower()

# opens user.txt file and adds all usernames to username list and all passwords to password list from their position in each line
with open("user.txt", "r") as f_temp:
    lines = f_temp.readlines()
    for line in lines:
        words = line.strip("\n")
        words = words.split(", ")
        usernames_list.append(words[0])
        passwords_list.append(words[1])
    dict = dict(zip(usernames_list, passwords_list))

# loop to check if username exists in list, if password exists in list and if they match
while username not in usernames_list:
    username = input("The username does not exist. \nEnter your username:")
else:
    password = input("Enter your password:")
    while password != (dict.get(username)):
        password = input("Incorrect password. \nEnter your password:")
    else:
        print("You are logged in")


# main menu loop
while True:

    # calls username function and asks for input, if it's 'r' only admin has access to admin_reg function
    print(username_fun())
    menu = input().lower()
    if menu == "r" and username == "admin":
        admin_reg()
    elif menu == "r" and username != "admin":
        print("You do not have access to this option.")

    # if menu is 'a' calls new_task function
    elif menu == "a":
        new_task()

    # if it's 'va' calls view_all function
    elif menu == "va":    
        view_all()

    # if it's 'vm' opens tasks.txt, reads lines, calls view_mine function and asks input to select task or go back
    # if user goes back calls menu function, if user selects task that is within range of tasks number allows to edit
    # depending on the option chosen calls the right function, if user asks to edit complete task shows error message
    elif menu == "vm":
        tasks_temp3 = open("tasks.txt", "r")
        line_vm = tasks_temp3.readlines()
        view_mine()
        tasks_temp3.close()
        edit_menu = int(input("Enter task number to select task or\nPress -1 to return to main menu:"))
        if edit_menu == -1:
            username_fun()
        elif edit_menu not in range(len(line_vm)):
            print("Task does not exist.")
        else:
            lines_vm = open("tasks.txt", "r")
            line_vm = lines_vm.readlines()
            line_task = line_vm[edit_menu].split(", ")
            if line_task[0] != username:
                print("Wrong task number.")
            else:
                edit_task = input("Type Y to mark task as complete or\nET to edit task:").lower()
                if edit_task == "y":
                    edit_compl(lines_vm)
                elif edit_task == "et" and line_task[5].strip("\n") == "No":
                    name_date_edit = input("Enter 'US' to change username or 'DD' to change due date:").lower()
                    edit_vm(lines_vm)
                elif edit_task == "et" and line_task[5].strip("\n") == "Yes":
                    print("Task already complete. Cannot edit.")
                else:
                    print("Non existing option.")

    # again only admin has access to 'vs' menu to view statistics from tasks.txt and user.txt files
    elif menu == "vs" and username == "admin":
        with open("tasks.txt", "r") as tasks_temp4:
            num_lines = tasks_temp4.readlines()
            print("\nThe total number of tasks is:")
            print(len(num_lines))
        with open("user.txt", "r") as user_temp2:
            no_lines = user_temp2.readlines()
            print("\nThe total number of registered users is:")
            print(len(no_lines))

    # if menu is 'gr' calls tasks_overview and user_overview functions
    elif menu == "gr":
        tasks_overview()
        user_overview()
        print("Reports generated as text files")

    # if menu is 'ds' again only admin can access it, asks for username of user to view reports
    # calls tasks and user functions to generate reports in case files don't exist
    # then calls the 2 display functions to view results on screen
    elif menu == "ds":
        if username != "admin":
            print("You don't have access to this menu option.")
        else:
            username_temp = username
            username = input("Enter username to view reports:")
            tasks_overview()
            user_overview()
            display_tasks = open("task_overview.txt", "r", encoding="utf-8")
            display_task()
            print()
            print("~" * 20)
            print()
            display_tasks.close()
            display_user = open("user_overview.txt", "r", encoding="utf-8")
            display_use()
            display_user.close()
            username = username_temp

    # if menu is 'e' exits program
    elif menu == "e":
        print("Goodbye :)")
        exit()    

    # if user enters any other menu input prints following message
    else:
        print("You have made a wrong choice. Please try again")        
        
  


