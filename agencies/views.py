from django.shortcuts import render, redirect
from django.db.models import Q


from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import csv

fs = FileSystemStorage(location="temp")

from agencies.upload_providers import UploadProvidersMixin

# Create your views here.
from agencies.models import Agency, Destination, ServiceProvider


def home(request):
    agencies = ServiceProvider.objects.all()[:6]

    categories = ServiceProvider.objects.values_list(
        "service_category", flat=True
    ).distinct()

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        service_category = request.POST.get("service_category")

        print(search_text, service_category)

        if search_text and service_category:
            agencies = ServiceProvider.objects.filter(
                Q(name__icontains=search_text)
                | Q(town__icontains=search_text)
                | Q(tra_number__icontains=search_text)
                | Q(county__icontains=search_text)
                | Q(region__icontains=search_text)
            ).filter(service_category=service_category)
    context = {"agencies": agencies, "categories": list(categories)}

    return render(request, "home.html", context)


def agency_details(request, id):
    agency = ServiceProvider.objects.get(id=id)

    context = {"agency": agency}
    return render(request, "agency_details.html", context)


def upload_service_provider(request):
    
    if request.method == "POST":
        providers_file = request.FILES["providers_file"]

        source_file_content = providers_file.read()
        source_file_content = ContentFile(source_file_content)
        source_file_name = fs.save("temp_source_file.csv", source_file_content)
        temp_source_file = fs.path(source_file_name)
        with open(temp_source_file) as f:
            data = list(csv.DictReader(f))
            try:
                upload_mixin = UploadProvidersMixin(data=data)
                upload_mixin.run()
            except Exception as e:
                raise e
        return redirect("/")
    return render(request, "upload_providers.html")


def verify_provider(request):
    context = {}
    if request.method == "POST":
        search_text = request.POST.get("search_text")

        print(f"You searched for: {search_text}")

        if search_text:
            provider = ServiceProvider.objects.filter(
                Q(name__icontains=search_text)
                | Q(tra_number__icontains=search_text)
            )

            context = {
                "provider_found": True,
                "provider": provider
            }

            print(context)
    print("***********Outside If Statement***********")
    print(context)
            
    return render(request, "verify_provider.html", context)