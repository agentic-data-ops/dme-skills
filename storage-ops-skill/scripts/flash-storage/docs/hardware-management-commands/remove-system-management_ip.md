# remove system management_ip


##### Function

The **remove system management_ip** command is used to delete an IP address of a management network port.

##### Format

**remove system management_ip** eth_port_id=? ip_type=?

##### Parameters

| Parameter   | Description      | Value                                                                                                                                                                                                                 |
|-------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eth_port_id | Network port ID. | To obtain the value, run "show system management_ip". The value contains 1 to 31 characters, including letters, digits and periods (.). The value cannot start with a digit or a period (.) or end with a period (.). |
| ip_type     | IP address type. | The value can be an "ipv4_address" or "ipv6_address".                                                                                                                                                                 |

##### Usage Guidelines

Running this command disconnects the user that uses the deleted IP address for login from the storage system.

##### Example

Delete the IPv4 address of a specipied management network port.

```text
admin:/>remove system management_ip eth_port_id=CTE0.A.MGMT ip_type=ipv4_address
WARNING: You are about to delete the IP address of management network port. After this operation, you cannot use this IP address to log in to DeviceManager of the storage system.
Suggestion: Before performing this operation, ensure that the IP address is no longer needed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the IPv6 address of a specipied management network port.

```text
admin:/>remove system management_ip eth_port_id=CTE0.A.MGMT ip_type=ipv6_address
WARNING: You are about to delete the IP address of management network port. After this operation, you cannot use this IP address to log in to DeviceManager of the storage system.
Suggestion: Before performing this operation, ensure that the IP address is no longer needed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
