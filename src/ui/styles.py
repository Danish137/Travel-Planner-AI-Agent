MAIN_STYLE = """
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ff5733;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
        }
        .stSlider > div {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 10px;
        }
        .flight-info {
            padding: 10px;
            border-radius: 5px;
            background-color: #f0f2f6;
            margin: 5px 0;
        }
        .destination-header {
            text-align: center;
            padding: 15px;
            background-color: #ffecd1;
            border-radius: 10px;
            margin-top: 20px;
        }
        .book-now-button {
            display: inline-block;
            padding: 8px 16px;
            background-color: #FF4B4B;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 10px;
            text-align: center;
            width: 100%;
        }
        .airline-logo {
            display: flex;
            justify-content: center;
        }
        .airline-logo img {
            width: 100px;
            object-fit: contain;
        }
    </style>
"""

DESTINATION_HEADER = """
    <div class="destination-header">
        <h3>🌟 Your {travel_theme} to {destination} is about to begin! 🌟</h3>
        <p>Let's find the best flights, stays, and experiences for your unforgettable journey.</p>
    </div>
"""

FLIGHT_CARD = """
    <div class="flight-info">
        <div class="airline-logo">
            <img src="{airline_logo}" alt="{airline_name}">
        </div>
        <div class="flight-details">
            <p>💰 <b>Price:</b> {price}</p>
            <p>⏱️ <b>Duration:</b> {duration}</p>
            <p>🛫 <b>Departure:</b> {departure_time}</p>
            <p>🛬 <b>Arrival:</b> {arrival_time}</p>
        </div>
        <a href="{booking_link}" target="_blank" class="book-now-button">
            🔗 Book Now
        </a>
    </div>
""" 