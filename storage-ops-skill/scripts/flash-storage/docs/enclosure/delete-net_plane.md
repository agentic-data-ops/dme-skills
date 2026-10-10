# delete net_plane


##### Function

The **delete net_plane** command is used to delete a network plane.

##### Format

**delete net_plane** net_plane_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id | Network plane ID. | The value is an integer ranging from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |

##### Usage Guidelines

Run the "**delete net_plane** net_plane_id=?" command to delete a network plane with a specified ID.

##### Example

Delete the network plane whose ID is "1".

```text

admin:/>delete net_plane net_plane_id=1
Command executed successfully.
```

##### System Response

None
