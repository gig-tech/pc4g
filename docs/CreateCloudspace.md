# CreateCloudspace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Cloudspace Name | 
**location** | **str** | Cloudspace location | 
**private_network** | **str** | Private Network | [optional] [default to '192.168.103.0/24']
**vcpu_quota** | **int** | VCPU Quota. If omitted the account will be able to provision an unlimited amount of VCPUs. | [optional] 
**vdisk_space_quota** | **int** | VDisk Quota, If omitted the account will be able to provision an unlimited amount of VDisks. | [optional] 
**memory_quota** | **int** | Memory Quota, If omitted the account will be able to provision an unlimited amount of Memory. | [optional] 
**public_ip_quota** | **int** | Public IP Quota, If omitted the account will be able to provision an unlimited amount of Public IPs. | [optional] 
**firewall** | **object** | Only one of parent_cloudspace_id or external_network_id should be passed | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


