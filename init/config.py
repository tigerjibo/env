import os
#PROJECT_FOLDER is the project folder name
PROJECT_FOLDER = 'env'
HOME = os.environ['HOME']
HOST_NAME =  (HOME.split('/'))[2]
CONFIG = 'ED_Linux'
BASE = os.path.join(HOME, CONFIG)
ENV_URL = os.path.join(HOME,PROJECT_FOLDER,'config')
#nfs mount dirname
EMBED_WORK = 'Embbed_work'
#tftp dirnmae,only use in Ubuntu os
TFTP_DIR = '/tftpboot'
#use to generate ssh public key
EMAIL = 'jibo.tiger@gmail.com'
#use to resolve goole and android ip address
ANDROID_IP = '203.208.46.172' 
#NET_AGENCY is network agency, According to individual needs to add or don't add
NET_AGENCY = ' '
