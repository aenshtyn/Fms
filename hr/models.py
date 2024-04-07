from django.db import models
from FMS.mixins import AgeMixin, GenderMixin, PersonDetailsMixin
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Employee(PersonDetailsMixin, AgeMixin, GenderMixin, models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_status = models.CharField(max_length=20, choices=[
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contractor', 'Contractor'),
    ])
    employee_id = models.CharField(max_length=20)
    active_status = models.BooleanField(default=True)


    def __str__(self):
       return f'{self.name}'
    
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='pending')
    category = models.CharField(max_length=100, blank=True)
    estimated_duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.BooleanField(default=False)
    leave_type = models.CharField(max_length=50, choices=[
        ('vacation', 'Vacation'),
        ('sick_leave', 'Sick Leave'),
        ('maternity_paternity_leave', 'Maternity/Paternity Leave'),
        ('other', 'Other'),
    ])

    def __str__(self):
        return f'{self.employee} - {self.start_date} to {self.end_date}'
    
class Onboarding(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    orientation_completed = models.BooleanField(default=False)
    training_completed = models.BooleanField(default=False)
    documents_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Onboarding for {self.employee}'
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    clock_in = models.TimeField()
    clock_out = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late')
    ])

    def __str__(self):
        return f'{self.employee} - {self.date}'
    
class Recruitment(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    vacancy = models.PositiveIntegerField()
    opening_date = models.DateField()
    closing_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'Recruitment for {self.position}'
    
class Feedback(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'Feedback for {self.employee}'