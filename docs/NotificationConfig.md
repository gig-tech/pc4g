# NotificationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | notification content | [optional] 
**created_at** | **int** | when notification was created | [optional] 
**from_time** | **int** | maintenance start time | [optional] 
**issuer_id** | **str** | GIG or CE:[ce_id] or VCO:[vco_id] | [optional] 
**locations** | [**list[NotificationConfigNotificationLocation]**](NotificationConfigNotificationLocation.md) | notification locations | [optional] 
**maintenance_status** | **str** | maintenance status [&#39;PLANNED&#39;, &#39;CANCELED&#39;] | [optional] 
**notification_type** | **str** | notification type [&#39;PLANNED_MAINTENANCE&#39;, &#39;OUTAGE_WARNING&#39;, &#39;NEWS_AND_UPDATES&#39;] | [optional] 
**reason** | **str** | maintenance reason | [optional] 
**sender** | **str** | notification sender | [optional] 
**service_impact** | **str** | the impact on the service                          [&#39;NOT_APPLICABLE&#39;, &#39;NO_IMPACT&#39;, &#39;LIMITED_IMPACT&#39;, &#39;DEGRADED_SERVICE&#39;, &#39;DOWN&#39;] | [optional] 
**status** | **str** | notification status [&#39;DRAFT&#39;, &#39;SENT&#39;] | [optional] 
**till_time** | **int** | maintenance end time | [optional] 
**title** | **str** | notification title | [optional] 
**id** | **str** | Notifications identifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


