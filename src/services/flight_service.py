from datetime import datetime
from typing import Dict, List, Optional
from serpapi import GoogleSearch
from src.config.settings import SERPAPI_KEY, FLIGHT_SEARCH_PARAMS

class FlightService:
    def __init__(self):
        self.api_key = SERPAPI_KEY

    def fetch_flights(self, source: str, destination: str, 
                     departure_date: datetime, return_date: datetime) -> Dict:
        """Fetch flight data from Google Flights via SerpAPI."""
        params = {
            **FLIGHT_SEARCH_PARAMS,
            "departure_id": source,
            "arrival_id": destination,
            "outbound_date": str(departure_date),
            "return_date": str(return_date),
            "api_key": self.api_key
        }
        
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            return results
        except Exception as e:
            print(f"Error fetching flights: {str(e)}")
            return {}

    def extract_cheapest_flights(self, flight_data: Dict) -> List[Dict]:
        """Extract top 3 cheapest flights from flight data."""
        if not flight_data or 'best_flights' not in flight_data:
            return []
            
        try:
            best_flights = flight_data.get("best_flights", [])
            sorted_flights = sorted(
                best_flights, 
                key=lambda x: float(''.join(c for c in str(x.get("price", "inf")) if c.isdigit() or c == '.'))
            )[:3]
            return sorted_flights
        except Exception as e:
            print(f"Error extracting cheapest flights: {str(e)}")
            return []

    def get_booking_details(self, flight_data: Dict, departure_token: str) -> Optional[Dict]:
        """Get booking details for a specific flight."""
        try:
            params = {
                **FLIGHT_SEARCH_PARAMS,
                "api_key": self.api_key,
                "departure_token": departure_token
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            return results.get('best_flights', [{}])[0] if results.get('best_flights') else None
        except Exception as e:
            print(f"Error getting booking details: {str(e)}")
            return None 