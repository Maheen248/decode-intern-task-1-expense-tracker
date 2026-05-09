expense_list = []
print("---welcome to expense tracker ---")
user_input = input("Enter how many expenses you wanted to add: ")
for i in range(int(user_input)):
    expense = input(f'Enter expense {i+1} name:').lower()
    try:
     amount = float(input(f'Enter expense {i+1} amount:'))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        continue
    expense_list.append({"name": expense, "amount": amount})

print(f"your current expenses are: {expense_list}")

def add_expense(expense_name , expense_amount):

    expense_list.append({"name" : expense_name , "amount": expense_amount} )
    print(f"{expense_name} has been added to your list")

def remove_expense():
    user_del = input("enter expense you wanted to remove:").lower()
    for exp in expense_list:
        if exp["name"] == user_del:
            expense_list.remove(exp)
            print(f"{user_del} has been removed from your list")
            return
    print(f"{user_del} is not in your list. Please enter a valid expense name.")

def update_expense_name(old_name , new_name):
    for expense in expense_list:
        if expense["name"] == old_name:
            expense["name"] = new_name
            print(f"{old_name} has been updated to {new_name}")
            return
    print(f"{old_name} is not in your list. Please enter a valid expense name.")

def update_expense_amount(name , new_amount):

    for exp in expense_list:
        if exp["name"] == name:
            exp["amount"] = new_amount
            print(f"{name} has been updated to {new_amount}")
            return
    else:
        print(f"{name} is not in your list. Please enter a valid expense name.")


def view_expense():
    if not expense_list:
        print("Your expense list is empty.")
    else:
        print("Your current expenses are: ")
        for exp in expense_list:
            print(f"{exp['name']} : {exp['amount']}")

def total_expense():
    total = sum(exp["amount"] for exp in expense_list)
    print(f"your total expenses are: {total}")

def save_to_file():
    with open("expense.txt" , "w") as file:
        for exp in expense_list:
            file.write(f"{exp['name']} : {exp['amount']}\n")

def view_expense_amount():
    view_amount = input("enter the name of expense you wanted to view amount:").lower()
    with open("expense.txt" , "r") as file:
        expenses = file.readlines()
    for exp in expenses:
        name , amount = exp.strip().split(" : ")
        if name == view_amount:
            print(f"The amount for {name} is: {amount}")
            return
    print(f"{view_amount} is not in your list. Please enter a valid expense name.")
    

while True:
    operation = input(" 1.Add expense \n 2.Remove expense \n 3.Update expense name \n 4.Update expense amount \n 5.View expenses \n 6.Total expenses \n 7.Save to file \n 8.View expense amount \n 9.Exit \n Please select an operation: ")
    if operation == "1":
        expense_name = input("enter the name of expense you wanted to add:").lower()
        expense_amount = float(input("enter the amount of expense you wanted to add:"))
        add_expense(expense_name , expense_amount)
        view_expense()

    elif operation == "2":
        remove_expense()
        view_expense()

    elif operation == "3":
        old_name = input("enter the name of expense you wanted to update:").lower()
        new_name = input("enter the updated name of expense:").lower()
        update_expense_name(old_name , new_name)
        view_expense()

    elif operation == "4":
        name = input("enter the name of expense you wanted to update:").lower()
        new_amount = float(input("enter the updated amount of expense:"))
        update_expense_amount(name , new_amount)
        view_expense()

    elif operation == "5":
        view_expense()

    elif operation == "6":
        total_expense() 
    
    elif operation == "7":
        save_to_file()
        print("Expenses saved to file.")
    
    elif operation == "8":
        view_expense_amount()

    elif operation == "9":
        print("---Thanks for using---")
        exit()