import os
import sys
import shutil
from datetime import datetime


def generate_unique_filename(dest_dir, filename):
    """
    Generates a unique filename by appending a timestamp if it already exists.
    """
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{base}_{timestamp}{ext}"
    return new_filename if os.path.exists(os.path.join(dest_dir, filename)) else filename


def backup_files(source_dir, destination_dir):
    """
    Copies files from source_dir to destination_dir with unique naming if needed.
    """
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not os.path.isdir(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        return

    try:
        files = os.listdir(source_dir)
        if not files:
            print("Source directory is empty. Nothing to back up.")
            return

        for file in files:
            src_path = os.path.join(source_dir, file)
            if os.path.isfile(src_path):
                unique_name = generate_unique_filename(destination_dir, file)
                dst_path = os.path.join(destination_dir, unique_name)
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {file} -> {unique_name}")

        print("Backup completed successfully.")

    except Exception as e:
        print(f"Backup failed: {str(e)}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        return

    source = sys.argv[1]
    destination = sys.argv[2]
    backup_files(source, destination)


if __name__ == "__main__":
    main()
