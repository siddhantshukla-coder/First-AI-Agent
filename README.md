# First AI Weather Agent

A simple AI-powered weather agent built using Python and Google's Gemini model through LangChain.

## Features

* Extracts a location from a user's weather-related query.
* Uses a custom weather tool to retrieve weather information.
* Generates a natural language response using Gemini.
* Demonstrates the basic architecture of an AI agent:

  * User Query
  * Location Extraction
  * Tool Execution
  * LLM Response Generation

## Technologies Used

* Python
* LangChain
* Google Gemini 2.5 Flash
* Python Dotenv

## Project Structure

```text
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Example Query

```python
result = agent.forecast(
    "Should I carry an umbrella at Delhi today?"
)
```

### Sample Output

```text
Data: 28°C, Cloudy

Summary:
The weather in Delhi today is 28°C and cloudy.
Based on the available weather information, carrying an umbrella may be helpful.
```

## Learning Goals

This project was created to understand:

* Basic AI Agent Architecture
* Tool Calling
* Prompt Engineering
* LangChain Integration
* Gemini API Usage

## Future Improvements

* Integrate a real weather API
* Add multiple tools
* Implement tool selection logic
* Use structured outputs with Pydantic
* Add memory and chat history support
