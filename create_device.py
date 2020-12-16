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
        number_devices = sys.argv[1]
        while (number_devices!=0):
            rest_client.login(username=username, password=password)
            # creating a Device
            temp = "NodeMCU " + str(number_devices)
            device = Device(name="NodeMCU", type="thermometer")
            device = rest_client.save_device(device)
            number_devices -= 1
    except ApiException as e:
        logging.exception(e)