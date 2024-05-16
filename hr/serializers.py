from rest_framework import serializers
from .models import Employee, Task, Leave, Onboarding, Attendance, Recruitment, Feedback
import datetime


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ReadOnlyField(source='assigned_to.name')
    class Meta:
        model = Task
        fields = 'assigned_to', 'title', 'description', 'category', 'status', 'priority'

class LeaveSerializer(serializers.ModelSerializer):
    employee = serializers.ReadOnlyField(source='employee.name')
    class Meta:
        model = Leave
        fields = 'employee', 'leave_duration', 'start_date', 'end_date'

class OnboardingSerializer(serializers.ModelSerializer):
   
    employee = serializers.ReadOnlyField(source='employee.name')
    class Meta:
        model = Onboarding
        fields = 'id','employee', 'orientation_completed', 'training_completed', 'documents_completed'

class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.ReadOnlyField(source='employee.name')
    class Meta:
        model = Attendance
        fields = '__all__'

class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    employee = serializers.ReadOnlyField(source='employee.name')
    class Meta:
        model = Feedback
        fields = '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    pending_tasks = serializers.SerializerMethodField()
    completed_tasks = serializers.SerializerMethodField()
    department_name = serializers.SerializerMethodField()
    position_title = serializers.SerializerMethodField()
    time_worked_for_company = serializers.SerializerMethodField()
    # pending_leave_days = serializers.SerializerMethodField()
    # orientation_status = serializers.SerializerMethodField()
    # training_status = serializers.SerializerMethodField()
    # late_days = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = 'name', 'age', 'phone', 'gender', 'salary' ,'hire_date' , 'pending_tasks' , 'completed_tasks', 'department_name', 'position_title', 'time_worked_for_company'
    def get_pending_tasks(self, obj):
        pending_tasks = Task.objects.filter(assigned_to=obj, status='pending')
        serializer = TaskSerializer(pending_tasks, many=True)
        return serializer.data

    def get_completed_tasks(self, obj):
        completed_tasks = Task.objects.filter(assigned_to=obj, status='completed')
        serializer = TaskSerializer(completed_tasks, many=True)
        return serializer.data

    def get_department_name(self, obj):
        return obj.department.name if obj.department else None

    def get_position_title(self, obj):
        return obj.position.title if obj.position else None
    
    def get_time_worked_for_company(self, obj):
        """
        Calculate the total time worked for the company by the employee.

        Returns:
            str: The total time worked for the company formatted as years and months.
        """
        # Get the current date
        current_date = datetime.datetime.now().date()

        # Calculate the duration since the employee's hire date
        time_worked = current_date - obj.hire_date

        # Extract the number of years and months from the duration
        years = time_worked.days // 365
        months = (time_worked.days % 365) // 30  # Assuming 30 days per month

        # Format the total time worked as years and months
        if years == 0:
            return f"{months} {'month' if months == 1 else 'months'}"
        elif months == 0:
            return f"{years} {'year' if years == 1 else 'years'}"
        else:
            return f"{years} {'year' if years == 1 else 'years'}, {months} {'month' if months == 1 else 'months'}"
        
        

    # def get_pending_leave_days(self, obj):
    #     pending_leave_days = Leave.objects.filter(employee=obj, status='pending').aggregate(total_days=Sum('days'))
    #     return pending_leave_days['total_days'] if pending_leave_days['total_days'] else 0

    # def get_orientation_status(self, obj):
        
    #     # orientation_status = 
    #     # Logic to determine orientation status
    #     return "Completed" if obj.orientation else "Pending"

    # def get_training_status(self, obj):
    #     # Logic to determine training status
    #     return "Completed" if obj.training_completed else "Pending"

    # def get_late_days(self, obj):
    #     # Logic to calculate late days
    #     return obj.late_days()