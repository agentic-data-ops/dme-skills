# show system management_ip


##### Function

The **show system management_ip** command is used to query the IP address of the management port on a controller.

##### Format

**show system management_ip**

##### Parameters

None

##### Usage Guidelines

Running this command queries the IP address of the management port on a controller.

##### Example

Query all IP addresses of the management port on a controller.

```text
admin:/>show system management_ip
Port ID : CTE0.SMM0.MGMT0
IPv4 Address : 10.15.3.32
Subnet Mask : 255.255.0.0
IPv4 Gateway : 10.15.0.1
IPv6 Address : 3003::10
IPv6 Prefix Length : 16
IPv6 Gateway : 3003::1
--------------------------------------
Port ID : CTE0.SMM0.MGMT1
IPv4 Address : 10.15.3.31
Subnet Mask : 255.255.0.0
IPv4 Gateway : 10.15.0.1
IPv6 Address : --
IPv6 Prefix Length : --
IPv6 Gateway :
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                  |
|--------------------|------------------------------------------|
| IPv4 Address       | IPv4 address of the management port.     |
| Subnet Mask        | IPv4 subnet mask of the management port. |
| IPv4 Gateway       | IPv4 gateway of the management port.     |
| IPv6 Address       | IPv6 address of the management port.     |
| IPv6 Prefix Length | IPv6 mask of the management port.        |
| IPv6 Gateway       | IPv6 gateway of the management port.     |
| Port ID            | Location of the management port.         |
