import csv
import json
import subprocess
import urllib.parse
import sys

# Function to query Crossref API for the title
def fetch_title_from_crossref(publication_url):
    # URL encode the publication value
    encoded_publication_url = urllib.parse.quote(publication_url)
    
    # Build the curl command to query the Crossref API
    curl_command = f"curl -X 'GET' 'https://api.crossref.org/works/{encoded_publication_url}' -H 'accept: application/json'"
    
    try:
        # Run the curl command
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        # Parse the JSON response
        response_json = json.loads(result.stdout)
        
        # Extract the title from the response
        if 'message' in response_json and 'title' in response_json['message']:
            return response_json['message']['title'][0]  # Titles are usually in a list
    except Exception as e:
        print(f"Error fetching title: {e}", file=sys.stderr)
    
    return None  # Return None if no title was found

# Use sys.stdin for input and sys.stdout for output
reader = csv.DictReader(sys.stdin)
writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

# Write the header to stdout
writer.writeheader()

# Iterate over each row
for row in reader:
    if not row['title']:  # If the title is empty
        publication_url = row['publication']
        if publication_url:
            print(f"Fetching title for publication: {publication_url}", file=sys.stderr)
            title = fetch_title_from_crossref(publication_url)
            if title:
                print(f"Title found: {title}", file=sys.stderr)
                row['title'] = title  # Update the title in the row
            else:
                print(f"No title found for {publication_url}", file=sys.stderr)
    
    # Write the updated (or unchanged) row to stdout
    writer.writerow(row)
