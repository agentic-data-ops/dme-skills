# delete container_image


##### Function

The **delete container_image** command is used to delete an application image package imported by a user.

##### Format

**delete container_image** name=? version=?

##### Parameters

| Parameter | Description          | Value |
|-----------|----------------------|-------|
| name      | Application name.    | \-    |
| version   | Application version. | \-    |

##### Usage Guidelines

Before running this command, run the "show container_image" command to query information about the imported application image packages.

##### Example

Delete the image package of application "OceanStor-100P 8.1.0" of version 8.1.0.

```text
admin:/>delete container_image name=OceanStor-100P version=8.1.0
Command executed successfully.
```

##### System Response

None
