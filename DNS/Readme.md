#### `DNS`
- DNS maps domain names to respective ip addresses.
- DNS servers eliminate the need to remember the respective ip address for each device
- We can use **dnspython** library for dns services i.e. queries, zone transfers and dynamic updates
- **nb** read more on how a dns search is made recursively up to the ns records.
- For resolving dns records, here is a simple script:
- [BasicDnsQueries](./dnsbasic.py)

#### `DNS zone transfers`
- is process by which a  DNS server passes a copy of part of its database to another dns server
- Used to replicate dns records across dns servers
- Here is a simple script:
- [DnsZoneTransfer](./dnszonetransfer.py)

#### `Reverse dns Lookup`
- Refers to determining a domain name from an ip address
- uses special domain use the special domain in-addr.arpa e.g 8.8.8.8.in-addr.arpa
- Here is a simple script:
- [ReverseDnsLookup](./reversednslookup.py)
