from flask import Flask, render_template, request  # Use direct import for render_template
from genChapters import yes
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generator')
def generator():
    return render_template('test.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.route('/run_script', methods=['GET', 'POST'])
def run_script():
    if request.method == 'POST':
        
        # Handle the POST request (execute script, etc.)
        result = yes()  # Call a function to execute genfiles.py
        return result  # Return some response to the client if needed
    else:
        # Handle the GET request (if needed)
        return "This route only accepts POST requests."

@app.route('/chapters/<int:chapter_number>')
def show_chapter(chapter_number):
    # Path to the subfolder containing HTML files
    subfolder_path = os.path.join(app.root_path, 'templates', 'chapters')

    # Get a list of all HTML files in the subfolder
    html_files = [file for file in os.listdir(subfolder_path) if file.endswith('.html')]

    html_files.sort(key=lambda x: int(x.split('-')[1].split('.')[0]))   
     
    # Check if the requested chapter number is within the range of available chapters
    if chapter_number < 1 or chapter_number > len(html_files):
        return "Chapter not found."

    # Render the HTML file for the requested chapter
    chapter_file = html_files[chapter_number - 1]  # Adjusting for 0-based index
    with open(os.path.join(subfolder_path, chapter_file), 'r', encoding='utf-8') as f:
        rendered_html = f.read()

    return rendered_html


@app.route('/chapters')
def index():
    # Path to the subfolder containing HTML files
    subfolder_path = os.path.join(app.root_path, 'templates', 'chapters')

    # Get a list of all HTML files in the subfolder
    html_files = [file for file in os.listdir(subfolder_path) if file.endswith('.html')]

    # Extract chapter numbers from file names
    chapter_numbers = [int(file.split('-')[1].split('.')[0]) for file in html_files]

    # Sort chapter numbers
    chapter_numbers.sort()

    # Render the HTML template with links to each chapter
    return render_template('chapters.html', chapter_numbers=chapter_numbers)
    
    
if __name__ == '__main__':
    app.run(debug=True)
