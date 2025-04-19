import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Default values
DEFAULT_SOURCE = "BOM"
DEFAULT_DESTINATION = "DEL"
DEFAULT_TRIP_DURATION = 5
DEFAULT_ACTIVITIES = "Relaxing on the beach, exploring historical sites"

# Currency settings
CURRENCY = "INR"
CURRENCY_SYMBOL = "₹"

# Flight search settings
FLIGHT_SEARCH_PARAMS = {
    "engine": "google_flights",
    "currency": CURRENCY,
    "hl": "en"
}

# UI Theme settings
PAGE_TITLE = "🌍 AI Travel Planner"
PAGE_LAYOUT = "wide"

# Travel themes
TRAVEL_THEMES = [
    "💑 Couple Getaway",
    "👨‍👩‍👧‍👦 Family Vacation",
    "🏔️ Adventure Trip",
    "🧳 Solo Exploration"
]

# Budget options
BUDGET_OPTIONS = ["Economy", "Standard", "Luxury"]
FLIGHT_CLASSES = ["Economy", "Business", "First Class"]
HOTEL_RATINGS = ["Any", "3⭐", "4⭐", "5⭐"]

# Default packing list
DEFAULT_PACKING_LIST = {
    "👕 Clothes": True,
    "🩴 Comfortable Footwear": True,
    "🕶️ Sunglasses & Sunscreen": False,
    "📖 Travel Guidebook": False,
    "💊 Medications & First-Aid": True
} 