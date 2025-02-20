import json
import argparse
import os
from warcio.archiveiterator import ArchiveIterator
from urllib.parse import urlparse

def generate_pages_index(warc_file, domain):
    # Extract the base name for the jsonl output file
    base_name = os.path.splitext(os.path.splitext(warc_file)[0])[0]
    output_file = f"{base_name}_pages.jsonl"
    
    # Create a list to store page data
    pages = []

    # Open the WARC file and process records
    with open(warc_file, 'rb') as f:
        for record in ArchiveIterator(f):
            if record.rec_type == 'response':  # We're only interested in HTTP response records
                # Extract metadata from the WARC record
                url = record.rec_headers.get('WARC-Target-URI', '')
                if domain not in url:  # Only process URLs that contain the given domain
                    continue
                
                status = record.http_headers.get('Status', '')
                timestamp = record.rec_headers.get('Date', '')  # Can be adjusted if you need another timestamp
                length = record.rec_headers.get('Content-Length', '0')
                
                # Create a page index entry
                page_data = {
                    'url': url,
                    'status': status,
                    'timestamp': timestamp,
                    'content_length': length
                }
                
                # Append the page data to the list
                pages.append(page_data)
    
    # Reverse the order of pages
    pages.reverse()
    
    # Write the reversed pages data to the output JSONL file
    with open(output_file, 'w') as out:
        for page_data in pages:
            out.write(json.dumps(page_data) + '\n')
                
    print(f"Pages index saved to {output_file}")

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Generate pages index for a WARC file")
    parser.add_argument('warc_file', help="The WARC file to process")
    parser.add_argument('domain', help="The domain to filter pages by (e.g., www.cs.albany.edu)")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to generate the pages index
    generate_pages_index(args.warc_file, args.domain)

if __name__ == '__main__':
    main()
