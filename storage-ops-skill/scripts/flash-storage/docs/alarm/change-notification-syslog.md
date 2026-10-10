# change notification syslog


##### Function

The **change notification syslog** command is used to set the syslog alarm notification function.

##### Format

**change notification syslog** { enabled=? \| level=? \| { ip=? \| address=? } \| enable_alarm=? \| enable_recovery_alarm=? \| enable_event=? \| enable_send_system_name=? \| port=? \| channel=? \| function_test=? \| enable_call_home=? \| enable_security_log=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to enable the syslog alarm notification. | The value can be "yes" or "no". where: <br>"yes": enables the syslog alarm notification.<br>"no": disables the syslog alarm notification. |
| level=? | Lowest alarm severity for a storage system to report alarms. | The value can be "warning", "major", "critical", or "informational". |
| ip=? | IP address of the syslog server. | A maximum of four syslog servers can be configured. Separate the server IP addresses with commas (,). |
| enable_alarm=? | Whether to enable the syslog alarm notification. | The value can be "yes" or "no". where <br>"yes": enables the syslog alarm notification.<br>"no": disables the syslog alarm notification. |
| enable_recovery_alarm=? | Whether to enable the syslog recovery alarm notification. | The value can be "yes" or "no". where <br>"yes": enables the syslog recovery alarm notification.<br>"no": disables the syslog recovery alarm notification. |
| enable_event=? | Whether to enable the syslog event notification. | The value can be "yes" or "no". where <br>"yes": enables the syslog event notification.<br>"no": disables the syslog event notification. |
| port=? | Receiving port of the syslog server. | The value must be an integer from 1 to 65535. The default value is "514". |
| enable_send_system_name=? | Whether the storage system name is included in syslogs. | The value can be "yes" or "no". where: <br>"yes": The storage system name is included in syslogs.<br>"no": The storage system name is not included in syslogs. |
| channel=? | Sending channel of syslogs. | The value can be "UDP", "TCP", or "TLS". The default value is "UDP", where: <br>"UDP": The UDP channel is used.<br>"TCP": The TCP channel is used.<br>"TLS": The TCP encryption channel is used. |
| address=? | Syslog server address. | The value can be a domain name or an IPv4 or IPv6 address. The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| function_test=? | Whether to test the connectivity of the syslog server. | The value can be "yes" or "no". where: <br>"yes": The connectivity of the syslog server is tested.<br>"no": The connectivity of the syslog server is not tested. |
| enable_call_home | Whether to enable the call home service syslog notification. This parameter is supported in OceanStor Dorado 5000 V6 and Dorado 6000 V6 storage systems. | The value can be "yes" or "no". where <br>"yes": enables the call home service syslog notification.<br>"no": disables the call home service syslog notification. |
| enable_security_log=? | Whether to enable security log Syslog notification. | The value can be "yes" or "no", where: <br>"yes": enables security log Syslog notification.<br>"no": disables security log Syslog notification.<br> The default value is "no". |

##### Usage Guidelines

 

When changing syslog configurations for the first time, you need to set the IP address of the syslog server and the severity of alarms for which syslog notifications need to be sent.

-   After configuring the syslog alarm notification function, the system will send alarms to the specified application server or maintenance terminal. The display format is as follows:

Info Receive Time \| Facility \| Severity \| Info

2013/6/19 10:55:19 \| User \| Notice \| : \<186\>2015-06-19 10:47:10 xxx.xxx.xxx.xxx Huawei.Storage 240788 0xF00A000C Major(1): Hard disk (Controller Enclosure CTE0, slot 2, serial-number XXXXXXXX) is in single-link state.

2013/6/19 10:58:53 \| User \| Notice \| : \<188\>2015-06-19 10:57:44 xxx.xxx.xxx.xxx 241093 0xF0C90001 Warning(1): The license feature (HyperCopy) is going to expire on 2015-08-14.

-   "Info Receive Time" is the time for receiving information, "Facility" is the information source, "Severity" is the information severity, "Info" is the information content. The first three parameters are defined by the syslog server. The fields vary with the parsing tool.

-   The value of parameter "Info" is fixed. The first part of parameter "Info" indicates the process that sends messages. It varies with syslog protocol version and can be left blank. The information in \<\> is the prefix of the syslog protocol and indicates the severity and source of the message. It is defined by the syslog protocol.

-   "Info" contains the following alarm information:
-   Time when the alarm is generated, for example, 2015-06-19 10:47:10.
-   IP address, IP address of the storage device about which the alarm is generated.
-   System name, system name of the storage device about which the alarm is generated.
-   Alarm SN, SN of the alarm in the storage device. The value ranges from 1 to 4,294,967,295, for example, 240788.
-   Alarm ID, a certain type of alarm, expressed in the hexadecimal format, for example, 0xF00A000C.
-   Alarm severity. Alarm severities include info, warning, major, and critical.
-   Alarm type. Alarm types include event (0), fault alarm (1), recovery alarm (2), operation log (3), and internal event (6). Currently, only event (0), fault alarm (1), and recovery alarm (2) support syslog.
-   Alarm information, for example, "The license feature (HyperCopy) is going to expire on 2015-08-14."

-   The parameter IP and address are exclusive from each other. The parameter IP can be an IPv4 or IPv6 address. The parameter address can be a domain name or an IP address (IPv4 or IPv6).

-   If function_test is yes, the test is performed but the syslog configuration is not modified after the command is executed.

-   If enable_call_home=yes, the system automatically sends file messages returned by the array to the cloud to the syslog server.

-   If enable_security_log=yes, the system automatically sends security logs to the Syslog server.

##### Example

Enable the syslog alarm notification function, set the syslog server IP address to "192.168.8.211" and lowest alarm severity for a storage system to report alarms to "critical", enable the alarm syslog notification function, and write the storage system name to syslogs.

```text

admin:/>change notification syslog enabled=yes ip=192.168.8.211 level=critical enable_alarm=yes enable_send_system_name=yes
Command executed successfully.

```

Test the connectivity of the syslog server. The IP address of the server is "192.168.8.211", the receiving port number is "514", and the sending channel is "UDP".

```text
admin:/>change notification syslog address=192.168.8.211 port=514 channel=UDP function_test=yes
Command executed successfully.

```

##### System Response

None
