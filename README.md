# Learning Python Scripts

This repository is a collection of small Python scripts and projects that I've created while learning Python.

## Scripts

- [Email Sender](email_sender.py): This Python script uses the ***Simple Mail Transfer Protocol*** (SMTP) to send an email from one email account to another. The email's content, including the sender's name, recipient email, subject, and message, are defined in the script. It sends the email using the Gmail SMTP server and requires the login credentials for the email account from which the email is being sent. Once the email is sent, the script will print "All good" to the console. You can modify the email's content by changing the email object's attributes in the script.

- [Guess the number](guess_the_number_game.py): This Python script generates a random number within a specified range and prompts the user to guess it. The range is determined by two integer values passed as command-line arguments. The script validates the user's input to ensure that it is within the specified range and that it is a valid integer. If the user guesses correctly, the script terminates and prints a congratulatory message. If not, the script continues to prompt the user for a guess until a correct answer is given.

To use the script, run it from the command line and pass two integer values as arguments, like this: ***python guess_number.py 1 100*** (this will generate a random number between 1 and 100). You can modify the range of the numbers by changing the values passed as arguments to the script.


- [Pwned Password Checker](password_checker.py): Allows you to check whether a password has been compromised by querying the ***Have I Been Pwned*** API. It takes one or more passwords as command-line arguments and returns a message indicating whether each password has been found in any known data breaches. If a password has been compromised, the script recommends that you change it immediately.

- [PDF Combiner](pdf_combiner.py): This Python script uses the PyPDF2 library to merge multiple PDF files into a single PDF file named 'super.pdf'. The script accepts a list of PDF files as command-line arguments and defines a function called 'pdf_combiner' that takes in the list of PDF files and merges them using the PyPDF2.PdfFileMerger() class. The merged PDF file is written to a new file named 'super.pdf'. To use the script, simply run it in the command line and provide a list of PDF files to be merged as arguments. Example usage: python pdf_combiner.py file1.pdf file2.pdf file3.pdf

- [PDF Watermark](pdf_watermark.py): A Python script that adds a watermark to every page of a PDF file. It requires two input PDF files: 'input.pdf' and 'watermark.pdf'. The watermarked PDF is saved as 'watermarked_output.pdf'. To use, place the input and watermark PDF files in the same directory as the script and run with 'python watermark.py'.

- [Scheduled email sender](scheduled_email_sender.py): This Python script schedules an email to be sent at a specific time. The script uses ***smtplib*** to send the email and ***time*** to schedule it. Customize the ***send_email*** function with your email and recipient information, along with a send_time variable in the format ***YYYY-MM-DD HH:MM:SS***. To use, run python ***email_scheduler.py*** in your terminal. 

- [Scheduled SMS](scheduled_sms_twilio.py): This Python script sends an SMS at a scheduled time using the ***Twilio API***. Customize the ***send_sms*** function with your ***Twilio account information*** and SMS details, along with a ***send_time*** variable in the format YYYY-MM-DD HH:MM:SS. To use, run python ***scheduled_sms.py*** in your terminal. 

- [Hacker News Top Stories Scraper](scrape_hackernews.py): This Python script utilizes the ***requests*** and ***BeautifulSoup*** libraries to scrape the first two pages of news articles from ***YCombinator's*** Hacker News website (https://news.ycombinator.com/news). The script retrieves article links, titles, and their respective vote counts. By filtering and sorting these articles based on a minimum threshold of 100 votes, the script outputs a curated list of popular articles in a more readable format. To accomplish this, the create_custom_hn function processes the links and subtext of each article, while the ***sort_stories_by_votes*** function organizes the list in descending order based on vote counts. Simply run the script to obtain a refined list of top Hacker News articles, making it easier to stay updated on the most relevant news and discussions in the tech community.
