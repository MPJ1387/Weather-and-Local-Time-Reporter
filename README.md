# Weather and Local Time Reporter
#### Video Demo: https://youtu.be/sDcEIkhoNf4
#### Description:

For my final project, I decided to build a command-line tool that I'd actually use it everyday in my life. Often, when I check the weather for cities in other countries, I also want to know what time it is there (to know if it's day or night).

This program connects to the OpenWeatherMap API to fetch online and real-time data. However instead of just dumping the raw JSON data, I wrote a script to format it cleanly with emojis and, most importantly, calculate the exact local time of that city using the timezone offset provided by the API.

### How it Works
The program asks the user for a city name, sends a request to the API, and then processes the response.
- It uses the `requests` library to handle the API calls.
- It uses the `datetime` library to convert the "timezone offset" (which comes in seconds) into a readable date and time string.
- It handles errors gracefully, so if you type a city that doesn't exist, it won't crash.

### Project Structure
I structured the code into three main custom functions to keep it clean and testable(some other functions are only for getting data and etc.):

1. **`calc_local_time(timezone_offset)`**: This was the trickiest part. It takes the UTC time and shifts it by the offset seconds to get the city's actual time.
2. **`get_emoji(description)`**: A simple helper function that looks at the weather description (like "clear sky" or "rain") and returns a matching emoji (☀️, 🌧️, etc.) to make the output look better.
3. **`Format_output(data, city)`**: This function brings everything together. It takes the raw data, calls the other two functions, and creates the final string that user sees.

### Files
- `project.py`: Main script.
- `test_project`: Unit tests for the custom functions.
- `requirements.txt`: List of libraries nedded (`requests`).

### How to Run
First, install the required library:
`pip install -r requirements.txt`
Then run the script:
`python project.py`
*(Note: You need an internet connection for this to work as it fetches live data).*
