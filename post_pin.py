"""
Zen Matcha Guide — Daily Pinterest Auto-Poster
Posts one pin per day, cycling through 12 blog articles.
Designed to run via GitHub Actions cron.
"""

import os
import json
import requests

# --- Config from environment / GitHub Secrets ---
PINTEREST_ACCESS_TOKEN = os.environ["PINTEREST_ACCESS_TOKEN"]
SITE_URL = "https://candid-brioche-f2af3c.netlify.app"

# Pinterest API v5 base
API_BASE = "https://api.pinterest.com/v5"
HEADERS = {
    "Authorization": f"Bearer {PINTEREST_ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

# --- Content Calendar ---
PINS = [
    {
        "title": "10 Proven Health Benefits of Matcha Green Tea You Need to Know",
        "description": "Discover the science-backed health benefits of matcha green tea — from boosting metabolism to improving focus. Learn why Japanese matcha is the ultimate superfood. #matcha #healthbenefits #greentea #wellness #superfood #japanesetea",
        "link": f"{SITE_URL}/blog/matcha-health-benefits.html",
        "image_url": f"{SITE_URL}/images/pins/matcha-health-benefits-pin.png",
        "board_name": "Matcha Health & Wellness",
    },
    {
        "title": "Matcha vs Coffee: Which Is Actually Better for You?",
        "description": "Tired of coffee jitters? Compare matcha vs coffee side by side — caffeine, energy, health benefits, and taste. Find out why millions are switching to matcha. #matcha #matchavscoffee #coffeealternative #healthydrinks #wellness",
        "link": f"{SITE_URL}/blog/matcha-vs-coffee.html",
        "image_url": f"{SITE_URL}/images/pins/matcha-vs-coffee-pin.png",
        "board_name": "Matcha Health & Wellness",
    },
    {
        "title": "8 Easy Matcha Recipes You Can Make at Home Today",
        "description": "From matcha lattes to matcha smoothie bowls — these 8 easy recipes are perfect for beginners. No special equipment needed! #matcharecipes #matchalatte #healthyrecipes #matchalover #easyrecipes",
        "link": f"{SITE_URL}/blog/easy-matcha-recipes.html",
        "image_url": f"{SITE_URL}/images/pins/easy-matcha-recipes-pin.png",
        "board_name": "Matcha Recipes",
    },
    {
        "title": "How to Make the Perfect Matcha Latte at Home (Step-by-Step)",
        "description": "Learn the exact method to make a creamy, cafe-quality matcha latte at home. Includes hot and iced versions plus tips on choosing the right matcha powder. #matchalatte #matchaathome #latterecipe #matchadrink #homecafe",
        "link": f"{SITE_URL}/blog/how-to-make-matcha-latte.html",
        "image_url": f"{SITE_URL}/images/pins/matcha-latte-pin.png",
        "board_name": "Matcha Recipes",
    },
    {
        "title": "Matcha vs Hojicha: The Ultimate Japanese Tea Comparison",
        "description": "What's the difference between matcha and hojicha? Compare flavor, caffeine, health benefits, and brewing methods of Japan's two most popular teas. #matcha #hojicha #japanesetea #teacomparison #tealovers",
        "link": f"{SITE_URL}/blog/matcha-vs-hojicha.html",
        "image_url": f"{SITE_URL}/images/pins/matcha-vs-hojicha-pin.png",
        "board_name": "Japanese Tea Guide",
    },
    {
        "title": "7 Best Matcha Brands in 2026 (Tested & Ranked by Experts)",
        "description": "We tested 20+ matcha brands so you don't have to. Here are the 7 best matcha powders for lattes, ceremonial drinking, and cooking. #bestmatcha #matchabrands #matchapowder #matchareview #japanmatcha",
        "link": f"{SITE_URL}/blog/best-matcha-brands-2026.html",
        "image_url": f"{SITE_URL}/images/pins/best-matcha-brands-pin.png",
        "board_name": "Matcha Health & Wellness",
    },
    {
        "title": "Can Matcha Help You Lose Weight? Science-Backed Guide",
        "description": "Discover how matcha green tea can support your weight loss goals naturally. Learn the science behind matcha's metabolism-boosting EGCG and how to use it effectively. #matchaweightloss #weightloss #metabolism #healthyliving #matcha",
        "link": f"{SITE_URL}/blog/matcha-weight-loss-guide.html",
        "image_url": f"{SITE_URL}/images/pins/matcha-weight-loss-pin.png",
        "board_name": "Matcha Health & Wellness",
    },
    {
        "title": "How Matcha Naturally Reduces Anxiety & Stress (L-Theanine)",
        "description": "Feeling stressed? Matcha contains L-theanine, a natural amino acid that promotes calm focus without drowsiness. Learn how to use matcha for anxiety and stress relief. #matchaforanxiety #stressrelief #ltheanine #naturalremedies #calmfocus",
        "link": f"{SITE_URL}/blog/matcha-for-anxiety-stress-relief.html",
        "image_url": f"{SITE_URL}/images/pins/matcha-anxiety-relief-pin.png",
        "board_name": "Matcha Health & Wellness",
    },
    {
        "title": "The Complete Guide to Japanese Tea Ceremony (Chanoyu)",
        "description": "Everything you need to know about the Japanese tea ceremony — history, etiquette, tools, and how to host your own. A beautiful tradition rooted in mindfulness. #teaceremony #japaneseculture #chanoyu #matcha #mindfulness #japan",
        "link": f"{SITE_URL}/blog/japanese-tea-ceremony-guide.html",
        "image_url": f"{SITE_URL}/images/pins/tea-ceremony-guide-pin.png",
        "board_name": "Japanese Tea Guide",
    },
    {
        "title": "Hojicha Health Benefits: Japan's Roasted Green Tea Secret",
        "description": "Hojicha is Japan's cozy, low-caffeine roasted green tea. Discover its surprising health benefits — antioxidants, digestion, sleep quality, and more. #hojicha #japanesetea #roastedtea #healthbenefits #tealovers",
        "link": f"{SITE_URL}/blog/hojicha-health-benefits.html",
        "image_url": f"{SITE_URL}/images/pins/hojicha-health-benefits-pin.png",
        "board_name": "Japanese Tea Guide",
    },
    {
        "title": "How to Make the Perfect Hojicha Latte at Home",
        "description": "This creamy hojicha latte is the ultimate cozy drink. Made with roasted Japanese green tea, it's naturally sweet with a nutty, caramel-like flavor. Easy 5-minute recipe! #hojichalatte #hojichatea #latterecipe #cosydrinks #japanesetea",
        "link": f"{SITE_URL}/blog/hojicha-latte-recipe.html",
        "image_url": f"{SITE_URL}/images/pins/hojicha-latte-pin.png",
        "board_name": "Matcha Recipes",
    },
    {
        "title": "5 Best Hojicha Brands in 2026 (Expert Picks & Reviews)",
        "description": "Looking for authentic hojicha? We tested the top brands and picked the 5 best hojicha teas for lattes, daily drinking, and gifting. #besthojicha #hojichabrands #japanesetea #tearanking #hojichapowder",
        "link": f"{SITE_URL}/blog/best-hojicha-brands-2026.html",
        "image_url": f"{SITE_URL}/images/pins/best-hojicha-brands-pin.png",
        "board_name": "Japanese Tea Guide",
    },
]


def get_or_create_board(board_name: str) -> str:
    """Return the board ID for board_name, creating it if necessary."""
    resp = requests.get(f"{API_BASE}/boards", headers=HEADERS, params={"page_size": 50})
    resp.raise_for_status()
    for board in resp.json().get("items", []):
        if board["name"].lower() == board_name.lower():
            return board["id"]

    resp = requests.post(
        f"{API_BASE}/boards",
        headers=HEADERS,
        json={
            "name": board_name,
            "description": f"{board_name} — curated by Zen Matcha Guide",
            "privacy": "PUBLIC",
        },
    )
    resp.raise_for_status()
    board_id = resp.json()["id"]
    print(f"Created board '{board_name}' \u2192 {board_id}")
    return board_id


def create_pin(pin_data: dict, board_id: str) -> dict:
    """Create a pin via Pinterest API v5."""
    payload = {
        "title": pin_data["title"],
        "description": pin_data["description"],
        "board_id": board_id,
        "media_source": {
            "source_type": "image_url",
            "url": pin_data["image_url"],
        },
        "link": pin_data["link"],
    }
    resp = requests.post(f"{API_BASE}/pins", headers=HEADERS, json=payload)
    resp.raise_for_status()
    return resp.json()


def get_current_index() -> int:
    """Read the current pin index from GitHub Actions artifact or env."""
    index_str = os.environ.get("PIN_INDEX", "0")
    return int(index_str)


def main():
    index = get_current_index()
    pin_data = PINS[index % len(PINS)]

    print(f"Posting pin {index % len(PINS) + 1}/{len(PINS)}: {pin_data['title']}")

    board_id = get_or_create_board(pin_data["board_name"])
    print(f"Board: {pin_data['board_name']} ({board_id})")

    result = create_pin(pin_data, board_id)
    pin_id = result.get("id", "unknown")
    print(f"Pin created successfully! ID: {pin_id}")

    next_index = (index + 1) % len(PINS)
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"next_index={next_index}\\n")
    print(f"Next index: {next_index}")


if __name__ == "__main__":
    main()
