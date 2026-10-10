# show remote_support agreement


##### Function

The **show remote_support agreement** command is used to query the letter of authorization and its status.

##### Format

**show remote_support agreement** \[ content=? \]

##### Parameters

| Parameter | Description                                                     | Value               |
|-----------|-----------------------------------------------------------------|---------------------|
| content   | Whether to display the contents of the letter of authorization. | The value is "yes". |

##### Usage Guidelines

This command is used to query the letter of authorization and its status, including its contents, status of the electronic signature, and its photo upload status.

##### Example

Query the letter of authorization and its status.

```text
admin:/>show remote_support agreement content=yes
Authorization Status                 : Signed
Upload Status                        : Imported
Letter of Authorization for eService : Purposes of Authorization:
To ensure secure, stable, and efficient operation of Huawei devices and eliminate hidden problems, Huawei OceanStor eService (eService for short) sends the customer's network data (excluding service data) related to Huawei devices by email or over HTTPS to Huawei and provides the proactive alarm reporting and log collection services after [Customer] deploys eService.
[Customer] hereby authorizes Huawei to deploy eService and process the following network data:
1. Contact information of [Customer]'s operation and maintenance personnel, including names, telephone numbers, email addresses, and company or corporation names.
2. Alarm information and alarm clearance information, including alarm IDs, names, sequence numbers, severities, generation time, details, and handling measures.
3. Huawei device software and hardware configuration data, including device models, names, serial numbers, versions and management IP addresses.
4. Huawei device inspection reports, including device operating status, configurations, health inspection results (excluding customer service data and private data).
5. Huawei device logs, including key operational events, device electronic labels, operational logs of disks and devices, operating configurations, operating status information (excluding customer service data and private data).
6. Huawei device performance logs, including performance indicators (excluding customer service data and private data).
Proactive fault handling: Huawei can contact authorized contacts in working and non-working hours (around the clock) after receiving alarms.
Disposal of Customer Network Data After Processing: Archived within the authorization period and deleted permanently after the authorization expires.
Authorization Start Date: Start date of device warranty/maintenance service.
Authorization End Date: End date of device warranty/maintenance service.
```

Query the letter of authorization status.

```text
admin:/>show remote_support agreement

Authorization Status : Signed
Upload Status        : Imported
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                                      |
|----------------------|----------------------------------------------|
| Authorization Status | Signing status of a letter of authorization. |
| Upload Status        | Upload status of a letter of authorization.  |
