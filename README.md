# Open Source Intelligence (OSINT) Gathering

## Overview

The OSINT Gathering project is designed to collect and analyze publicly available information about a target (e.g., domain, IP address) using various open-source tools and libraries. This project demonstrates techniques for reconnaissance and surveillance using tools like Recon-ng, theHarvester, and Shodan, and methods for web scraping and browser automation.

## Project Aim

The primary aim of this project is to:
1. Collect information about a target domain and IP address from multiple sources.
2. Analyze and visualize the collected data to identify potential security vulnerabilities or gather actionable intelligence.
3. Provide a comprehensive example of integrating different OSINT tools and libraries in Python.

## Technologies and Libraries

This project uses the following technologies and libraries:
- **Python**: The main programming language for scripting and automation.
- **Recon-ng**: A web reconnaissance framework.
- **theHarvester**: A tool for gathering emails, subdomains, and other information.
- **Shodan**: A search engine for internet-connected devices.
- **BeautifulSoup**: A library for web scraping.
- **Requests**: A library for making HTTP requests.
- **Selenium**: A tool for web automation.

## Prerequisites

Before running the script, ensure you have the following installed:
- **Python 3.x**: Install from [python.org](https://www.python.org/downloads/).
- **ChromeDriver**: Download from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system's PATH.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Anshuman1812-lab/OSINT-Gathering.git
   cd osint-gathering

2. **Install Required Python Libraries**

   ```bash
   pip install requests beautifulsoup4 selenium shodan
   
3. **Install Additional Tools**
   - *Recon-ng: Install via pip*
     ```bash
     pip install recon-ng
     
   - *theHarvester: Clone the repository and install.*
     ```bash
     git clone https://github.com/laramies/theHarvester.git
     cd theHarvester
     pip install -r requirements.txt

## Setup
1. **Shodan API Key**
   - Obtain an API key from [Shodan](https://account.shodan.io/) and replace 'YOUR_SHODAN_API_KEY' in the script with your actual key.

2. **ChromeDriver**
   - Ensure [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) is downloaded and added to your system's PATH.

## Usage
1. Edit the Script
  - Open **`osint_gathering.py`** and replace:
    - `example.com` with your target domain.
    - `8.8.8.8` with your target IP address.
    - `YOUR_SHODAN_API_KEY` with your actual Shodan API key.
2. Run the Script
```bash
python3 osint_gathering.py
```

## Script Details
1. ***run_recon_ng(domain)*** - Runs Recon-ng with a predefined script to gather domain information.
2. ***run_the_harvester(domain)*** - Executes theHarvester to collect emails, subdomains, and other information related to the domain.
3. ***get_shodan_info(ip)*** - Fetches information from Shodan for a given IP address, including open ports, hostnames, and organization details.
4. ***scrape_website(url)*** - Scrapes the given website URL using BeautifulSoup to extract static links.
5. ***automate_browser(url)*** - Uses Selenium to automate browser tasks and extract dynamic content from the website.
6. ***collect_info(domain, ip)*** - Main function that integrates all the above methods to collect and print information about the specified domain and IP address.

## Sample Output
Here is a sample of what you might see when running the script:
```bash
Collecting information for example.com using Recon-ng...
[Recon-ng output logs]
Collecting emails and subdomains for example.com using theHarvester...
[theHarvester output logs]
Collecting Shodan data for 8.8.8.8...
{'ip_str': '8.8.8.8',
 'ports': [53, 443],
 'hostnames': ['dns.google'],
 'org': 'Google LLC',
 'os': 'Linux',
 'location': {'city': 'Mountain View', 'country_code': 'US', 'latitude': 37.4192, 'longitude': -122.0574},
 'tags': ['dns', 'public'],
 'data': [ ... ]}  # Sample Shodan output

Scraping data from example.com...
Links found on the website:
http://example.com/about
http://example.com/contact
http://example.com/blog

Automating browser to collect data from example.com...
Dynamic links found on the website:
http://example.com/articles
http://example.com/events
```
## Ethical Considerations
Ensure compliance with legal and ethical standards. Avoid accessing unauthorized or private information.

## Contribution
Contributions are welcome! Please open an issue or submit a pull request on the [GitHub Repository](https://github.com/Anshuman1812-lab/OSINT-gathering/issues) if you have suggestions or improvements.

## Acknowledgments
- [Recon-ng](https://github.com/lanmaster53/recon-ng)
- [theHarvester](https://github.com/laramies/theHarvester)
- [Shodan](https://www.shodan.io/dashboard)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)
