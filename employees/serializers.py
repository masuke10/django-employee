from rest_framework import serializers
from .models import Employee
from departments.serializers import DepartmentSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'address', 
                 'date_of_joining', 'department', 'department_name', 'created_at']

class EmployeeDetailSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'address', 
                 'date_of_joining', 'department', 'created_at'] 