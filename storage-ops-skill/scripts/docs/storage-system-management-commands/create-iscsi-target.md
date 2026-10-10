# create iscsi target


##### Function

The **create iscsi target** command is used to create a target over iSCSI links. Run this command if the LUN copy or remote replication is to be configured between a storage system and a remote device over iSCSI links. (The command format with local_control_id is not recommended.)

##### Format

**create iscsi target** \[ local_port_id=? local_control_id=? \] \[ remote_ip=? \] \[ chap_user=? \| chap_enabled=? \| port=? \| recovery_policy=? \] \*

**create iscsi target** \[ local_control_id=? local_port_id=? \] \[ remote_ip=? \] \[ chap_user=? \| chap_enabled=? \| port=? \| recovery_policy=? \] \*

**create iscsi target** \[ local_port_name=? \] \[ remote_ip=? \] \[ chap_user=? \| chap_enabled=? \| port=? \| recovery_policy=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_ip=? | IP address of a remote device. | - |
| local_port_id=? | ID of the employed port on an iSCSI local device. | To obtain the value, run "show port general". |
| local_control_id=? | ID of a local controller to which an iSCSI link routes. | The value is in the format of "XA", "XB", "XC", or "XD", where "X" indicates an integer from "0" to "3", for example, "0A" or "1C". |
| port=? | ID of the employed port on a remote device. | The value ranges from "1" to "65535". The default value is "3260". |
| recovery_policy=? | iSCSI link recovery policy. | The value can be: <br>"automatic": indicates automatic recovery.<br>"manual": indicates manual recovery.<br> The default value is "automatic". |
| chap_enabled=? | Switch of the Challenge Handshake Authentication Protocol (CHAP) authentication function. | The value can be "yes" or "no", where: <br>"yes": The CHAP authentication function will be enabled.<br>"no": The CHAP authentication function will be disabled.<br> The default value is "no". |
| chap_user=? | Name of a CHAP user. | The value contains 4 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |
| local_port_name=? | Logical port name. | Run the "show logical_port general" command without any parameters to obtain the value. |

##### Usage Guidelines

Running this command with "chap_enabled=?" set to "yes" will prompt you to type CHAP passwords in interactive mode. The passwords are subject to the following conditions:

-   Each password is case-sensitive and contains 12 to 16 characters.
-   Each password must be a combination of at least two of the following items:
-   Lowercase characters
-   Uppercase characters
-   Digits
-   Special characters and the following: \` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \\ \| \[ { } \] ; : ' " , \< . \> / ?
-   Each password must be different from the user name or the user name in reverse order.

##### Example

Create a target over iSCSI links, where the ID of the employed port is "CTE0.B.IOM1.P0.V4", the port number is "3260", the IP address of the remote device is "10.10.10.21", and the link recovery policy is automatic.

```text

admin:/>create iscsi target local_port_name=CTE0.B.IOM1.P0.V4 remote_ip=10.10.10.21
Command executed successfully.

```

##### System Response

None
