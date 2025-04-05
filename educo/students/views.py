# students/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# View details of a specific student
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

# Create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')  # Redirect to the student list after creation
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

# Edit an existing student
def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')  # Redirect to the student list after editing
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form})

# Delete a student
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('students:student_list')  # Redirect to the student list after deletion

    return render(request, 'students/student_confirm_delete.html', {'student': student})
