from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='должность')
    date_of_employment = models.DateField(verbose_name='дата приема на работу')
    salary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='размер заработной платы')
    department = TreeForeignKey('Department', on_delete=models.PROTECT, related_name='employees', verbose_name='подразделение')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Department(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='название подразделения')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='подразделение выше')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'name']]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name
