from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Course, Session
from .forms import CourseForm, SessionForm
from instructors.models import Instructor


# View to display all courses
def course_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'courses/course_list.html', {
        'courses': Course.objects.all(),
    })

# View to display a single course
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Retrieve the course by ID or return a 404 if not found
    return render(request, 'courses/course_detail.html', {'course': course})

# View to add a new course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:course_list')  # Redirect to course list
    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form, 'instructors': Instructor.objects.all()})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    session_form = SessionForm(request.POST or None)

    if request.method == 'POST':
        if 'save_course' in request.POST:  # If the course form is submitted
            course_form = CourseForm(request.POST, instance=course)
            if course_form.is_valid():
                course_form.save()
                return redirect('courses:edit_course', course_id=course.id)  # Redirect to itself after saving
        elif 'add_session' in request.POST:  # If the session form is submitted
            session_form = SessionForm(request.POST)
            if session_form.is_valid():
                new_session = session_form.save(commit=False)
                new_session.course = course  # Associate session with the current course
                new_session.save()
                return redirect('courses:edit_course', course_id=course.id)  # Stay on the same page to view changes

    else:
        course_form = CourseForm(instance=course)  # For GET, load the course data into the form

    # Get all the sessions for this course
    sessions = course.sessions.all()

    return render(request, 'courses/edit_course.html', {
        'course': course,
        'course_form': course_form,
        'session_form': session_form,
        'sessions': sessions,
    })

# View to delete a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Retrieve the course by ID
    if request.method == 'POST':
        course.delete()  # Delete the course from the database
        return redirect('courses:course_list')  # Redirect to the list of courses
    return render(request, 'courses/delete_course.html', {'course': course})

# View to toggle course status (active/inactive)
def toggle_course_status(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.is_active = not course.is_active  # Toggle the active status
    course.save()  # Save the changes
    return JsonResponse({'status': 'success', 'is_active': course.is_active})  # Return success response


def session_list(request: HttpRequest):
    sessions = Session.objects.all()
    return render(request, 'sessions/session_list.html', {
        'sessions': sessions
    })

# View to edit a session
def edit_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('courses:edit_course', course_id=session.course.id)  # Redirect to the course edit page
    else:
        form = SessionForm(instance=session)

    return render(request, 'courses/edit_session.html', {'form': form, 'session': session})

# View to delete a session
def delete_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        session.delete()
        return redirect('courses:edit_course', course_id=session.course.id)  # Redirect to the course edit page after deletion
    return render(request, 'courses/confirm_delete.html', {'session': session})