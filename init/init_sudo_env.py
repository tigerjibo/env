import shutil
import os
from os.path import join as pjoin
from config import HOME, BASE, CONFIG, ENV_URL,EMBED_WORK,HOST_NAME,TFTP_DIR,ANDROID_IP


def setup_hosts():
    fd = open('/etc/hosts', 'a')
    fd.write('\n')
    fd.write("# Generated by env_init\n\t")
    fd.write("[%s]  www.googlesource.com  \n\t" %ANDROID_IP)
    fd.write("[%s]  android.googlesource.com \n\t"  %ANDROID_IP)
    fd.write("[%s]  cache.pack.google.com \n\t"  %ANDROID_IP)
   
def setup_tftp():
    shutil.copy(pjoin(BASE, 'tftp'),'/etc/xinetd.d/tftp')
    if os.path.exists(TFTP_DIR):
        print 'TFTP DIR EXITS'
    else:
        os.mkdir(TFTP_DIR)
        s,o = getso("chmod 777 -R %s" %TFTP_DIR)


def setup_export():
    fd = open('/etc/exports', 'a')
    fd.write('\n')
    fd.write("# Generated by env_init\n")
    fd.write("%s  *(rw,sync,no_root_squash) \n" % pjoin(HOME,EMBED_WORK))
    fd.close()
def setup_sambo():
    fd = open('/etc/samba/smb.conf','a')
    fd.write('\n')
    fd.write("# Generated by env_init\n")
    fd.write("[%s]\n\t" %HOST_NAME)
    fd.write("path=%s\n\t" %HOME)
    fd.write("valid users=%s\n\t" %HOST_NAME)
    fd.write("public=no\n\t")
    fd.write("writable=yes\n\t")
    fd.write("printable=no\n\t")
    fd.write("create mask=0765\n\t")
    fd.write("security = user\n")
    fd.close()

def do():
    setup_hosts()
    setup_tftp()
    setup_export()
    setup_sambo()
