# remove net_plane ipv6_address


##### Function

The **remove net_plane ipv6_address** command is used to delete the IPv6 address of a network plane.

##### Format

**remove net_plane ipv6_address** net_plane_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id | Network plane ID. | The value is an integer ranging from 1 to 1024.<br>You can obtain the value by running the "show net_plane general" command without parameters. |

##### Usage Guidelines

The IPv6 address of a network plane can be deleted only when the network plane is configured with an IPv6 address.

##### Example

Remove the IPv6 address of the network plane whose ID is "1". The ID and command output vary depending on products.

```text
admin:/>remove net_plane ipv6_address net_plane_id=1
WARNING: You are about to modify the network configuration of the network plane. This operation will restart the container service that uses the current network plane.
Suggestion: Before performing this operation, ensure that the current operation is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
