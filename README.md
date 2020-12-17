# Simulate thingsboard
Python 3
# pip requiremments
    pip3 install -r requirement.txt

# Docker thingsboard
    - Deploy docker
        docker-compose up
    - Shutdown docker
        docker-compose down

# Create NodeMCU devices on thingsboard
    python3 create_devices.py <number devices>
        (Devices Name: NodeMCU <N>)

# Run simulate NodeMCU devices on thingsboard
    python3 test_device.py <token> (Send Data DHT11)

# Or run all device: copy token device from thingsboard to token.txt and run
    chmod u+x test_device.py
    python3 run_simulate.py
