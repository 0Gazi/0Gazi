import requests
import json
from tinydb import TinyDB, Query
from broadcast import send_broadcast, receive_broadcast
# Initialize the TinyDB database
db = TinyDB('db.json')

def insert_json_array(json_array):
    try:
        for item in json_array:
            # Check if the item already exists in the database based on a unique identifier, e.g., 'id'
            existing_item = Query()
            db.upsert(item, existing_item.id == item['id'])  # Update the existing item
    except Exception as e:
        print("Error:", e)

def send_get_request():
    url = 'http://192.168.1.57:5000'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes.
        print("Response:", response.text)
        insert_json_array(response.json())
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def query_item_by_uuid(json_str):
    try:
        
        data = json.loads(json_str)  # JSON verisini Python veri türlerine dönüştürür
        
        if "id" in data:
            id = data["id"]
            uuid = data["uuid"]
            print("id:", id)
            print("uuid:", uuid)

            db.update({'uuid': uuid},Query().id== id)
            print("asasdadasasd")
            send_broadcast(json_str)
        else:
            print("JSON verisinde 'uuid' anahtarı bulunamadı.")
    except json.JSONDecodeError:
        print("Geçersiz JSON formatı.")
    # Define the Query object to perform the search
    
    
    # Query the database for an item with the given UUID
    # {"id": 20, "name": "Ahmet20", "uuid": "ıjıj"}

if __name__ == "__main__":
    
    send_get_request()
while True:
    # Get UUID from the user input
    user_uuid = input("Giriş yapan kişinin verileri: ")
    query_item_by_uuid(user_uuid)
    