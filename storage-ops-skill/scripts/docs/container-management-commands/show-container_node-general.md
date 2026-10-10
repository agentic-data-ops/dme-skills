# show container_node general


##### Function

The **show container_node general** command is used to query container node information.

##### Format

**show container_node general**

##### Parameters

None

##### Usage Guidelines

This command cannot be used in the following situations:

1\. Run the show container_service general command. If the value of Enabled is Off, the container is not activated.

2\. The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query container node information.

```text
admin:/>show container_node general
Node  Status  Cpu Count  Memory  Local Image Repository LUN Name  Local Image Repository LUN ID  Local Image Repository Total Capacity  Local Image Repository Used Capacity  Front End Module Number  Front End Module ID List  Back End Module Number  Back End Module ID List
----  ------  ---------  ------  ------------------------------  ------------------------------  -------------------------------------  ------------------------------------  -----------------------  ------------------------  ----------------------  ----------------------
0A   Running   8         6.000GB  LOCAL_IMAGE_0                   0                                                          200.000GB                              50.000GB  2                        CTE0.A1,CTE0.A2           2                        CTE0.A6,CTE0.A7
0B   Stopped   8         6.000GB  LOCAL_IMAGE_1                   1                                                          200.000GB                              50.000GB  2                        CTE0.B1,CTE0.B2           2                        CTE0.B6,CTE0.B7
```

##### System Response

The following table describes the parameter meanings.

| Parameter                             | Meaning                                            |
|---------------------------------------|----------------------------------------------------|
| Node                                  | Name of a controller node.                         |
| Status                                | Status of the container service on the node.       |
| Cpu Count                             | Number of CPU cores used by the container service. |
| Memory                                | Memory used by the container service.              |
| Local Image Repository LUN Name       | Name of the local image LUN.                       |
| Local Image Repository LUN ID         | ID of the local image LUN.                         |
| Local Image Repository Total Capacity | Total capacity of the local image LUN.             |
| Local Image Repository Used Capacity  | Used capacity of the local image LUN.              |
| Front End Module Number               | Number of front-end interface modules.             |
| Front End Module ID List              | List of front-end interface modules.               |
| Back End Module Number                | Number of back-end interface modules.              |
| Back End Module ID List               | Back-end interface module list.                    |
