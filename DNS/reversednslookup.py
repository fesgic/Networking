#perfom a dns reverse lookup

#!/usr/bin/python3
import dns.reversename
import sys
import dns.resolver

def resolve(address):
	address = str(address)
	domain_address = dns.reversename.from_address(address)
	domain_name = str(dns.resolver.resolve(domain_address, 'PTR')[0])
	print(domain_name)


if __name__ == "__main__":
	try:
		address = sys.argv[1].strip()
	except IndexError:
		print("[-] Usage: python %s <address>" % sys.argv[0].strip())
		print("[-] Example: python %s 8.8.8.8" % sys.argv[0].strip())
	
if resolve(address):
	a
else:
	print(None)
