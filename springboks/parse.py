import csv
import json
import urllib.parse
import sys
import requests

def check_doi_existence(publication_url):
    # URL encode the publication value
    encoded_publication_url = urllib.parse.quote(publication_url)

    # Build the request URL to query the DOI
    url = f"https://doi.org/doiRA/{encoded_publication_url}"

    try:
        # Send the GET request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            if data and data[0].get('status') == 'DOI does not exist':
                return False
    except Exception as e:
        print(f"Error checking DOI existence: {e}")

    return True

# Function to query Crossref API for the title and status
def fetch_title_from_crossref(publication_url):
    # URL encode the publication value
    encoded_publication_url = urllib.parse.quote(publication_url)
    
    # Build the request URL to query the Crossref API
    url = f"https://api.crossref.org/works/{encoded_publication_url}"
    
    try:
        # Send the GET request
        response = requests.get(url, headers={'accept': 'application/json'})
        
        # Get the HTTP status code
        status_code = response.status_code
        
        # Parse the JSON response
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            return None, str(status_code)
        
        # Extract the title from the response
        if 'message' in response_json and 'title' in response_json['message']:
            return response_json['message']['title'][0], str(status_code)  # Titles are usually in a list
        
        return None, str(status_code)  # Return None if no title was found, but include the status code
    except Exception as e:
        print(f"Error fetching title: {e}", file=sys.stderr)
    
    return None, '000'  # Return None and a dummy status code if an error occurred

# Use sys.stdin for input and sys.stdout for output
reader = csv.DictReader(sys.stdin)
fieldnames = reader.fieldnames + ['crossref-status', 'doi-exists']  # Add the new fields
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
            if status == '404':
                doi_exists = check_doi_existence(publication_url)
                row['doi-exists'] = 'Yes' if doi_exists else 'No'
            row['crossref-status'] = status  # Update the status in the row
    else:
        row['crossref-status'] = ''  # If title is already present, leave status empty
    
    # Write the updated (or unchanged) row to stdout
    writer.writerow(row)
