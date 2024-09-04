import csv
import json
import subprocess
import urllib.parse
import sys

# Function to query Crossref API for the title and status
def fetch_title_from_crossref(publication_url):
    # URL encode the publication value
    encoded_publication_url = urllib.parse.quote(publication_url)
    
    # Build the curl command to query the Crossref API
    curl_command = f"curl -s -w '\n%{{http_code}}' 'https://api.crossref.org/works/{encoded_publication_url}' -H 'accept: application/json'"
    
    try:
        # Run the curl command
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        
        # Split the output to get the JSON response and the HTTP status code
        response_body, status_code = result.stdout.rsplit('\n', 1)
        
        # Parse the JSON response
        try:
            response_json = json.loads(response_body)
        except json.JSONDecodeError:
            return None, status_code
        
        # Extract the title from the response
        if 'message' in response_json and 'title' in response_json['message']:
            return response_json['message']['title'][0], status_code  # Titles are usually in a list
        
        return None, status_code  # Return None if no title was found, but include the status code
    except Exception as e:
        print(f"Error fetching title: {e}", file=sys.stderr)
    
    return None, '000'  # Return None and a dummy status code if an error occurred

# Use sys.stdin for input and sys.stdout for output
reader = csv.DictReader(sys.stdin)
fieldnames = reader.fieldnames + ['status']  # Add the new 'status' field
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

# Write the header to stdout
writer.writeheader()

# Iterate over each row
for row in reader:
    if not row['title']:  # If the title is empty
        publication_url = row['publication']
        if publication_url:
            print(f"Fetching title for publication: {publication_url}", file=sys.stderr)
            title, status = fetch_title_from_crossref(publication_url)
            if title:
                print(f"Title found: {title}", file=sys.stderr)
                row['title'] = title  # Update the title in the row
            else:
                print(f"No title found for {publication_url}", file=sys.stderr)
            row['status'] = status  # Update the status in the row
    else:
        row['status'] = ''  # If title is already present, leave status empty
    
    # Write the updated (or unchanged) row to stdout
    writer.writerow(row)
