# change system management_ip


##### Function

The **change system management_ip** command is used to configure the IP address of a management port on new hardware. Both an IPv4 and IPv6 address can be configured, which is used by terminals to access the disk array.

##### Format

**change system management_ip** eth_port_id=? ip_type=? \[ ipv4_address=? mask=? \[ gateway_ipv4=? \] \] \[ ipv6_address=? prefix_length=? \[ gateway_ipv6=? \] \] \[ delete_gateway=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| eth_port_id | Port ID. | To obtain the value, run "show system management_ip". The value contains 1 to 31 characters, including letters, digits and periods (.). The value cannot start with a digit or a period (.) or end with a period (.). |
| ip_type | IP address type. | The value can be an "ipv4_address" or "ipv6_address". |
| ipv4_address | IPv4 address. | The IPv4 address cannot start with 0 or an integer from 224 to 255. |
| mask | IPv4 subnet mask of the management port. | The value must be an IPv4 subnet mask. |
| gateway_ipv4 | Configured IPv4 gateway. | The IPv4 gateway cannot start with 0 or an integer from 224 to 255. |
| ipv6_address | Configured IPv6 address of the management port. | The value must be an IPv6 address. |
| prefix_length | Configured IPv6 subnet mask. | The value must be an IPv6 subnet mask. |
| gateway_ipv6 | Indicates the configured IPv6 gateway of the management port. | The value must be an IPv6 address. |
| delete_gateway | Whether the original gateway needs to be deleted when you configure an IP address for the management port. | The value can be "yes" or "no", where: <br>"yes": The gateway of the port will be deleted.<br>"no": The gateway of the port will not be deleted. |

##### Usage Guidelines

-   When the maintenance terminal and the storage system are not in the same network segment, the terminal cannot access the storage system. You have to add a route to the maintenance terminal and a gateway to the storage system so that the maintenance terminal can access the storage system.
-   Before performing the operation, ensure that the address you entered is valid and the IPv4 address cannot start with 0.
-   Changing the IP address of the management port may disconnect a user that has logged in from the storage system. Log in to the storage system again after changing the IP address.
-   The maintenance terminal can access the storage system through an IPv4 address or an IPv6 address.

##### Example

Set the IPv4 address of a specified management network port to 192.168.190.2, the subnet mask to 255.255.0.0, and the gateway address to 192.168.0.1. The command output varies depending on a specific product.

```text
admin:/>change system management_ip eth_port_id=CTE0.A.MGMT ip_type=ipv4_address ipv4_address=192.168.190.2 mask=255.255.0.0 gateway_ipv4=192.168.0.1
WARNING: You are about to change the IP address of management network port. If you enter an unavailable IP address, the DeviceManager will become inaccessible. This operation will clear the configured routes on the IP address that is modified on this management port.
Suggestion: Before performing this operation, ensure that the entered IP address is available.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
