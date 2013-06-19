import os
from os.path import join as pjoin
from handle_error import handle
from commands import getstatusoutput as getso

from config import HOME, CONFIG, BASE, ENV_URL,EMAIL

def check_dir():
    import os
    if os.path.exists(BASE):
	return
    else:
        os.mkdir(BASE)
        return

def clone_config():
    s,o = getso("cp -rf %s/* %s" % (ENV_URL, BASE))
    handle(s,o)

def generate_sshkey():
    print 'configure ssh-key'
    s,o = getso("ssh-keygen -t dsa -C %s -f ~/.ssh/%s"  %(EMAIL,EMAIL))
    handle(s,o)

def do():
    check_dir()
    clone_config()
    generate_sshkey()
