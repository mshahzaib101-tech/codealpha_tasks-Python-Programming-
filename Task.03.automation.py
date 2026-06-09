import os
import shutil

def organize_images(source_folder, destination_folder):
    # Check agar source folder exist karta hai
    if not os.path.exists(source_folder):
        print(f"Error: Folder '{source_folder}' nahi mila.")
        return

    # Agar destination folder nahi hai, to create karein
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files_moved = 0
    # Source folder mein files check karein
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename}")
            files_moved += 1

    print(f"\nTask Complete! Total {files_moved} images moved.")

# Usage
# source = "C:/Users/Downloads" 
# destination = "C:/Users/Pictures/MyImages"
# organize_images(source, destination)

