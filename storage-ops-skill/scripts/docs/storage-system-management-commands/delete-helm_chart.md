# delete helm_chart


##### Function

The **delete helm_chart** command is used to delete an application chart package imported by a user.

##### Format

**delete helm_chart** name=? version=?

##### Parameters

| Parameter | Description          | Value |
|-----------|----------------------|-------|
| name      | Application name.    | \-    |
| version   | Application version. | \-    |

##### Usage Guidelines

Before running this command, run the "show helm_chart" command to query information about the imported chart packages.

##### Example

Delete the chart package of application "OceanStor-100P 8.1.0" of version 8.1.0.

```text
admin:/>delete helm_chart name=OceanStor-100P version=8.1.0
Command executed successfully.
```

##### System Response

None
