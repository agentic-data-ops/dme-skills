# reboot storage service


##### Function

The **reboot storage service** command is used to restart storage system services.

##### Format

**reboot storage service** service_name=? \[ controller_id=? \]

##### Parameters

| Parameter       | Description                          | Value                                                                                       |
|-----------------|--------------------------------------|---------------------------------------------------------------------------------------------|
| service_name=?  | Name of the service to be restarted. | The value of "service_name" is "DeviceManager".                                             |
| controller_id=? | ID of a controller.                  | For example, 0A or 1C. You can run the show controller general command to obtain the value. |

##### Usage Guidelines

-   Run the **reboot storage service** service_name=DeviceManager command to restart the DeviceManager service on all online controllers.
-   Run the **reboot storage service** service_name=DeviceManager \[ controller_id=? \] command to restart the DeviceManager service on a specific controller.

##### Example

Restart the DeviceManager service on all online controllers.

```text
admin:/>reboot storage service service_name=DeviceManager
DANGER: You are about to restart DeviceManager for the storage system.
This operation causes DeviceManager unavailable temporarily.
Suggestion: Before performing this operation, ensure that all users have exited DeviceManager.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
