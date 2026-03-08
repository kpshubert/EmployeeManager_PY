from django.db import connection

def employees_in_department(DepartmentID):
    with connection.cursor() as cursor:
        cursor.execute("USE dEmployeeManager")
        cursor.execute("SELECT COUNT(*) FROM tEM_Employee WHERE tEM_Employee.DepartmentID =" + str(DepartmentID))
        result = cursor.fetchall()
        return result[0][0]

def prepend_if_not_empty(operation_string, prepend_string):
    return_value = ''

    if operation_string == '':
        return_value = ''
    else:
        return_value = f'{prepend_string}{operation_string}'

    return return_value
