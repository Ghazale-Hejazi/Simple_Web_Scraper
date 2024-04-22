import re
import requests
from bs4 import BeautifulSoup

OUTPUT_FILE = 'output.txt'

def main():
    while True:
        # Get user input URL
        user_url = input("Enter the URL: ").strip()
        
        # Validate the input URL
        if validate_url_input(user_url):
            # Attempt to fetch URL information
            success, page_content = get_url_info(user_url)

            if success:
                # Extract desired information from the page content
                page_info = extract_page_info(page_content)

                # Display information to the user
                print_info(page_info)

                # Save information to a file
                save_info_to_file(page_info)
                print(f"\nData has been saved to {OUTPUT_FILE}")
                break
            else:
                print("Error fetching the website. Please try again.")
        else:
            print("Invalid URL. Please make sure it starts with http://, https://, or www.")


def validate_url_input(url):
    # Define a regex pattern for valid URLs
    url_pattern = re.compile(r'^(http://|https://|www\.)\S+')
    
    # Check if the input matches the pattern
    return bool(url_pattern.match(url))


def get_url_info(url):
    try:
        # Make a request to the URL
        response = requests.get(url)

        # Raise an exception for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Return a tuple indicating success and page content
        return True, response.text
    
    except requests.RequestException as e:
        # Print an error message and return a tuple indicating failure
        print(f"Error during GET request: {e}")
        return False, None


def extract_page_info(page_content):
    # Use BeautifulSoup to parse HTML content
    content = BeautifulSoup(page_content, 'html.parser')

    # Extract page title
    page_title = content.title.string.strip() if content.title else 'Not Found'

    # Extract links in the body of the page
    body_links = [a['href'] for a in content.find_all('a', href=True) if a['href']] if content.find_all('a', href=True) else 'Not Found'

    # Extract values of tags h1 to h6 (without attribute)
    heading_values = {}
    for i in range(1, 7):
        headings = content.find_all(f'h{i}')
        heading_values[f'h{i}'] = [re.sub('\n+', ';', heading.text.strip()) for heading in headings] if headings else 'Not Found'

    # Create a dictionary to store the extracted information
    page_info = {
        'Page Title': page_title,
        'Links in Body': body_links,
        'Heading Values': heading_values,
    }

    return page_info


def print_info(page_info):
    # Display information from the dictionary
    for key, value in page_info.items():
        if key == 'Heading Values':
            print(f"\n{key}:")
            for heading, values in value.items():
                print(f"  {heading}: {values}")
        else:
            print(f"\n{key}: {value}")


def save_info_to_file(page_info):
    # Save information from the dictionary to a file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for key, value in page_info.items():
            if key == 'Heading Values':
                f.write(f"\n{key}:\n")
                for heading, values in value.items():
                    f.write(f"  {heading}: {values}\n")
            else:
                f.write(f"\n{key}: {value}\n")


if __name__ == "__main__":
    main()
