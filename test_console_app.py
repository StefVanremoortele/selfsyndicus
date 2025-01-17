import requests
import json

# Define the API base URL
BASE_URL = "http://localhost:8000/api/"  # Replace with your actual API URL


# 1. Create a new building
def create_building(name, address):
    url = f"{BASE_URL}buildings/"
    data = {"name": name, "address": address}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"Building created: {response.json()}")
        return response.json()["id"]  # Return the building ID
    else:
        print(f"Failed to create building: {response.status_code}, {response.text}")
        return None


# 2. Create privatives
def create_privative(name, description, area):
    url = f"{BASE_URL}privatives/"
    data = {"name": name, "description": description, "area": area, "building": 1}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"Privative created: {response.json()}")
        return response.json()["id"]  # Return the privative ID
    else:
        print(f"Failed to create privative: {response.status_code}, {response.text}")

    return None


# 3. Add privatives to a building
def add_privative_to_building(building_id, privative_id, area):
    url = f"{BASE_URL}privatives/{privative_id}"
    data = {"area": area, "building": building_id}
    response = requests.put(url, json=data)
    if response.status_code == 201:
        print(f"Privative {privative_id} added to building {building_id}")
    else:
        print(
            f"Failed to add privative to building: {response.status_code}, {response.text}"
        )


# 4. Create users
def create_user(username, email, password):
    url = f"{BASE_URL}users/"
    data = {"username": username, "email": email, "password": password}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"User created: {response.json()}")
        response.json()["id"]  # Return the user ID
    else:
        print(f"Failed to create user: {response.status_code}, {response.text}")
        # return None


# 5. Add user to privative
def add_user_to_privative(privative_id, user_id):
    url = f"{BASE_URL}privatives/{privative_id}/"
    data = {
        "owner": user_id,
        "area": 50.5,
        "building": 1,
    }
    response = requests.put(url, json=data)
    if response.status_code == 201:
        print(f"User {user_id} added to privative {privative_id}")
    else:
        print(
            f"Failed to add user to privative: {response.status_code}, {response.text}"
        )


# Main flow
def run_flow():
    # Step 1: Create building
    building_name = "Building A"
    building_address = "123 Main St"
    building_id = create_building(building_name, building_address)

    if not building_id:
        return

    # Step 2: Create privatives
    privative_1_id = create_privative("Apartment 101", "A beautiful apartment", 50.5)
    privative_2_id = create_privative("Apartment 102", "A spacious apartment", 75.5)
    if not privative_1_id or not privative_2_id:
        return

    # # Step 3: Add privatives to building
    add_privative_to_building(building_id, privative_1_id, 50.5)
    add_privative_to_building(building_id, privative_2_id, 75.5)

    # # Step 4: Create users
    user_1_id = create_user("john_doe", "john_doe@gmail.com", "password123")
    user_2_id = create_user("jane_smith", "jane_smith@gmail.com", "password456")
    # if not user_1_id or not user_2_id:
    #     return

    # # Step 5: Add users to privatives
    if not user_1_id:
        user_1_id = 2

    if not user_2_id:
        user_2_id = 3

    add_user_to_privative(privative_1_id, user_1_id)  # Assign user 1 to privative 1
    add_user_to_privative(privative_2_id, user_2_id)  # Assign user 2 to privative 2


if __name__ == "__main__":
    # todo: clear db
    run_flow()
