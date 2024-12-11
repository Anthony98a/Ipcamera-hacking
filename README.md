This tool is designed for educational purposes and for scanning authorized devices only. Unauthorized use of this tool is strictly prohibited.
IP Camera Weak Credential Checker
This project provides a simple tool to search for IP cameras via the Shodan API and test for weak credentials (such as the default admin username with an empty password). Its primary goal is to help authorized users audit their own devices to identify and mitigate security risks.

Features
Shodan Integration: Uses Shodan’s search capabilities to identify IP cameras that match specific query criteria.
Weak Credential Checks: Attempts to log in with commonly known weak credentials (e.g., admin with an empty password).
Results Export: Outputs scan results locally and can optionally export them to a results.csv file for further analysis.
Configurable Queries: Allows you to customize Shodan query strings to focus on specific regions, brands, or device features.
Usage
Obtain a Shodan API Key:
You will need a valid Shodan API Key. Do not hardcode this in your source code. Instead, use environment variables or configuration files excluded from version control.

Install Dependencies:
Install required Python packages with:

bash
Copy code
pip install -r requirements.txt
Run the Tool:
Edit main.py to include your Shodan API Key (retrieved securely, e.g., from an environment variable). Then run:

bash
Copy code
python3 main.py
The script will:

Search Shodan with the default query (JAWS/1.0 http.favicon.hash:90066852) or another query if you modify the code.
Test the discovered IP cameras for weak credentials.
Print the results and, if configured, write them to results.csv.
Customizing Queries and Testing:

Modify the query variable in main.py to change which devices are searched.
Adjust the COMMON_CREDENTIALS list to test different username/password combinations.
Integrate additional logic or advanced filtering to refine results.
Advanced Query Tips
Beyond the default query, you can explore various Shodan filters and keywords:

By Brand or Firmware:

arduino
Copy code
Hikvision
"Server: GoAhead-Webs"
http.title:"IPCAM"
http.title:"Network Camera"
By Favicon Hash or Specific Page Content:

makefile
Copy code
http.favicon.hash:90066852
http.html:"/cgi-bin/gw.cgi"
Geolocation and Port Filtering:

vbnet
Copy code
country:"CN"
port:80
port:8080
port:8888
Combining Keywords:

arduino
Copy code
"JAWS/1.0" port:80
Review Shodan’s official documentation for more advanced filters and discover more device-specific traits by examining your initial results and iterating.

Legal and Ethical Considerations
Authorized Use Only:
This tool is intended solely for use on devices you own or are authorized to test. Scanning or attempting to log into devices without proper authorization is illegal and unethical. Always comply with local, national, and international laws regarding computer security and privacy.

Shodan Terms of Service:
You must abide by Shodan’s Terms of Service. Unauthorized or malicious use of this tool might violate these terms and can lead to the suspension of your API Key or legal repercussions.

Disclaimer of Liability:
This project is provided “as is” without any warranties. The developers are not responsible for any misuse, direct or indirect damages resulting from the use of this tool. The user assumes all responsibility for ensuring lawful, ethical, and authorized usage.

License
Include a valid open-source license file (e.g., MIT, Apache 2.0, GPL) in the repository. For example, the MIT License:

css
Copy code
MIT License © [Year] [Your Name]
Contributing
Bug Reports & Improvements:
Submit issues or pull requests to contribute. Make sure your suggestions comply with relevant laws and protect the privacy and security of others.

Education & Awareness:
Feel free to add documentation, examples, or visualizations (like charts, graphs, or geographical heat maps) to help raise security awareness and guide device owners in strengthening their defenses.

Contact
For questions, suggestions, or discussions, please open an issue in this repository.
