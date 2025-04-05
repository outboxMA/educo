from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Instructor
from .forms import InstructorForm

# List all instructors
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors/instructor_list.html', {'instructors': instructors})

# View instructor details
def instructor_detail(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    return render(request, 'instructors/instructor_detail.html', {'instructor': instructor})

# Add a new instructor
def instructor_add(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('instructors:instructor_list')  # Redirect to the list view
    else:
        form = InstructorForm()
    return render(request, 'instructors/instructor_form.html', {'form': form})

# Edit an existing instructor
def instructor_edit(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructors:instructor_detail', pk=instructor.pk)  # Redirect to the detail view
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'instructors/instructor_form.html', {'form': form})

# Delete an instructor
def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.delete()
        return redirect('instructors:instructor_list')  # Redirect to the list view
    return render(request, 'instructors/instructor_confirm_delete.html', {'instructor': instructor})
