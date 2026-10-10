# snmp

Manage SNMP settings, including communities, users, versions, and ports.

Manage SNMP settings, including communities, users, versions, and ports.

| command | function |
|---|---|
| add snmp cache | add an SNMP cache object. No cache object is added by default. |
| add snmp usm | add a USM user. |
| change snmp cache | change the interval of updating the cache data of an SNMP cache object. |
| change snmp community | change the SNMP read-only community string and read-write community string. SNMPv1 and SNMPv2c use community strings for authentication purposes. Run this command if you need to change community strings for improved system security. |
| change snmp port | set the port number of the SNMP service. |
| change snmp safe_strategy | change the security policy of the SNMP service. |
| change snmp usm | modify the configuration of a USM user. |
| change snmp version | set the status of the SNMPv1 and SNMPv2c protocols and the switch status of the SNMP unique controller enclosure ID function. |
| delete snmp usm | delete a USM user. |
| remove snmp cache | remove an SNMP cache object. |
| show snmp cache | show the current SNMP cache object. |
| show snmp context_name | query the Simple Network Management Protocol (SNMP) context name of the storage system. |
| show snmp engineid | query the SNMP controller enclosure ID of a controller. |
| show snmp port | query the port number of the SNMP service. |
| show snmp safe_strategy | query the security policy of the SNMP service. |
| show snmp usm | query the configuration of the USM user. |
| show snmp version | check the status of the SNMPv1 and SNMPv2c protocols as well as status of the SNMP unique controller enclosure ID switch. |