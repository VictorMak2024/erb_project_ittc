from django.shortcuts import render, get_object_or_404
from jobspost.models import Jobs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from jobspost.choices import Salary_choices, Job_type_choices 

# Create your views here.
def jobspost(request):

    # jobsposts=Jobs.objects.all()
    
    # for job in jobsposts:
        
    #     context = {'jobs': jobsposts}


    # print(jobsposts)
    # print(context)
    # print(jobsposts[0].post_date)

  #  return render(request, 'jobspost/jobs.html', context)
    #return render(request, 'jobspost/jobsdetail.html', context)
  # listings = Listing.objects.all()
   # for listing in listings:
   #     print(listing)
    #print(list(listings)) 
   # listings= listing.objects.filter 
   # listings = Listing.objects.order_by('-list_date').filter(is_published=True)
   # listings = Listing.objects.filter(Q(district='tst') | ~Q(district='mk'))
  #  listings = Listing.objects.filter(district=F('address'))

    
    Jobss=Jobs.objects.order_by('-post_date')
    paginator=Paginator(Jobss,9) 
    page = request.GET.get('page')
    paged_Jobs = paginator.get_page(page)
    #print(paged_Jobs)
    values = request.GET.copy()  
    context = {
        'salary_choices': Salary_choices,
        'job_type_choices': Job_type_choices,
       # 'listings': queryset_list,
        'jobs': paged_Jobs,         
        'values': values
    }
    return render(request, 'jobspost/jobslisting.html', context)

# def jobspost_detail(request, **kwargs):
#     print(kwargs)
#     job_id = kwargs.get('job_id')
#     print(job_id)
#     job = get_object_or_404(Jobs, pk=job_id)
#     context = {'Jobs': job}
#     return render(request, 'jobspost/jobsdetail.html', context)
def jobspost_detail(request, job_id):
    #  print("jobspost_detail")
    #  print(request.user)  # Prints the user object
    #  print(request.user.is_authenticated)
     job = get_object_or_404(Jobs, pk=job_id)
     context = {'job': job}
     return render(request, 'jobspost/jobsdetail.html', context)


def search(request):
    queryset_list = Jobs.objects.order_by('-post_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(requirement__icontains=keywords) | Q(responsibilities__icontains=keywords)
                |Q(title__icontains=keywords)|Q(company__icontains=keywords)
            )
    # if 'title' in request.GET:
    #     title = request.GET['title']
    #     if title:
    #         queryset_list = queryset_list.filter(title__icontains=title)
    if 'jobtype' in request.GET:
        jobtype = request.GET['jobtype']
        if jobtype:
            queryset_list = queryset_list.filter(job_type__iexact=jobtype)
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(location__icontains=location)
    if 'salary' in request.GET:
        salary = request.GET['salary']
        if salary:
            queryset_list = queryset_list.filter(salary__lte=salary)
    # if 'company' in request.GET:
    #     company = request.GET['company']
    #     if company:
    #         queryset_list = queryset_list.filter(company__iexact=company)
    paginator=Paginator(queryset_list,9) 
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)  
    values = request.GET.copy()  
    if 'page' in values:
        del values["page"]    
    context = {
        'salary_choices': Salary_choices,
        'job_type_choices': Job_type_choices,
       # 'listings': queryset_list,
        'jobs': paged_jobs,         
        'values': values
    }
    return render(request, 'jobspost/jobslisting.html', context)