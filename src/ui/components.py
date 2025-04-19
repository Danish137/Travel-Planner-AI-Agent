import streamlit as st
from datetime import datetime
from typing import Dict, List
from src.config.settings import (
    DEFAULT_SOURCE, DEFAULT_DESTINATION, DEFAULT_TRIP_DURATION,
    DEFAULT_ACTIVITIES, TRAVEL_THEMES, BUDGET_OPTIONS,
    FLIGHT_CLASSES, HOTEL_RATINGS, DEFAULT_PACKING_LIST
)
from src.utils.formatters import format_datetime, format_price, format_duration, format_booking_url
from src.ui.styles import MAIN_STYLE, DESTINATION_HEADER, FLIGHT_CARD

def setup_page():
    """Initialize page configuration and styling."""
    st.set_page_config(page_title="🌍 AI Travel Planner", layout="wide")
    st.markdown(MAIN_STYLE, unsafe_allow_html=True)
    st.markdown('<h1 class="title">✈️ AI-Powered Travel Planner</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Plan your dream trip with AI! Get personalized recommendations for flights, hotels, and activities.</p>', unsafe_allow_html=True)

def user_input_section():
    """Render the user input section."""
    st.markdown("### 🌍 Where are you headed?")
    source = st.text_input("🛫 Departure City (IATA Code):", DEFAULT_SOURCE)
    destination = st.text_input("🛬 Destination (IATA Code):", DEFAULT_DESTINATION)

    st.markdown("### 📅 Plan Your Adventure")
    num_days = st.slider("🕒 Trip Duration (days):", 1, 14, DEFAULT_TRIP_DURATION)
    travel_theme = st.selectbox("🎭 Select Your Travel Theme:", TRAVEL_THEMES)

    st.markdown("---")
    st.markdown(
        DESTINATION_HEADER.format(
            travel_theme=travel_theme,
            destination=destination
        ),
        unsafe_allow_html=True
    )

    activity_preferences = st.text_area(
        "🌍 What activities do you enjoy?",
        DEFAULT_ACTIVITIES
    )

    departure_date = st.date_input("Departure Date")
    return_date = st.date_input("Return Date")

    return {
        "source": source,
        "destination": destination,
        "num_days": num_days,
        "travel_theme": travel_theme,
        "activity_preferences": activity_preferences,
        "departure_date": departure_date,
        "return_date": return_date
    }

def sidebar_options():
    """Render the sidebar options."""
    st.sidebar.title("🌎 Travel Assistant")
    st.sidebar.subheader("Personalize Your Trip")

    # Travel Preferences
    budget = st.sidebar.radio("💰 Budget Preference:", BUDGET_OPTIONS)
    flight_class = st.sidebar.radio("✈️ Flight Class:", FLIGHT_CLASSES)
    hotel_rating = st.sidebar.selectbox("🏨 Preferred Hotel Rating:", HOTEL_RATINGS)

    # Packing Checklist
    st.sidebar.subheader("🎒 Packing Checklist")
    packing_list = {}
    for item, default_value in DEFAULT_PACKING_LIST.items():
        packing_list[item] = st.sidebar.checkbox(item, value=default_value)

    # Travel Essentials
    st.sidebar.subheader("🛂 Travel Essentials")
    visa_required = st.sidebar.checkbox("🛃 Check Visa Requirements")
    travel_insurance = st.sidebar.checkbox("🛡️ Get Travel Insurance")
    currency_converter = st.sidebar.checkbox("💱 Currency Exchange Rates")

    return {
        "budget": budget,
        "flight_class": flight_class,
        "hotel_rating": hotel_rating,
        "packing_list": packing_list,
        "visa_required": visa_required,
        "travel_insurance": travel_insurance,
        "currency_converter": currency_converter
    }

def display_flights(flights: List[Dict], source: str, destination: str, 
                   departure_date: datetime, return_date: datetime):
    """Display flight search results."""
    st.subheader("✈️ Cheapest Flight Options")
    
    if not flights:
        st.warning("No flights found for the specified route and dates. Please try different dates or routes.")
        return

    cols = st.columns(len(flights))
    for idx, flight in enumerate(flights):
        with cols[idx]:
            try:
                airline_logo = flight.get("airline_logo", "")
                airline_name = flight.get("airline", "Unknown Airline")
                price = format_price(flight.get("price", "Not Available"))
                total_duration = format_duration(flight.get("total_duration", "N/A"))
                
                flights_info = flight.get("flights", [{}])
                departure = flights_info[0].get("departure_airport", {})
                arrival = flights_info[-1].get("arrival_airport", {})
                
                departure_time = format_datetime(departure.get("time", "N/A"))
                arrival_time = format_datetime(arrival.get("time", "N/A"))
                
                departure_token = flight.get("departure_token", "")
                booking_link = format_booking_url(
                    source, destination, departure_date, 
                    return_date, departure_token
                )

                st.markdown(
                    FLIGHT_CARD.format(
                        airline_logo=airline_logo,
                        airline_name=airline_name,
                        price=price,
                        duration=total_duration,
                        departure_time=departure_time,
                        arrival_time=arrival_time,
                        booking_link=booking_link
                    ),
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"Error displaying flight {idx+1}: {str(e)}")

def display_hotels_restaurants(content: str):
    """Display hotels and restaurants information."""
    st.subheader("🏨 Hotels & Restaurants")
    st.write(content)

def display_itinerary(content: str):
    """Display the travel itinerary."""
    st.subheader("🗺️ Your Personalized Itinerary")
    st.write(content)

def show_success():
    """Display success message."""
    st.success("✅ Travel plan generated successfully!") 