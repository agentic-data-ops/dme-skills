# change user_ssh_auth_info general


##### Function

The **change user_ssh_auth_info general** command is used to change the SSH authentication mode of a user.

##### Format

**change user_ssh_auth_info general** user_name=? auth_mode=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_name=? | Name of a user. | The value contains 1 to 64 ASCII characters, excluding double quotation marks ("). To obtain the value, run the "show user" command. |
| auth_mode=? | SSH authentication mode. | Possible values are "password" and "publickey": <br>"password": password authentication.<br>"publickey": public key authentication. |

##### Usage Guidelines

-   The public key is required only when "auth_mode" is set to "publickey".
-   Only public keys generated using the SSH-2 RSA/DSA encryption algorithm and using keys whose lengths range from 2048 to 8192 bits are supported.
-   A public key supports a maximum of 8192 characters. You are advised to copy a public key.
-   When the SSH authentication mode of a user is set to password authentication, the user cannot use the public key to authenticate SSH login. When the SSH authentication mode of a user is set to public key authentication, the user cannot use the password to authenticate SSH login.

##### Example

Change the SSH authentication mode of local account "testuser" to password authentication.

```text
admin:/>change user_ssh_auth_info general user_name=testuser auth_mode=password
Command executed successfully.
```

Change the SSH authentication mode of local account "testuser" to public key authentication. The public key is "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQPLuhb/KuHbyZi1n7yX6N3v5KG0JX8XdDnX0dfhN4yP7V+WXeqRt93YGepnsxIuvve1QCms3jxT8uy2kDMwRY6opLRV2qh5QCk1M54owpdnjwphs1g2oKyddt5iZ7xl0svZU7gfR2qP4WgGI8lBa9rA8bQlZWOd+mW6OJ80Wey37FcyZwNJpRNciTWfg2ju2sQuuvmtmum8hALQu930LbRWmTTtP33IAW/a1LMXjeEj49yhAAfL5OXVvyGMvDi3UfZJmWUZMF6eAG8joSiM50K8QuW7YUzW43t1LAXfGa7wBsp2u6HvckMXxzyr/3tanHkc1nuGZ55+Byw9mbnNn2Z root@Storage".

```text
admin:/>change user_ssh_auth_info general user_name=testuser auth_mode=publickey
CAUTION:Only public keys generated using the SSH-2 RSA/DSA encryption algorithm and using keys whose lengths range from 2048 to 8192 bits are supported.
Public key:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQPLuhb/KuHbyZi1n7yX6N3v5KG0JX8XdDnX0dfhN4yP7V+WXeqRt93YGepnsxIuvve1QCms3jxT8uy2kDMwRY6opLRV2qh5QCk1M54owpdnjwphs1g2oKyddt5iZ7xl0svZU7gfR2qP4WgGI8lBa9rA8bQlZWOd+mW6OJ80Wey37FcyZwNJpRNciTWfg2ju2sQuuvmtmum8hALQu930LbRWmTTtP33IAW/a1LMXjeEj49yhAAfL5OXVvyGMvDi3UfZJmWUZMF6eAG8joSiM50K8QuW7YUzW43t1LAXfGa7wBsp2u6HvckMXxzyr/3tanHkc1nuGZ55+Byw9mbnNn2Z root@Storage
Command executed successfully.
```

##### System Response

None
