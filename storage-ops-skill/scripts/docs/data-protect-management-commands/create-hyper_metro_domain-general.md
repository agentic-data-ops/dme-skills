# create hyper_metro_domain general


##### Function

The **create hyper_metro_domain general** command is used to create a HyperMetro domain.

##### Format

**create hyper_metro_domain general** remote_device_id=? name=? \[ description=? \]

##### Parameters

| Parameter          | Description                      | Value                                                                                                                                                               |
|--------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| remote_device_id=? | ID of the remote storage device. | Run the "show remote_device general" command without parameters to obtain the value.                                                                                |
| name=?             | Name of the HyperMetro domain.   | The value contains 1 to 31 ASCII characters including digits, letters, underscores (\_), hyphens (-), and periods (.), and can only start with a digit or a letter. |
| description=?      | Description information.         | The value contains 1 to 127 letters.                                                                                                                                |

##### Usage Guidelines

None

##### Example

Create a HyperMetro domain whose remote device ID is "1" and name is "domainA".

```text
admin:/>create hyper_metro_domain general remote_device_id=1 name=domainA
Command executed successfully.
```

Create a HyperMetro domain whose remote device ID is "1" and name is "domainA" between two storage arrays of different models.

```text
admin:/>create hyper_metro_domain general remote_device_id=1 name=domainA
WARNING: You are about to use two storage arrays of different models to create a HyperMetro domain. Different product models have different performance and specifications. When the service pressure exceeds the capability of the array with the lower specifications, the HyperMetro pair may be disconnected.
Suggestion: Confirm that you want to perform this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
