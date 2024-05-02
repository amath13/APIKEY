import requests
def get_api_response(url):
    # Envoi d'une requête GET à l'URL spécifiée avec les en-têtes et les données spécifiés
    response = requests.get(url)
    # Retourne le contenu de la réponse
    return response.text
# URL de l'API
url = "https://api.le-systeme-solaire.net/rest/knowncount/"
# Appel de la fonction pour envoyer la requête et récupérer la réponse
response_text = get_api_response(url)
# Affichage du contenu de la réponse
print(response_text)
