import os
import shutil

# Define the path to the Downloads directory
downloads_dir = os.path.expanduser('~/Downloads')

# Define target directories for various file types
target_dirs = {
    'Documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx',"odt","ods"],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'heic', 'tiff'],
    'Videos': ['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv'],
    'Music': ['mp3', 'wav', 'aac', 'flac', 'ogg'],
    'Archives': ['zip', 'rar', 'tar', 'gz', 'bz2', '7z'],
    'Software': ['dmg', 'pkg', 'exe', 'iso'],
    'Others': []
}

# Create target directories if they don't exist
for dir_name in target_dirs.keys():
    dir_path = os.path.join(downloads_dir, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Function to get the file extension
def get_extension(filename):
    return filename.split('.')[-1].lower()

# Move files to their respective directories
for filename in os.listdir(downloads_dir):
    file_path = os.path.join(downloads_dir, filename)
    
    if os.path.isfile(file_path):
        file_extension = get_extension(filename)
        moved = False
        
        for dir_name, extensions in target_dirs.items():
            if file_extension in extensions:
                target_path = os.path.join(downloads_dir, dir_name, filename)
                shutil.move(file_path, target_path)
                moved = True
                break
        
        # Move to 'Others' directory if file extension doesn't match any category
        if not moved:
            target_path = os.path.join(downloads_dir, 'Others', filename)
            shutil.move(file_path, target_path)

print("Downloads directory organized successfully.")