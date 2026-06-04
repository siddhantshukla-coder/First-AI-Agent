from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()




llm=GoogleGenerativeAI(model="gemini-2.5-flash")
# response=llm.invoke("What is the meaning of my life" )
# print(response)

class ResponseType:
    def __init__(self,summary,sources,tools_used):
        self.summary=summary
        self.sources=sources
        self.tools_used=tools_used

class WeatherTool:
    def get_weather(self,location):
        return "28°C, Cloudy"
def getlocation(llm,query):
    prompt=f"Use the {query} to see what location the user is asking and return the location only as the response "
    response=llm.invoke(prompt)
    return response
class WeatherAgent:
    def __init__(self,llm,weather_tool):
        self.llm=llm
        self.weather_tool=weather_tool
    def forecast(self,query):
        location=getlocation(self.llm,query)
        weather_data=self.weather_tool.get_weather(location)
        prompt = f"""
            You are a weather forecasting agent.
            When {query} is given, extract the location asked, and 
            use only {weather_data} to get the weather at the time and return
            the response in the format:
            Data: {weather_data}
            Summary:
            
            
            Also answer the user's question based on the data recieved.
        """
        response=self.llm.invoke(prompt)
        return ResponseType(
            summary=response,
            sources=["WeatherTool"],
            tools_used=["WeatherTool"]
        )
tool=WeatherTool()
agent=WeatherAgent(
    llm=llm,
    weather_tool=tool
)
result=agent.forecast("Should I carry an umbrealla at Delhi today?")

print(result.summary)
