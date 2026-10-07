import pprint


def read_config():
    network_data = {}

    with open("Day3\\network.cfg", "r") as f:

        for line in f:
            line = line.strip()

            if line:
                key, value = line.split("=")

                network_data[key] = value

    return network_data


def display_config(network_data):
    pprint.pprint(network_data)


def update_config(network_data):

    network_data["Interface"] = "eth1"
    network_data["onboot"] = "yes"
    network_data["bootproto"] = "static"
    network_data["IPADDR"] = "192.168.1.10"
    network_data["PREFIX"] = "24"
    network_data["DNS1"] = "122.33.344.555"

    return network_data


def write_config(network_data):

    with open("new_network.cfg", "w") as f:

        for key, value in network_data.items():
            f.write(f"{key}={value}\n")


# Step 1: Read original configuration
network_data = read_config()

print("Original Configuration:")
display_config(network_data)


# Step 2: Update configuration
updated_data = update_config(network_data)

print("\nUpdated Configuration:")
display_config(updated_data)


# Step 3: Create new configuration file
write_config(updated_data)

print("\nnew_network.cfg created successfully")