# CreateCloudspaceFirewall

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **bool** | Private cloudspace | [default to False]
**external_network_id** | **int** | Cloudspace Parent external network ID. Otherwise if empty default network will be used | [optional] 
**parent_cloudspace_id** | **str** | Parent Cloudspace ID, used for nested cloudspace, needs to be in the same location | [optional] 
**custom** | **object** | Custom firewall specs, if not passed default virtual gateway will be used with external_network_id Only one cdrom_id or image_id should be passed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


