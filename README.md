
# IP Camera Weak Credential Scanner

This project is a Python-based tool to test IP cameras for weak credentials. It checks devices for common default username and password combinations and validates the login response.

## Features

- **Two-step Validation**:
  - Step 1: Verify if the device is online.
  - Step 2: Test common username and password combinations.
- **Response-Based Validation**: Uses response content (e.g., `errno` values) to determine success or failure.
- **Customizable Credentials**: Easily expand the list of weak credentials to test.
- **Multi-Port Support**: Test devices on multiple ports.

## Requirements

- Python 3.x
- Required libraries:
  - `requests`

Install the dependencies using:
```bash
pip install requests
```

## Usage

1. Clone the repository or download the script.
2. Replace the IP address and ports in the `test_single_ip` function with your target device's details.
3. Run the script:
```bash
python scanner.py
```

### Example Output

#### Successful Login
```
[*] Testing device at 192.168.1.100:80...
[+] Login successful for admin: at http://192.168.1.100:80
```

#### Failed Login
```
[*] Testing device at 192.168.1.100:80...
[-] Login failed for admin: at http://192.168.1.100:80.
[-] No weak credentials found for 192.168.1.100:80
```

## Customization

### Modify Credentials
To test additional default credentials, update the `COMMON_CREDENTIALS` list:
```python
COMMON_CREDENTIALS = [
    ("admin", "admin"),
    ("admin", "12345"),
    ("root", "root"),
    ("user", "user"),
]
```

### Test Multiple Ports
To test devices on multiple ports, modify the `ports` list in the `test_single_ip` function:
```python
ports = [80, 8080, 443]
```

## Notes

- **Legal Use Only**: Ensure you have authorization to test the devices. Unauthorized access or testing may be illegal in your jurisdiction.
- The tool is designed for educational purposes and authorized security assessments.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
