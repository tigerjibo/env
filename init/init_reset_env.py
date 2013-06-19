import os
from os.path import join as pjoin
from handle_error import handle
from commands import getstatusoutput as getso
from config   import HOST_NAME 
def reset_tftp():
    print 'reset tftp server...\n'
    s,o = getso("/etc/init.d/xinetd reload")
    handle(s,o)
    s,o = getso("/etc/init.d/xinetd restart")
    handle(s,o)

def reset_nfs():
    print 'reset nfs server...\n'
    s,o = getso("exportfs -rv")
    handle(s,o)
    s,o = getso("/etc/init.d/nfs-kernel-server restart")
    handle(s,o)

def reset_sambo():
    print 'input sambo passwd..\n'
    s,o = getso("smbpasswd -a %s" %HOST_NAME)
    handle(s,o)
    print 'reset samba server...'
    s,o = getso("service smbd restart")
    handle(s,o)

def do():
    reset_tftp()
    reset_nfs()
    reset_sambo()
