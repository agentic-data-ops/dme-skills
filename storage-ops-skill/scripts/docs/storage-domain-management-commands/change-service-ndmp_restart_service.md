# change service ndmp_restart_service


##### Function

The **change service ndmp_restart_service** command is used to restart the NDMP service.

##### Format

**change service ndmp_restart_service**

##### Parameters

None

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Restart the NDMP service.

```text
admin:/>change service ndmp_restart_service
WARNING: You are about to restart the NDMP service.This operation will automatically restart the NDMP service and interrupt the NDMP service of all vStores.
Suggestion: If there is the NDMP service, confirm that the service needs to be restarted.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
