import requests

def fetch_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["value"]
    else:
        return "Could not fetch joke."

# Chương trình chính
if __name__ == "__main__":
    joke = fetch_chuck_norris_joke()
    print(joke)
