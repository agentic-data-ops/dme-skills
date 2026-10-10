# help object


##### Function

The **help object** command is used to query online help information on an object, including the list of available commands, formats of those commands, descriptions for available parameters, usage guidelines, and command instances.

##### Format

**help object**

##### Parameters

| Parameter | Description                                                               | Value                                                                               |
|-----------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| object    | Name of an object that you want to query for its online help information. | To obtain the name of an object, enter help and press "Tab" for command supplement. |

##### Usage Guidelines

-   This command can display the online help information on all the commands available for an object.
-   The second segment of a command line identifies an object. For example, to query the online help information on the object of the **change cli** command, run **help cli** as the second segment is cli.
-   Press "q" to exits the online help screen.
-   To move backward or forward within help information screens, press "PageUp" or "PageDown" respectively. To move upward or downward within the same help information screen, press "↑" or "↓" respectively.
-   In online help information, an parameter in angle brackets (\<\>) is required and that in brackets (\[\]) is optional.
-   Press "h" to view the usage of the linux less command.

##### Example

To query the online help information on all the commands available for the cli object, The command output varies depending on cli interface, run the following command.

```text
admin:/>help cli
NAME
cli - CLI management commands

SYNOPSIS
show cli configuration
show cli history [N=?]
change cli [timeout=?] [capacity_mode=?] [more_enabled=?] [silent_enabled=?]
export cli history <ip=?> <user=?>   [port=?] [protocol=?]

DESCRIPTION
You can manage the configuration for the CLI(Command Line Interface) using those commands.
For example, you can view the setting of CLI, view the history commands, specify the
management console for the session, and so on.
OPTIONS
N
Type the number of most recently executed commands that you want to query.
The value ranges from 1 to 1024.

timeout
Timeout(in minutes) after which you are automatically logged out of the
system due to user inactivity or a system problem.
The value ranges from 1 to 100.

capacity_mode
Type the display option of capacity. The value is one of the following:
"automatic" : The unit of the capacity will be displayed automatically.
"precise" : The unit of the capacity will be displayed precisely.

more_enabled
Whether the more (display information page by page) function is enabled to display information.
The value is one of the following: yes or no.

silent_enabled
Allow a command to be completed by suppressing the output and not requiring user confirmation.
This is useful when there are commands in scripts.
The value is one of the following:
"yes" : Suppress the output.
"no" : Not suppress the output.

ip
Type the IP address of the FTP/SFTP server to store the history commands file or command script file.

path
Type the file path in the FTP/SFTP server to store the history commands or command script.
'/test/' indicates that script file or history file is saved in the test folder on the FTP/SFTP server. The
file name is automatically generated. '/test' indicates that script file or history file is saved in
the test file.

user
Type the name of the user that can access the FTP/SFTP server.

password
Type the password of the user.

port
Type the port number of FTP/SFTP server.
The value ranges from 1 to 65535.
The default value is "22".
If the protocol is set to "FTP", the default value will be set to "21".

protocol
File transfer protocol: FTP or SFTP, default is SFTP.
NOTE: To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP).

COMMANDS
show cli configuration
View the configuration of CLI.

show cli history [N=?]
View the lastest N history commands.
If parameter N is not specified, the CLI display all history commands.

change cli [timeout=?] [capacity_mode=?] [more_enabled=?] [silent_enabled=?]
Change the configuration of CLI.

export cli history <ip=?> <user=?>   [port=?] [protocol=?]
Export the history commands as a file to an FTP/SFTP server.

EXAMPLES
View the configuration of CLI.
admin:/>show cli configuration
More enabled(display page by page) : Yes
Silent enabled : No
Capacity Mode : Automatic
Timeout : 30 min

View the lastest 10 history commands.
admin:/>show cli history N=10
[2014-03-25 12:32:25] [admin] [192.168.30.224 52493] [idle timeout exit] [succeeded]
[2014-03-25 14:48:43] [admin] [192.168.30.224 51209] [cli startup in interactive mode] [succeeded]
[2014-03-25 14:49:25] [admin] [192.168.30.224 51209] [show lun_migration count ] [succeeded]
[2014-03-25 14:50:18] [admin] [192.168.30.224 51209] [show lun_migration general ] [succeeded]
[2014-03-25 14:53:25] [admin] [192.168.30.224 51209] [show lun_migration general source_lun_id=5 ] [succeeded]
[2014-03-25 14:53:41] [admin] [192.168.30.224 51209] [change lun_migration source_lun_id=5 speed=High ] [succeeded]
[2014-03-25 14:56:14] [admin] [192.168.30.224 51209] [delete lun_migration source_lun_id=5 ] [succeeded]
[2014-03-25 15:02:40] [admin] [192.168.30.224 51209] [show cli configuration ] [succeeded]
[2014-03-25 15:04:33] [admin] [192.168.30.224 51209] [show cli history ] [succeeded]
[2014-03-25 15:04:48] [admin] [192.168.30.224 51209] [show cli history N=5 ] [succeeded]

Change the capacity display mode to precise.
admin:/>change cli capacity_mode=precise
Command executed successfully.

Export the history CLI commands as a file to FTP server(192.168.5.98).
admin:/>export cli history ip=192.168.5.98 admin=ftp_admin password=****** path=/cli_history_1
Command executed successfully.
```

To query the online information on the show bbu command, run the following command. In this case, the second segment of show bbu identifies bbu as the object, so you can query the online help information on the object by running help bbu. The command output varies depending on a specific product.

```text
admin:/>help bbu
NAME
bbu - BBU management commands

SYNOPSIS
show bbu general [bbu_id=?]
show bbu life

DESCRIPTION
Backup Battery Unit (BBU) provides power to the system when the primary source of power is unavailable.
The BBU module is installed in the controller enclosure, to provide power-off protection function for the controller.
OPTIONS
bbu_id
ID of a BBU.
To obtain the value, run "show bbu general" without parameter.

COMMANDS
show bbu general [bbu_id=?]
View the information about BBUs.
If the parameter bbu_id is not specified, the CLI will report the information
about all BBUs.

show bbu life
View the information about BBUs life.

EXAMPLES
View the information about all BBUs.
admin:/>show bbu general
ID Health Status Running Status Current Voltage(V) Number Of Discharges
--------- ------------- -------------- ------------------ --------------------
CTE0.PSU0 Normal Online 16.1 7
CTE0.PSU1 Normal Online 16.2 5

View the information about BBUs life.
admin:/>show bbu life
ID Remaining Lifetime(days)
--------- ------------------------
CTE0.PSU0 2536
CTE0.PSU1 2535
```

##### System Response

None
