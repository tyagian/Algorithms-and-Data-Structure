#Python script to check if the website is up
#https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-14/
import requests
producturl="http://100daysofdevops.com/contact-us/"

res = requests.get(producturl, timeout=5)
if res.status_code != 200:
    raise "website not reachable"
    