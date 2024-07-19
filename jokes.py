joke_base_url = 'https://v2.jokeapi.dev/joke/Programming,Pun?'


def get_joke(joke_type: str | None = None):
    params = {}
    if joke_type:
        params["type"] = joke_type
    response = requests.get(joke_base_url, params)
    if response.status_code != 200:
        return
    js_data = response.json()
    if js_data.get("error"):
        return
    return js_data

def get_rand_joke_text():
    js_data = get_joke("single")
    if not js_data:
        return "Error"
    return js_data["joke"]


def get_two_part_joke():
    js_data = get_joke("twopart")
    if not js_data:
        return "Error"

    return js_data["setup"], js_data["delivery"]
