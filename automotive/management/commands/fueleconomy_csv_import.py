import os
import sys
import csv
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand

from automotive.models import Brand, Model
from automotive.util import download_file, extract_zipfile


VEHICLES_CSV_URL = getattr(settings, "FUELECONOMY_VEHICLES_CSV_URL", 
                           "http://www.fueleconomy.gov/feg/epadata/vehicles.csv.zip")


class Command(BaseCommand):
    def handle(self, *args, **options):
        sys.stdout.write("Downloading {}...\n".format(VEHICLES_CSV_URL))
        download = download_file(VEHICLES_CSV_URL)
        sys.stdout.write("\nDone.\n\n")
        print("Extracting .zip file...")
        data_dir = extract_zipfile(download)
        os.unlink(download.name)
        csv_file = os.path.join(data_dir, "vehicles.csv")
        reader = csv.DictReader(open(csv_file, 'r'))
        print("Importing...")
        for row in reader:
            brand, created = Brand.objects.get_or_create(name=row["make"])
            if created:
                print(" * {} created.".format(brand.name))
            model, created = Model.objects.get_or_create(name=row["model"], brand=brand, year=row["year"])
            if created:
                print(" * {} created.".format(model.name))
        shutil.rmtree(data_dir)
        print("Done.")
