import fitz
import io
from PIL import Image
import os

pdf_path = "e:/ASIAN/my-app/Asian Engineering & Surveying-1.pdf"
doc = fitz.open(pdf_path)

# Extract text from page 2 (index 1) for About Us
print("--- Page 2 Text (About Us) ---")
print(doc[1].get_text())

# Extract text from page 3 and 4 (index 2 and 3) for Services
print("--- Page 3 Text (Services) ---")
print(doc[2].get_text())

print("--- Page 4 Text (Services) ---")
print(doc[3].get_text())

# Try to extract the logo from page 1 (index 0)
page1 = doc[0]
images = page1.get_images()
print("Images on Page 1:", images)

if len(images) > 0:
    for i, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image.save(f"e:/ASIAN/my-app/public/extracted_logo_{i}.{image_ext}")
        print(f"Saved extracted_logo_{i}.{image_ext}")
else:
    print("No images found on page 1")
    
# Extract images from Services pages (page 3 and 4)
for p_idx in [2, 3]:
    page = doc[p_idx]
    images = page.get_images()
    for i, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image.save(f"e:/ASIAN/my-app/public/services_img_p{p_idx}_{i}.{image_ext}")
        print(f"Saved services_img_p{p_idx}_{i}.{image_ext}")

doc.close()
