import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory for fetched images
    os.makedirs("Fetched_Images", exist_ok=True)

    # Prompt user for the image URL
    image_url = input("Please enter the image URL: ")

    # Extract filename from URL
    parsed_url = urlparse(image_url)
    filename = os.path.basename(parsed_url.path)

    # Generate default filename if URL has no name
    if not filename:
        filename = "downloaded_image.jpg"

    # Fetch the image
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        file_path = os.path.join("Fetched_Images", filename)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching the image: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
