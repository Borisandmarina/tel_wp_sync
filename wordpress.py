import requests
import state
import config

def update_wp():
    data = state.get_state()
    current = data["current"]
    text = data[current]["text"]
    image_url = f"{config.MEDIA_BASE_URL}/{data[current]['image']}"

    content_html = f'<img src="{image_url}" alt="{current}"><p>{text}</p>'

    headers = {
        "Authorization": f"Bearer {config.WP_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": content_html
    }

    url = f"{config.WP_API_URL}/wp/v2/pages/{config.WP_PAGE_ID}"
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка обновления WordPress: {e}")
