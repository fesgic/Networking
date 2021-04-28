#script makes a basic dns record search and displays the result:

#!/bin/python3
import sys
import dns.resolver


#records to fecth
records =['A','AAAA','PTR','NS','MX','SOA','CNAME','TXT']
def dns_search(name):
	for qtype in records:
		#make query
		answer = dns.resolver.resolve(name,qtype,raise_on_no_answer=False)
		#display results
		if answer.rrset is not None:
			print(answer.rrset)

if __name__ == "__main__":
	try:
		#dns records to resolve
		name = sys.argv[1].strip()
	except IndexError:
		print("[-] Usage: python %s <url>" % sys.argv[0].strip())
		print("[-] Example: python %s google.com" % sys.argv[0].strip())
		sys.exit(-1)

if dns_search(name):
	print(answer.rrset)=
else:
	print()
