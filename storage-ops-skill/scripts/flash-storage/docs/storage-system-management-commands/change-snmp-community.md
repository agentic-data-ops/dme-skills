# change snmp community


##### Function

The **change snmp community** command is used to change the SNMP read-only community string and read-write community string. SNMPv1 and SNMPv2c use community strings for authentication purposes. Run this command if you need to change community strings for improved system security.

##### Format

**change snmp community** read_community=? write_community=?

##### Parameters

| Parameter         | Description                                                                                                                                                                   | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| read_community=?  | Read-only community string that is used for reading device information. To obtain the security policy of the password, run the "show snmp safe_strategy" command.             | \-    |
| write_community=? | Read-write community string that is used for reading or writing device information. To obtain the security policy of the password, run the "show snmp safe_strategy" command. | \-    |

##### Usage Guidelines

When you log in for the first time, change the community name immediately, to ensure system security.

-   The format of the community name must meet the following requirements:
-   The community name is a string of 8 to 32 case-sensitive characters. You can run the "change snmp safe_strategy" command to change the length range.
-   The community name must contain special characters \` -! @ \# $ % ^ & amp;; \* ( ) - \_ = + \\ \| \[ { } \]; :'", & lt;. \> /? and spaces.
-   The community name must meet the following password complexity requirements:
-   When the password complexity requirement is common, the community name must contain at least two of the following types: lowercase letters, uppercase letters, and digits.
-   When the password complexity requirement is high, the community name must contain lower-case letters, upper-case letters, and digits.
-   The read-only community name cannot be the same as the read-write community name.

 

-   To ensure compatibility, the system reserves the support for SNMPv1 and SNMPv2c. To ensure data security, SNMPv3 is strongly recommended.
-   You can run the "change snmp safe_strategy" command to modify the read-only and read/write community policies.

##### Example

Change the SNMP read-only community string to "Storage@Public1" and the read-write community string to "Storage@Private1".

```text
admin:/>change snmp community read_community=*************** write_community=****************
Command executed successfully.
```

##### System Response

None
