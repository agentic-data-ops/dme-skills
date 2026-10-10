# show net_plane route


##### Function

The **show net_plane route** command is used to query the route information of the network plane on the storage system.

##### Format

**show net_plane route** net_plane_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id | Network plane ID. | The value ranges from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |

##### Usage Guidelines

Run the "**show net_plane route** net_plane_id=?" command to query the route information of a specified network plane.

##### Example

Query the route information of the network plane whose ID is "1".

```text
admin:/>show net_plane route net_plane_id=1
Net Plane ID   Destination  Mask             Gateway
------------   -----------  ---------------  -----------
1              198.168.3.0  255.255.255.0    192.168.1.1
1              196.168.4.0  255.255.255.0    192.168.1.2
```

##### System Response

The following table describes the parameter meanings.

| Parameter    | Meaning                                        |
|--------------|------------------------------------------------|
| Net Plane ID | Network plane ID.                              |
| Destination  | IP address of the destination network segment. |
| Mask         | Mask of the destination network segment.       |
| Gateway      | Gateway of the destination network segment.    |
