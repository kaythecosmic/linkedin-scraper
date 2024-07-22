# LinkedIn Profile Scraper

## Description
Extracts the user's name and title from their LinkedIn profile page.

## Dependencies

- `requests`  for making HTTP requests.
- `beautifulsoup4` for parsing HTML and XML documents.
- `payload` that should includes `cookies` and `headers` for making requests.

## Setup

1. Install the required libraries ou can install them using pip:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure that the `payload.py` file is correctly set up with the necessary `cookies` and `headers`. Follow the steps below for the setup.
   1. Go to your own linked in **profile page** at `https://www.linkedin.com/in/<your-username>`
   2. Enable the developer tools using `Ctrl+Shift+I` and open the `Networks` Tab.
   3. Refresh the webpage and you should see the top request being made with the name `<your-username>/`.
   4. Right Click on that  and  `"Copy" > "Copy as cURL (bash)"`
   5. Paste the contents of the clipboard in the text area here [Curl Converter](https://curlconverter.com/)
   6. You should see the python code for this request in the text are below. Copy the `cookies` and the `headers` objects and paste them into your `payload` file.

## Usage

1. Input Your Target LinkedIn Profile Link by modify the `target` variable with the LinkedIn profile URL you want to scrape.

   ```python
   target = "https://www.linkedin.com/in/lexfridman/"
   ```

## Example

```python
# Example LinkedIn profile link
target = "https://www.linkedin.com/in/lexfridman/"

# Fetch user data
targetData = fetchUserData(target)

# Print the fetched data
print(targetData)
```