def process_response(response_data):
    # Parcourir les éléments de knowncount
    for item in response_data["knowncount"]:
        print("ID:", item["id"])
        print("Known Count:", item["knownCount"])
        print("Update Date:", item["updateDate"])
        print("Rel:", item["rel"])
        print("------------------------------------")
response_data = {
    "knowncount": [
        {
            "id": "planet",
            "knownCount": 8,
            "updateDate": "24/08/2006",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/planet"
        },
        {
            "id": "dwarfPlanet",
            "knownCount": 5,
            "updateDate": "24/08/2006",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/dwarfPlanet"
        },
        {
            "id": "asteroid",
            "knownCount": 1113527,
            "updateDate": "21/11/2021",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/asteroid"
        },
        {
            "id": "comet",
            "knownCount": 3743,
            "updateDate": "08/08/2021",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/comet"
        },
        {
            "id": "moonsPlanet",
            "knownCount": 285,
            "updateDate": "01/08/2023",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/moonsPlanet"
        },
        {
            "id": "moonsDwarfPlanet",
            "knownCount": 9,
            "updateDate": "02/05/2016",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/moonsDwarfPlanet"
        },
        {
            "id": "moonsAsteroid",
            "knownCount": 558,
            "updateDate": "21/11/2021",
            "rel": "https://api.le-systeme-solaire.net/rest/knowncount/moonsAsteroid"
        }
    ]
}
process_response(response_data)
