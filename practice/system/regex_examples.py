# https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-10-regular-expression/
"""
#url: (http)?s?\:?\/?\/?(www\.)?[a-zA-Z0-9]+\.com
1: Phone number
Regex: \d{1,3}[.-]\d{1,3}[.-]\d{1,4}
2: Email id
Regex: [a-zA-Z0-9.-]+\@[a-z-]+\.[a-z]+
3: URL matching
Regex: https?:\/\/(www.)?[a-z]+\.\w+

4. IP address: 
beginner- "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
advance-  "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
"""
