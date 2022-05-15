import os
"""
os.system("ls -l")
# drawback of os module, it store exit code not output
# So, subprocess can be used to save output

#Instead of os.system("ls -l"), can use os.listdir() or os.listdir("/path")
 os.listdir()
['.config', 'pagerduty_integration', 'Music', '.docker', '.anyconnect', 'go', '.DS_Store', '.vault-token', 'VirtualBox VMs', '.CFUserTextEncoding', 'bin', 'terraform-aws-eks-addons', 'auth', 'helm_values', '.psql_history', 'include', 'Pictures', 'aws_config', 'Postman', 'query_exporter_config', 'pyvenv.cfg', '.zsh_history', 'Desktop', 'Library', 'python_pd_integration', 'prometheus-exporter', 'pd_status_page_integration', '.pgadmin', 'testing', 'pagertesting', '.bash_sessions', '# Script to delete pushgateway jobs with.py', 'Public', 'sandbox', '.idlerc', '.kube', '.cisco', '.ssh', 'Movies', 'ctlog', 'Applications', 'lib', 'fluentbit-es-ehi', 'query_exporter', '.Trash', '.terraform.d', 'Documents', 'auth1', '.ngrok2', 'bitbucket', '.vscode', '.bash_profile', 'statuspager', 'Downloads', '.python_history', '.aws', 'aws_cred_backuo', '.gitconfig', 'prometheus-alert', '.bash_history', '.viminfo', 'metrics.txt']

os.mknod("file_name") # To create a file
os.mkdir("dir_name") # To create a directory
os.makedirs ("dir_name/sub_dir") # to create directories recursively
os.environ()
os.environ.get("put_variable_here")
os.environ.set("name var_name")
os.getuid()
os.rmdir()
os.path()   
dir(os.path) # to see methods supported by this module
os.path.exists("/etc/hos") -> to check if the path exist or not 
os.walk() # print directory tree. Generator and tuple of 
os.path.isdir()
os.path.islink()
os.path.islink("/etc/")
os.path.getsize("/etc/hosts")

>>> os.path.basename("/etc/hosts")
'hosts'
>>> os.path.dirname("/etc/hosts")
'/etc'
>>> os.path.join("/home","testfile")
'/home/testfile'
"""


import os
for dirname, dirpath, filename in os.walk("/Users/atyagi/Downloads"):
    #print (dirname)
    for file in filename:
        print (os.path.join(dirname, file))