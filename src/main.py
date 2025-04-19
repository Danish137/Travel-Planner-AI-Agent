import streamlit as st
from src.config.settings import GOOGLE_API_KEY, SERPAPI_KEY
from src.services.flight_service import FlightService
from src.ui.components import (
    setup_page, user_input_section, sidebar_options,
    display_flights, display_hotels_restaurants,
    display_itinerary, show_success
)
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.models.google import Gemini
import os

# Set up Google API key for Gemini
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Initialize services
flight_service = FlightService()

# Initialize AI agents
researcher = Agent(
    name="Researcher",
    instructions=[
        "Identify the travel destination specified by the user.",
        "Gather detailed information on the destination, including climate, culture, and safety tips.",
        "Find popular attractions, landmarks, and must-visit places.",
        "Search for activities that match the user's interests and travel style.",
        "Prioritize information from reliable sources and official travel guides.",
        "Provide well-structured summaries with key insights and recommendations."
    ],
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[SerpApiTools(api_key=SERPAPI_KEY)],
    add_datetime_to_instructions=True,
)

planner = Agent(
    name="Planner",
    instructions=[
        "Gather details about the user's travel preferences and budget.",
        "Create a detailed itinerary with scheduled activities and estimated costs.",
        "Ensure the itinerary includes transportation options and travel time estimates.",
        "Optimize the schedule for convenience and enjoyment.",
        "Present the itinerary in a structured format."
    ],
    model=Gemini(id="gemini-2.0-flash-exp"),
    add_datetime_to_instructions=True,
)

hotel_restaurant_finder = Agent(
    name="Hotel & Restaurant Finder",
    instructions=[
        "Identify key locations in the user's travel itinerary.",
        "Search for highly rated hotels near those locations.",
        "Search for top-rated restaurants based on cuisine preferences and proximity.",
        "Prioritize results based on user preferences, ratings, and availability.",
        "Provide direct booking links or reservation options where possible."
    ],
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[SerpApiTools(api_key=SERPAPI_KEY)],
    add_datetime_to_instructions=True,
)

def main():
    """Main application function."""
    # Set up the page
    setup_page()

    # Get user inputs
    user_inputs = user_input_section()
    sidebar_inputs = sidebar_options()

    # Generate Travel Plan
    if st.button("🚀 Generate Travel Plan"):
        with st.spinner("✈️ Fetching best flight options..."):
            flight_data = flight_service.fetch_flights(
                user_inputs["source"],
                user_inputs["destination"],
                user_inputs["departure_date"],
                user_inputs["return_date"]
            )
            cheapest_flights = flight_service.extract_cheapest_flights(flight_data)

        # AI Processing
        with st.spinner("🔍 Researching best attractions & activities..."):
            research_prompt = (
                f"Research the best attractions and activities in {user_inputs['destination']} "
                f"for a {user_inputs['num_days']}-day {user_inputs['travel_theme'].lower()} trip. "
                f"The traveler enjoys: {user_inputs['activity_preferences']}. "
                f"Budget: {sidebar_inputs['budget']}. Flight Class: {sidebar_inputs['flight_class']}. "
                f"Hotel Rating: {sidebar_inputs['hotel_rating']}. "
                f"Visa Requirement: {sidebar_inputs['visa_required']}. "
                f"Travel Insurance: {sidebar_inputs['travel_insurance']}."
            )
            research_results = researcher.run(research_prompt, stream=False)

        with st.spinner("🏨 Searching for hotels & restaurants..."):
            hotel_restaurant_prompt = (
                f"Find the best hotels and restaurants near popular attractions in "
                f"{user_inputs['destination']} for a {user_inputs['travel_theme'].lower()} trip. "
                f"Budget: {sidebar_inputs['budget']}. Hotel Rating: {sidebar_inputs['hotel_rating']}. "
                f"Preferred activities: {user_inputs['activity_preferences']}."
            )
            hotel_restaurant_results = hotel_restaurant_finder.run(hotel_restaurant_prompt, stream=False)

        with st.spinner("🗺️ Creating your personalized itinerary..."):
            planning_prompt = (
                f"Based on the following data, create a {user_inputs['num_days']}-day itinerary "
                f"for a {user_inputs['travel_theme'].lower()} trip to {user_inputs['destination']}. "
                f"The traveler enjoys: {user_inputs['activity_preferences']}. "
                f"Budget: {sidebar_inputs['budget']}. Flight Class: {sidebar_inputs['flight_class']}. "
                f"Hotel Rating: {sidebar_inputs['hotel_rating']}. "
                f"Visa Requirement: {sidebar_inputs['visa_required']}. "
                f"Travel Insurance: {sidebar_inputs['travel_insurance']}. "
                f"Research: {research_results.content}. "
                f"Hotels & Restaurants: {hotel_restaurant_results.content}."
            )
            itinerary = planner.run(planning_prompt, stream=False)

        # Display Results
        display_flights(
            cheapest_flights,
            user_inputs["source"],
            user_inputs["destination"],
            user_inputs["departure_date"],
            user_inputs["return_date"]
        )
        display_hotels_restaurants(hotel_restaurant_results.content)
        display_itinerary(itinerary.content)
        show_success()

if __name__ == "__main__":
    main() 