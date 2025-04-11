from flask import Flask, render_template, request
import os
import shutil
from datetime import datetime

# Initialize the Flask web application
app = Flask(__name__)


def generate_unique_filename(dest_dir, filename):
    """
    Generate a unique filename by appending a timestamp if a file
    with the same name already exists in the destination directory.

    Args:
        dest_dir (str): Path to the destination directory
        filename (str): Name of the file to check

    Returns:
        str: A unique filename with timestamp if needed
    """
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # If file already exists, generate a new name with timestamp
    new_filename = f"{base}_{timestamp}{ext}"
    return new_filename if os.path.exists(os.path.join(dest_dir, filename)) else filename


def backup_files(source_dir, destination_dir):
    """
    Copy all files from the source directory to the destination directory.
    If a file with the same name exists, it adds a timestamp to avoid overwriting.

    Args:
        source_dir (str): Path to the source directory
        destination_dir (str): Path to the destination directory

    Returns:
        str: Status message indicating the result of the backup operation
    """
    # Check if source directory exists
    if not os.path.isdir(source_dir):
        return f"Source directory '{source_dir}' does not exist."

    # Check if destination directory exists
    if not os.path.isdir(destination_dir):
        return f"Destination directory '{destination_dir}' does not exist."

    try:
        files = os.listdir(source_dir)
        if not files:
            return "Source directory is empty. Nothing to back up."

        # Iterate through each file in the source directory
        for file in files:
            src = os.path.join(source_dir, file)
            # Only process regular files (skip subdirectories)
            if os.path.isfile(src):
                # Generate unique filename and copy to destination
                final_name = generate_unique_filename(destination_dir, file)
                shutil.copy2(src, os.path.join(destination_dir, final_name))

        return "Backup completed successfully."

    except Exception as e:
        # Catch and return any unexpected errors
        return f"Backup failed: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle GET and POST requests for the home page.
    On POST, it performs the backup based on form input and shows a message.

    Returns:
        Rendered HTML page with optional status message.
    """
    message = None
    if request.method == 'POST':
        # Get user input from the form
        source = request.form['source'].strip()
        destination = request.form['destination'].strip()
        # Perform the backup and get the result message
        message = backup_files(source, destination)

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
