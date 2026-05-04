# import os
# import read_write_model as read_model

# basedir = './data/razorback'
# images_bin = os.path.join(basedir, 'sparse/0/images.bin')

# # 1. Get the list of images COLMAP actually registered
# imdata = read_model.read_images_binary(images_bin)
# registered_names = [imdata[k].name for k in imdata]

# # 2. Check the image folders and remove the unregistered frame
# for folder in ['images', 'images_4', 'images_8']: 
#     img_dir = os.path.join(basedir, folder)
#     if not os.path.exists(img_dir): 
#         continue
    
#     for img_file in os.listdir(img_dir):
#         if img_file.lower().endswith(('png', 'jpg', 'jpeg')):
#             if img_file not in registered_names:
#                 filepath = os.path.join(img_dir, img_file)
#                 os.remove(filepath)
#                 print(f"Removed unregistered image: {filepath}")

# print(f"Cleanup complete! Total registered images retained: {len(registered_names)}")

import os
from PIL import Image

base_dir = './data/razorback'
img_dir = os.path.join(base_dir, 'images')
out_dir = os.path.join(base_dir, 'images_4')

os.makedirs(out_dir, exist_ok=True)

for img_name in sorted(os.listdir(img_dir)):
    # Check for image extensions
    if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')): 
        continue
    
    img_path = os.path.join(img_dir, img_name)
    with Image.open(img_path) as img:
        # Downsample by a factor of 4
        new_width = img.width // 4
        new_height = img.height // 4
        resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        resized.save(os.path.join(out_dir, img_name))
        print(f"Resized {img_name} to {new_width}x{new_height}")

print("Done! The images_4 folder is ready.")