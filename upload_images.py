import os
import cloudinary
import cloudinary.uploader
import django
import sys

# SETUP DJANGO
sys.path.append("C:/Users/vendr/OneDrive/Documents/web Development/welding website/backend> ")  # 👉 change this
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backendServer.settings")
django.setup()

from api.models import WorkImage  # 👉 change this

# SETUP CLOUDINARY
cloudinary.config(
  cloud_name = "dfnbvtqae",    # 👉 change this
  api_key = "982118876977128",          # 👉 change this
  api_secret = "iBYUBiFqyG0wOslWdoEB1qDrvc4"     # 👉 change this
)

# FOLDER CONTAINING YOUR SUBFOLDERS
BASE_FOLDER = "C:/Users/vendr/Documents/designs"

# LOOP THROUGH CATEGORIES
for category in os.listdir(BASE_FOLDER):
    category_path = os.path.join(BASE_FOLDER, category)
    if os.path.isdir(category_path):
        for filename in os.listdir(category_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(category_path, filename)
                print(f"Uploading {filepath}...")

                result = cloudinary.uploader.upload(
                    filepath,
                    folder=f"raju_works/{category}"
                )

                # Save to Django
                WorkImage.objects.create(
                    category=category,
                    image_url=result['secure_url']
                )

                print(f"✅ Uploaded: {filename} -> {result['secure_url']}")
