import requests
import json
filename = "unsplash_data.json"
for i in range(1, 10):
    link = (
        f"https://unsplash.com/napi/search/photos?page=1&per_page={i}&query=aesthetic"
    )
    response = requests.get(link)
    if response.status_code == 200:
        data = response.json()
        try:
            with open(filename, "r") as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    raise ValueError("Existing data is not a list.")
        except (FileNotFoundError, json.JSONDecodeError, ValueError):

            existing_data = []

        if "results" in data and isinstance(data["results"], list):
            existing_data.extend(data["results"])
        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
        break

raw_urls = []
try:
    with open(filename, "r") as file:
        data = json.load(file)
        if isinstance(data, list):
            for item in data:

                if isinstance(item, dict) and "urls" in item and "raw" in item["urls"]:
                    raw_urls.append(item["urls"]["raw"])
        else:
            print("Error: The data in the file is not a list.")
except FileNotFoundError:
    print(f"Error: {filename} not found.")
except json.JSONDecodeError:
    print(f"Error: {filename} contains invalid JSON.")
except Exception as e:
    print(f"An error occurred: {e}")


print(f"Extracted {len(raw_urls)} raw URLs.")
for url in raw_urls:
    print(url)
