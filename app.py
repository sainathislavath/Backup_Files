from flask import Flask, render_template, request
import os
import shutil
from datetime import datetime

app = Flask(__name__)


def generate_unique_filename(dest_dir, filename):
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{base}_{timestamp}{ext}"
    return new_filename if os.path.exists(os.path.join(dest_dir, filename)) else filename


def backup_files(source_dir, destination_dir):
    if not os.path.isdir(source_dir):
        return f"Source directory '{source_dir}' does not exist."

    if not os.path.isdir(destination_dir):
        return f"Destination directory '{destination_dir}' does not exist."

    try:
        files = os.listdir(source_dir)
        if not files:
            return "Source directory is empty. Nothing to back up."

        for file in files:
            src = os.path.join(source_dir, file)
            if os.path.isfile(src):
                final_name = generate_unique_filename(destination_dir, file)
                shutil.copy2(src, os.path.join(destination_dir, final_name))

        return "Backup completed successfully."

    except Exception as e:
        return f"Backup failed: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        source = request.form['source'].strip()
        destination = request.form['destination'].strip()
        message = backup_files(source, destination)
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
