  Smart Screenshot Organizer

The Story Behind It
Have you ever opened your screenshots folder and felt lost? Screenshots for coding, studying, shopping, or social chats  all jumbled together. I found myself wasting more time searching than actually using them.

That’s when I thought: there has to be a smarter way.  

And so, **Smart Screenshot Organizer** was born — a simple tool that **automatically sorts your screenshots** into categories like **Coding, Study, Shopping, Social, and Others**, making your life organized and stress-free.

How It Works
1. Upload a screenshot through a clean Streamlit interface.  
2. The system uses OCR (Tesseract) to read text inside the screenshot.  
3. Based on detected keywords, the screenshot is moved to the correct category folder.  
4. Instantly view a gallery of your screenshots or filter them by category.  

It’s like having a personal assistant for your screenshots!  

 Tech Behind the Magic
-Python 3.x – The backbone of the project  
- Streamlit– Creates the interactive web interface  
- PIL (Pillow) – Handles image opening and processing  
- Pytesseract – Detects and extracts text from screenshots  
- OS Module – Organizes files into categories automatically  


smart-screenshot-organizer/
│
├─ app.py             # Streamlit interface
├─ classifier.py      # Screenshot categorization logic
├─ screenshots/       # Temporary uploaded screenshots
├─ categorized/       # Organized screenshots
└─ requirements.txt   # Python dependencies

I built this project to save time and stay organized, and I hope it helps anyone who deals with hundreds of screenshots every day.
