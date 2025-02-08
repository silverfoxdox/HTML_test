from bs4 import BeautifulSoup


def html_to_text():
    # Open and read the HTML file with r at the beginning indicates a raw string
    with open(r'C:\Users\t1mpa\OneDrive\Documents\Text\sample-html-files-sample2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    print(html_content)
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text from the parsed HTML
    text_content = soup.get_text()
    print(text_content)

    # Write the text content to a text file
    with open(r'C:\Users\t1mpa\OneDrive\Documents\Text\htotext.txt', 'w', encoding='utf-8') as file:
        file.write(text_content)


html_to_text()

# Example usage
# html_file = 'example.html'
# text_file = 'output.txt'
# html_to_text(html_file, text_file)
