import requests
from bs4 import BeautifulSoup

def get_whois(domain):
    url = f"https://www.whois.com/whois/{domain}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    whois_data = soup.find('pre', {'id': 'registryData'})
    return whois_data.text if whois_data else "No WHOIS data found."

def get_dns_records(domain):
    url = f"https://dns.google/resolve?name={domain}"
    response = requests.get(url).json()
    dns_records = response.get('Answer', [])
    return dns_records if dns_records else "No DNS records found."

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    subdomains = set()
    
    for td in soup.find_all('td', text=True):
        if domain in td.text:
            subdomains.add(td.text.strip())
    
    return list(subdomains) if subdomains else "No subdomains found."

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    return response

def main():
    domain = input("Enter the domain to gather information about: ")

    print("\nFetching WHOIS data...")
    whois_data = get_whois(domain)
    print(whois_data)

    print("\nFetching DNS records...")
    dns_records = get_dns_records(domain)
    for record in dns_records:
        print(record)

    print("\nFetching subdomains...")
    subdomains = get_subdomains(domain)
    for subdomain in subdomains:
        print(subdomain)

    print("\nFetching IP information...")
    ip = input("Enter the IP address to gather information about: ")
    ip_info = get_ip_info(ip)
    for key, value in ip_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
