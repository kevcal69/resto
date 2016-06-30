from flask import Flask, render_template
from locu.api import VenueApiClient, MenuItemApiClient

app = Flask(__name__)
KEY = '2b3bce161a06a5a037a9466fa3decf3d9e6d0eb1'


@app.route("/")
def main():
    venue_client = VenueApiClient(KEY)
    venues = venue_client.search(name="mcdo")
    data = []

    # details = venue_client.get_details([venues['objects'][0]['id']])
    # print details
    for obj in venues['objects']:
        place = {
            'name': obj['name'],
            'locality': obj['locality'],
            'country': obj['country'],
            'id': obj['id'],
            'lat': obj['lat'],
            'long': obj['long'],
            'phone': obj['phone'] if obj['phone'] else 000-000,
        }
        data.append(place)
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
