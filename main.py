import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
import os


# EXAMPLE URL 'https://lightnovelpub.vip/novel/the-beginning-after-the-end-548/chapter-482'


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }

    try:
        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(urlEntry.get())
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            
        
            chapter_title = soup.find(class_='chapter-title')
            if chapter_title:
                chapterNumber = chapter_title.get_text().split()[1]
            else:
                print("Error: 'chapter-title' not found on the page.")
                return
            
            for letter in chapterNumber:
                if not letter.isdigit():
                    chapterNumber = chapterNumber.replace(letter, '')
            
            chapter_container = soup.find('div', id='chapter-container')
            if chapter_container:
                chapter_text = chapter_container.get_text(separator='\n').strip()
                
            
                
                html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter {chapterNumber}</title>
    <style>
        /* Basic reset */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        /* Body styles */
        body {{
            background-color: #121212; /* Dark background */
            color: #E0E0E0; /* Light text */
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}

        /* Chapter container */
        .chapter {{
            background-color: #1E1E1E; /* Slightly lighter background for contrast */
            border-radius: 10px;
            padding: 20px;
            max-width: 120vh; /* Increased width */
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.2); /* Subtle glow effect */
            margin: 0 auto; /* Center the container */
        }}

        /* Content paragraph */
        .content {{
            font-size: 1.2em;
            line-height: 1.6; /* Improved readability */
        }}

        /* Speaker names */
        .content .speaker {{
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            color: #BB86FC; /* Highlight color for speaker names */
            font-size: 60px;
        }}

        /* Dialogue text */
        .content .dialogue {{
            margin-left: 20px; /* Indent dialogue for clarity */
            margin-bottom: 10px; /* Space between dialogues */
        }}

        /* Adding link styles */
        a {{
            color: #03DAC5; /* Highlight color for links */
            text-decoration: none;
            transition: color 0.3s ease;
        }}

        a:hover {{
            color: #BB86FC; /* Link hover color */
        }}
        
        ::-webkit-scrollbar {{
            width: 10px; /* Width of the scrollbar */
        }}

        /* Scrollbar Handle */
        ::-webkit-scrollbar-thumb {{
            background: #bb86fc8e; /* Color of the scrollbar handle */
            border-radius: 5px; /* Border radius of the scrollbar handle */
        }}

        /* Scrollbar Track */
        ::-webkit-scrollbar-track {{
            background: #000000; /* Background color of the scrollbar track */
        }}

        /* Scrollbar Handle on hover */
        ::-webkit-scrollbar-thumb:hover {{
            background: #bb86fcab; /* Color of the scrollbar handle on hover */
        }}

        ::-webkit-scrollbar-thumb:active {{
            background: #bb86fc; /* Color of the scrollbar handle on hover */
        }}
    </style>
</head>
<body>
    <div class="chapter">
        <div class="content">
            <span class="speaker">
                Chapter {chapterNumber}
            </span>
            <p class="content">
                {chapter_text.replace('\n', '<br>')}
            </p>
        </div>
    </div>
</body>
</html>"""
                if not os.path.exists('Chapters'):
                    os.makedirs('Chapters')
                
                with open(os.path.join('Chapters', f'chapter-{chapterNumber}.html'), 'w', encoding='utf-8') as file:
                    file.write(html_template)
                    
                print("HTML file created successfully.")
                webbrowser.open(os.path.join('Chapters', f'chapter-{chapterNumber}.html'))
                os._exit(0)
            else:
                print("Error: 'chapter-container' not found on the page.")
            
            
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

app = tk.Tk()
app.title("Chapter Scraper")
app.geometry("400x150") 

extraInfoLabel = tk.Label(app, text="Link:")
extraInfoLabel.pack()

urlEntry = tk.Entry(app, width=55)
urlEntry.pack(pady=10)  

confirmButton = tk.Button(app, text="Get Chapter", command=main)
confirmButton.pack(padx=5, pady=5)

def openDC():
    webbrowser.open("https://discord.gg/k5HBFXqtCB")

infoLabel = tk.Label(app, text="Links must be from 'lightnovelpub.vip'\nIf you need help join the discord:\ndiscord.gg/k5HBFXqtCB")
infoLabel.pack()
infoLabel.bind("<Button-1>", lambda self: openDC())

if __name__ == '__main__':
    app.mainloop()



