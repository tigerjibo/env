import os
#PROJECT_FOLDER is the project folder name
PROJECT_FOLDER = 'env'
HOME = os.environ['HOME']
HOST_NAME =  (HOME.split('/'))[2]
CONFIG = 'CV_Linux'
BASE = os.path.join(HOME, CONFIG)
ENV_URL = os.path.join(HOME,PROJECT_FOLDER,'config')
#nfs mount dirname
EMBED_WORK = 'Embbed_work'
#use to generate ssh public key
EMAIL = 'jibo.tiger@gmail.com'
#NET_AGENCY is network agency, According to individual needs to add or don't add
NET_AGENCY = ' '
