# change nas_service active


##### Function

The **change nas_service active** command is used to activate the NAS feature service for the first time.

##### Format

**change nas_service active** password=?

##### Parameters

| Parameter  | Description                   | Value                                        |
|------------|-------------------------------|----------------------------------------------|
| password=? | Password of the current user. | The value is a string of 1 to 64 characters. |

##### Usage Guidelines

OceanStor Dorado 3000 V6 storage systems supports this command.

##### Example

Activate the NAS feature.

```text
admin:/>change nas_service active password=******
WARNING: You are about to activate the NAS service. This operation will cause all controllers to be upgraded and restarted in batches, and the read/write performance may deteriorate.
Suggestion: Before performing this operation, ensure that the preceding risks are acceptable.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
