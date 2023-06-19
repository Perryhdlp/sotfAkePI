import requests
import json
import os
import re
import sys
import time

def create_folders(data, path):
    if isinstance(data, dict):
        for key, value in data.items():
            folder_name = key.replace(":", "_")  # Replace colons with underscores
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            create_folders(value, folder_path)
    elif isinstance(data, list):
        for item in data:
            create_folders(item, path)
    else:
        with open(os.path.join(path, "value.txt"), "w") as file:
            file.write(str(data))

def get_data(curl_file):
    # Read the cURL request from the curl.txt file
    with open(curl_file, "r") as file:
        curl_command = file.read().strip()

    # Extract the URL from the cURL command
    url = re.search('curl "(.*?)"', curl_command).group(1)

    # Extract the headers from the cURL command
    headers = {}
    header_matches = re.findall(r'-H "(.*?)"', curl_command)
    for header in header_matches:
        key, value = header.split(': ')
        headers[key] = value

    # Send the request and get the response
    response = requests.get(url, headers=headers)
    data = response.json()

    return data

def main():
    # Get the path of the current script
    script_dir = os.path.dirname(sys.argv[0])

    # Set the interval in seconds
    interval = 60

    while True:
        # Get the data
        data = get_data(os.path.join(script_dir, "curl.txt"))

        # Create the master folder
        master_folder = os.path.join(script_dir, "API")
        os.makedirs(master_folder, exist_ok=True)

        # Create subfolders based on the data hierarchy
        ships = data.get("Ships", [])
        for ship in ships:
            ship_name = ship.get("Name") or ship.get("LocalisedTitle")
            folder_name = ship_name.replace(":", "_")  # Replace colons with underscores
            folder_path = os.path.join(master_folder, "Ships", folder_name)

            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Create subfolders and write values recursively
            alignments = ship.get("Alignments", [])
            for alignment in alignments:
                title = alignment.get("Title")
                alignment_folder = os.path.join(folder_path, "Alignments", title.replace(":", "_"))

                os.makedirs(alignment_folder, exist_ok=True)

                accolades = alignment.get("Accolades", [])
                for accolade in accolades:
                    accolade_folder = os.path.join(alignment_folder, "Accolades")
                    os.makedirs(accolade_folder, exist_ok=True)

                    stats = accolade.get("Stats", [])
                    for stat in stats:
                        localised_title = stat.get("LocalisedTitle")
                        stat_folder = os.path.join(accolade_folder, "Stats", localised_title.replace(":", "_"))
                        os.makedirs(stat_folder, exist_ok=True)

                        value = stat.get("Value")
                        with open(os.path.join(stat_folder, "value.txt"), "w") as file:
                            file.write(str(value))

        print("Query Successful. Next Query 60 Seconds.")

        # Wait for the interval before refreshing the data
        time.sleep(interval)

if __name__ == "__main__":
    main()
