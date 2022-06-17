# InvoiceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_timestamp** | **int** | Creation unix timestamp | [optional] 
**currency** | **str** | Currency used for this invoice | [optional] 
**customer_id** | **str** |  | [optional] 
**due_date_timestamp** | **int** | Invoice due date unix timestamp | [optional] 
**id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**latest_payment_timestamp** | **int** | latest payment unix timestamp | [optional] 
**locations** | [**list[Location]**](Location.md) |  | [optional] 
**month** | **int** | Month for the invoiced services unix timestamp | [optional] 
**number** | **str** | Invoice formatted number | [optional] 
**payment_status** | **str** |  | [optional] 
**sent_timestamp** | **int** | Invoice sending unix timestamp | [optional] 
**sequence_number** | **int** | Invoice yearly sequence number | [optional] 
**status** | **str** |  | [optional] 
**total_ex** | **float** | Total invoice amount without VAT | [optional] 
**total_incl** | **float** | Total Invoice amount after VAT | [optional] 
**vat** | **float** | Total VAT amount | [optional] 
**vat_comment** | **str** | VAT comment | [optional] 
**vat_legal_term** | **str** | VAT Legal Terms | [optional] 
**vat_pct** | **float** | Vat percentage | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


