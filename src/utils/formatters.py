from datetime import datetime
from src.config.settings import CURRENCY_SYMBOL

def format_datetime(iso_string: str) -> str:
    """Format datetime string to readable format."""
    try:
        dt = datetime.strptime(iso_string, "%Y-%m-%d %H:%M")
        return dt.strftime("%b-%d, %Y | %I:%M %p")  # Example: Mar-06, 2025 | 6:20 PM
    except:
        return "N/A"

def format_price(price_str: str) -> str:
    """Format price string to currency format."""
    try:
        # Remove any non-numeric characters except decimal point
        price = ''.join(c for c in price_str if c.isdigit() or c == '.')
        price = float(price)
        # If price seems unreasonably high (more than 1,000,000 INR), divide by 100
        if price > 1000000:
            price = price / 100
        return f"{CURRENCY_SYMBOL}{price:,.2f}"
    except:
        return price_str

def format_duration(duration: str) -> str:
    """Format duration string to readable format."""
    try:
        if isinstance(duration, (int, float)):
            hours = int(duration // 60)
            minutes = int(duration % 60)
            return f"{hours}h {minutes}m"
        return duration
    except:
        return duration

def format_booking_url(source: str, destination: str, departure_date: datetime, 
                      return_date: datetime, departure_token: str) -> str:
    """Generate Google Flights booking URL."""
    try:
        formatted_departure = departure_date.strftime("%Y-%m-%d")
        formatted_return = return_date.strftime("%Y-%m-%d")
        
        return (
            f"https://www.google.com/travel/flights/search?"
            f"f=0&"  # Search flights
            f"q=Flights%20to%20{destination}%20from%20{source}&"  # Search query
            f"source=FLIGHTER_SEARCH&"
            f"hl=en&"  # Language
            f"curr=INR&"  # Currency
            f"tfs={departure_token}&"  # Flight token
            f"d1={formatted_departure}&"  # Departure date
            f"r1={formatted_return}"  # Return date
        )
    except Exception as e:
        print(f"Error generating booking URL: {str(e)}")
        return "#" 