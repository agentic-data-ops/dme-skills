# remote_device

Manage remote devices for remote replication, including link and white list configuration.

| command | function |
|---|---|
| change remote_device general | modify the name and link of remote devices. |
| change remote_device user_password | The "**change remote_device user_password**" command is used to change the user's password that logging in to remote device. |
| change remote_device white_list | modify the white list of heterogeneous disk arrays. |
| create remote_device general | create remote devices. You must create a remote device by running this command before you can effortlessly perform remote replication tasks between the storage system and remote device. |
| delete remote_device | delete a specific remote device. When the forcible deletion flag is set to "TRUE", this command can be used to forcibly delete a remote device. |
| show remote_device elink | query information about the heterogeneous links connected to a storage system. |
| show remote_device general | query information about a remote device. |
| show remote_device link | query information about existing links to a storage system. |
| show remote_device white_list | query the white list of heterogeneous disk arrays. |