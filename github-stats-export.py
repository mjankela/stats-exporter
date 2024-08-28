import requests
import csv
from datetime import datetime, timedelta
import os

# GitHub API endpoint
BASE_URL = "https://api.github.com"

# Your GitHub personal access token
TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"

# Your GitHub username and repository name
USERNAME = "YOUR_USERNAME"
REPO = "YOUR_REPOSITORY"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_traffic_data(endpoint):
    url = f"{BASE_URL}/repos/{USERNAME}/{REPO}/traffic/{endpoint}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching {endpoint} data: {response.status_code}")
        return None

def get_clones():
    return get_traffic_data("clones")

def get_views():
    return get_traffic_data("views")

def get_referrers():
    return get_traffic_data("popular/referrers")

def get_paths():
    return get_traffic_data("popular/paths")

def export_to_csv(data, filename):
    if not data:
        print(f"No data to export for {filename}")
        return

    keys = data[0].keys() if isinstance(data, list) else data.keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        if isinstance(data, list):
            dict_writer.writerows(data)
        else:
            dict_writer.writerow(data)

def main():
    # Create a directory for the exports
    export_dir = "github_stats_export"
    os.makedirs(export_dir, exist_ok=True)
    
    # Get the current date and time to include in the filenames
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Get and export clones data
    clones_data = get_clones()
    if clones_data:
        export_to_csv(clones_data['clones'], f"{export_dir}/{current_time}_clones.csv")

    # Get and export views data
    views_data = get_views()
    if views_data:
        export_to_csv(views_data['views'], f"{export_dir}/{current_time}_views.csv")

    # Get and export referrers data
    referrers_data = get_referrers()
    if referrers_data:
        export_to_csv(referrers_data, f"{export_dir}/{current_time}_referrers.csv")

    # Get and export paths data
    paths_data = get_paths()
    if paths_data:
        export_to_csv(paths_data, f"{export_dir}/{current_time}_paths.csv")

    print(f"Data exported to {export_dir} directory")

if __name__ == "__main__":
    main()
