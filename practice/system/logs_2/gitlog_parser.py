"""
commit 80eab6766c4718cb27d4f6aa40bf71e79ba3ebcc
Author: John Chiu <jchiu@paypal.com>
Date:   Sun Oct 13 17:59:43 2013 -0700

    Upgraded to 4.X and added Fragments

commit 30ce75f436a0b8a493e022c20e4c3d7138126030
Author: johnkchiu <johnkchiu@yahoo.com>
Date:   Sun Oct 13 17:00:24 2013 +0000

    Created new branch dev

commit 2677b9d6d8b100d85fbd6da1b4a4187a21b676ab
Author: John Chiu <jchiu@paypal.com>
Date:   Tue Oct 16 20:33:33 2012 -0700

    - Rewrote song properties
    - Added Android Support Library
    - Clean up some code

commit 55b61986d82842f20788310cf7ffe4a02ca49437
Author: Chiu <jchiu@LM-SJN-00713306.(none)>
Date:   Thu Apr 5 23:43:30 2012 -0700
"""
#!/usr/bin/env python

import sys
import re

# array to store dict of commit data
commits = []

def parseCommit(commitLines):
	# dict to store commit data
	commit = {}
	# iterate lines and save
	for nextLine in commitLines:
		if nextLine == '' or nextLine == '\n':
			# ignore empty lines
			pass
		elif bool(re.match('commit', nextLine, re.IGNORECASE)):
			# commit xxxx
			if len(commit) != 0:		## new commit, so re-initialize
				commits.append(commit)
				commit = {}
			commit = {'hash' : re.match('commit (.*)', nextLine, re.IGNORECASE).group(1) }
		elif bool(re.match('merge:', nextLine, re.IGNORECASE)):
			# Merge: xxxx xxxx
			pass
		elif bool(re.match('author:', nextLine, re.IGNORECASE)):
			# Author: xxxx <xxxx@xxxx.com>
			m = re.compile('Author: (.*) <(.*)>').match(nextLine)
			commit['author'] = m.group(1)
			commit['email'] = m.group(2)
		elif bool(re.match('date:', nextLine, re.IGNORECASE)):
			# Date: xxx
			pass
		elif bool(re.match('    ', nextLine, re.IGNORECASE)):
			# (4 empty spaces)
			if commit.get('message') is None:
				commit['message'] = nextLine.strip()
		else:
			print ('ERROR: Unexpected Line: ' + nextLine)

if __name__ == '__main__':

	parseCommit(sys.stdin.readlines())

	# print commits
	print ('Author'.ljust(15) + '  ' + 'Email'.ljust(20) +'  ' + 'Hash'.ljust(8) + '  ' + 'Message'.ljust(20))
	print ("=================================================================================")
	for commit in commits:
		print (commit['author'].ljust(15) + '  ' + commit['email'][:20].ljust(20) + '  ' +  commit['hash'][:7].ljust(8) + '  ' + commit['message'])