# User Management Commands

User management commands are used to create or delete users, change or initialize user passwords, force users to go offline, and query user information.

## role

- add role permit: add permissions to roles.
- change role general: modify basic information about roles.
- create role general: create roles.
- delete role general: The **delete role general** command to used to delete roles.
- remove role permit: remove role permissions.
- show role system: query information about system roles.

## safe_strategy

- add weak_password: add a user-defined weak password to the weak password dictionary.
- change safe_strategy: change the password and login policies of a storage system.
- change weak_password_dictionary switch: enable or disable the weak password dictionary function.
- delete weak_password: delete a weak password from the weak password dictionary.
- import weak_password_dictionary: import and overwrite a complete weak password dictionary.
- show safe_strategy: view the password and login policies of a storage system.
- show weak_password_dictionary: query weak passwords in the weak password dictionary.
- show weak_password_switch: check whether the weak password dictionary function is enabled.

## ssh

- delete ssh known_hosts: delete the server "known_hosts" file or a certain record in the file that is saved by the SSH client.
- import ssh_host_key_file: replace the public key file and private key file on the SSH server.

## sso

- change sso general: modify the single sign-on (SSO) configuration.
- show sso general: query the single sign-on (SSO) configuration.
- test sso general: test the connectivity of the single sign-on (SSO) server.

## user

- change radius configuration: modify the RADIUS configuration.
- change user: operate users, including resetting users' login passwords, changing user role IDs, forcing users offline, modifying a user's login method, modifying a user's authentication factors, and setting a specified user's password to never expire.
- change user_lock: lock a user. If you want to prevent a user from logging in to a storage system, use this command.
- change user_unlock: unlock a user. If you want to allow a restricted user to log in to a storage system, use this command.
- create user: **create user**s or user groups. You can **create user**s in different roles to manage and utilize the storage system by running this command.
- delete user: delete a user or user group. You can delete the users that are no longer required for managing and maintaining the storage system by running this command.
- show host reachable: query whether a host is reachable.
- show radius configuration: query the RADIUS configuration.
- test radius configuration: test the connectivity of the RADIUS server.

## user_mode

- change user_mode enabled: set the supported views.
- show user_mode enabled: query the supported views.
