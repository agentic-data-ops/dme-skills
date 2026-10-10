# change isns server_ip


##### Function

The **change isns server_ip** command is used to set the IP address of the Internet Storage Name Service (iSNS) server.

##### Format

**change isns server_ip** ip=?

##### Parameters

| Parameter | Description                    | Value |
|-----------|--------------------------------|-------|
| ip=?      | IP address of the iSNS server. | \-    |

##### Usage Guidelines

-   Running this command prevents the storage system from obtaining target information based on the previous IP address of the iSNS server.
-   Before running this command, ensure that the selected iSNS server is normal.

##### Example

To set the IP address of the iSNS server to "192.168.43.5", run the following command:

```text
admin:/>change isns server_ip ip=192.168.43.5
WARNING: You are about to change IP address of the iSNS server. This operation will cause that the target information cannot be obtained through the original IP address of the iSNS server.
Suggestion: Before you perform this operation, ensure that you select the correct iSNS server.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
