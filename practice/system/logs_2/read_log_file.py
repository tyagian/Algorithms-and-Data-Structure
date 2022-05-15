"""
Background
You have 10GB of text logs. Each log line corresponds to a single HTTP response from web frontend. You goal is to write a simple, reusable tool that returns the percentage of responses that were HTTP 5xx errors, broken down by domain, for a given timeframe.
Output should look something like this:
Between time XXXXXXXXXX and time YYYYYYYYYY:
vimeo.com returned 2.15% 5xx errors
player.vimeo.com returned 3.01% 5xx errors
api.vimeo.com returned 0.01% errors

The input to your tool will be a start time, an end time, and a list of files. You should consider lines at or after the start time, and strictly before the end time. You may choose to take input in whatever format you like.
Each log line looks like this (this is a single line, which may be wrapped on your screen):
1493969101.644 | https | vimeo.com | GET | 404 | 1493969101583195,1493969101635320, | IAD |  | 10.10.3.59 | 0.009

The fields are:
1.	Time of response (seconds since epoch, as a float)
2.	Response scheme ("http" or "https")
3.	HTTP Host (domain)
4.	HTTP request method
5.	HTTP status
6.	CDN information
7.	CDN ingress point
8.	Remote address metadata
9.	Remote address
10.	Time taken by request in seconds
Each field is separated by " | " (a pipe enclosed by spaces). The fields you care about are (1), (3), and (5).
log_sample.txt contains a small sample of log entries.
We wrote a sample solution in about 1 hour, and we're expecting something of a similar level of complexity -- we don't need something complex, and it doesn't need to solve use cases other than the one we're describing.
Our Questions
1.	Please write a program to solve the problem above, in Python, Ruby, or Go. (If you don't know any of these languages, talk to us and we'll figure something out.)
2.	Please write a README file including the following information:
i.	A sample invocation of your program and its output.
ii.	A list of any external dependencies of your program, and any applicable installation instructions.
iii.	A list of any assumptions you made in your solution.
Thanks for taking the time to complete this exercise!
<3, Vimeo
"""


