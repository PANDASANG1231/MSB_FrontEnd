
import csv
import requests
import os

def download_images(csv_filename="fake_data.csv", output_dir="images", num_images=100):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i >= num_images: # Limit the number of images downloaded
                break
            acct_no = row["acct_no"]
            din = row["DIN"]
            
            # Create subfolder for each acct_no
            acct_no_folder = os.path.join(output_dir, f"Acct_{acct_no}")
            os.makedirs(acct_no_folder, exist_ok=True)

            image_url = "https://picsum.photos/400/300" # Random image URL
            filename = f"{din}.jpg" # New naming convention
            filepath = os.path.join(acct_no_folder, filename)
            
            try:
                response = requests.get(image_url, stream=True)
                response.raise_for_status() # Raise an exception for HTTP errors
                with open(filepath, 'wb') as out_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        out_file.write(chunk)
                print(f"Downloaded {filepath}") # Print full path for clarity
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {filepath}: {e}")

if __name__ == "__main__":
    download_images(num_images=10) # Download 10 images as a sample
