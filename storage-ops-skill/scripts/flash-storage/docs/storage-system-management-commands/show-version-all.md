# show version all


##### Function

The **show version all** command is used to query the version information on the storage system's controllers, expansion modules, and BBUs.

##### Format

**show version all**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

To query the version information on the storage system's controllers, expansion modules, and BBUs, run the following command. The command output varies depending on a specific product. The command output varies depending on a specific product.

```text
admin:/>show version all

Product Version : VXXXRXXXCXX
Controller:

Controller       : 0A
Software Version : 2.50.02.100
PCB Version      : STL1SPCA01H VER.A
SES Version      : 6.03T11
BMC Version      : 6.03T11
Logic Version    : 230T01
BIOS Version     : 06.03.05T02
Disk Version     : 0:2358,1:56347
--------------------------------------
Controller       : 0B
Software Version : 2.50.02.100
PCB Version      : STL1SPCA01H VER.A
SES Version      : 6.03T11
BMC Version      : 6.03T11
Logic Version    : 230T01
BIOS Version     : 06.03.05T02
Disk Version     : 0:2358,1:56347
Expansion Module:

ID        Logic Version  PCB Version     SES Version
--------  -------------  --------------  -----------
DAE000.A  120T01         STL1DESA VER.B  10.03T27
DAE000.B  120T01         STL1DESA VER.B  10.03T27
BBU:

ID       Firmware Version
-------  ----------------
ENG0.A0  1.18T03
ENG0.A1  1.18T03
ENG0.B0  1.18T03
ENG0.B1  1.18T03
```

##### System Response

None
