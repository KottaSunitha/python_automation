import csv


def write():
    """this is write function"""
    with open(r"C:\Users\sk21163\Desktop\sunithanew\employee.csv", "w", newline="", encoding="utf8") as file:
        fieldnames = ["emp_id", "emp_name", "emp_salary"]
        obj = csv.DictWriter(file, fieldnames=fieldnames)
        obj.writeheader()
        obj.writerow({"emp_id": 21000, "emp_name": "sunitha", "emp_salary": 60000})
        obj.writerow({"emp_id": 21001, "emp_name": "anvesh", "emp_salary": 80000})
        obj.writerow({"emp_id": 21002, "emp_name": "tirumal", "emp_salary": 40000})

        def update():
            obj.writerow({"emp_id": 21271, "emp_name": "banala", "emp_salary": 20000})
        update()


write()