import decimal
import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from employee_list.models import Department, Employee

fake = Faker()

def department_factory(parent=Department.objects.create(name=fake.word().capitalize() + '_department',)):

    if len(parent.get_ancestors()) >= 5:
        return
    else:
        parent = Department.objects.create(
                name=fake.word().capitalize() + '_department',
                parent=parent,
            )
        return department_factory(parent=parent)

def employee_factory(parent_qs):
    for parent in parent_qs:
        for _ in range(400):
            salary = decimal.Decimal('%d.%d' % (random.randint(0,9999999),random.randint(0,99)))
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                date_of_employment=fake.date(),
                salary=salary,
                department=parent,
            )

class Command(BaseCommand):
    help = 'наполняет базу данных подразделениями и сотрудниками'


    def handle(self, *args, **options):
        for _ in range(5):
            department_factory()
        self.stdout.write(f'Подразделения сохранены')

        employee_factory(Department.objects.all())
        self.stdout.write(f'Сотрудники сохранены')
