from commands import getstatusoutput as getso
from handle_error import handle
from config import NET_AGENCY

def do():
    fd = open('/etc/apt/apt.conf','w')
    fd.write('%s' %NET_AGENCY)
    fd.close()

    s,o = getso("apt-get update")

    handle(s,o)

    s,o = getso("apt-get upgrade -y")

    handle(s,o)
