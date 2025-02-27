## Weather CLI Tool

A simple command-line tool to fetch and display the current weather for a given city using the OpenWeatherMap API.

## Features
- Fetch real-time weather data for any city.
- Display weather conditions, temperature, and humidity.
- Save weather data to a text file for future reference.
- Easy-to-use command-line interface.

## Installation

### Clone the Repository
```bash
git clone https://github.com/med.zouari07/weather-cli-tool.git
cd weather-cli-tool
```

### Set up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install requests
```

### API Key Setup
1. Get your API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Replace `your_openweathermap_api_key` in the `weather_cli.py` file with your actual API key.

## Usage
Run the script from the command line:
```bash
python weather_cli.py <city_name>
```

### Example
```bash
python weather_cli.py London
```
**Output:**
```plaintext
Weather in London:
Condition: clear sky
Temperature: 15.0°C
Humidity: 72%
```

The weather data will also be saved in a file named `weather_data.txt`.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## Contact
For questions or suggestions, please reach out to zouarimohamrd@gmail.com