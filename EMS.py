#Employee Management System (EMS)
import os
def clear():
    os.system('clear')
    
EMS = []

def add_employee():
    clear()
    while True:
        try:
            print("\n \t=====ADD Employee=====")
            
            e_id = int(input("Enter [4] digit employee ID::- "))
            if len(str(e_id)) != 4:
                raise ValueError("\n \t Please enter an [4] digit number to create employee ID ")
            
            name = str(input("Enter Employee name::- "))
        
            age = int(input("Enter the Age::- "))
            if len(str(age)) != 2:
                raise ValueError("\n \t Please enter an [2] digit number to insert age to the EMS")
            
            phone = int(input("Enter phone number::- "))
            if len(str(phone)) != 10:
                raise ValueError("\n \t Please enter an [10] digit number to insert phone number to the EMS ")
            
            position = str(input("Enter the position::- "))
            
            employee = {
                'ID':e_id,
                'Name':name,
                'Age':age,
                'Phone':phone,
                'Position':position
            }
            
            EMS.append(employee)
            print(f"\n \t Employee {name} with ID{e_id} added to the EMS successfully.")
            print("\n",employee)
            break
            
        except:
         print("\n \tInvalid input. Please provide valid input")

def view_all_employee():
    clear()
    print("=====ALL EMPLOYEE DETAILS=====")
    if len(EMS) == 0:
        print("\n Provide some data to display here")
    else:
        for employee in EMS:
            print(f"\nEmployee ID  :{employee['ID']} \nName         :{employee['Name']} \nAge           :{employee['Age']} \nPhone        :{employee['Phone']} \nPosition     :{employee['Position']}")


def search_employee():
    clear()
    try:
        print("=====SEARCH EMPLOYEE=====")
        user_input_3 = int(input("Enter [4] digit employee ID::- "))
        if len(str(user_input_3)) != 4:
                raise ValueError("\n \t Please enter an [4] digit number to create employee ID ")
                
        for employee in EMS:
            if employee['ID'] == user_input_3:
                print(f"\nEmployee ID  :{employee['ID']} \nName         :{employee['Name']} \nAge           :{employee['Age']} \nPhone        :{employee['Phone']} \nPosition     :{employee['Position']}")

            else:
                print(f"Employee ID {user_input_3} not found")
    except:
        print("\n \tInvalid input. Please provide valid input")
        
def delete_employee():
    clear()
    try:
        print("=====DELETE EMPLOYEE FROM EMS=====")
        user_input_4 = int(input("Enter [4] digit employee ID::- "))
        if len(str(user_input_4)) != 4:
            raise ValueError
        for i in EMS:
            if i['ID'] == user_input_4:
                print(f"\nEmployee ID  :{i['ID']} \nName         :{i['Name']} \nAge          :{i['Age']} \nPhone        :{i['Phone']} \nPosition     :{i['Position']}")
                user_input_5 = str(input(f"would u like to remove employee {i['Name']} ID:{i['ID']} (Y/N)::- "))
                if user_input_5.lower() == 'y':
                    EMS.remove(i)
                    print(f"\nEmployee {i['Name']} with ID:-{i['ID']} removed from EMS successfully.")
                    break
                elif user_input_5.lower() == 'n':
                    print("User canceled the choice")
                else:
                    print("Enter the given choice (y/n)")
    except:
        print("\n \tInvalid input. Please provide valid input")

def main():
    clear()
    while True:
        try:
            print("\n \t=====Employee Management System======")
            print("\n1.Add employee details \n2.View all employee details \n3.Search employee details \n4.Delete employee details \n5.Exit")
            
            options = int(input("Enter any choice 1 / 2 / 3 / 4 / 5::- "))
            if options == 1:
                add_employee()
            elif options == 2:
                view_all_employee()
            elif options == 3:
                search_employee()
            elif options == 4:
                delete_employee()
            elif options == 5:
                user_input_1 = str(input("Would you like to exit from the program (Y/N):- "))
                if user_input_1.lower() == 'y':
                    print("\n \tExiting from the program !!!HAND!!! ")
                    break
                elif user_input_1.lower() == 'n':
                    print("\n \tProgram continueing")
            else:
                print(f"\n \t{options} is not valid provide a valid input.")
            
        except ValueError:
            print("\n \tInvalid input. Please provide valid input")
        
if __name__ == "__main__":
    main()