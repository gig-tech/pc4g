# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username of the user | [optional] 
**firstname** | **str** | User&#39;s first name | [optional] 
**lastname** | **str** | User&#39;s last name | [optional] 
**email** | **str** | User&#39;s email | [optional] 
**emails** | **list[str]** | User&#39;s list of validated emails | [optional] 
**is_admin** | **bool** | is user admin or not | [optional] 
**iam_domain** | **str** | IAM domain | [optional] 
**vco_website** | **str** | Website | [optional] 
**vco_name** | **str** | Company Name | [optional] 
**vco_support_email** | **str** | VCO Support E-mail | [optional] 
**customers** | [**list[UserCustomer]**](UserCustomer.md) | List of the user&#39;s Customers | [optional] 
**admin_of_customers** | [**list[UserCustomer]**](UserCustomer.md) | List of the Customers which the user can administrate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


