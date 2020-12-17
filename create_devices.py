# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException
import sys
import json
# ThingsBoard REST API URL
url = "http://localhost:8080"
# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    # Auth with credentials
    rest_client.login(username=username, password=password)
    number_devices = int(sys.argv[1])
    count_devices = 1;
    while (count_devices <= number_devices):
        try:
            # creating a Device
            temp = "NodeMCU" + str(count_devices)
            device = Device(name = temp, type="default")
            device = rest_client.save_device(device)
            print("Create:", temp)
            count_devices += 1

        except ApiException as e:
            count_devices += 1
            number_devices += 1