#perfom a basic dns transfer

#!/usr/bin/python3

#import dns.query
import dns.zone
import sys
import dns.query

def transfer(first_zone,second_zone):
	zone = dns.zone.from_xfr(dns.query.xfr(first_zone,second_zone))
	names = zone.nodes.keys()
	names.sort()
	for i in names:
		print(zone[i].to_text(i))

if __name__ == "__main__":
	try:
		first_zone = sys.argv[1].strip()
		second_zone = sys.argv[2].strip()
	except IndexError:
		print("[-] Usage: python %s <first_zone> <second_zone>" % sys.argv[0].strip())
		print("[-] Example: python %s abcd.com efgh.com" % sys.argv[0].strip())
		sys.exit(-1)


if transfer(first_zone,second_zone):
	print(a)
else:
	print()
