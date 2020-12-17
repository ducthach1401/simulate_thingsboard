# simulate_thingsboard

# pip requiremments
    pip3 install -r requirement.txt
    
# docker thingsboard
    docker-compose up
    docker-compose down

# Create NodeMCU devices on thingsboard
    python3 create_devices.py <number devices>

# Run simulate NodeMCU devices on thingsboard
    python3 test_device.py <token>
