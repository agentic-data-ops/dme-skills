# delete domain nis


##### Function

The **delete domain nis** command is used to initialize the configuration of an NIS domain.

##### Format

**delete domain nis**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the NIS configuration before deletion.

```text
admin:/>show domain nis

IP Address List : 10.71.129.66
Name            : nis
```

Delete the NIS configuration.

```text
admin:/>delete domain nis
WARNING: You are about to run the command for configuring the NIS domain. The NIS domain does not support encrypted transmission, which may cause security risks.
Suggestion: Before performing this operation, ensure that the risk is acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query the NIS configuration after deletion.

```text
admin:/>show domain nis

IP Address List :
Name            :
```

##### System Response

None
