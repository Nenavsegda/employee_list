import decimal
import random

from employee_list.models import Department, Employee
from faker import Faker

fake = Faker()

parent_1 = Department.objects.create(name=fake.word().capitalize(),)

def department_factory(parent=parent_1):
    from employee_list.models import Department
    from faker import Faker

    fake = Faker()
    if len(parent.get_ancestors()) >= 4:
        return print('Done')
    else:
        parent = Department.objects.create(
                name=fake.word().capitalize(),
                parent=parent,
            )
        department_factory(parent=parent)
        return print('Not yet!')


def employee_factory(parent_qs):
    for parent in parent_qs:
        for _ in range(400):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                date_of_employment=fake.date(),
                salary=decimal.Decimal('%d.%d' % (random.randint(0,9999999),random.randint(0,99))),
                department=parent,
            )
