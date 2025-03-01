import requests
import time
import random
from stem import Signal
from stem.control import Controller

# Target product URLs
PRODUCTS = {
    "Pokémon Scarlet & Violet S3.5 Booster Bundle Box": "https://www.target.com/p/pokemon-scarlet-violet-s3-5-booster-bundle-box/-/A-88897904#lnk=sametab",
    "Pokémon Scarlet & Violet S8.5 Elite Trainer Box": "https://www.target.com/p/2024-pok-scarlet-violet-s8-5-elite-trainer-box/-/A-93954435#lnk=sametab",
    "Pokémon Scarlet & Violet 151 Ultra Premium Collection": "https://www.target.com/p/pokemon-trading-card-game-scarlet-38-violet-151-ultra-premium-collection/-/A-88897906#lnk=sametab"
}

# Use TOR Proxy
PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050",
}

# Function to rotate TOR IP
def rotate_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    print("🔄 New TOR IP assigned!")

# Function to check stock status
def check_stock():
    for product_name, url in PRODUCTS.items():
        try:
            response = requests.get(url, proxies=PROXIES, timeout=10)
            if "Out of stock" not in response.text:
                print(f"✅ {product_name} is in stock! {url}")
            else:
                print(f"❌ {product_name} is still out of stock.")
        except Exception as e:
            print(f"Error checking {product_name}: {e}")

# Loop to check stock with TOR rotation
while True:
    check_stock()
    
    # Rotate IP every 5-10 requests
    if random.randint(1, 10) > 5:
        rotate_tor_ip()
    
    # Wait 5-15 seconds to mimic human behavior
    sleep_time = random.randint(5, 15)
    print(f"🕒 Waiting {sleep_time} seconds...")
    time.sleep(sleep_time)
