import subprocess

"""
sp = subprocess.Popen(command,shell=True/False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)

shell=True/False --> avoid shell=True. If shell=True, and python program is executing, 
it will fork a new shell for your program. Then, needs to follow syntax/semantics of your shell and
this may lead to a security leak.
So, use shell=False , except for some cases like
if you're depending on the shell for some variables.
"""
#command=["ls","-l"] # when shell = True
command="ls -l" # when shell=False

sp = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
rt = sp.wait()
out, err = sp.communicate()
print (out)
print (err)
