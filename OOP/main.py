import re
import validators

email1 = 'maks@coder.com'
ip = '192.168.03.14'
url = 'http://sait.com'
url1 = 'sait.com'

print(re.search(r'\w{}', email1))
print(validators.email(email1), email1)
print(validators.ip_address.ipv4(ip), ip)
print(validators.url(url), url)
print(validators.domain(url1),url1)