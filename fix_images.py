import os
from PIL import Image

public_dir = "e:/ASIAN/my-app/public"

def convert_to_rgb():
    print("Converting images to RGB...")
    for filename in os.listdir(public_dir):
        if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
            filepath = os.path.join(public_dir, filename)
            try:
                with Image.open(filepath) as img:
                    if img.mode == 'CMYK' or img.mode == 'RGBA' or img.mode == 'P':
                        rgb_img = img.convert('RGB')
                        rgb_img.save(filepath, format='JPEG', quality=90)
                        print(f"Converted {filename} to RGB.")
                    else:
                        # Re-save just to ensure it's a valid web-friendly JPEG
                        rgb_img = img.convert('RGB')
                        rgb_img.save(filepath, format='JPEG', quality=90)
                        print(f"Re-saved {filename} as standard RGB JPEG.")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    convert_to_rgb()
