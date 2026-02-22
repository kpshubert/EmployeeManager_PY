from django.db import connection

def employees_in_department(DepartmentID):
    with connection.cursor() as cursor:
        cursor.execute("USE dEmployeeManager")
        cursor.execute("SELECT COUNT(*) FROM tEM_Employee WHERE tEM_Employee.DepartmentID =" + str(DepartmentID))
        result = cursor.fetchall()
        return result[0][0]