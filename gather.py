import requests
from bs4 import BeautifulSoup
import shodan
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Replace with your actual Shodan API key
SHODAN_API_KEY = 'Your_Shodan_API_Key'
api = shodan.Shodan(SHODAN_API_KEY)

# Function to run Recon-ng
def run_recon_ng(domain):
    with open('recon-ng-script.rc', 'w') as f:
        f.write(f"""
        workspaces create {domain}
        modules load recon/domains-hosts/bing_domain_web
        options set SOURCE {domain}
        run
        exit
        """)
    os.system("python3 recon-ng/recon-ng -r recon-ng-script.rc")

# Function to run theHarvester
def run_the_harvester(domain):
    os.system(f"python3 theHarvester/theHarvester.py -d {domain} -l 500 -b all")

# Function to get information from Shodan
def get_shodan_info(ip):
    try:
        ipinfo = api.host(ip)
        return ipinfo
    except shodan.APIError as e:
        print(f"Error: {e}")
        return None

# Function to scrape a website using BeautifulSoup
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    return links

# Function to automate browser tasks using Selenium
def automate_browser(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    elements = driver.find_elements_by_tag_name('a')
    links = [element.get_attribute('href') for element in elements if element.get_attribute('href')]
    driver.quit()
    return links

# Main function to collect OSINT
def collect_info(domain, ip):
    # Run Recon-ng
    print(f"Collecting information for {domain} using Recon-ng...")
    run_recon_ng(domain)

    # Run theHarvester
    print(f"Collecting emails and subdomains for {domain} using theHarvester...")
    run_the_harvester(domain)

    # Get Shodan information
    print(f"Collecting Shodan data for {ip}...")
    shodan_info = get_shodan_info(ip)
    if shodan_info:
        print(shodan_info)

    # Scrape website
    print(f"Scraping data from {domain}...")
    links = scrape_website(f"http://{domain}")
    print("Links found on the website:")
    for link in links:
        print(link)

    # Automate browser
    print(f"Automating browser to collect data from {domain}...")
    dynamic_links = automate_browser(f"http://{domain}")
    print("Dynamic links found on the website:")
    for link in dynamic_links:
        print(link)

# Example usage
domain = 'tesla.com'
ip = '8.8.8.8'
collect_info(domain, ip)
