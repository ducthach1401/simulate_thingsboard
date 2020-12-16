import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://localhost:8080"
# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        # Auth with credentials
        while (
        rest_client.login(username=username, password=password)
        # creating a Device
        device = Device(name="Thermometer 1", type="thermometer")
        device = rest_client.save_device(device)
        logging.info(" Device was created:\n%r\n", device)
    except ApiException as e:
        logging.exception(e)