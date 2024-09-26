from agencies.models import ServiceProvider


class UploadProvidersMixin(object):
    def __init__(self, data):
        self.data = data

    def run(self):
        self.__upload_new_stock()

    def __upload_new_stock(self):
        items = self.data

        items_list = []

        for item in items:
            provider = {
                "tra_number": item["File Number"],
                "name": item["Company Name"],
                "county": item["County"],
                "region": item["Regional Office"],
                "service_category": item["Service Category Name"],
                "email": item["Email"],
                "phone_number": str(item["Phone"]),
                "town": item["Regional Office"],
            }
            items_list.append(ServiceProvider(**provider))

        # File Number,Company Name,County,Regional Office,Service Category Name,Email,Phone
        ServiceProvider.objects.bulk_create(items_list)
        print("*******Service Providers Created Successfully!!************")
