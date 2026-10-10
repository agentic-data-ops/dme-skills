# show system client_name


##### Function

The **show system client_name** command is used to query the address information about a storage system maintenance terminal.

##### Format

**show system client_name**

##### Parameters

None

##### Usage Guidelines

By default, the storage system does not have the maintenance terminal address. By running the "change system client_name" command, you can configure or change the maintenance terminal address for the storage system.

##### Example

Query the address information about a storage system maintenance terminal. After running this command, you can see the address information about the maintenance terminal in "Client Name" of the output if you had configured the information. Otherwise, "Client Name" is blank and the actual output prevails.

```text
admin:/>show system client_name

Client Name : CDHW
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning              |
|-------------|----------------------|
| Client Name | Maintenance address. |
