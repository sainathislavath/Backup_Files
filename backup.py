import os
import sys
import shutil
from datetime import datetime


def generate_unique_filename(dest_dir, filename):
    """
    Generate a unique filename by appending a timestamp if a file with the same name
    already exists in the destination directory.

    Args:
        dest_dir (str): Path to the destination directory
        filename (str): Original filename to check

    Returns:
        str: Original filename if unique, else a timestamped version to avoid overwriting
    """
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{base}_{timestamp}{ext}"

    # Check if file with the original name exists in destination
    if os.path.exists(os.path.join(dest_dir, filename)):
        return new_filename
    return filename


def backup_files(source_dir, destination_dir):
    """
    Copy files from source_dir to destination_dir. If a file with the same name exists
    in the destination, a unique name is generated using a timestamp.

    Args:
        source_dir (str): Directory containing files to back up
        destination_dir (str): Directory where files should be copied
    """
    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists
    if not os.path.isdir(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        return

    try:
        files = os.listdir(source_dir)
        if not files:
            print("Source directory is empty. Nothing to back up.")
            return

        # Loop through each item in the source directory
        for file in files:
            src_path = os.path.join(source_dir, file)

            # Only process regular files (skip subdirectories)
            if os.path.isfile(src_path):
                # Generate a unique name and copy the file
                unique_name = generate_unique_filename(destination_dir, file)
                dst_path = os.path.join(destination_dir, unique_name)
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {file} -> {unique_name}")

        print("Backup completed successfully.")

    except Exception as e:
        # Handle and display any unexpected errors
        print(f"Backup failed: {str(e)}")


def main():
    """
    Entry point of the script. Expects two command-line arguments:
    source directory and destination directory.
    """
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        return

    source = sys.argv[1]
    destination = sys.argv[2]
    backup_files(source, destination)

if __name__ == "__main__":
    main()
