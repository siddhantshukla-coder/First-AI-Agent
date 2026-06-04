# First AI Weather Agent

A simple AI-powered weather agent built using Python, Google's Gemini model, and the OpenWeatherMap API.

The agent takes a natural language weather query, extracts the location using Gemini, fetches real-time weather information from OpenWeatherMap, and generates a user-friendly response.

## Features

* Natural language weather queries
* Location extraction using Gemini
* Real-time weather data using OpenWeatherMap API
* Custom-built WeatherTool and WeatherAgent classes
* AI-generated weather recommendations based on live weather data

## Technologies Used

* Python
* LangChain
* Google Gemini 2.5 Flash
* OpenWeatherMap API
* Python Dotenv
* Requests

## How It Works

```text
User Query
     ↓
Gemini extracts location
     ↓
WeatherTool calls OpenWeatherMap API
     ↓
Weather data returned
     ↓
Gemini generates final response
```

## Example Query

```python
result = agent.forecast(
    "Should I carry an umbrella at Delhi today?"
)
```

## Example Weather Data

```python
{
    "location": "Delhi",
    "temperature": 41.85,
    "humidity": 15,
    "conditions": "clear sky"
}
```

## Sample Response

```text
The weather in Delhi is currently 41.85°C with clear skies.

Based on the current weather conditions, carrying an umbrella is not necessary unless rain is expected later in the day.
```

## Project Structure

```text
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Concepts Learned

* AI Agent Architecture
* Tool Calling
* Prompt Engineering
* API Integration
* Environment Variables
* LangChain Basics
* LLM-Powered Information Extraction

## Future Improvements

* Multiple tool support
* Tool selection and routing
* Weather forecasts for upcoming days
* Structured responses using Pydantic
* Agent memory and chat history
* Async API calls
* Error handling and retries
