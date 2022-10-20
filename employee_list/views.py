from django.views.generic import ListView

from employee_list.models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = "employee_list/base.html"
