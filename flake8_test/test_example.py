employees = {
    "Alex": {"age": 25, "salary": 2500, "department": "IT"},
    "John": {"age": 31, "salary": 3200, "department": "HR"},
    "Mike": {"age": 28, "salary": 4100, "department": "IT"},
    "Kate": {"age": 22, "salary": 2800, "department": "IT"},
}
new_employees = {}
def get_it_employees(employees):
    for key, value in employees.items():
        if value["department"] == "IT":
            new_employees[key] = value
    return new_employees
def get_hr_employees(employees):


    