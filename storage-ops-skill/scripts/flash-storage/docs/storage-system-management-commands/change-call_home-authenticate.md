# change call_home authenticate


##### Function

The **change call_home authenticate** command is used to authenticate the Call Home service.

##### Format

**change call_home authenticate** username=? password=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| username | Support account of the technical support engineer. | The account supports the following two formats: <br>An account can start with a letter or a digit, and contains letters, digits, underscores (_), periods (.), and hyphens (-) only. The value contains 1 to 63 characters. Example: Jack_Wang.<br>The account can be an email in the following format: support@huawei.com. The value contains 1 to 100 characters. |
| password | Password of a support account. | A password contains 1 to 63 characters. |

##### Usage Guidelines

This command requires the support account and password to authenticate the Call Home service.

##### Example

Authenticate the Call Home service.

```text
admin:/>change call_home authenticate username=x12345678 Password=**********
Command executed successfully.
```

##### System Response

None
