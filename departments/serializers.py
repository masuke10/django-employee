from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'created_at', 'employee_count']
    
    def get_employee_count(self, obj):
        return obj.employees.count() 