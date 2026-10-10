# delete ldap configuration


##### Function

The **delete ldap configuration** command is used to delete the configuration information on Lightweight Directory Application Protocol (LDAP) servers.

##### Format

**delete ldap configuration**

##### Parameters

None

##### Usage Guidelines

-   Running this command permanently deletes the configuration information on LDAP servers from the storage system.
-   After running this command, you cannot access the storage system using LDAP access authentication.

##### Example

To delete the configuration information on LDAP servers, run the following command:

```text
admin:/>delete ldap configuration
DANGER: You are about to delete LDAP connection settings. After this operation, all domain users can no longer log in.
Suggestion: Before performing this operation, check whether domain users need to log in.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
