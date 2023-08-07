import requests

def get_data_from_url(url):
    try:
        response = requests.get(url)
        print("Success! Response Content")
    except RequestException as e:
        print("Error: {e}")

if __name__ == "__main__":
    url = "https://www.google.com"
    get_data_from_url(url)
