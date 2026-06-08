import requests


def fetch_and_display_users(num_users):
    """Fetch users from JSONPlaceholder and display selected fields.

    Args:
        num_users: The number of users to display from the API response.

    Returns:
        None if an error occurs, otherwise None after successful printing.
    """
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as error:
        print(f"Network error while fetching users: {error}")
        return None

    if response.status_code != 200:
        print(
            f"API request failed with status code {response.status_code}: "
            f"{response.reason}"
        )
        return None

    try:
        users = response.json()
    except ValueError as error:
        print(f"Failed to parse JSON from response: {error}")
        return None

    if not isinstance(users, list):
        print("Unexpected JSON structure: expected a list of users.")
        return None

    print(f"Displaying up to {num_users} users:")
    printed_count = 0

    for user in users:
        if printed_count >= num_users:
            break

        try:
            name = user["name"]
            email = user["email"]
            city = user["address"]["city"]
        except (KeyError, TypeError) as error:
            print(f"Unexpected user data format: {error}")
            return None

        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print("---")
        printed_count += 1

    if printed_count == 0:
        print("No users were displayed.")


if __name__ == "__main__":
    # Example calls from the task
    fetch_and_display_users(4)
    print()
    fetch_and_display_users(16)
