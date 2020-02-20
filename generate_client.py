import json

import fitbit


def load_creds():
    with open("creds.json", "r") as f:
        return json.load(f)


def creds_expiry_callback(new_creds: dict):
    print("Gotta regenerate and save the creds again")
    old_creds = load_creds()

    new_creds_to_save = {
        "client_id": old_creds["client_id"],
        "client_secret": old_creds["client_secret"],
        "access_token": new_creds["access_token"],
        "refresh_token": new_creds["refresh_token"],
        "expires_at": new_creds["expires_at"],
    }
    print(f"New creds: {new_creds_to_save}")

    with open("creds.json", "w") as f:
        json.dump(new_creds_to_save, f, indent=4)


def generate_client():
    return fitbit.Fitbit(
        **load_creds(),
        refresh_cb=creds_expiry_callback,
        redirect_uri="http://127.0.0.1:8080/",
    )

client = generate_client()
