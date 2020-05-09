
########################################################################################
                                    Coding
########################################################################################

Import a CSV / JSON file. If condition is met, print two attributes for that condition.  
Add each number in an array until the sum equals the rest of the array  

Overall I thought I had done well with the coding interview because one of the questions involved around "battleship" which I clarified I am just familiar with

The Bulb Switcher question you can find on Leetcode.  
Given an array of numbers(ex [3 2 5]), find if its possible to split it into 2 parts with equal sum without reordering (ex [3 2 ] and [5] ) and false if not possible!  
Split array apart into two equal sums.  
Binary tree traversal  
Convert a sentence to goat latin which has been mentioned a lot by others. The second question is to count the pair of elements in an integer array based on some selection constraints.
read csv files, array operation 

Split an array and add up the numbers so that the first part of the array equals the sum of the second part of possible.
Question about manipulating data from stdin and battleship problem.  
Given a string, determine if it is a palindrome.  
Given a file with multiple columns, print the first and the third column out and find a new value based on the values of those two columns.  
e.g. I/O, python script testing, CSV file reading, and processing; 
was asked to take input text and identify the unique words in the text and how many times each word occurred.
Write a function to sort a list of integers that looks like this [5,2,0,3,0,1,6,0] -&gt; [1,2,3,5,6,0,0,0] in the most efficient way.  
Battleship game: write a function that finds a ship and return its coordinates.
Write a script that connects to 100 hosts, looks for a particular process and sends an email with a report.
Given a sentence convert the sentence to the modified pig-latin language:
Words beginning with a vowel, remove the vowel letter and append the letter to the end.
All words append the letters 'ni' to the end.
All words incrementally append the letter 'j'. i.e. 'j','jj','jjj', etc…  
The coding interview started about 1 weeks later. I was asked to code using stypi and there are two questions in 45 minutes. One is translate English to "Goat Latin" language with a set of predefined rules. It was not hard but I still spent 20-30 minutes on that, partly because I cared too much about the detail. The second question is more a shell-script coding, although I did not realize it immediately. I was asked to obfuscate local parts of email addresses found in all HTML files under a folder (also subfolders). Due to the time limit, I did not write a clean and complete code for it. But I discussed with the interviewers for the possible solutions (shell script + python regex operation).


You will be supplied with two data files in CSV format. The  first file contains statistics about various dinosaurs. The second file contains additional data. Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) Where g = 9.8 m/s^2 (gravitational constant) Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest. Do not print any other information. $ cat dataset1.csv NAME,LEG_LENGTH,DIET Hadrosaurus,1.2,herbivore Struthiomimus,0.92,omnivore Velociraptor,1.0,carnivore Triceratops,0.87,herbivore Euoplocephalus,1.6,herbivore Stegosaurus,1.40,herbivore Tyrannosaurus Rex,2.5,carnivore $ cat dataset2.csv NAME,STRIDE_LENGTH,STANCE Euoplocephalus,1.87,quadrupedal Stegosaurus,1.90,quadrupedal Tyrannosaurus Rex,5.76,bipedal Hadrosaurus,1.4,bipedal Deinonychus,1.21,bipedal Struthiomimus,1.34,bipedal Velociraptor,2.72,bipedal

Technical Phone Screen Coding question: You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.  

Problem with many formulas to get speed of different animals based on the number of legs. Information comes from 2 different files. Process the info and display animals from fastest to slowest  

Reverse a part of a vector, CSV parsing, anonymize email addresses
Given a list of integers, output all subsets of size three, which sum to zero.  
Take a paragraph as Input and output the top three most repeated words  
Extract and modify emails/urls from html files.  
Find a fast way to extract patterns from a 2d matrix.  
You receive a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) you have to reverse the order of the elements.


Some of the basics of java networking library. Like how to send HTTP GET/POST? how to verify host is up or not through scripts?
 I got goat Latin and dinosaur CSV parsing question.

How to sort hashmap by key and value?
How to implement basic data structures(priority queue, set, HashSet, LinkedHashmap, treemap, etc.) using the Java library?
Time complexity of all the Java data structures.
File reading and writing

String operations

########################################################################################
                                    Systems
########################################################################################

Linux commands, issues, process, kernel level, node full, file descriptor full, micro services, application loading time (database), performance based, automation (ansible, chef in ruby for facebook),  yaml/jinja templates
ansible push mode - mount os, system image - custom image, kickstart automation, kernel, package, local yum packages (centos red-hat apt-get similar)
database change, playbook, check server, configuration pull mode, Operating system (linux), GRUB, boot loader, boot process for linux issue for server slow, google.com - network question



OS level:
load average, application monitoring
OS upgrade, Apache, Sysctl (parameters), forward queuing
CDN - database, web server, caches upgrade using git hooks
cron job, downtime
DNS virtual domain name - VIP
load balancer, DNS - nginx (use it as load balancer)
Load balancer algorithm, staging, Caching - video streaming, 5.6 TB/second
Networking - BGP border gateway protocol, ISP, ASN number, subnet classes, public private, 10 172 192 private, ipv6, subnetting, traffic separate,   capacity management, SRE DB, web server. capacity manager, 
Caching - Memcache, 10 Linux sysadmin/networking questions (What command would you use to do _____?). 
What is the default signal that is generated when sending a kill command to a process in Linux?  
In IPv6 what is the A record equivalent?  
Questions usually start very general but quickly go very in depth. Know TCP/IP, BigO, kernel internals, etc. Try to think at big scale.
Systems round
They will ask you Linux questions .........till you feel.... you are out of your depth e. - an in-depth KNOWLEDGE OF LINUX INTERNALs is minimum criteria to clear this round.
Pick up a Linux Kernel book.... (own it.)........ and have an Overview of Performance related commands( Truth --- >> know each parameter( if it changes(increase/decrease) and how it affects performance( This is where i failed) ---- )
Last minute preparation: Study the Entire Linux kernel and Performance related commands for 10-15 days before the interview.
Try to understand how web farms(servers) are maintained.... Expect some very vague problem statements( troubleshooting question). Be ready for a set of large scale (Web scale) troubleshooting related questions. .... they just want to examine your approach, (there are no right or wrong answers).................. ( For Vague problem statements---- >> ask questions or better state your assumptions but keep the flow. Its key.

Linux Performance commands..... ( Well the engineer spent  ...15 mins on one command.. ) Know Kernel to the CPU interrupt level…

Name three states a process can be in.  
Algorithm to find 3 integers adding up to 0  

linux troubleshooting.
Given output of command vmstat and analyze the system.  
Send packets to remote machines and try to upgrade the packet remotely. Troubleshooting why some of the machines are not updated.  

Swap management, server flags, process management. A recommendation for a book called "The Linux Programming Interface.”
What part of the tcp header does traceroute modify? 
How do you make a process a service?  
What is a zombie process?  
Know the kernel in incredible depth
Linux kernel, Network deep dive, distributed system design 
What happens during the boot process from the moment you turn on the machine until you get a login prompt?
Systems internals, vmstat, netcat, shell scripting  
Third, there was a systems round which was related to Linux Internal and Troubleshooting a system under load. All relevant topics for this round could easily be read up in Brendan Gregg's blog and his book.
How would you troubleshoot a system in which you are not able to start an application on the server?  
Explain containerization?  
What happens in Linux when you type ls -l?  
Explain pagination(might be different wordings)  
'httpd' is not serving files from '/var/www/html'. Why might this be happening? How might you go about diagnosing and fixing this?”
We have a database running unusually slow in production. Why might this be happening?  
What does "$?" mean in bash?  
Questions about SIGTERMS, Unix commands, and networking fundamentals.  

last round system questions such like what will happen if push the bottom to boot the Linux system
How do you see which disks are currently mounted?  - 
 Think about this sort of information: what problems are you going to run into while doing IPC (pipes, shared memory structures etc.)? How exactly does the OS transfer information across a pipe? What are the limits or bottlenecks?
How do you do ____ across a large number of systems? How do you do it without interrupting production? How long will it take?
  - Be familiar with packet routing (How does the source computer know where to route packets? How do packets move across a network?).
  - Know how to configure and use at least one client/server network service (and talk about it intelligently). How does it work internally? What are the features of XXX protocol?
port numbers, subnet math, Linux commands.
Second interview was a coding test. Engineer had me to write two script for csv data processing, and system monitoring.

Third one was for system administration. The questions were pretty open. The interviewer had me to dig into the internals of operating system, such as performance tuning, memory model, paging, swap, process forking, system call, interrupt, and etc.

 Familiar with operating system internals and system analysis tools
 - Familiar with networks and infrastructures (TCP/IP, DNS, HTTP, and etc)
 - Think about scalability

Interview Questions

How can you find whether a process is I/O bound or CPU bound?  
https://unix.stackexchange.com/questions/208368/how-can-i-tell-which-process-is-io-bound
Explain everything that happens over the network when a client tries to access a website. 
What options do you have, nefarious or otherwise, to stop people on a wireless network you are also on (but have no admin rights to) from hogging bandwidth by streaming videos?  


Next was a phone interview for systems administration. I was given the bare minimum information possible about a system and told to describe how I discover running services and potential issues. As I progressed, the interviewer gave me information reasonable based on my descriptions and identified when I had correctly discovered a problem or possible problem. In investigating problems, it was important to be specific about why the problem was occurring and how to address the issue. When addressing problems, the performance, scalability, and maintainability of the solution was very important. Be prepared to identify how a file system is mounted or if it's local, and be prepared to encounter a single central share mounted by many servers with active read/write activity from them all. This will be difficult for anyone without good real-world Linux systems administration experience.
what happens when you type "telnet www.facebook.com 80”
Some real curveballs about how specific protocols worked. HTTP, SMTP, etc.  
For a given set of software checkins, write a program that will determine which part along the branch where the fault lies.  
Why wouldn't you want a root DNS server to answer queries for you, instead of delegating you to an authoritative server?  
Phone screening was general system stuff: DNS, TCP, CLI tools, etc.
First phone interview was coding based.
Phone interview was very linux-y, system calls, signals (term, kill, etc), load vs cpu util.
What is a filesystem, how does it work? File permissions, properties, file types. A write operation failed with an error, how do you figure out what happened? What's a signal and how is it handled by the kernel? What's a zombie process?

Talk about an iostat output (what does user vs system cpu load mean, what does iowait% mean, cache vs buffers, why do we need caching, how much cache is needed, how can disk performance be improved, where is the bottleneck)
How do TCP, UDP work? Describe what happens when a client opens a web page. How does DNS work? How does HTTP work? How does a router work?
Various questions about your current experience, talk about a conflict situation and how you handled it.
How would you design a system that manipulates content sent from a client (e.g. clean bad words in a comment post)?

Then the recruiter told me I passes the first round and we moved on to system interview, which began 5 days later. Since it is totally new to me, I read lots of posts in glassdoor and other interviewing forums and there are very useful. The interview questions requires solid knowledge about Linux, operating system, performance monitoring. They both starts with a relatively simple questions but ends with lots of followup questions. Try your best to be open-minded and always talk with the interviewer. They want not only an correct answer, but also how you get this solution.

Explain in every single step about what will happen after you type " ls * " in your terminal.  

Suppose there is a server with high CPU load but there is no process with high CPU time. What could be the reason for that? How do you debug this problem? Does your solution always work, and if not, what's the reason for that?  

Port number for HTTP, HTTPS, FTP, DNS
How would you design a cache API?  
when you saw many system interrupts, what could be the possible reason in linux 
System interview will ask more details questions regarding with Linux and networking, like what happens when you typed 'ls' in the terminal. 
CareerCup and the Unix and Linux System Administration Handbook by Evi Nemeth were invaluable.
Given a database with slow I/O, how can we improve it?  
Given a list of words, create a master list that has sublists that contain anagrams. 
With very little detailed information, how would you approach tackling a performance problem in a web application (i.e., step through your thought process of what steps you would take, information you would seek, etc.).  

Where is the dns file located?  
3 Answers
What signal do you send a service to end it?  
2 Answers
What is the type of record that resolves urls to ip records?  
4 Answers
Under ps, what are three states that a service can be in?  
1 Answer
Out of the 5-6 states you can find under ps, which two takes up system memory?  
1 Answer
If 0 is STDIN and 1 is STDOUT, what's 2?  
Initial tech screen asked very basic questions, like what the "uname" command does, or what type of packet terminates a TCP connection.  
Technical Phone screen systems: various questions on linux internal and troubleshooting,
few examples: Swap space, strace command, memory related troubleshooting.  
He/she asks questions about operating systems and debugging Linux systems. They go deeper and deeper into concepts until you don't know what is going on. Study Operating Systems fundamentals and tools to debug Linux systems (top, vmstat, dstat, sys trace, etc.).
Describe in detail on the kernel level how signals from terminal user reach processes.  

What command would be used to check file system consistency?
What command would be used to check for packet loss?
What are the 3 steps in a TCP handshake?

What information is not in the inode ?
- User ID
- File's name
- File ID  
What does the command uname -r do?  
Systems phone interview: if you had a program that needed 1TB of RAM and you only have 16GB, how does the linux system allocate memory.   
What is the purpose of tcpdump?  


`Resources by recruiter:`
```
 https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55
 https://github.com/chassing/linux-sysadmin-interview-questions
 https://syedali.net/engineer-interview-questions/
 https://github.com/0xAX/linux-insides/blob/master/SUMMARY.md
 https://www.linuxatemyram.com/
```