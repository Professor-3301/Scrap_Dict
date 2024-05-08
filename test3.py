import zipfile
import os

def zip_folder(folder_path, zip_path):
    """
    Create a zip file from a folder.

    Args:
    - folder_path: The path to the folder to be zipped.
    - zip_path: The path to save the created zip file.

    Returns:
    - None
    """
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate the relative path inside the zip file
                relative_path = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, relative_path)

# Example usage:
folder_to_zip = './images'
output_zip_file = './images.zip'
zip_folder(folder_to_zip, output_zip_file)
