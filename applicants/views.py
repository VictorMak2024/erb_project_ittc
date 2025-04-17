from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Applicant
from django.core.mail import send_mail
from datetime import datetime
from jobspost.models import Jobs
from django.core.mail import EmailMessage

# Create your views here.
def applicant(request):
    if request.method == 'POST':
        job_id = request.POST['job_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # work_experience = request.POST['work_experience']
        # qualification = request.POST['qualification']
        # expected_salary = request.POST['expected_salary']
        # date_available = request.POST['date_available']
        user_id = request.POST['user_id']
        job = get_object_or_404(Jobs, pk=job_id)
        title = job.title
        company = job.company
        apply_date = datetime.now()  # Set apply_date to the current date and time
        employer_email = request.POST['employer_email']

        # Handle file upload for CV
        if 'cv_file' in request.FILES:
            cv_file = request.FILES['cv_file']
        else:
            messages.error(request, 'Please upload your CV')
            return redirect('/jobspost/' + job_id)

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            has_applied = Applicant.objects.all().filter(job_id=job_id, email=email)
            if has_applied:
             messages.error(request, 'You have already applied for this job')
             return redirect('/jobspost/' + job_id)

        applicant = Applicant(
            title=title,
            job_id=job_id,
            # work_experience=work_experience,
            # qualification=qualification,
            # expected_salary=expected_salary,
            company=company,
            apply_date=apply_date,
            # date_available=date_available,
            name=name,
            email=email,
            phone=phone,
            user_id=user_id,
            cv_file=cv_file  # Save the uploaded CV file
        )

        applicant.save()

        # Send email with attachment
        email_message = EmailMessage(
            subject='Application for ' + title,
            body=(
            'There has been an application for ' + title + '.\n\n'
            'Details:\n'
            f'Name: {name}\n'
            f'Email: {email}\n'
            f'Phone: {phone}\n'
            # f'Work Experience: {work_experience}\n'
            # f'Qualification: {qualification}\n'
            # f'Expected Salary: {expected_salary}\n'
            # f'Date Available: {date_available}'
            ),
            from_email='pythonprogramtesting3@gmail.com',  # from email
            to=[employer_email],  # to email
        )
        cv_file.seek(0)  # Reset file pointer to the beginning
        email_message.attach(cv_file.name, cv_file.read(), cv_file.content_type)
        email_message.send(fail_silently=False)

        # Send success message
        messages.success(request, 'Your application has been submitted, a recruiter will get back to you soon')
        return redirect('/jobspost/' + job_id)


# Create your views here.
