# tel_wp_sync/wordpress.py
import config
import requests
import state
import base64

def get_auth_header():
    creds = f"{config.WP_USERNAME}:{config.WP_APP_PASSWORD}"
    encoded = base64.b64encode(creds.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

def update_wp():
    state_key = state.get_current_state()
    text = state.get_text(state_key)
    image_url = f"{config.MEDIA_BASE_URL}/{state_key}.png"

    payload = {
        "content": f"<p><img src=\"{image_url}\"></p><p>{text}</p>"
    }

    response = requests.put(
        f"{config.WP_API_URL}/{config.WP_PAGE_ID}",
        headers=get_auth_header(),
        json=payload
    )

    try:
        response.raise_for_status()
    except Exception:
        print("Ошибка при обновлении страницы:", response.status_code, response.text)