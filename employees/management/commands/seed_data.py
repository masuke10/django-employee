from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from employees.models import Employee
from departments.models import Department
import random

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create departments
        departments = [
            'Engineering',
            'Marketing',
            'Sales',
            'Human Resources',
            'Finance',
            'Operations',
            'Research & Development'
        ]
        
        department_objects = []
        for dept_name in departments:
            dept, created = Department.objects.get_or_create(name=dept_name)
            department_objects.append(dept)
            if created:
                self.stdout.write(f'Created department: {dept_name}')
        
        # Create employees
        for _ in range(20):  # Create 20 employees
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            department = random.choice(department_objects)
            date_of_joining = fake.date_between(start_date='-5y', end_date='today')
            
            employee = Employee.objects.create(
                name=name,
                email=email,
                phone_number=phone,
                department=department,
                date_of_joining=date_of_joining,
                position=fake.job(),
                salary=random.randint(30000, 150000)
            )
            self.stdout.write(f'Created employee: {name}')