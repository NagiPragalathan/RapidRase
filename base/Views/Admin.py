from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from base.forms.Detailsform import DetailsForm, ImageForm
from base.models import Details, DetailsImage

# View to list all Details
def details_list(request):
    details = Details.objects.all()
    return render(request, 'admin/details_list.html', {'details': details})

# View to add or edit Details
def details_create_edit(request, uuid=None):
    if uuid:
        detail = get_object_or_404(Details, uuid=uuid)
        if request.method == 'POST':
            form = DetailsForm(request.POST, instance=detail)
            if form.is_valid():
                form.save()
                return redirect('details_list')
        else:
            form = DetailsForm(instance=detail)
    else:
        if request.method == 'POST':
            form = DetailsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('details_list')
        else:
            form = DetailsForm()

    return render(request, 'admin/details_form.html', {'form': form})

# View to delete Details
def details_delete(request, uuid):
    detail = get_object_or_404(Details, uuid=uuid)
    detail.delete()
    return redirect('details_list')

# View to upload an image for Details
def image_upload(request, details_uuid):
    detail = get_object_or_404(Details, uuid=details_uuid)
    if request.method == 'POST':
        # Process each file in the list of uploaded files
        images = request.FILES.getlist('images')
        for image_file in images:
            DetailsImage.objects.create(details=detail, image=image_file)
        return redirect('details_list')
    else:
        form = ImageForm()  # Keep the form for potential other fields or validations
    return render(request, 'admin/image_form.html', {'form': form, 'detail': detail})


def detail_view(request, uuid):
    detail = get_object_or_404(Details, uuid=uuid)
    images = detail.images.all()  # Fetches all related images using the 'related_name'
    return render(request, 'admin/detail_view.html', {'detail': detail, 'images': images})

def image_delete(request, image_id):
    image = get_object_or_404(DetailsImage, id=image_id)
    detail_uuid = image.details.uuid
    image.delete()
    return redirect('detail_view', uuid=detail_uuid)

