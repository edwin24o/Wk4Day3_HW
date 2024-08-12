# (1)Task 1: Define Budget Category Class
# (2)Task 2: Implement Getters and Setters
# (3)Task 3: Add Budget Functionality

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name   #(1) created private category
        self.__allocated_budget = allocated_budget   #(1) created private category
        self.__remaining_budget = allocated_budget  #(3) create a 
    
    def get_category_name(self):   #(2)adding getter to have access and view the __category_name.
        return self.__category_name
    def set_category_name(self, category_name):  #(2)creating setter to control info alteration
        self.__category_name = category_name    
    
    def get_allocated_budget(self): #(2)adding getter to have access and view the __allocated_budget.
        return self.__allocated_budget
    def set_allocated_budget(self, allocated_budget):  #(2)creating setter to control info alteration
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            raise ValueError("Budget must be a positive number")
        
    def add_expense(self,amount):  #(3)added expense to a category and adjusted budget accordingly
        if amount <= 0:
            raise ValueError("Expense amount must be a positive number")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds the remaining budget") #(3) subtracting amount with the added expense 
        self.__remaining_budget -= amount  

    def display_category_summary(self):   #(4) created method to display info 
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(400)
food_category.display_category_summary()