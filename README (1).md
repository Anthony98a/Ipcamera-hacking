
# IP Camera Weak Credential Scanner

This project is a Python-based tool to test IP cameras for weak credentials. It checks devices for common default username and password combinations and validates the login response.

## Features

- Two-step Validation:
  - Verify if the device is online.
  - Test common username and password combinations.
- Response-Based Validation: Uses Shodan API responses to determine success or failure.
- Customizable Credentials: Easily expand the list of weak credentials to test.
- Multi-Port Support: Test devices on multiple ports.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-repo/ip-camera-scanner.git
   cd ip-camera-scanner
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Shodan API key:
   ```
   SHODAN_API_KEY=your_shodan_api_key_here
   ```

## Usage

1. Run the main program:
   ```
   python src/main.py
   ```

2. Enter your Shodan query when prompted.

## Notes

- **Legal Use Only**: Ensure you have authorization to test the devices. Unauthorized access or testing may be illegal in your jurisdiction.
- **Educational Purposes Only**: This tool is intended solely for learning, research, and authorized security assessments. The developers are not responsible for any misuse or damage caused by this tool.
- **Raise Awareness**: The purpose of this tool is to help identify and address weak credentials, improving the security of IP camera systems.

## License

This project is licensed under the MIT License.
