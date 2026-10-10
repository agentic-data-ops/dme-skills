# user

Manage device users, including creation, lock/unlock, and RADIUS authentication.

| command | function |
|---|---|
| change radius configuration | modify the RADIUS configuration. |
| change user | operate users, including resetting users' login passwords, changing user role IDs, forcing users offline, modifying a user's login method, modifying a user's authentication factors, and setting a specified user's password to never expire. |
| change user_lock | lock a user. If you want to prevent a user from logging in to a storage system, use this command. |
| change user_unlock | unlock a user. If you want to allow a restricted user to log in to a storage system, use this command. |
| create user | **create user**s or user groups. You can **create user**s in different roles to manage and utilize the storage system by running this command. |
| delete user | delete a user or user group. You can delete the users that are no longer required for managing and maintaining the storage system by running this command. |
| show host reachable | query whether a host is reachable. |
| show radius configuration | query the RADIUS configuration. |
| test radius configuration | test the connectivity of the RADIUS server. |