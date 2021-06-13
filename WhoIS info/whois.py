import dns.resolver
import whois
import sys
from pyfiglet import Figlet 


# Setting the colors
white='\033[0m'
fail=red='\033[91m'
success=green='\033[92m'
yellow='\033[93m'
blue='\033[94m'


fonts = Figlet(font='slant')
print(fonts .renderText(f"{yellow}WHO{green}IS"))


records = ['A','AAA','PTR','NS','MX','SOA','CNAME','TXT']

def dns_resolve_final(url):
    print(f"[{green}OK{white}] Checking the DNS Records and Resolving Servers")
    for qtype in records:
        #make query
        answer = dns.resolver.resolve(url,qtype,raise_on_no_answer=False)
        #display results
        if answer.rrset is not None:
            print(f"[{green}OK{white}] Drawing the DNS Resolving Tree")
            print(f"DNS Resolving Tree\n ORDER: A, AAA, PTR, NS, MX, SOA, CNAME, TXT\n {answer.rrset}\n\n")


def whois_info(url):
    info = whois.whois(url)
    print(f"""
    \n{blue}Site Info
    {green}Domain Name: {yellow}{info.domain_name}\n
    {green}Registration Name: {yellow}{info.name}\n
    {green}Organisation Name: {yellow}{info.org}
    {green}Registration Date: {yellow}{info.creation_date}\n
    {green}Expiry Date: {yellow}{info.expiration_date}\n
    {green}Address: {yellow}{info.address}\n
    {green}City : {yellow}{info.city}\n
    {green}State : {yellow}{info.state}\n
    {green}Country : {yellow}{info.country}\n

    {blue}\nAdditional Info
    {green}Registrar: {yellow}{info.registrar}\n
    {green}WhoIs Server: {yellow}{info.whois_server}\n
    {green}Updated on date: {yellow}{info.updated_date}\n
    {green}NameServers: {yellow}{info.name_servers}\n
    {green}Status: {yellow}{info.status}\n

    {blue}\n Extra Info
    {green}Emails: {yellow}{info.emails}\n\
    {green}DnsSec: {yellow}{info.dnssec}\n
    """)


if __name__ == "__main__":
	try:
		#dns records to resolve
		url = sys.argv[1].strip()
	except IndexError:
		print("[-] Usage: python %s <url>" % sys.argv[0].strip())
		print("[-] Example: python %s google.com" % sys.argv[0].strip())
		sys.exit(-1)