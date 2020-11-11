# KNetbOX: Device Discovery and Creator for Netbox

1. KNetbOX prompts the user if they would like to scaffold their initial config files (YML) that will be used by Nornir
2. If y, KNetbOX prompts for a subnet to ping and find alive hosts
3. It will ask for default credentials in order to create the groups.yml file
4. It will then use Nornir and Scrapli to SSH into each device and collect facts needed to create a device
5. It will then perform REST API requests against Netbox to gather necessary info to build the payload
6. Then it will compare the gathered facts with the Netbox information. If a device already exists, it moves on
7. If the device needs to be added, it will prompt for Site and Role info (while giving contextual help)
8. It lastly performs the device creation

# Contact 
- https://learn.gg/dataknox
- https://twitter.com/data_knox
- https://youtube.com/c/dataknox