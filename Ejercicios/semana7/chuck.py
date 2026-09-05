import requests

def obtener_chiste():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()  # Lanza un error para respuestas malas (4xx o 5xx)
        data = response.json()
        print("\nChuck Norris Joke:")
        print("------------------")
        print(data['value'])
    except requests.exceptions.RequestException as e:
        print(f"Error al contactar la API: {e}")

if __name__ == "__main__":
    obtener_chiste()
