import json

import fitbit


def creds_expiry_callback(new_creds: dict):
    print("Gotta regenerate and save the creds again")

    new_creds_to_save = {
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "access_token": new_creds["access_token"],
        "refresh_token": new_creds["refresh_token"],
        "expires_at": new_creds["expires_at"],
    }
    print(f"New creds: {new_creds_to_save}")

    with open("creds.json", "w") as f:
        json.dump(new_creds_to_save, f, indent=4)


def generate_client():
    with open("creds.json", "r") as f:
        creds = json.load(f)

    return fitbit.Fitbit(
        **creds,
        refresh_cb=creds_expiry_callback,
        redirect_uri="http://127.0.0.1:8080/",
    )

client = generate_client()
