from cs50 import*
import random

def load_data():
    print('this is load data')
    file = open("emp.txt", 'r')
    employee_id_list = []
    firstname_list = []
    surname_list = []
    salary_list = []
    email_list = []
    while True:
        data = file.readline()
        if(data == ''):
            break
        list1 = data.split(",")
        employee_id_list.append(list1[0])
        firstname_list.append(list1[1])
        surname_list.append(list1[2])
        salary_list.append(list1[4])
        email_list.append(list1[3])
    file.close()
    return employee_id_list, firstname_list, surname_list, email_list, salary_list

def show_all_employee(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    for item in employee_id_list:
        print(item, " ", end="")
    print('\n')
    for item in firstname_list:
        print(item, " ", end="")
    print('\n')
    for item in surname_list:
        print(item, ' ', end="")
    print('\n')
    for item in email_list:
        print(item, ' ', end="")
    print('\n')
    for item in salary_list:
        item = item.strip('\n')
        print(item, ' ', end="")
    print('\n')

def show_employee(empid, employee_id_list, firstname_list, surname_list, email_list, salary_list):
    position = find_employee_pos_in_list(empid, employee_id_list)
    if position != -1:
        print(employee_id_list[position], ' ', end="")
        print(firstname_list[position], ' ', end="")
        print(surname_list[position], ' ', end="")
        print(email_list[position], ' ', end="")
        print(salary_list[position], ' ', end="")
        print('\n')
    else:
        print('Employee id is incorrect.')

def remove_employee(empid, employee_id_list, firstname_list, surname_list, email_list, salary_list):
    position = find_employee_pos_in_list(empid, employee_id_list)
    if position != -1:
        del employee_id_list[position]
        del firstname_list[position]
        del surname_list[position]
        del email_list[position]
        del salary_list[position]
        file1 = open('emp.txt', 'r')
        lines = file1.readlines()
        file2 = open('emp.txt', 'w')
        for line in lines:
            if not line.startswith(empid):
                file2.write(line)
        file1.close()
        file2.close()

    else:
        print('Employee id is incorrect')

def find_employee_pos_in_list(empid, employee_id_list):
    if empid in employee_id_list:
        position = employee_id_list.index(empid)
        return position
    else:
        return -1

def change_salary(empid, employee_id_list, salary_list):
    position = find_employee_pos_in_list(empid, employee_id_list)
    if position != -1:
        salary = str(input('Enter Salary: '))
        if(float(salary) >= 0):
            oldsal = str(salary_list[position])
            salary_list.insert(position, salary)
            del salary_list[position+1]
            file1 = open('emp.txt', 'r')
            line = file1.read()
            file2 = open('emp.txt', 'w')

            if oldsal in line:
                salary = salary + '\n'
                file2.write(line.replace(oldsal, salary))
            file1.close()
            file2.close()
        else:
            print('Salary cannot be set negative')
    else:
        print('Employee id is incorrect.')

def generate_unique_id(employee_id_list):
    valid = 'false'
    while valid == 'false':
        empid = str(random.randint(100000,999999))
        if not empid in employee_id_list:
            valid = 'true'
    return empid

def generate_unique_email(email_list, firstname, surname):
    valid = 'false'
    while valid == 'false':
        temp = str(random.randint(1,100))
        email = str(firstname + '.' + surname + temp + '@cit.com')
        if not email in email_list:
            valid = 'true'
    return email

def add_employee(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    empid = generate_unique_id(employee_id_list)
    firstname = str(input('Enter Firstname: '))
    surname = str(input('Enter Surname: '))
    salary = str(input('Enter salary: '))
    email = generate_unique_email(email_list, firstname, surname)
    line = str('\n' + empid + ',' + firstname + ',' + surname + ',' + email +',' + salary)
    employee_id_list.append(empid)
    firstname_list.append(firstname)
    surname_list.append(surname)
    email_list.append(email)
    salary_list.append(salary)
    return line

def show_menu(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    ans = 'n'
    while(ans != 'y'):
        print('Press 1 for All Employee Data')
        print('Press 2 for Show Employee')
        print('Press 3 for Change Salary')
        print('Press 4 for Add Employee')
        print('Press 5 for Remove Employee')
        print('Press 6 for Save Bonus Info')
        print('Press 7 for Generate Report')
        choice = input('Input your choice: ')

        if(int(choice) ==1):
            show_all_employee(employee_id_list, firstname_list, surname_list, email_list, salary_list)

        elif(int(choice) == 2):
            empid = str(input('Employee id: '))
            show_employee(empid, employee_id_list, firstname_list, surname_list, email_list, salary_list)

        elif(int(choice) == 3):
            empid = str(input('Employee id: '))
            change_salary(empid, employee_id_list, salary_list)

        elif(int(choice) == 4):
            line = add_employee(employee_id_list, firstname_list, surname_list, email_list, salary_list)
            return line

        elif(int(choice) == 5):
            empid = str(input('Employee id: '))
            remove_employee(empid, employee_id_list, firstname_list, surname_list, email_list, salary_list)
        elif(int(choice)== 6):
            generate_bonus_info(firstname_list,surname_list,employee_id_list,salary_list)

        elif(int(choice) == 7):
            generate_report(salary_list, firstname_list, surname_list)
        ans = input('do u want to exit? type y for yes and n for no: ')
        ans = ans.lower()

    line = 'true'
    return line


def save_data(line):
    if not line == 'true':
        file1 = open('emp.txt', 'r')
        lines = file1.read()
        file2 = open('emp.txt', 'a')
        file2.write(line)
        file1.close()
        file2.close()
    print('Data is Saved')
    employee_id_list, firstname_list, surname_list, email_list, salary_list = load_data()
    show_menu(employee_id_list, firstname_list, surname_list, email_list, salary_list);

def generate_bonus_info(firstname_list,surname_list,employee_id_list,salary_list):
    percent = float(input('type percentage :>'))
    length = len(employee_id_list)
    file3=open("bonus.txt",'w')
    file3.close()
    file3=open('bonus.txt', 'a')
    for i in range(0,length):
        name = firstname_list[i] + surname_list[i]
        empid = employee_id_list[i]
        bonus = str(percent*float(salary_list[i]))
        line = str(empid) + ',' + str(name) + ',' + bonus + '\n'
        file3.write(line)
    file3.close()

def generate_report(salary_list, firstname_list, surname_list):
    length = len(salary_list)
    salary_sum = 0.00
    new_salary_list = []
    for i in range(0,length):
        new_salary_list.append(float(salary_list[i]))
        salary_sum = salary_sum + new_salary_list[i]

    avg_salary = salary_sum / length
    print('Average Salary: ',avg_salary)

    highest_salary = max(new_salary_list)
    print('Employees earning highest salary are:')
    for i in range(0,length):
        if highest_salary == new_salary_list[i]:
            print(firstname_list[i], end="")
            print(' ',surname_list[i])

def main():
    employee_id_list, firstname_list, surname_list, email_list, salary_list = load_data();
    line = show_menu(employee_id_list, firstname_list, surname_list, email_list, salary_list);
    if not line == 'true' :
        save_data(line)

if __name__ == "__main__":
    main()
