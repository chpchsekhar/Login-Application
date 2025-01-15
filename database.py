def read_users_from_csv(file_path):
    users = {}
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ensure the row is not empty
                    username, password = row
                    users[username] = password
    except FileNotFoundError:
        pass  # If the file does not exist, return an empty dictionary
    return users

def write_user_to_csv(file_path, username, password):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def username_exists(file_path, username):
    users = read_users_from_csv(file_path)
    return username in users