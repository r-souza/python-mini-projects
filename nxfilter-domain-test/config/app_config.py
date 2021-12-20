from os import environ, path

from dotenv import load_dotenv, find_dotenv

def load_enviroment():
    load_dotenv(find_dotenv())

load_enviroment()

# Define App Config
NXFILTER_USERNAME = environ.get('NXFILTER_USERNAME')
NXFILTER_PASSWORD = environ.get('NXFILTER_PASSWORD')
NXFILTER_GUI = environ.get('NXFILTER_GUI', 'default')

# NxFilter URIs
NXFILTER_BASEURL = environ.get('NXFILTER_BASEURL')
NXFILTER_LOGIN_URI = '{}/admin.jsp'.format(NXFILTER_BASEURL)
NXFILTER_CATEGORY_URI = '{}/category,domain_test.jsp'.format(NXFILTER_BASEURL)

# Paths
OUTPUT_CLASSIFIED_CSV = environ.get('OUTPUT_CLASSIFIED_CSV', '{}/Downloads/classified.csv'.format(path.expanduser('~')))