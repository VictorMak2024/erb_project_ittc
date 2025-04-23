from django.shortcuts import render
from .models import SupportResource, Srdetail

def supportresources(request):
    # Retrieve all Srdetail objects
    srdetail_data = Srdetail.objects.all()

    # Dictionary mapping each Srdetail ID to its corresponding SupportResource objects
    combined_data = []
    for srdetail in srdetail_data:
        support_resources = SupportResource.objects.filter(sr_items_id=srdetail.id).order_by('-list_date')  # Retrieve all related SupportResource objects
        
        combined_data.append({
            'srdetail_id': srdetail.id,
            'items_no': srdetail.items_no,
            'itemsname': srdetail.itemsname,
            'supportresources': list(support_resources)  # Store multiple values as a list
        })

    print(f"Combined Data: {combined_data}")

    # Organizing data into a structured context for rendering
    context = {
        'combined_data': combined_data,
    }

    return render(request, 'supportresources/supportresources.html', context)
