# change snmp port


##### Function

The **change snmp port** command is used to set the port number of the SNMP service.

##### Format

**change snmp port** port_number=?

##### Parameters

| Parameter     | Description                      | Value                                                             |
|---------------|----------------------------------|-------------------------------------------------------------------|
| port_number=? | Port number of the SNMP service. | The value can be "161" or an integer ranging from 20000 to 20100. |

##### Usage Guidelines

-   After the SNMP service port number is configured successfully, the SNMP service on the system restarts and uses the new port number.
-   Before performing this operation, disconnect the NMS software from the SNMP service. After the configuration is successful, use the new port number to connect to the SNMP service.

##### Example

Set the SNMP service port to 161.

```text
admin:/>change snmp port port_number=161
WARNING: You are about to change the port number of the SNMP service. This operation will cause the SNMP service to restart and use the new port number.
Suggestion: Before performing this operation, disconnect the NMS software from the SNMP service. After this operation is successful, use the new port number to connect to the SNMP service.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
