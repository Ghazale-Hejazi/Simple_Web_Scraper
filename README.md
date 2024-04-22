# Web Scraper
This Python script serves as a simple web scraper using the BeautifulSoup library to extract information from a given URL. The script fetches the page content, extracts the page title, links in the body, and values of heading tags (h1 to h6), and then displays the information to the user. Additionally, the extracted data is saved to an output file.

## Dependencies
- `requests`: Used for making HTTP requests to the provided URL.
- `bs4` (Beautiful Soup): A library for pulling data out of HTML and XML files.


## Installation

1. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the script is located.

2. **Install Dependencies:**
   - Install the required dependencies using the following command:
        pip install -r requirements.txt
     

## Usage

1. **Run the Script:**
   - Execute the script by running the following command in your terminal or command prompt:
        python main.py

2. **Enter URL:**
   - You will be prompted to enter a URL. Ensure the URL starts with `http://`, `https://`, or `www.` for validation.

3. **View Information:**
   - The script will display the extracted information, including the page title, links in the body, and values of heading tags.

4. **Save to File:**
   - The information is saved to the 'output.txt' file in the script's directory.


## Example
1. **Input:**
   Enter the URL: https://example.com  

2. **Output:**
   Page Title: Example Domain
   
   Links in Body: ['https://www.iana.org/domains/example']
   
   Heading Values:
     h1: ['Example Domain']
     h2: Not Found
     h3: Not Found
     h4: Not Found
     h5: Not Found
     h6: Not Found
   
   Data has been saved to output.txt


## Notes
- The script currently saves the extracted information to 'output.txt' each time it is run, overwriting the existing file.

