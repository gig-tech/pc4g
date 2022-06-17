# pc4g.CustomersApi

All URIs are relative to the base URL of pc4g.Configuration(HOST)

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cloudspace_anti_affinity_group**](CustomersApi.md#add_cloudspace_anti_affinity_group) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups | 
[**add_cloudspace_external_network**](CustomersApi.md#add_cloudspace_external_network) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/external-network | 
[**add_cloudspace_network_route**](CustomersApi.md#add_cloudspace_network_route) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/routes | 
[**add_customer_location**](CustomersApi.md#add_customer_location) | **POST** /customers/{customer_id}/locations | 
[**add_remote_cloudspace**](CustomersApi.md#add_remote_cloudspace) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/connected-cloudspaces | 
[**add_support_access**](CustomersApi.md#add_support_access) | **POST** /customers/{customer_id}/support-access | 
[**add_virtual_machine_anti_affinity_groups**](CustomersApi.md#add_virtual_machine_anti_affinity_groups) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups/{group_id}/vms | 
[**attach_disk_virtual_machine**](CustomersApi.md#attach_disk_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/disks | 
[**attach_external_networks_virtual_machine**](CustomersApi.md#attach_external_networks_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/external-nics | 
[**attach_virtual_machine_cdrom**](CustomersApi.md#attach_virtual_machine_cdrom) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/cdrom-images | 
[**change_agent_status**](CustomersApi.md#change_agent_status) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/agent | 
[**clone_disk_snapshot**](CustomersApi.md#clone_disk_snapshot) | **POST** /customers/{customer_id}/locations/{location}/disks/{disk_id}/snapshots/{snapshot_id}/clone | 
[**compliance_scan**](CustomersApi.md#compliance_scan) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/compliance-scan | 
[**connect_objectspace**](CustomersApi.md#connect_objectspace) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/objectspaces | 
[**create_bucket**](CustomersApi.md#create_bucket) | **POST** /customers/{customer_id}/objectspaces/{objectspace_id}/buckets/{bucket_id} | 
[**create_cloudspace**](CustomersApi.md#create_cloudspace) | **POST** /customers/{customer_id}/cloudspaces | 
[**create_cloudspace_note**](CustomersApi.md#create_cloudspace_note) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/notes | 
[**create_customer**](CustomersApi.md#create_customer) | **POST** /customers | 
[**create_customer_cdrom_image**](CustomersApi.md#create_customer_cdrom_image) | **POST** /customers/{customer_id}/locations/{location}/cdrom-images | 
[**create_customer_certificate**](CustomersApi.md#create_customer_certificate) | **POST** /customers/{customer_id}/certificates/ssl | 
[**create_customer_image**](CustomersApi.md#create_customer_image) | **POST** /customers/{customer_id}/locations/{location}/vm-images | 
[**create_disk**](CustomersApi.md#create_disk) | **POST** /customers/{customer_id}/locations/{location}/disks | 
[**create_disk_note**](CustomersApi.md#create_disk_note) | **POST** /customers/{customer_id}/locations/{location}/disks/{disk_id}/notes | 
[**create_objectspace**](CustomersApi.md#create_objectspace) | **POST** /customers/{customer_id}/objectspaces | 
[**create_objectspace_note**](CustomersApi.md#create_objectspace_note) | **POST** /customers/{customer_id}/objectspaces/{objectspace_id}/notes | 
[**create_portforward**](CustomersApi.md#create_portforward) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/portforwards | 
[**create_role**](CustomersApi.md#create_role) | **POST** /customers/{customer_id}/roles | 
[**create_template_from_vm**](CustomersApi.md#create_template_from_vm) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/template | 
[**create_virtual_machine**](CustomersApi.md#create_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms | 
[**create_virtual_machine_from_s3**](CustomersApi.md#create_virtual_machine_from_s3) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/import-s3 | 
[**create_virtual_machine_note**](CustomersApi.md#create_virtual_machine_note) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/notes | 
[**delete_anti_affinity_group_virtual_machine**](CustomersApi.md#delete_anti_affinity_group_virtual_machine) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups/{group_id}/vms/{vm_id} | 
[**delete_bucket**](CustomersApi.md#delete_bucket) | **DELETE** /customers/{customer_id}/objectspaces/{objectspace_id}/buckets/{bucket_id} | 
[**delete_certificate**](CustomersApi.md#delete_certificate) | **DELETE** /customers/{customer_id}/certificates/ssl/{domain} | 
[**delete_cloudspace**](CustomersApi.md#delete_cloudspace) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id} | 
[**delete_cloudspace_anti_affinity_group**](CustomersApi.md#delete_cloudspace_anti_affinity_group) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups/{group_id} | 
[**delete_cloudspace_note**](CustomersApi.md#delete_cloudspace_note) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/notes/{note_id} | 
[**delete_cloudspace_proxy_config**](CustomersApi.md#delete_cloudspace_proxy_config) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/proxy-server | 
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /customers/{customer_id} | 
[**delete_customer_cdrom_image**](CustomersApi.md#delete_customer_cdrom_image) | **DELETE** /customers/{customer_id}/locations/{location}/cdrom-images/{cdrom_id} | 
[**delete_customer_image**](CustomersApi.md#delete_customer_image) | **DELETE** /customers/{customer_id}/locations/{location}/vm-images/{image_id} | 
[**delete_disk**](CustomersApi.md#delete_disk) | **DELETE** /customers/{customer_id}/locations/{location}/disks/{disk_id} | 
[**delete_disk_note**](CustomersApi.md#delete_disk_note) | **DELETE** /customers/{customer_id}/locations/{location}/disks/{disk_id}/notes/{note_id} | 
[**delete_disk_snapshot**](CustomersApi.md#delete_disk_snapshot) | **DELETE** /customers/{customer_id}/locations/{location}/disks/{disk_id}/snapshots/{snapshot_id} | 
[**delete_file**](CustomersApi.md#delete_file) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/file | 
[**delete_objectspace**](CustomersApi.md#delete_objectspace) | **DELETE** /customers/{customer_id}/objectspaces/{objectspace_id} | 
[**delete_objectspace_note**](CustomersApi.md#delete_objectspace_note) | **DELETE** /customers/{customer_id}/objectspaces/{objectspace_id}/notes/{note_id} | 
[**delete_portforward**](CustomersApi.md#delete_portforward) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/portforwards/{portforward_id} | 
[**delete_remote_cloudspace_connection**](CustomersApi.md#delete_remote_cloudspace_connection) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/connected-cloudspaces/{connected_cloudspace_id} | 
[**delete_role**](CustomersApi.md#delete_role) | **DELETE** /customers/{customer_id}/roles/{role_id} | 
[**delete_support_access**](CustomersApi.md#delete_support_access) | **DELETE** /customers/{customer_id}/support-access | 
[**delete_virtual_machine**](CustomersApi.md#delete_virtual_machine) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id} | 
[**delete_virtual_machine_note**](CustomersApi.md#delete_virtual_machine_note) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/notes/{note_id} | 
[**detach_disk_virtual_machine**](CustomersApi.md#detach_disk_virtual_machine) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/disks/{disk_id} | 
[**detach_external_networks_virtual_machine**](CustomersApi.md#detach_external_networks_virtual_machine) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/external-nics/{external_ip_address} | 
[**detach_virtual_machine_cdrom**](CustomersApi.md#detach_virtual_machine_cdrom) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/cdrom-images/{cdrom_id} | 
[**disable_cloudspace**](CustomersApi.md#disable_cloudspace) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/disable | 
[**disable_customer**](CustomersApi.md#disable_customer) | **PUT** /customers/{customer_id}/disable | 
[**disconnect_objectspace**](CustomersApi.md#disconnect_objectspace) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/objectspaces | 
[**enable_cloudspace**](CustomersApi.md#enable_cloudspace) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/enable | 
[**enable_customer**](CustomersApi.md#enable_customer) | **PUT** /customers/{customer_id}/enable | 
[**execute_command**](CustomersApi.md#execute_command) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/exec | 
[**export_virtual_machine_to_s3**](CustomersApi.md#export_virtual_machine_to_s3) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/export-s3 | 
[**expose_disk**](CustomersApi.md#expose_disk) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/exposed-disks | 
[**get_agent_status**](CustomersApi.md#get_agent_status) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/agent | 
[**get_bucket**](CustomersApi.md#get_bucket) | **GET** /customers/{customer_id}/objectspaces/{objectspace_id}/buckets/{bucket_id} | 
[**get_certificate_info**](CustomersApi.md#get_certificate_info) | **GET** /customers/{customer_id}/certificates/ssl/{domain} | 
[**get_cloudspace_anti_affinity_group**](CustomersApi.md#get_cloudspace_anti_affinity_group) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups/{group_id} | 
[**get_cloudspace_consumption**](CustomersApi.md#get_cloudspace_consumption) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/consumption | 
[**get_cloudspace_consumption_series**](CustomersApi.md#get_cloudspace_consumption_series) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/consumption/series | 
[**get_cloudspace_default_gateway**](CustomersApi.md#get_cloudspace_default_gateway) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/default-gateway | 
[**get_cloudspace_info**](CustomersApi.md#get_cloudspace_info) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id} | 
[**get_cloudspace_nested_cloudspaces**](CustomersApi.md#get_cloudspace_nested_cloudspaces) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/nested-cloudspaces | 
[**get_cloudspace_notes**](CustomersApi.md#get_cloudspace_notes) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/notes | 
[**get_cloudspace_proxy_config**](CustomersApi.md#get_cloudspace_proxy_config) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/proxy-server | 
[**get_cloudspace_stats**](CustomersApi.md#get_cloudspace_stats) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/statistics | 
[**get_currencies**](CustomersApi.md#get_currencies) | **GET** /customers/currencies | 
[**get_customer_compliance_overview**](CustomersApi.md#get_customer_compliance_overview) | **GET** /customers/compliance | 
[**get_customer_compliance_report**](CustomersApi.md#get_customer_compliance_report) | **GET** /customers/{customer_id}/compliance | 
[**get_customer_compliance_series**](CustomersApi.md#get_customer_compliance_series) | **GET** /customers/{customer_id}/statistics/license-compliance | 
[**get_customer_consumption**](CustomersApi.md#get_customer_consumption) | **GET** /customers/{customer_id}/locations/{location}/consumption | 
[**get_customer_consumption_series**](CustomersApi.md#get_customer_consumption_series) | **GET** /customers/{customer_id}/locations/{location}/consumption/series | 
[**get_customer_info**](CustomersApi.md#get_customer_info) | **GET** /customers/{customer_id} | 
[**get_customer_invoice_pdf**](CustomersApi.md#get_customer_invoice_pdf) | **GET** /customers/{customer_id}/invoices/{invoice_id}/pdf | 
[**get_customer_location_capacity**](CustomersApi.md#get_customer_location_capacity) | **GET** /customers/{customer_id}/locations/{location}/capacity | 
[**get_customer_location_datacenter**](CustomersApi.md#get_customer_location_datacenter) | **GET** /customers/{customer_id}/locations/{location}/datacenter | 
[**get_customer_location_pricing**](CustomersApi.md#get_customer_location_pricing) | **GET** /customers/{customer_id}/locations/{location}/prices | 
[**get_customer_pricing**](CustomersApi.md#get_customer_pricing) | **GET** /customers/{customer_id}/prices | 
[**get_disk_consumption**](CustomersApi.md#get_disk_consumption) | **GET** /customers/{customer_id}/locations/{location}/disks/{disk_id}/consumption | 
[**get_disk_consumption_series**](CustomersApi.md#get_disk_consumption_series) | **GET** /customers/{customer_id}/locations/{location}/disks/{disk_id}/consumption/series | 
[**get_disk_info**](CustomersApi.md#get_disk_info) | **GET** /customers/{customer_id}/locations/{location}/disks/{disk_id} | 
[**get_disk_notes**](CustomersApi.md#get_disk_notes) | **GET** /customers/{customer_id}/locations/{location}/disks/{disk_id}/notes | 
[**get_disk_snapshot**](CustomersApi.md#get_disk_snapshot) | **GET** /customers/{customer_id}/locations/{location}/disks/{disk_id}/snapshots/{snapshot_id} | 
[**get_external_network**](CustomersApi.md#get_external_network) | **GET** /customers/{customer_id}/locations/{location}/external-networks/{external_network_id} | 
[**get_external_networks_virtual_machine**](CustomersApi.md#get_external_networks_virtual_machine) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/external-nics/{external_ip_address} | 
[**get_image**](CustomersApi.md#get_image) | **GET** /customers/{customer_id}/locations/{location}/vm-images/{image_id} | 
[**get_objectspace**](CustomersApi.md#get_objectspace) | **GET** /customers/{customer_id}/objectspaces/{objectspace_id} | 
[**get_objectspace_notes**](CustomersApi.md#get_objectspace_notes) | **GET** /customers/{customer_id}/objectspaces/{objectspace_id}/notes | 
[**get_os_names**](CustomersApi.md#get_os_names) | **GET** /customers/vm-images/os-names | 
[**get_os_types**](CustomersApi.md#get_os_types) | **GET** /customers/vm-images/os-types | 
[**get_portforward**](CustomersApi.md#get_portforward) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/portforwards/{portforward_id} | 
[**get_remote_cloudspace_connection_status**](CustomersApi.md#get_remote_cloudspace_connection_status) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/connected-cloudspaces/{connected_cloudspace_id} | 
[**get_role**](CustomersApi.md#get_role) | **GET** /customers/{customer_id}/roles/{role_id} | 
[**get_support_access**](CustomersApi.md#get_support_access) | **GET** /customers/{customer_id}/support-access | 
[**get_virtual_machine_anti_affinity_groups**](CustomersApi.md#get_virtual_machine_anti_affinity_groups) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups/{group_id}/vms | 
[**get_virtual_machine_console**](CustomersApi.md#get_virtual_machine_console) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/console | 
[**get_virtual_machine_consumption**](CustomersApi.md#get_virtual_machine_consumption) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/consumption | 
[**get_virtual_machine_consumption_series**](CustomersApi.md#get_virtual_machine_consumption_series) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/consumption/series | 
[**get_virtual_machine_info**](CustomersApi.md#get_virtual_machine_info) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id} | 
[**get_virtual_machine_notes**](CustomersApi.md#get_virtual_machine_notes) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/notes | 
[**get_virtual_machine_stats**](CustomersApi.md#get_virtual_machine_stats) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/statistics | 
[**get_vm_price_simulation**](CustomersApi.md#get_vm_price_simulation) | **GET** /customers/{customer_id}/locations/{location}/vm-price-simulation | 
[**get_vmcdrom_info**](CustomersApi.md#get_vmcdrom_info) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/cdrom-images/{cdrom_id} | 
[**list_buckets**](CustomersApi.md#list_buckets) | **GET** /customers/{customer_id}/objectspaces/{objectspace_id}/buckets | 
[**list_cloudspace_anti_affinity_groups**](CustomersApi.md#list_cloudspace_anti_affinity_groups) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups | 
[**list_cloudspace_external_networks**](CustomersApi.md#list_cloudspace_external_networks) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/external-network | 
[**list_cloudspace_network_routes**](CustomersApi.md#list_cloudspace_network_routes) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/routes | 
[**list_cloudspace_objectspaces**](CustomersApi.md#list_cloudspace_objectspaces) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/objectspaces | 
[**list_cloudspace_virtual_machines**](CustomersApi.md#list_cloudspace_virtual_machines) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms | 
[**list_cloudspaces**](CustomersApi.md#list_cloudspaces) | **GET** /customers/{customer_id}/cloudspaces | 
[**list_customer_cdrom_images**](CustomersApi.md#list_customer_cdrom_images) | **GET** /customers/{customer_id}/locations/{location}/cdrom-images | 
[**list_customer_certificates**](CustomersApi.md#list_customer_certificates) | **GET** /customers/{customer_id}/certificates/ssl | 
[**list_customer_images**](CustomersApi.md#list_customer_images) | **GET** /customers/{customer_id}/locations/{location}/vm-images | 
[**list_customer_invoices**](CustomersApi.md#list_customer_invoices) | **GET** /customers/{customer_id}/invoices | 
[**list_customer_locations**](CustomersApi.md#list_customer_locations) | **GET** /customers/{customer_id}/locations | 
[**list_customers**](CustomersApi.md#list_customers) | **GET** /customers | 
[**list_disk_snapshots**](CustomersApi.md#list_disk_snapshots) | **GET** /customers/{customer_id}/locations/{location}/disks/{disk_id}/snapshots | 
[**list_disks**](CustomersApi.md#list_disks) | **GET** /customers/{customer_id}/locations/{location}/disks | 
[**list_disks_virtual_machine**](CustomersApi.md#list_disks_virtual_machine) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/disks | 
[**list_exposed_disks**](CustomersApi.md#list_exposed_disks) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/exposed-disks | 
[**list_external_network_interface_models**](CustomersApi.md#list_external_network_interface_models) | **GET** /customers/external-network-interfaces/models | 
[**list_external_networks**](CustomersApi.md#list_external_networks) | **GET** /customers/{customer_id}/locations/{location}/external-networks | 
[**list_external_networks_virtual_machine**](CustomersApi.md#list_external_networks_virtual_machine) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/external-nics | 
[**list_objectspaces**](CustomersApi.md#list_objectspaces) | **GET** /customers/{customer_id}/objectspaces | 
[**list_portforwards**](CustomersApi.md#list_portforwards) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/portforwards | 
[**list_remote_cloudspace_connections**](CustomersApi.md#list_remote_cloudspace_connections) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/connected-cloudspaces | 
[**list_role_grants**](CustomersApi.md#list_role_grants) | **GET** /customers/{customer_id}/roles/{role_id}/grants | 
[**list_roles**](CustomersApi.md#list_roles) | **GET** /customers/{customer_id}/roles | 
[**list_roles_on_cloudspace**](CustomersApi.md#list_roles_on_cloudspace) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/granted-roles | 
[**list_roles_on_customer**](CustomersApi.md#list_roles_on_customer) | **GET** /customers/{customer_id}/granted-roles | 
[**list_roles_on_location**](CustomersApi.md#list_roles_on_location) | **GET** /customers/{customer_id}/locations/{location}/granted-roles | 
[**list_roles_on_virtual_machine**](CustomersApi.md#list_roles_on_virtual_machine) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/granted-roles | 
[**list_virtual_machine_cdro_ms**](CustomersApi.md#list_virtual_machine_cdro_ms) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/cdrom-images | 
[**move_virtual_machine**](CustomersApi.md#move_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/move | 
[**pause_virtual_machine**](CustomersApi.md#pause_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/pause | 
[**read_file**](CustomersApi.md#read_file) | **GET** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/file | 
[**reboot_virtual_machine**](CustomersApi.md#reboot_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/reboot | 
[**recycle_bin**](CustomersApi.md#recycle_bin) | **GET** /customers/{customer_id}/recycle-bin | 
[**remove_cloudspace_external_network**](CustomersApi.md#remove_cloudspace_external_network) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/external-network | 
[**remove_cloudspace_network_route**](CustomersApi.md#remove_cloudspace_network_route) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/routes | 
[**remove_customer_location**](CustomersApi.md#remove_customer_location) | **DELETE** /customers/{customer_id}/locations/{location} | 
[**rename_cloudspace**](CustomersApi.md#rename_cloudspace) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/name | 
[**rename_virtual_machine**](CustomersApi.md#rename_virtual_machine) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/name | 
[**reset_bucket_limit**](CustomersApi.md#reset_bucket_limit) | **PUT** /customers/{customer_id}/objectspaces/{objectspace_id}/{bucket_id}/reset-limit | 
[**reset_objectspace**](CustomersApi.md#reset_objectspace) | **PUT** /customers/{customer_id}/objectspaces/{objectspace_id}/reset | 
[**reset_virtual_machine**](CustomersApi.md#reset_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/reset | 
[**resize_disk**](CustomersApi.md#resize_disk) | **PUT** /customers/{customer_id}/locations/{location}/disks/{disk_id}/size | 
[**resize_virtual_machine**](CustomersApi.md#resize_virtual_machine) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/size | 
[**restore_bucket**](CustomersApi.md#restore_bucket) | **PUT** /customers/{customer_id}/objectspaces/{objectspace_id}/{bucket_id}/restore | 
[**restore_cloudspace**](CustomersApi.md#restore_cloudspace) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/restore | 
[**restore_customer_cdrom_image**](CustomersApi.md#restore_customer_cdrom_image) | **PUT** /customers/{customer_id}/locations/{location}/cdrom-images/{cdrom_id}/restore | 
[**restore_customer_image**](CustomersApi.md#restore_customer_image) | **PUT** /customers/{customer_id}/locations/{location}/vm-images/{image_id}/restore | 
[**restore_disk**](CustomersApi.md#restore_disk) | **PUT** /customers/{customer_id}/locations/{location}/disks/{disk_id}/restore | 
[**restore_objectspace**](CustomersApi.md#restore_objectspace) | **PUT** /customers/{customer_id}/objectspaces/{objectspace_id}/restore | 
[**restore_virtual_machine**](CustomersApi.md#restore_virtual_machine) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/restore | 
[**resume_virtual_machine**](CustomersApi.md#resume_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/resume | 
[**rollback_disk_snapshot**](CustomersApi.md#rollback_disk_snapshot) | **POST** /customers/{customer_id}/locations/{location}/disks/{disk_id}/snapshots/{snapshot_id}/rollback | 
[**self_create_customer**](CustomersApi.md#self_create_customer) | **POST** /customers/self-creation | 
[**set_bucket_limit**](CustomersApi.md#set_bucket_limit) | **PUT** /customers/{customer_id}/objectspaces/{objectspace_id}/{bucket_id}/bucket-limit | 
[**set_cloudspace_default_gateway**](CustomersApi.md#set_cloudspace_default_gateway) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/default-gateway | 
[**set_cloudspace_proxy_config**](CustomersApi.md#set_cloudspace_proxy_config) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/proxy-server | 
[**set_disk_limit_io**](CustomersApi.md#set_disk_limit_io) | **PUT** /customers/{customer_id}/locations/{location}/disks/{disk_id}/limitio | 
[**start_virtual_machine**](CustomersApi.md#start_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/start | 
[**stop_virtual_machine**](CustomersApi.md#stop_virtual_machine) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/stop | 
[**take_disk_snapshot**](CustomersApi.md#take_disk_snapshot) | **POST** /customers/{customer_id}/locations/{location}/disks/{disk_id}/snapshots | 
[**unexpose_disk**](CustomersApi.md#unexpose_disk) | **DELETE** /customers/{customer_id}/cloudspaces/{cloudspace_id}/exposed-disks/{disk_id} | 
[**upate_objectspace_note**](CustomersApi.md#upate_objectspace_note) | **PUT** /customers/{customer_id}/objectspaces/{objectspace_id}/notes/{note_id} | 
[**update_certificate**](CustomersApi.md#update_certificate) | **PUT** /customers/{customer_id}/certificates/ssl/{domain} | 
[**update_cloudspace_anti_affinity_group**](CustomersApi.md#update_cloudspace_anti_affinity_group) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/anti-affinity-groups/{group_id} | 
[**update_cloudspace_external_network_metric**](CustomersApi.md#update_cloudspace_external_network_metric) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/external-network | 
[**update_cloudspace_note**](CustomersApi.md#update_cloudspace_note) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/notes/{note_id} | 
[**update_cloudspace_quota**](CustomersApi.md#update_cloudspace_quota) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/quota | 
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /customers/{customer_id} | 
[**update_disk_model**](CustomersApi.md#update_disk_model) | **PUT** /customers/{customer_id}/locations/{location}/disks/{disk_id}/model | 
[**update_disk_note**](CustomersApi.md#update_disk_note) | **PUT** /customers/{customer_id}/locations/{location}/disks/{disk_id}/notes/{note_id} | 
[**update_network_interface_model**](CustomersApi.md#update_network_interface_model) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/network-interfaces/{mac_address}/model | 
[**update_portforward**](CustomersApi.md#update_portforward) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/portforwards/{portforward_id} | 
[**update_role**](CustomersApi.md#update_role) | **PUT** /customers/{customer_id}/roles/{role_id} | 
[**update_role_grants**](CustomersApi.md#update_role_grants) | **PUT** /customers/{customer_id}/roles/{role_id}/grants | 
[**update_virtual_machine_description**](CustomersApi.md#update_virtual_machine_description) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/description | 
[**update_virtual_machine_note**](CustomersApi.md#update_virtual_machine_note) | **PUT** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/notes/{note_id} | 
[**write_file**](CustomersApi.md#write_file) | **POST** /customers/{customer_id}/cloudspaces/{cloudspace_id}/vms/{vm_id}/file | 


# **add_cloudspace_anti_affinity_group**
> SuccessModel add_cloudspace_anti_affinity_group(customer_id, cloudspace_id, spread, group_id, x_fields=x_fields)



Add anti-affinity group

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
spread = 56 # int | Amount of physical nodes to spread vms over. Set to -1 for infinite spread
group_id = 'group_id_example' # str | Name of the group
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.add_cloudspace_anti_affinity_group(customer_id, cloudspace_id, spread, group_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->add_cloudspace_anti_affinity_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **spread** | **int**| Amount of physical nodes to spread vms over. Set to -1 for infinite spread | 
 **group_id** | **str**| Name of the group | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cloudspace_external_network**
> SuccessModel add_cloudspace_external_network(customer_id, cloudspace_id, metric=metric, external_network_ip=external_network_ip, external_network_type=external_network_type, external_network_id=external_network_id, x_fields=x_fields)



Add cloudspace external network

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
metric = 56 # int | external network metric(low priority is highest priority)if omitted lowest priority is used (optional)
external_network_ip = 'external_network_ip_example' # str | optional ip address inside the external network (optional)
external_network_type = 'external' # str | optional, default is 'external'. 'cloudspace' connects to an existing network (optional) (default to external)
external_network_id = 56 # int | optional id to take ip address from.If omited will search for available network (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.add_cloudspace_external_network(customer_id, cloudspace_id, metric=metric, external_network_ip=external_network_ip, external_network_type=external_network_type, external_network_id=external_network_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->add_cloudspace_external_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **metric** | **int**| external network metric(low priority is highest priority)if omitted lowest priority is used | [optional] 
 **external_network_ip** | **str**| optional ip address inside the external network | [optional] 
 **external_network_type** | **str**| optional, default is &#39;external&#39;. &#39;cloudspace&#39; connects to an existing network | [optional] [default to external]
 **external_network_id** | **int**| optional id to take ip address from.If omited will search for available network | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cloudspace_network_route**
> SuccessModel add_cloudspace_network_route(customer_id, cloudspace_id, destination, gateway, table=table, metric=metric, x_fields=x_fields)



Add extra route to network

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
destination = 'destination_example' # str | Destination network to route
gateway = 'gateway_example' # str | Gateway to route desination over
table = 56 # int | routing table to add route to (optional)
metric = 56 # int | external network metric(low priority is highest priority) if omitted lowest priority is used (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.add_cloudspace_network_route(customer_id, cloudspace_id, destination, gateway, table=table, metric=metric, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->add_cloudspace_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **destination** | **str**| Destination network to route | 
 **gateway** | **str**| Gateway to route desination over | 
 **table** | **int**| routing table to add route to | [optional] 
 **metric** | **int**| external network metric(low priority is highest priority) if omitted lowest priority is used | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_location**
> add_customer_location(customer_id, payload)



Add location for Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
payload = pc4g.LocationPricing() # LocationPricing | 

try:
    api_instance.add_customer_location(customer_id, payload)
except ApiException as e:
    print("Exception when calling CustomersApi->add_customer_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **payload** | [**LocationPricing**](LocationPricing.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_remote_cloudspace**
> add_remote_cloudspace(customer_id, cloudspace_id, connected_cloudspace_id)



Add remote connection to cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
connected_cloudspace_id = 'connected_cloudspace_id_example' # str | Cloudspace to connect to

try:
    api_instance.add_remote_cloudspace(customer_id, cloudspace_id, connected_cloudspace_id)
except ApiException as e:
    print("Exception when calling CustomersApi->add_remote_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **connected_cloudspace_id** | **str**| Cloudspace to connect to | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_support_access**
> add_support_access(customer_id)



add support organization access

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.add_support_access(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->add_support_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_virtual_machine_anti_affinity_groups**
> SuccessModel add_virtual_machine_anti_affinity_groups(customer_id, cloudspace_id, group_id, vm_id, x_fields=x_fields)



Add virtual machine anti-affinity group

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
group_id = 'group_id_example' # str | 
vm_id = 56 # int | VM ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.add_virtual_machine_anti_affinity_groups(customer_id, cloudspace_id, group_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->add_virtual_machine_anti_affinity_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **group_id** | **str**|  | 
 **vm_id** | **int**| VM ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_disk_virtual_machine**
> SuccessModel attach_disk_virtual_machine(customer_id, cloudspace_id, vm_id, disk_id, x_fields=x_fields)



Attach a disk on virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
disk_id = 56 # int | Disk ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.attach_disk_virtual_machine(customer_id, cloudspace_id, vm_id, disk_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->attach_disk_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **disk_id** | **int**| Disk ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_external_networks_virtual_machine**
> SuccessModel attach_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, external_network_id, external_network_ip=external_network_ip, model=model, x_fields=x_fields)



Attach external network (NIC) to virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
external_network_id = 56 # int | External network ID
external_network_ip = 'external_network_ip_example' # str | IP Address to reserve for this Machine's NIC (optional)
model = 'model_example' # str | the new NIC model (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.attach_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, external_network_id, external_network_ip=external_network_ip, model=model, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->attach_external_networks_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **external_network_id** | **int**| External network ID | 
 **external_network_ip** | **str**| IP Address to reserve for this Machine&#39;s NIC | [optional] 
 **model** | **str**| the new NIC model | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_virtual_machine_cdrom**
> SuccessModel attach_virtual_machine_cdrom(customer_id, cloudspace_id, vm_id, cdrom_id, x_fields=x_fields)



Attach CDROM image to Virtual Machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
cdrom_id = 56 # int | ID of the CD-ROM image
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.attach_virtual_machine_cdrom(customer_id, cloudspace_id, vm_id, cdrom_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->attach_virtual_machine_cdrom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **cdrom_id** | **int**| ID of the CD-ROM image | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_agent_status**
> SuccessModel change_agent_status(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)



Enable/Disable virtual machine agent

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
payload = pc4g.ChangeAgentStatus() # ChangeAgentStatus | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.change_agent_status(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->change_agent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **payload** | [**ChangeAgentStatus**](ChangeAgentStatus.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_disk_snapshot**
> CloneDiskSnapshot clone_disk_snapshot(customer_id, location, disk_id, snapshot_id, name, description=description, all_vm_disks=all_vm_disks, x_fields=x_fields)



Clone Disk snapshot

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
snapshot_id = 'snapshot_id_example' # str | 
name = 'name_example' # str | New disk name
description = 'description_example' # str | New disk Description (optional)
all_vm_disks = true # bool | Create clones of all snapshots that were created in the same action (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.clone_disk_snapshot(customer_id, location, disk_id, snapshot_id, name, description=description, all_vm_disks=all_vm_disks, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->clone_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **snapshot_id** | **str**|  | 
 **name** | **str**| New disk name | 
 **description** | **str**| New disk Description | [optional] 
 **all_vm_disks** | **bool**| Create clones of all snapshots that were created in the same action | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloneDiskSnapshot**](CloneDiskSnapshot.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_scan**
> SuccessModel compliance_scan(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



execute octopus scanner in the virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.compliance_scan(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->compliance_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_objectspace**
> SuccessModel connect_objectspace(customer_id, cloudspace_id, objectspace_id, x_fields=x_fields)



Connecting objectspace to a cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | The objectspace id to be added to the cloudspace
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.connect_objectspace(customer_id, cloudspace_id, objectspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->connect_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **objectspace_id** | **str**| The objectspace id to be added to the cloudspace | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bucket**
> SuccessModel create_bucket(customer_id, objectspace_id, bucket_id, limit=limit, x_fields=x_fields)



Create a bucket

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
bucket_id = 'bucket_id_example' # str | 
limit = 2000 # int | limit of IOPS for the bucket (optional) (default to 2000)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_bucket(customer_id, objectspace_id, bucket_id, limit=limit, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **bucket_id** | **str**|  | 
 **limit** | **int**| limit of IOPS for the bucket | [optional] [default to 2000]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloudspace**
> CloudspaceIDModel create_cloudspace(customer_id, payload, x_fields=x_fields)



Create cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
payload = pc4g.CreateCloudspace() # CreateCloudspace | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_cloudspace(customer_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **payload** | [**CreateCloudspace**](CreateCloudspace.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceIDModel**](CloudspaceIDModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloudspace_note**
> SuccessModel create_cloudspace_note(customer_id, cloudspace_id, payload, x_fields=x_fields)



Create cloudspace note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_cloudspace_note(customer_id, cloudspace_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_cloudspace_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer**
> str create_customer(payload)



Add new customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
payload = pc4g.CustomerCreate() # CustomerCreate | 

try:
    api_response = api_instance.create_customer(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CustomerCreate**](CustomerCreate.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_cdrom_image**
> CDROMIdModel create_customer_cdrom_image(customer_id, location, name, url, os_type, os_name, x_fields=x_fields)



Create CDROM image

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
name = 'name_example' # str | CD-ROM Name
url = 'url_example' # str | CD-ROM image URL
os_type = 'os_type_example' # str | OS Type
os_name = 'os_name_example' # str | Specific name of the Operating system
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_customer_cdrom_image(customer_id, location, name, url, os_type, os_name, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer_cdrom_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **name** | **str**| CD-ROM Name | 
 **url** | **str**| CD-ROM image URL | 
 **os_type** | **str**| OS Type | 
 **os_name** | **str**| Specific name of the Operating system | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CDROMIdModel**](CDROMIdModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_certificate**
> Certificates create_customer_certificate(customer_id, payload, x_fields=x_fields)



Create certificate

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
payload = pc4g.CreateCustomerCertificate() # CreateCustomerCertificate | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_customer_certificate(customer_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **payload** | [**CreateCustomerCertificate**](CreateCustomerCertificate.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Certificates**](Certificates.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_image**
> ImageID create_customer_image(customer_id, location, name, url, memory, boot_disk_size, boot_type, os_name, os_type, add_memory=add_memory, add_vcpu=add_vcpu, remove_vcpu=remove_vcpu, add_disk=add_disk, remove_disk=remove_disk, add_nic=add_nic, remove_nic=remove_nic, username=username, password=password, user_data=user_data, tags=tags, md5_sum=md5_sum, x_fields=x_fields)



Create customer Image

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
name = 'name_example' # str | Image Name
url = 'url_example' # str | Image URL
memory = 56 # int | Minimum required memory for this image
boot_disk_size = 56 # int | Minimum Boot disk size
boot_type = 'boot_type_example' # str | Boot Type
os_name = 'os_name_example' # str | Specific name of the Operating system
os_type = 'os_type_example' # str | OS Type
add_memory = true # bool | This image supports hot memory addition (optional) (default to true)
add_vcpu = true # bool | This image supports hot VCPU addition (optional) (default to true)
remove_vcpu = true # bool | This image supports hot VCPU removal (optional) (default to true)
add_disk = true # bool | This image supports hot disk addition (optional) (default to true)
remove_disk = true # bool | This image supports hot disk removal (optional) (default to true)
add_nic = true # bool | This image supports hot NIC addition (optional) (default to true)
remove_nic = true # bool | This image supports hot NIC removal (optional) (default to true)
username = 'username_example' # str | Optional os username for the image (optional)
password = 'password_example' # str | Optional os password for the image (optional)
user_data = 'user_data_example' # str | Userdata about image such as product key (optional)
tags = 'tags_example' # str | tags for the image (optional)
md5_sum = 'md5_sum_example' # str | optional md5sum to check validity of the image (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_customer_image(customer_id, location, name, url, memory, boot_disk_size, boot_type, os_name, os_type, add_memory=add_memory, add_vcpu=add_vcpu, remove_vcpu=remove_vcpu, add_disk=add_disk, remove_disk=remove_disk, add_nic=add_nic, remove_nic=remove_nic, username=username, password=password, user_data=user_data, tags=tags, md5_sum=md5_sum, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **name** | **str**| Image Name | 
 **url** | **str**| Image URL | 
 **memory** | **int**| Minimum required memory for this image | 
 **boot_disk_size** | **int**| Minimum Boot disk size | 
 **boot_type** | **str**| Boot Type | 
 **os_name** | **str**| Specific name of the Operating system | 
 **os_type** | **str**| OS Type | 
 **add_memory** | **bool**| This image supports hot memory addition | [optional] [default to true]
 **add_vcpu** | **bool**| This image supports hot VCPU addition | [optional] [default to true]
 **remove_vcpu** | **bool**| This image supports hot VCPU removal | [optional] [default to true]
 **add_disk** | **bool**| This image supports hot disk addition | [optional] [default to true]
 **remove_disk** | **bool**| This image supports hot disk removal | [optional] [default to true]
 **add_nic** | **bool**| This image supports hot NIC addition | [optional] [default to true]
 **remove_nic** | **bool**| This image supports hot NIC removal | [optional] [default to true]
 **username** | **str**| Optional os username for the image | [optional] 
 **password** | **str**| Optional os password for the image | [optional] 
 **user_data** | **str**| Userdata about image such as product key | [optional] 
 **tags** | **str**| tags for the image | [optional] 
 **md5_sum** | **str**| optional md5sum to check validity of the image | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ImageID**](ImageID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_disk**
> DiskIdModel create_disk(customer_id, location, disk_name, description, disk_size, iops=iops, disk_type=disk_type, vm_id=vm_id, x_fields=x_fields)



Create disk

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_name = 'disk_name_example' # str | Name of disk to create
description = 'description_example' # str | Disk description
disk_size = 56 # int | Disk size in GB
iops = 2000 # int | Disk IOPS (optional) (default to 2000)
disk_type = 'DATA' # str | Disk Type (optional) (default to DATA)
vm_id = 'vm_id_example' # str | (Optional) VM ID of Virtual Machine to attach to (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_disk(customer_id, location, disk_name, description, disk_size, iops=iops, disk_type=disk_type, vm_id=vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_name** | **str**| Name of disk to create | 
 **description** | **str**| Disk description | 
 **disk_size** | **int**| Disk size in GB | 
 **iops** | **int**| Disk IOPS | [optional] [default to 2000]
 **disk_type** | **str**| Disk Type | [optional] [default to DATA]
 **vm_id** | **str**| (Optional) VM ID of Virtual Machine to attach to | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**DiskIdModel**](DiskIdModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_disk_note**
> SuccessModel create_disk_note(customer_id, location, disk_id, payload, x_fields=x_fields)



Create disk note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_disk_note(customer_id, location, disk_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_disk_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_objectspace**
> CreateObjectspaceModel create_objectspace(customer_id, name, location, x_fields=x_fields)



Create an object space

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
name = 'name_example' # str | Name of the Object Space
location = 'location_example' # str | The location of the objectspace
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_objectspace(customer_id, name, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **name** | **str**| Name of the Object Space | 
 **location** | **str**| The location of the objectspace | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CreateObjectspaceModel**](CreateObjectspaceModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_objectspace_note**
> SuccessModel create_objectspace_note(customer_id, objectspace_id, payload, x_fields=x_fields)



Create objectspace note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_objectspace_note(customer_id, objectspace_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_objectspace_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portforward**
> PortforwardID create_portforward(customer_id, cloudspace_id, local_port, public_port, protocol, vm_id=vm_id, nested_cs_id=nested_cs_id, x_fields=x_fields)



Create cloudspace port forward

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
local_port = 56 # int | Local port
public_port = 56 # int | Public port
protocol = 'protocol_example' # str | Protocol for port forwarding
vm_id = 56 # int | Virtual Machine ID (optional)
nested_cs_id = 56 # int | Nested Cloudspace ID (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_portforward(customer_id, cloudspace_id, local_port, public_port, protocol, vm_id=vm_id, nested_cs_id=nested_cs_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_portforward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **local_port** | **int**| Local port | 
 **public_port** | **int**| Public port | 
 **protocol** | **str**| Protocol for port forwarding | 
 **vm_id** | **int**| Virtual Machine ID | [optional] 
 **nested_cs_id** | **int**| Nested Cloudspace ID | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**PortforwardID**](PortforwardID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> CustomerRole create_role(customer_id, payload, x_fields=x_fields)



Create customer role

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
payload = pc4g.CustomerRoleCreate() # CustomerRoleCreate | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_role(customer_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **payload** | [**CustomerRoleCreate**](CustomerRoleCreate.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRole**](CustomerRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_from_vm**
> CreateTemplateModel create_template_from_vm(customer_id, cloudspace_id, vm_id, template_name, callback_url=callback_url, x_fields=x_fields)



Create a template from virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
template_name = 'template_name_example' # str | Name of the template to be created
callback_url = 'callback_url_example' # str | Callback url so that the API caller can be notified If this is specified the G8 will not send an email itself upon completion. (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_template_from_vm(customer_id, cloudspace_id, vm_id, template_name, callback_url=callback_url, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_template_from_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **template_name** | **str**| Name of the template to be created | 
 **callback_url** | **str**| Callback url so that the API caller can be notified If this is specified the G8 will not send an email itself upon completion. | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CreateTemplateModel**](CreateTemplateModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_machine**
> VmIdModel create_virtual_machine(customer_id, cloudspace_id, name, description, vcpus, memory, data_disks=data_disks, private_ip=private_ip, user_data=user_data, image_id=image_id, disk_size=disk_size, cdrom_id=cdrom_id, boot_disk_id=boot_disk_id, os_type=os_type, os_name=os_name, enable_vm_agent=enable_vm_agent, snapshot_id=snapshot_id, all_vm_disks=all_vm_disks, boot_type=boot_type, payload=payload, x_fields=x_fields)



Create VirtualMachine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
name = 'name_example' # str | Virtual Machine name
description = 'description_example' # str | Virtual Machine Description
vcpus = 56 # int | Number of cpu to assign to machine
memory = 56 # int | Amount of memory to assign to machine in MiB
data_disks = [[]] # list[int] | List of extra disk sizes (optional) (default to [])
private_ip = 'private_ip_example' # str | Private ip of the machine (optional)
user_data = 'user_data_example' # str | Custom user data in a YAML string for cloud-init (optional)
image_id = 56 # int | Id of the specific image (optional)
disk_size = 56 # int | Boot Disk Size in GiB (optional)
cdrom_id = 56 # int | CD-ROM Image ID (optional)
boot_disk_id = 56 # int | BOOT Disk ID for creating with snapshot or with existing disk (optional)
os_type = 'os_type_example' # str | OS type used on machine (optional)
os_name = 'os_name_example' # str | Image OS name (optional)
enable_vm_agent = false # bool | whether or not to enable agent communication (optional) (default to false)
snapshot_id = 'snapshot_id_example' # str | Boot Disk Snapshot ID (optional)
all_vm_disks = false # bool | Create clones of all snapshots that were created in the same snapshot (optional) (default to false)
boot_type = 'bios' # str | Boot type to be used when creating from snapshot or creating empty machine (optional) (default to bios)
payload = pc4g.VMCreateExtentions() # VMCreateExtentions |  (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_virtual_machine(customer_id, cloudspace_id, name, description, vcpus, memory, data_disks=data_disks, private_ip=private_ip, user_data=user_data, image_id=image_id, disk_size=disk_size, cdrom_id=cdrom_id, boot_disk_id=boot_disk_id, os_type=os_type, os_name=os_name, enable_vm_agent=enable_vm_agent, snapshot_id=snapshot_id, all_vm_disks=all_vm_disks, boot_type=boot_type, payload=payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **name** | **str**| Virtual Machine name | 
 **description** | **str**| Virtual Machine Description | 
 **vcpus** | **int**| Number of cpu to assign to machine | 
 **memory** | **int**| Amount of memory to assign to machine in MiB | 
 **data_disks** | [**list[int]**](int.md)| List of extra disk sizes | [optional] [default to []]
 **private_ip** | **str**| Private ip of the machine | [optional] 
 **user_data** | **str**| Custom user data in a YAML string for cloud-init | [optional] 
 **image_id** | **int**| Id of the specific image | [optional] 
 **disk_size** | **int**| Boot Disk Size in GiB | [optional] 
 **cdrom_id** | **int**| CD-ROM Image ID | [optional] 
 **boot_disk_id** | **int**| BOOT Disk ID for creating with snapshot or with existing disk | [optional] 
 **os_type** | **str**| OS type used on machine | [optional] 
 **os_name** | **str**| Image OS name | [optional] 
 **enable_vm_agent** | **bool**| whether or not to enable agent communication | [optional] [default to false]
 **snapshot_id** | **str**| Boot Disk Snapshot ID | [optional] 
 **all_vm_disks** | **bool**| Create clones of all snapshots that were created in the same snapshot | [optional] [default to false]
 **boot_type** | **str**| Boot type to be used when creating from snapshot or creating empty machine | [optional] [default to bios]
 **payload** | [**VMCreateExtentions**](VMCreateExtentions.md)|  | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmIdModel**](VmIdModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_machine_from_s3**
> VmIdModel create_virtual_machine_from_s3(customer_id, cloudspace_id, link, key, secret, region, bucket, object_name, name, description, vcpus, memory, os_name, private_ip=private_ip, strict=strict, boot_type=boot_type, os_type=os_type, x_fields=x_fields)



Import and create virtual machine from s3

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
link = 'link_example' # str | S3 server link
key = 'key_example' # str | access key to the server
secret = 'secret_example' # str | secret to access the server
region = 'region_example' # str | region of the s3 server
bucket = 'bucket_example' # str | Name of the bucket
object_name = 'object_name_example' # str | Name of the stored object in the bucker
name = 'name_example' # str | Virtual Machine name
description = 'description_example' # str | Virtual Machine Description
vcpus = 56 # int | Number of cpu to assign to machine
memory = 56 # int | Amount of memory to assign to machine in MiB
os_name = 'Linux - other' # str | Image OS name (default to Linux - other)
private_ip = 'private_ip_example' # str | Private ip of the machine (optional)
strict = false # bool | Import vm as close as possible to original hw (optional) (default to false)
boot_type = 'bios' # str | Boot type (optional) (default to bios)
os_type = 'Linux' # str | Image OS type (optional) (default to Linux)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_virtual_machine_from_s3(customer_id, cloudspace_id, link, key, secret, region, bucket, object_name, name, description, vcpus, memory, os_name, private_ip=private_ip, strict=strict, boot_type=boot_type, os_type=os_type, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_virtual_machine_from_s3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **link** | **str**| S3 server link | 
 **key** | **str**| access key to the server | 
 **secret** | **str**| secret to access the server | 
 **region** | **str**| region of the s3 server | 
 **bucket** | **str**| Name of the bucket | 
 **object_name** | **str**| Name of the stored object in the bucker | 
 **name** | **str**| Virtual Machine name | 
 **description** | **str**| Virtual Machine Description | 
 **vcpus** | **int**| Number of cpu to assign to machine | 
 **memory** | **int**| Amount of memory to assign to machine in MiB | 
 **os_name** | **str**| Image OS name | [default to Linux - other]
 **private_ip** | **str**| Private ip of the machine | [optional] 
 **strict** | **bool**| Import vm as close as possible to original hw | [optional] [default to false]
 **boot_type** | **str**| Boot type | [optional] [default to bios]
 **os_type** | **str**| Image OS type | [optional] [default to Linux]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmIdModel**](VmIdModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_machine_note**
> SuccessModel create_virtual_machine_note(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)



Create virtual machine note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_virtual_machine_note(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_virtual_machine_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_anti_affinity_group_virtual_machine**
> SuccessModel delete_anti_affinity_group_virtual_machine(customer_id, cloudspace_id, group_id, vm_id, x_fields=x_fields)



Delete anti-affinity group virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
group_id = 'group_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_anti_affinity_group_virtual_machine(customer_id, cloudspace_id, group_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_anti_affinity_group_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **group_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> SuccessModel delete_bucket(customer_id, objectspace_id, bucket_id, permanently=permanently, x_fields=x_fields)



Delete a given bucket

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
bucket_id = 'bucket_id_example' # str | 
permanently = false # bool | permanently deleting your bucket (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_bucket(customer_id, objectspace_id, bucket_id, permanently=permanently, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **bucket_id** | **str**|  | 
 **permanently** | **bool**| permanently deleting your bucket | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate**
> delete_certificate(customer_id, domain)



Delete certificate

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
domain = 'domain_example' # str | 

try:
    api_instance.delete_certificate(customer_id, domain)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **domain** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloudspace**
> SuccessModel delete_cloudspace(customer_id, cloudspace_id, permanently=permanently, reason=reason, x_fields=x_fields)



Delete cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
permanently = false # bool | Delete permanently (optional) (default to false)
reason = '' # str | Reason for deleting (optional) (default to )
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_cloudspace(customer_id, cloudspace_id, permanently=permanently, reason=reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **permanently** | **bool**| Delete permanently | [optional] [default to false]
 **reason** | **str**| Reason for deleting | [optional] [default to ]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloudspace_anti_affinity_group**
> SuccessModel delete_cloudspace_anti_affinity_group(customer_id, cloudspace_id, group_id, x_fields=x_fields)



Delete anti-affinity group

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
group_id = 'group_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_cloudspace_anti_affinity_group(customer_id, cloudspace_id, group_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_cloudspace_anti_affinity_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **group_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloudspace_note**
> SuccessModel delete_cloudspace_note(customer_id, cloudspace_id, note_id, x_fields=x_fields)



Delete cloudspace note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
note_id = 'note_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_cloudspace_note(customer_id, cloudspace_id, note_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_cloudspace_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **note_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloudspace_proxy_config**
> delete_cloudspace_proxy_config(customer_id, cloudspace_id)



Delete cloudspace proxy config

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 

try:
    api_instance.delete_cloudspace_proxy_config(customer_id, cloudspace_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_cloudspace_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(customer_id, reason=reason, recursive_delete=recursive_delete)



Delete customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
reason = 'reason_example' # str | Reason for deletion (Optional) (optional)
recursive_delete = false # bool | Delete the customer recursively (optional) (default to false)

try:
    api_instance.delete_customer(customer_id, reason=reason, recursive_delete=recursive_delete)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **reason** | **str**| Reason for deletion (Optional) | [optional] 
 **recursive_delete** | **bool**| Delete the customer recursively | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_cdrom_image**
> SuccessModel delete_customer_cdrom_image(customer_id, location, cdrom_id, permanently=permanently, x_fields=x_fields)



Delete customer CDROM images

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
cdrom_id = 56 # int | 
permanently = false # bool | If set to False, the CD-ROM will be moved to the Recycle Bin, if set to True the CD-ROM will be permanently deleted. (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_customer_cdrom_image(customer_id, location, cdrom_id, permanently=permanently, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_customer_cdrom_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **cdrom_id** | **int**|  | 
 **permanently** | **bool**| If set to False, the CD-ROM will be moved to the Recycle Bin, if set to True the CD-ROM will be permanently deleted. | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_image**
> SuccessModel delete_customer_image(customer_id, location, image_id, permanently=permanently, x_fields=x_fields)



Delete customer Image

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
image_id = 56 # int | 
permanently = false # bool | If set to False, the Image will be moved to the Recycle Bin, if set to True the Image will be permanently deleted. (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_customer_image(customer_id, location, image_id, permanently=permanently, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_customer_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **image_id** | **int**|  | 
 **permanently** | **bool**| If set to False, the Image will be moved to the Recycle Bin, if set to True the Image will be permanently deleted. | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disk**
> SuccessModel delete_disk(customer_id, location, disk_id, detach=detach, permanently=permanently, x_fields=x_fields)



Delete disk

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
detach = true # bool | Detach from Virtual Machine first (optional) (default to true)
permanently = false # bool | If set to False, the disk will be moved to the Recycle Bin, if set to True the disk will be permanently deleted. (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_disk(customer_id, location, disk_id, detach=detach, permanently=permanently, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **detach** | **bool**| Detach from Virtual Machine first | [optional] [default to true]
 **permanently** | **bool**| If set to False, the disk will be moved to the Recycle Bin, if set to True the disk will be permanently deleted. | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disk_note**
> SuccessModel delete_disk_note(customer_id, location, disk_id, note_id, x_fields=x_fields)



Delete disk note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
note_id = 'note_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_disk_note(customer_id, location, disk_id, note_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_disk_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **note_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disk_snapshot**
> SuccessModel delete_disk_snapshot(customer_id, location, disk_id, snapshot_id, x_fields=x_fields)



Delete Disk snapshot

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
snapshot_id = 'snapshot_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_disk_snapshot(customer_id, location, disk_id, snapshot_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **snapshot_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> SuccessModel delete_file(customer_id, cloudspace_id, vm_id, filepath, x_fields=x_fields)



Delete file from virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
filepath = 'filepath_example' # str | filepath to read from
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_file(customer_id, cloudspace_id, vm_id, filepath, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **filepath** | **str**| filepath to read from | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_objectspace**
> SuccessModel delete_objectspace(customer_id, objectspace_id, permanently=permanently, x_fields=x_fields)



Delete an objectspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
permanently = false # bool | deleting the object space permanently or not (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_objectspace(customer_id, objectspace_id, permanently=permanently, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **permanently** | **bool**| deleting the object space permanently or not | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_objectspace_note**
> SuccessModel delete_objectspace_note(customer_id, objectspace_id, note_id, x_fields=x_fields)



Delete objectspace note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
note_id = 'note_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_objectspace_note(customer_id, objectspace_id, note_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_objectspace_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **note_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portforward**
> Portforwards delete_portforward(customer_id, cloudspace_id, portforward_id, x_fields=x_fields)



Delete cloudspace port forward

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
portforward_id = 'portforward_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_portforward(customer_id, cloudspace_id, portforward_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_portforward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **portforward_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Portforwards**](Portforwards.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_cloudspace_connection**
> delete_remote_cloudspace_connection(customer_id, cloudspace_id, connected_cloudspace_id)



Delete remote connection to cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
connected_cloudspace_id = 'connected_cloudspace_id_example' # str | 

try:
    api_instance.delete_remote_cloudspace_connection(customer_id, cloudspace_id, connected_cloudspace_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_remote_cloudspace_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **connected_cloudspace_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(customer_id, role_id)



Delete customer role

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    api_instance.delete_role(customer_id, role_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_support_access**
> delete_support_access(customer_id)



delete support organization access

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.delete_support_access(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_support_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_machine**
> SuccessModel delete_virtual_machine(customer_id, cloudspace_id, vm_id, permanently=permanently, x_fields=x_fields)



Delete Virtual Machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
permanently = false # bool | If set to False, the virtual machine will be moved to the Recycle Bin, if set to True the virtual machine will be permanently deleted. (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_virtual_machine(customer_id, cloudspace_id, vm_id, permanently=permanently, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **permanently** | **bool**| If set to False, the virtual machine will be moved to the Recycle Bin, if set to True the virtual machine will be permanently deleted. | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_machine_note**
> SuccessModel delete_virtual_machine_note(customer_id, cloudspace_id, vm_id, note_id, x_fields=x_fields)



Delete virtual machine note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
note_id = 'note_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_virtual_machine_note(customer_id, cloudspace_id, vm_id, note_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_virtual_machine_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **note_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_disk_virtual_machine**
> SuccessModel detach_disk_virtual_machine(customer_id, cloudspace_id, vm_id, disk_id, x_fields=x_fields)



Detach a disk on virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
disk_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.detach_disk_virtual_machine(customer_id, cloudspace_id, vm_id, disk_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->detach_disk_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **disk_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_external_networks_virtual_machine**
> SuccessModel detach_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, external_ip_address, x_fields=x_fields)



Detach external network (NIC) from virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
external_ip_address = 'external_ip_address_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.detach_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, external_ip_address, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->detach_external_networks_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **external_ip_address** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_virtual_machine_cdrom**
> SuccessModel detach_virtual_machine_cdrom(customer_id, cloudspace_id, vm_id, cdrom_id, x_fields=x_fields)



Detach CDROM image from virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
cdrom_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.detach_virtual_machine_cdrom(customer_id, cloudspace_id, vm_id, cdrom_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->detach_virtual_machine_cdrom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **cdrom_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_cloudspace**
> SuccessModel disable_cloudspace(customer_id, cloudspace_id, reason=reason, x_fields=x_fields)



Disable cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reason = '' # str | Reason for disabling (optional) (default to )
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.disable_cloudspace(customer_id, cloudspace_id, reason=reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->disable_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reason** | **str**| Reason for disabling | [optional] [default to ]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_customer**
> disable_customer(customer_id)



Disable Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.disable_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->disable_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_objectspace**
> SuccessModel disconnect_objectspace(customer_id, cloudspace_id, objectspace_id, x_fields=x_fields)



Disconnecting objectspace from a cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | The objectspace id to be added to the cloudspace
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.disconnect_objectspace(customer_id, cloudspace_id, objectspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->disconnect_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **objectspace_id** | **str**| The objectspace id to be added to the cloudspace | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_cloudspace**
> SuccessModel enable_cloudspace(customer_id, cloudspace_id, reason=reason, x_fields=x_fields)



Enable cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reason = '' # str | Reason for enabling (optional) (default to )
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.enable_cloudspace(customer_id, cloudspace_id, reason=reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->enable_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reason** | **str**| Reason for enabling | [optional] [default to ]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_customer**
> enable_customer(customer_id)



Enable Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.enable_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->enable_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_command**
> VmCommandModel execute_command(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)



Execute command inside virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
payload = pc4g.VMExecuteModel() # VMExecuteModel | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.execute_command(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->execute_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **payload** | [**VMExecuteModel**](VMExecuteModel.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmCommandModel**](VmCommandModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_virtual_machine_to_s3**
> SuccessModel export_virtual_machine_to_s3(customer_id, cloudspace_id, vm_id, link, key, secret, region, bucket, object_name, x_fields=x_fields)



Export virtual machine to s3

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
link = 'link_example' # str | S3 server link
key = 'key_example' # str | access key to the server
secret = 'secret_example' # str | secret to access the server
region = 'region_example' # str | region of the s3 server
bucket = 'bucket_example' # str | Name of the bucket
object_name = 'object_name_example' # str | Name of the stored object in the bucker
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.export_virtual_machine_to_s3(customer_id, cloudspace_id, vm_id, link, key, secret, region, bucket, object_name, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->export_virtual_machine_to_s3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **link** | **str**| S3 server link | 
 **key** | **str**| access key to the server | 
 **secret** | **str**| secret to access the server | 
 **region** | **str**| region of the s3 server | 
 **bucket** | **str**| Name of the bucket | 
 **object_name** | **str**| Name of the stored object in the bucker | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expose_disk**
> ExposeDiskModel expose_disk(customer_id, cloudspace_id, disk_id, iops=iops, max_connections=max_connections, x_fields=x_fields)



Expose a disk via the cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
disk_id = 56 # int | Disk ID
iops = 56 # int | Total number of iops for the disk to be exposed (optional)
max_connections = 56 # int | Maximum number of concurrent connections (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.expose_disk(customer_id, cloudspace_id, disk_id, iops=iops, max_connections=max_connections, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->expose_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **disk_id** | **int**| Disk ID | 
 **iops** | **int**| Total number of iops for the disk to be exposed | [optional] 
 **max_connections** | **int**| Maximum number of concurrent connections | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExposeDiskModel**](ExposeDiskModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_status**
> GetAgentStatus get_agent_status(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Get virtual machine agent status

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_agent_status(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_agent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**GetAgentStatus**](GetAgentStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucket**
> GetBucketModel get_bucket(customer_id, objectspace_id, bucket_id, x_fields=x_fields)



Get the information for a bucket

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
bucket_id = 'bucket_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_bucket(customer_id, objectspace_id, bucket_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **bucket_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**GetBucketModel**](GetBucketModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_info**
> Certificate get_certificate_info(customer_id, domain, x_fields=x_fields)



Get certificate information

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
domain = 'domain_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_certificate_info(customer_id, domain, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_certificate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **domain** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_anti_affinity_group**
> GetCloudspaceAntiAffinityGroupModel get_cloudspace_anti_affinity_group(customer_id, cloudspace_id, group_id, x_fields=x_fields)



Get anti-affinity group

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
group_id = 'group_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_anti_affinity_group(customer_id, cloudspace_id, group_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_anti_affinity_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **group_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**GetCloudspaceAntiAffinityGroupModel**](GetCloudspaceAntiAffinityGroupModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_consumption**
> CloudspaceConsumptionModel get_cloudspace_consumption(customer_id, cloudspace_id, end, start, x_fields=x_fields)



Get cloudspace resource consumption

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_consumption(customer_id, cloudspace_id, end, start, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_consumption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceConsumptionModel**](CloudspaceConsumptionModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_consumption_series**
> CloudspaceConsumptionTsModel get_cloudspace_consumption_series(customer_id, cloudspace_id, end, start, step, units, x_fields=x_fields)



Get cloudspace resource consumption timeseries

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
step = 'step_example' # str | Step between each time point from [\"15m\", \"30m\", \"60m\", \"24h\"]
units = ['units_example'] # list[str] | List of units to include Possible values: [\"su\", \"tu\", \"nu\", \"vcu\", \"mu\", \"piu\", \"wu\"]
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_consumption_series(customer_id, cloudspace_id, end, start, step, units, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_consumption_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **step** | **str**| Step between each time point from [\&quot;15m\&quot;, \&quot;30m\&quot;, \&quot;60m\&quot;, \&quot;24h\&quot;] | 
 **units** | [**list[str]**](str.md)| List of units to include Possible values: [\&quot;su\&quot;, \&quot;tu\&quot;, \&quot;nu\&quot;, \&quot;vcu\&quot;, \&quot;mu\&quot;, \&quot;piu\&quot;, \&quot;wu\&quot;] | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceConsumptionTsModel**](CloudspaceConsumptionTsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_default_gateway**
> DefaultGateway get_cloudspace_default_gateway(customer_id, cloudspace_id, x_fields=x_fields)



Get cloudspace default gateway

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_default_gateway(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_default_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**DefaultGateway**](DefaultGateway.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_info**
> CloudspaceInfoModel get_cloudspace_info(customer_id, cloudspace_id, x_fields=x_fields)



Get cloudspace info

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_info(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceInfoModel**](CloudspaceInfoModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_nested_cloudspaces**
> CloudspaceChildren get_cloudspace_nested_cloudspaces(customer_id, cloudspace_id, x_fields=x_fields)



Get nested cloudspaces

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_nested_cloudspaces(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_nested_cloudspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceChildren**](CloudspaceChildren.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_notes**
> ResourceNotes get_cloudspace_notes(customer_id, cloudspace_id, x_fields=x_fields)



Get cloudspace notes

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_notes(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ResourceNotes**](ResourceNotes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_proxy_config**
> CloudspaceProxyConfigModel get_cloudspace_proxy_config(customer_id, cloudspace_id, x_fields=x_fields)



Get cloudspace proxy config

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_proxy_config(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceProxyConfigModel**](CloudspaceProxyConfigModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloudspace_stats**
> CloudspaceStatsModel get_cloudspace_stats(customer_id, cloudspace_id, end, start, include=include, x_fields=x_fields)



Get cloudspace statistics

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
include = ['include_example'] # list[str] | Cloudspace stats to include. If empty all stats will be returned Fields should be one of the parameters of series object in output model [cpu, network, memory, vdisk_latency,  vdisk_capacity, vdisk_bandwidth, vdisk_iops] (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_cloudspace_stats(customer_id, cloudspace_id, end, start, include=include, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_cloudspace_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **include** | [**list[str]**](str.md)| Cloudspace stats to include. If empty all stats will be returned Fields should be one of the parameters of series object in output model [cpu, network, memory, vdisk_latency,  vdisk_capacity, vdisk_bandwidth, vdisk_iops] | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CloudspaceStatsModel**](CloudspaceStatsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> list[str] get_currencies()



Get Currencies

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))

try:
    api_response = api_instance.get_currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_compliance_overview**
> VCOComplianceReport get_customer_compliance_overview(x_fields=x_fields)



Returns a list of customers that have compliance issues

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_compliance_overview(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_compliance_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VCOComplianceReport**](VCOComplianceReport.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_compliance_report**
> CustomerComplianceReport get_customer_compliance_report(customer_id, x_fields=x_fields)



get the information about noncompliant virtual machines in the last 24hr for this Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_compliance_report(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_compliance_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerComplianceReport**](CustomerComplianceReport.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_compliance_series**
> CustomerComplianceSeries get_customer_compliance_series(customer_id, x_fields=x_fields)



get the information about licensing issues over time for this Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_compliance_series(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_compliance_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerComplianceSeries**](CustomerComplianceSeries.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_consumption**
> AccountConsumptionModel get_customer_consumption(customer_id, location, end, start, x_fields=x_fields)



get location resource consumption for this Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_consumption(customer_id, location, end, start, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_consumption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**AccountConsumptionModel**](AccountConsumptionModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_consumption_series**
> AccountConsumptionTsModel get_customer_consumption_series(customer_id, location, end, start, step, units, x_fields=x_fields)



get location resource consumption timeseries for this Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
step = 'step_example' # str | Step between each time point from [\"15m\", \"30m\", \"60m\", \"24h\"]
units = ['units_example'] # list[str] | List of units to include Possible values: [\"su\", \"tu\", \"nu\", \"vcu\", \"mu\", \"piu\", \"wu\", \"ou\"]
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_consumption_series(customer_id, location, end, start, step, units, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_consumption_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **step** | **str**| Step between each time point from [\&quot;15m\&quot;, \&quot;30m\&quot;, \&quot;60m\&quot;, \&quot;24h\&quot;] | 
 **units** | [**list[str]**](str.md)| List of units to include Possible values: [\&quot;su\&quot;, \&quot;tu\&quot;, \&quot;nu\&quot;, \&quot;vcu\&quot;, \&quot;mu\&quot;, \&quot;piu\&quot;, \&quot;wu\&quot;, \&quot;ou\&quot;] | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**AccountConsumptionTsModel**](AccountConsumptionTsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_info**
> Customer get_customer_info(customer_id, x_fields=x_fields)



Get customer info

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_info(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_pdf**
> get_customer_invoice_pdf(customer_id, invoice_id)



Get customer Invoice PDF

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.get_customer_invoice_pdf(customer_id, invoice_id)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_invoice_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_location_capacity**
> CapacityModel get_customer_location_capacity(customer_id, location, x_fields=x_fields)



Get location Capacity

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_location_capacity(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_location_capacity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CapacityModel**](CapacityModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_location_datacenter**
> Datacenter get_customer_location_datacenter(customer_id, location, x_fields=x_fields)



Get customer location datacenter

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_location_datacenter(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_location_datacenter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Datacenter**](Datacenter.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_location_pricing**
> LocationPricing get_customer_location_pricing(customer_id, location, x_fields=x_fields)



Get location prices for this Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_location_pricing(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_location_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**LocationPricing**](LocationPricing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_pricing**
> VcoPricing get_customer_pricing(customer_id, x_fields=x_fields)



Get location prices for this Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_customer_pricing(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VcoPricing**](VcoPricing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_consumption**
> DiskConsumptionModel get_disk_consumption(customer_id, location, disk_id, end, start, x_fields=x_fields)



Get Disk resource consumption

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
end = 56 # int | End timestamp
start = 56 # int | Start timestamp
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_disk_consumption(customer_id, location, disk_id, end, start, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_disk_consumption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **end** | **int**| End timestamp | 
 **start** | **int**| Start timestamp | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**DiskConsumptionModel**](DiskConsumptionModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_consumption_series**
> DiskTimeseries get_disk_consumption_series(customer_id, location, disk_id, end, start, step, units, x_fields=x_fields)



Get Disk resource consumption timeseries

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
end = 56 # int | End timestamp
start = 56 # int | Start timestamp
step = 'step_example' # str | Step between each time point from [\"15m\", \"30m\", \"60m\", \"24h\"]
units = ['units_example'] # list[str] | List of units to include Possible values: [\"su\", \"tu\"]
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_disk_consumption_series(customer_id, location, disk_id, end, start, step, units, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_disk_consumption_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **end** | **int**| End timestamp | 
 **start** | **int**| Start timestamp | 
 **step** | **str**| Step between each time point from [\&quot;15m\&quot;, \&quot;30m\&quot;, \&quot;60m\&quot;, \&quot;24h\&quot;] | 
 **units** | [**list[str]**](str.md)| List of units to include Possible values: [\&quot;su\&quot;, \&quot;tu\&quot;] | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**DiskTimeseries**](DiskTimeseries.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_info**
> DiskModel get_disk_info(customer_id, location, disk_id, x_fields=x_fields)



Get disk Information

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_disk_info(customer_id, location, disk_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_disk_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**DiskModel**](DiskModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_notes**
> ResourceNotes get_disk_notes(customer_id, location, disk_id, x_fields=x_fields)



Get disk notes

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_disk_notes(customer_id, location, disk_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_disk_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ResourceNotes**](ResourceNotes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_snapshot**
> DiskSnapshotModel get_disk_snapshot(customer_id, location, disk_id, snapshot_id, all_vm_disks=all_vm_disks, x_fields=x_fields)



Get Disk snapshot

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
snapshot_id = 'snapshot_id_example' # str | 
all_vm_disks = true # bool | List disks have the same snapshot ID (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_disk_snapshot(customer_id, location, disk_id, snapshot_id, all_vm_disks=all_vm_disks, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **snapshot_id** | **str**|  | 
 **all_vm_disks** | **bool**| List disks have the same snapshot ID | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**DiskSnapshotModel**](DiskSnapshotModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_network**
> ExternalNetworkModel get_external_network(customer_id, location, external_network_id, x_fields=x_fields)



Get external network info

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
external_network_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_external_network(customer_id, location, external_network_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_external_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **external_network_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExternalNetworkModel**](ExternalNetworkModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_networks_virtual_machine**
> ExternalNIC get_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, external_ip_address, x_fields=x_fields)



Get external network (NIC) that the virtual machine is attached to

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
external_ip_address = 'external_ip_address_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, external_ip_address, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_external_networks_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **external_ip_address** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExternalNIC**](ExternalNIC.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> ImageModel get_image(customer_id, location, image_id, x_fields=x_fields)



Get image details

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
image_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_image(customer_id, location, image_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **image_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ImageModel**](ImageModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objectspace**
> GetObjectspaceModel get_objectspace(customer_id, objectspace_id, x_fields=x_fields)



Get the details of an objectspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_objectspace(customer_id, objectspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**GetObjectspaceModel**](GetObjectspaceModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objectspace_notes**
> ResourceNotes get_objectspace_notes(customer_id, objectspace_id, x_fields=x_fields)



Get objectspace notes

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_objectspace_notes(customer_id, objectspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_objectspace_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ResourceNotes**](ResourceNotes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_names**
> OSNamesMap get_os_names(x_fields=x_fields)



Get supported OS names

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_os_names(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_os_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**OSNamesMap**](OSNamesMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_types**
> get_os_types()



Get OS types

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))

try:
    api_instance.get_os_types()
except ApiException as e:
    print("Exception when calling CustomersApi->get_os_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portforward**
> PortforwardsModel get_portforward(customer_id, cloudspace_id, portforward_id, x_fields=x_fields)



Get cloudspace port forward

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
portforward_id = 'portforward_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_portforward(customer_id, cloudspace_id, portforward_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_portforward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **portforward_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**PortforwardsModel**](PortforwardsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_cloudspace_connection_status**
> RemoteConnectionStatus get_remote_cloudspace_connection_status(customer_id, cloudspace_id, connected_cloudspace_id, x_fields=x_fields)



Get remote connection status

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
connected_cloudspace_id = 'connected_cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_remote_cloudspace_connection_status(customer_id, cloudspace_id, connected_cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_remote_cloudspace_connection_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **connected_cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**RemoteConnectionStatus**](RemoteConnectionStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> CustomerRoleFull get_role(customer_id, role_id, x_fields=x_fields)



Get customer role

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_role(customer_id, role_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleFull**](CustomerRoleFull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_access**
> get_support_access(customer_id)



get support organization access

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.get_support_access(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->get_support_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_anti_affinity_groups**
> GetCloudspaceAntiAffinityGroupVmsModel get_virtual_machine_anti_affinity_groups(customer_id, cloudspace_id, group_id, x_fields=x_fields)



Get virtual machine anti-affinity groups

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
group_id = 'group_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_virtual_machine_anti_affinity_groups(customer_id, cloudspace_id, group_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_anti_affinity_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **group_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**GetCloudspaceAntiAffinityGroupVmsModel**](GetCloudspaceAntiAffinityGroupVmsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_console**
> str get_virtual_machine_console(customer_id, cloudspace_id, vm_id)



Get virtual machine console

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 

try:
    api_response = api_instance.get_virtual_machine_console(customer_id, cloudspace_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_console: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_consumption**
> VmConsumptionModel get_virtual_machine_consumption(customer_id, cloudspace_id, vm_id, end, start, x_fields=x_fields)



Get virtual machine resource consumption

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_virtual_machine_consumption(customer_id, cloudspace_id, vm_id, end, start, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_consumption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmConsumptionModel**](VmConsumptionModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_consumption_series**
> VmConsumptionTsModel get_virtual_machine_consumption_series(customer_id, cloudspace_id, vm_id, end, start, step, units, x_fields=x_fields)



Get virtual machine resource consumption timeseries

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
step = 'step_example' # str | Step between each time point from [\"15m\", \"30m\", \"60m\", \"24h\"]
units = ['units_example'] # list[str] | List of units to include Possible values: [\"su\", \"tu\", \"nu\", \"vcu\", \"mu\", \"piu\", \"wu\"]
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_virtual_machine_consumption_series(customer_id, cloudspace_id, vm_id, end, start, step, units, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_consumption_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **step** | **str**| Step between each time point from [\&quot;15m\&quot;, \&quot;30m\&quot;, \&quot;60m\&quot;, \&quot;24h\&quot;] | 
 **units** | [**list[str]**](str.md)| List of units to include Possible values: [\&quot;su\&quot;, \&quot;tu\&quot;, \&quot;nu\&quot;, \&quot;vcu\&quot;, \&quot;mu\&quot;, \&quot;piu\&quot;, \&quot;wu\&quot;] | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmConsumptionTsModel**](VmConsumptionTsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_info**
> VmInfoModel get_virtual_machine_info(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Get virtual machine info

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_virtual_machine_info(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmInfoModel**](VmInfoModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_notes**
> ResourceNotes get_virtual_machine_notes(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Get virtual machine notes

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_virtual_machine_notes(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ResourceNotes**](ResourceNotes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_stats**
> VmStatsModel get_virtual_machine_stats(customer_id, cloudspace_id, vm_id, end, start, include=include, x_fields=x_fields)



Get Virtual Machine Statistics

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
end = 56 # int | End timestamp presented as a unix timestamp in seconds
start = 56 # int | Start timestamp presented as a unix timestamp in seconds
include = ['include_example'] # list[str] | Virtual machines stats to include. If empty all stats will be returned Fields should be one of the parameters of series object in output model [cpu, network, memory, vm_capacity, vm_latency, vm_iops, vm_bandwidth, vdisk_latency, vdisk_capacity, vdisk_bandwidth, vdisk_iops] (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_virtual_machine_stats(customer_id, cloudspace_id, vm_id, end, start, include=include, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_virtual_machine_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **end** | **int**| End timestamp presented as a unix timestamp in seconds | 
 **start** | **int**| Start timestamp presented as a unix timestamp in seconds | 
 **include** | [**list[str]**](str.md)| Virtual machines stats to include. If empty all stats will be returned Fields should be one of the parameters of series object in output model [cpu, network, memory, vm_capacity, vm_latency, vm_iops, vm_bandwidth, vdisk_latency, vdisk_capacity, vdisk_bandwidth, vdisk_iops] | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmStatsModel**](VmStatsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_price_simulation**
> VMPrice get_vm_price_simulation(customer_id, location, memory, vcpus, disksize, iops, is_windows_vm, x_fields=x_fields)



get estimated VM price per month

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
memory = 56 # int | Amount of memory in MiB
vcpus = 56 # int | Number of VCPUs
disksize = 56 # int | Total disk size in GiB
iops = 2000 # int | IOPS of the bootdisk (default to 2000)
is_windows_vm = false # bool | Indicates if VM requires Windows license (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vm_price_simulation(customer_id, location, memory, vcpus, disksize, iops, is_windows_vm, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_vm_price_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **memory** | **int**| Amount of memory in MiB | 
 **vcpus** | **int**| Number of VCPUs | 
 **disksize** | **int**| Total disk size in GiB | 
 **iops** | **int**| IOPS of the bootdisk | [default to 2000]
 **is_windows_vm** | **bool**| Indicates if VM requires Windows license | [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VMPrice**](VMPrice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vmcdrom_info**
> CDROMModel get_vmcdrom_info(customer_id, cloudspace_id, vm_id, cdrom_id, x_fields=x_fields)



Get virtual machine attached CDROM image Info

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
cdrom_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vmcdrom_info(customer_id, cloudspace_id, vm_id, cdrom_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_vmcdrom_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **cdrom_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CDROMModel**](CDROMModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buckets**
> Buckets list_buckets(customer_id, objectspace_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)



List all of the buckets connected to the objectspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
include_deleted = false # bool | optionally return soft-deleted buckets (optional) (default to false)
only_deleted = false # bool | Only include deleted buckets (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_buckets(customer_id, objectspace_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **include_deleted** | **bool**| optionally return soft-deleted buckets | [optional] [default to false]
 **only_deleted** | **bool**| Only include deleted buckets | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Buckets**](Buckets.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspace_anti_affinity_groups**
> AntiAffinityGroups list_cloudspace_anti_affinity_groups(customer_id, cloudspace_id, x_fields=x_fields)



List anti-affinity groups

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cloudspace_anti_affinity_groups(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_cloudspace_anti_affinity_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**AntiAffinityGroups**](AntiAffinityGroups.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspace_external_networks**
> list_cloudspace_external_networks(customer_id, cloudspace_id)



List cloudspace external networks

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 

try:
    api_instance.list_cloudspace_external_networks(customer_id, cloudspace_id)
except ApiException as e:
    print("Exception when calling CustomersApi->list_cloudspace_external_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspace_network_routes**
> list_cloudspace_network_routes(customer_id, cloudspace_id)



List cloud space routes

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 

try:
    api_instance.list_cloudspace_network_routes(customer_id, cloudspace_id)
except ApiException as e:
    print("Exception when calling CustomersApi->list_cloudspace_network_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspace_objectspaces**
> ObjectspacesForCloudspace list_cloudspace_objectspaces(customer_id, cloudspace_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)



Listing the objectspaces for specific cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
include_deleted = false # bool | Include deleted Object spaces (optional) (default to false)
only_deleted = false # bool | Only include deleted Object spaces (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cloudspace_objectspaces(customer_id, cloudspace_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_cloudspace_objectspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **include_deleted** | **bool**| Include deleted Object spaces | [optional] [default to false]
 **only_deleted** | **bool**| Only include deleted Object spaces | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ObjectspacesForCloudspace**](ObjectspacesForCloudspace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspace_virtual_machines**
> VirtualMachines list_cloudspace_virtual_machines(customer_id, cloudspace_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)



List VMs on this cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
include_deleted = false # bool | Include deleted machines (optional) (default to false)
only_deleted = false # bool | Only include deleted machines (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cloudspace_virtual_machines(customer_id, cloudspace_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_cloudspace_virtual_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **include_deleted** | **bool**| Include deleted machines | [optional] [default to false]
 **only_deleted** | **bool**| Only include deleted machines | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VirtualMachines**](VirtualMachines.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspaces**
> Cloudspaces list_cloudspaces(customer_id, include_deleted=include_deleted, only_deleted=only_deleted, include_disabled=include_disabled, locations=locations, x_fields=x_fields)



List cloudspaces for the customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
include_deleted = false # bool | Include deleted Cloud spaces (optional) (default to false)
only_deleted = false # bool | Only include deleted Cloud spaces (optional) (default to false)
include_disabled = true # bool | include disabled cloudspaces (optional) (default to true)
locations = ['[]'] # list[str] | Locations filter (optional) (default to [])
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cloudspaces(customer_id, include_deleted=include_deleted, only_deleted=only_deleted, include_disabled=include_disabled, locations=locations, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_cloudspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **include_deleted** | **bool**| Include deleted Cloud spaces | [optional] [default to false]
 **only_deleted** | **bool**| Only include deleted Cloud spaces | [optional] [default to false]
 **include_disabled** | **bool**| include disabled cloudspaces | [optional] [default to true]
 **locations** | [**list[str]**](str.md)| Locations filter | [optional] [default to []]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Cloudspaces**](Cloudspaces.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_cdrom_images**
> CDROMs list_customer_cdrom_images(customer_id, location, x_fields=x_fields)



List public images and customer's CDROM images

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_customer_cdrom_images(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customer_cdrom_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CDROMs**](CDROMs.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_certificates**
> CertificatesSimple list_customer_certificates(customer_id, x_fields=x_fields)



List customer certificates

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_customer_certificates(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customer_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CertificatesSimple**](CertificatesSimple.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_images**
> Images list_customer_images(customer_id, location, x_fields=x_fields)



list public images and customer's account images

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_customer_images(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customer_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Images**](Images.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_invoices**
> CustomerInvoiceList list_customer_invoices(customer_id, x_fields=x_fields)



List customer Invoices

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_customer_invoices(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customer_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerInvoiceList**](CustomerInvoiceList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_locations**
> VcoPricing list_customer_locations(customer_id, x_fields=x_fields)



List customer available locations

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_customer_locations(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customer_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VcoPricing**](VcoPricing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> CustomersSimple list_customers(x_fields=x_fields)



List customers

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_customers(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomersSimple**](CustomersSimple.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disk_snapshots**
> Snapshots list_disk_snapshots(customer_id, location, disk_id, include_automatic=include_automatic, x_fields=x_fields)



List Disk snapshots

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
include_automatic = false # bool | Include automatic snapshots (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_disk_snapshots(customer_id, location, disk_id, include_automatic=include_automatic, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_disk_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **include_automatic** | **bool**| Include automatic snapshots | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Snapshots**](Snapshots.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disks**
> Disks list_disks(customer_id, location, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)



List customer disks

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
include_deleted = false # bool | Include deleted disks (optional) (default to false)
only_deleted = false # bool | Only include deleted disks (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_disks(customer_id, location, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **include_deleted** | **bool**| Include deleted disks | [optional] [default to false]
 **only_deleted** | **bool**| Only include deleted disks | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Disks**](Disks.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disks_virtual_machine**
> VirtualMachineDisks list_disks_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



List disks on virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_disks_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_disks_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VirtualMachineDisks**](VirtualMachineDisks.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exposed_disks**
> ExposedDisks list_exposed_disks(customer_id, cloudspace_id, x_fields=x_fields)



List exposed disks

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_exposed_disks(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_exposed_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExposedDisks**](ExposedDisks.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_network_interface_models**
> ExternalNICModels list_external_network_interface_models(x_fields=x_fields)



List supported external network interface models

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_external_network_interface_models(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_external_network_interface_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExternalNICModels**](ExternalNICModels.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_networks**
> ExternalNetworks list_external_networks(customer_id, location, x_fields=x_fields)



List of the available external networks in a location

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_external_networks(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_external_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExternalNetworks**](ExternalNetworks.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_networks_virtual_machine**
> ExternalNICS list_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



List external networks (NIC) that the virtual machine is attached to

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_external_networks_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_external_networks_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExternalNICS**](ExternalNICS.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_objectspaces**
> ObjectSpaces list_objectspaces(customer_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)



List all object spaces for a customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
include_deleted = false # bool | Include deleted Object spaces (optional) (default to false)
only_deleted = false # bool | Only include deleted Object spaces (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_objectspaces(customer_id, include_deleted=include_deleted, only_deleted=only_deleted, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_objectspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **include_deleted** | **bool**| Include deleted Object spaces | [optional] [default to false]
 **only_deleted** | **bool**| Only include deleted Object spaces | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ObjectSpaces**](ObjectSpaces.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portforwards**
> Portforwards list_portforwards(customer_id, cloudspace_id, x_fields=x_fields)



Get cloudspace port forwards

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_portforwards(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_portforwards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Portforwards**](Portforwards.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_cloudspace_connections**
> ConnectedCloudspaces list_remote_cloudspace_connections(customer_id, cloudspace_id, x_fields=x_fields)



List remote connections to cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_remote_cloudspace_connections(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_remote_cloudspace_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ConnectedCloudspaces**](ConnectedCloudspaces.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_grants**
> CustomerRoleResources list_role_grants(customer_id, role_id, x_fields=x_fields)



List cloud resources to which the role has access

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_role_grants(customer_id, role_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_role_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleResources**](CustomerRoleResources.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> CustomerRoleList list_roles(customer_id, x_fields=x_fields)



Get customer roles

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_roles(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleList**](CustomerRoleList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles_on_cloudspace**
> CustomerRoleList list_roles_on_cloudspace(customer_id, cloudspace_id, x_fields=x_fields)



List roles with access to this cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_roles_on_cloudspace(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_roles_on_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleList**](CustomerRoleList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles_on_customer**
> CustomerRoleList list_roles_on_customer(customer_id, x_fields=x_fields)



List roles with customer wide access

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_roles_on_customer(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_roles_on_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleList**](CustomerRoleList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles_on_location**
> CustomerRoleList list_roles_on_location(customer_id, location, x_fields=x_fields)



List roles with access to this location

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_roles_on_location(customer_id, location, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_roles_on_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleList**](CustomerRoleList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles_on_virtual_machine**
> CustomerRoleList list_roles_on_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



List roles with access to a virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_roles_on_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_roles_on_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**CustomerRoleList**](CustomerRoleList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_cdro_ms**
> VirtualMachineDisks list_virtual_machine_cdro_ms(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



List CDROM images attached to virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_virtual_machine_cdro_ms(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_virtual_machine_cdro_ms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VirtualMachineDisks**](VirtualMachineDisks.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_virtual_machine**
> SuccessModel move_virtual_machine(customer_id, cloudspace_id, vm_id, target_cloudspace_id, target_ip_address=target_ip_address, x_fields=x_fields)



Move virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
target_cloudspace_id = 'target_cloudspace_id_example' # str | ID of target Cloudspace
target_ip_address = 'target_ip_address_example' # str | IP Address for the VM at the target Cloudspace Should be a valid and available IP address in target Cloudspace network (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.move_virtual_machine(customer_id, cloudspace_id, vm_id, target_cloudspace_id, target_ip_address=target_ip_address, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->move_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **target_cloudspace_id** | **str**| ID of target Cloudspace | 
 **target_ip_address** | **str**| IP Address for the VM at the target Cloudspace Should be a valid and available IP address in target Cloudspace network | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_virtual_machine**
> SuccessModel pause_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Pause virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.pause_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->pause_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_file**
> VmReadFileModel read_file(customer_id, cloudspace_id, vm_id, size, filepath, seek=seek, x_fields=x_fields)



Read file from virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
size = 56 # int | Size of data to read maximuxm 2MiB
filepath = 'filepath_example' # str | filepath to read from
seek = 0 # int | Offset in the file to read from (optional) (default to 0)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.read_file(customer_id, cloudspace_id, vm_id, size, filepath, seek=seek, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->read_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **size** | **int**| Size of data to read maximuxm 2MiB | 
 **filepath** | **str**| filepath to read from | 
 **seek** | **int**| Offset in the file to read from | [optional] [default to 0]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmReadFileModel**](VmReadFileModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_virtual_machine**
> SuccessModel reboot_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Reboot virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.reboot_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->reboot_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recycle_bin**
> RecycleBin recycle_bin(customer_id, x_fields=x_fields)



list all deleted resources for the customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.recycle_bin(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->recycle_bin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**RecycleBin**](RecycleBin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cloudspace_external_network**
> SuccessModel remove_cloudspace_external_network(customer_id, cloudspace_id, external_network_ip, external_network_id, x_fields=x_fields)



Remove cloudspace external network

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
external_network_ip = 'external_network_ip_example' # str | optional ip address inside the external network
external_network_id = 56 # int | optional id to take ip address from.If omited will search for available network
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.remove_cloudspace_external_network(customer_id, cloudspace_id, external_network_ip, external_network_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->remove_cloudspace_external_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **external_network_ip** | **str**| optional ip address inside the external network | 
 **external_network_id** | **int**| optional id to take ip address from.If omited will search for available network | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cloudspace_network_route**
> SuccessModel remove_cloudspace_network_route(customer_id, cloudspace_id, destination, gateway, table=table, x_fields=x_fields)



Remove extra route from network

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
destination = 'destination_example' # str | Destination network to route
gateway = 'gateway_example' # str | Gateway to route desination over
table = 56 # int | routing table to add route to (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.remove_cloudspace_network_route(customer_id, cloudspace_id, destination, gateway, table=table, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->remove_cloudspace_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **destination** | **str**| Destination network to route | 
 **gateway** | **str**| Gateway to route desination over | 
 **table** | **int**| routing table to add route to | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_customer_location**
> remove_customer_location(customer_id, location)



remove location from Customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 

try:
    api_instance.remove_customer_location(customer_id, location)
except ApiException as e:
    print("Exception when calling CustomersApi->remove_customer_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_cloudspace**
> SuccessModel rename_cloudspace(customer_id, cloudspace_id, name, x_fields=x_fields)



Rename cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
name = 'name_example' # str | Cloudspace Name
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.rename_cloudspace(customer_id, cloudspace_id, name, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->rename_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **name** | **str**| Cloudspace Name | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_virtual_machine**
> VmIdModel rename_virtual_machine(customer_id, cloudspace_id, vm_id, name=name, x_fields=x_fields)



Update virtual machine name

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
name = 'name_example' # str | Virtual Machine name (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.rename_virtual_machine(customer_id, cloudspace_id, vm_id, name=name, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->rename_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **name** | **str**| Virtual Machine name | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmIdModel**](VmIdModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_bucket_limit**
> SuccessModel reset_bucket_limit(customer_id, objectspace_id, bucket_id, x_fields=x_fields)



Reset a bucket limit to default

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
bucket_id = 'bucket_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.reset_bucket_limit(customer_id, objectspace_id, bucket_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->reset_bucket_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **bucket_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_objectspace**
> ResetObjectspaceModel reset_objectspace(customer_id, objectspace_id, x_fields=x_fields)



Resetting objectspace secret and access key

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.reset_objectspace(customer_id, objectspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->reset_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ResetObjectspaceModel**](ResetObjectspaceModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_virtual_machine**
> SuccessModel reset_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Reset virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.reset_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->reset_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_disk**
> SuccessModel resize_disk(customer_id, location, disk_id, disk_size, x_fields=x_fields)



Update disk size

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
disk_size = 56 # int | Disk Size in GiB
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.resize_disk(customer_id, location, disk_id, disk_size, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->resize_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **disk_size** | **int**| Disk Size in GiB | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_virtual_machine**
> SuccessModel resize_virtual_machine(customer_id, cloudspace_id, vm_id, vcpus=vcpus, memory=memory, x_fields=x_fields)



Update virtual machine sizes of CPUs or memory

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
vcpus = 56 # int | Number of cpu to assign to machine (optional)
memory = 56 # int | Amount of memory to assign to machine in MiB (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.resize_virtual_machine(customer_id, cloudspace_id, vm_id, vcpus=vcpus, memory=memory, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->resize_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **vcpus** | **int**| Number of cpu to assign to machine | [optional] 
 **memory** | **int**| Amount of memory to assign to machine in MiB | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_bucket**
> SuccessModel restore_bucket(customer_id, objectspace_id, bucket_id, x_fields=x_fields)



Restore a soft-deleted bucket

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
bucket_id = 'bucket_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_bucket(customer_id, objectspace_id, bucket_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **bucket_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_cloudspace**
> SuccessModel restore_cloudspace(customer_id, cloudspace_id, reason=reason, x_fields=x_fields)



Restore cloudspace

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reason = '' # str | Reason for restoring (optional) (default to )
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_cloudspace(customer_id, cloudspace_id, reason=reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_cloudspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reason** | **str**| Reason for restoring | [optional] [default to ]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_customer_cdrom_image**
> SuccessModel restore_customer_cdrom_image(customer_id, location, cdrom_id, reason=reason, x_fields=x_fields)



Restore customer CDROM Image

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
cdrom_id = 56 # int | 
reason = '' # str | Reason for enabling (optional) (default to )
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_customer_cdrom_image(customer_id, location, cdrom_id, reason=reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_customer_cdrom_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **cdrom_id** | **int**|  | 
 **reason** | **str**| Reason for enabling | [optional] [default to ]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_customer_image**
> SuccessModel restore_customer_image(customer_id, location, image_id, x_fields=x_fields)



Restore customer Image

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
image_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_customer_image(customer_id, location, image_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_customer_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **image_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_disk**
> SuccessModel restore_disk(customer_id, location, disk_id, reason=reason, x_fields=x_fields)



Restore disk

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
reason = '' # str | Reason for enabling (optional) (default to )
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_disk(customer_id, location, disk_id, reason=reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **reason** | **str**| Reason for enabling | [optional] [default to ]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_objectspace**
> SuccessModel restore_objectspace(customer_id, objectspace_id, x_fields=x_fields)



Restoring deleted and destroyed objectspaces

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_objectspace(customer_id, objectspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_objectspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_virtual_machine**
> SuccessModel restore_virtual_machine(customer_id, cloudspace_id, vm_id, reason, x_fields=x_fields)



Restore virtual machine from recycle bin

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
reason = 'reason_example' # str | Reason for restoring
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.restore_virtual_machine(customer_id, cloudspace_id, vm_id, reason, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->restore_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **reason** | **str**| Reason for restoring | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_virtual_machine**
> SuccessModel resume_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)



Resume virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.resume_virtual_machine(customer_id, cloudspace_id, vm_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->resume_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_disk_snapshot**
> rollback_disk_snapshot(customer_id, location, disk_id, snapshot_id, all_vm_disks=all_vm_disks)



Rollback Disk snapshot

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
snapshot_id = 'snapshot_id_example' # str | 
all_vm_disks = true # bool | Rollback of all snapshots that were created in the same action (optional)

try:
    api_instance.rollback_disk_snapshot(customer_id, location, disk_id, snapshot_id, all_vm_disks=all_vm_disks)
except ApiException as e:
    print("Exception when calling CustomersApi->rollback_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **snapshot_id** | **str**|  | 
 **all_vm_disks** | **bool**| Rollback of all snapshots that were created in the same action | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_create_customer**
> str self_create_customer(payload)



Self-create a new customer

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
payload = pc4g.CustomerSelfCreate() # CustomerSelfCreate | 

try:
    api_response = api_instance.self_create_customer(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->self_create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CustomerSelfCreate**](CustomerSelfCreate.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_bucket_limit**
> SuccessModel set_bucket_limit(customer_id, objectspace_id, bucket_id, limit, x_fields=x_fields)



Set a bucket limit

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
bucket_id = 'bucket_id_example' # str | 
limit = 56 # int | the number of iops for the bucket
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.set_bucket_limit(customer_id, objectspace_id, bucket_id, limit, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->set_bucket_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **bucket_id** | **str**|  | 
 **limit** | **int**| the number of iops for the bucket | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cloudspace_default_gateway**
> set_cloudspace_default_gateway(customer_id, cloudspace_id, gateway)



Set cloudspace default gateway

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
gateway = 'gateway_example' # str | Default Gateway to set

try:
    api_instance.set_cloudspace_default_gateway(customer_id, cloudspace_id, gateway)
except ApiException as e:
    print("Exception when calling CustomersApi->set_cloudspace_default_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **gateway** | **str**| Default Gateway to set | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cloudspace_proxy_config**
> set_cloudspace_proxy_config(customer_id, cloudspace_id, payload, proxy_type=proxy_type)



Set cloudspace proxy config

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
payload = pc4g.AddProxyInput() # AddProxyInput | 
proxy_type = 'traefik:2.3' # str | Proxy Type, currently should be traefik:2.3 (optional) (default to traefik:2.3)

try:
    api_instance.set_cloudspace_proxy_config(customer_id, cloudspace_id, payload, proxy_type=proxy_type)
except ApiException as e:
    print("Exception when calling CustomersApi->set_cloudspace_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **payload** | [**AddProxyInput**](AddProxyInput.md)|  | 
 **proxy_type** | **str**| Proxy Type, currently should be traefik:2.3 | [optional] [default to traefik:2.3]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_disk_limit_io**
> SuccessModel set_disk_limit_io(customer_id, location, disk_id, iops=iops, x_fields=x_fields)



Set disk IO Tune

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
iops = 2000 # int | Total iops per sec. Minimum 100 (optional) (default to 2000)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.set_disk_limit_io(customer_id, location, disk_id, iops=iops, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->set_disk_limit_io: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **iops** | **int**| Total iops per sec. Minimum 100 | [optional] [default to 2000]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_virtual_machine**
> SuccessModel start_virtual_machine(customer_id, cloudspace_id, vm_id, rescue_disk_id=rescue_disk_id, x_fields=x_fields)



Start virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
rescue_disk_id = 56 # int | Rescue Disk ID (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.start_virtual_machine(customer_id, cloudspace_id, vm_id, rescue_disk_id=rescue_disk_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->start_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **rescue_disk_id** | **int**| Rescue Disk ID | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_virtual_machine**
> SuccessModel stop_virtual_machine(customer_id, cloudspace_id, vm_id, force=force, x_fields=x_fields)



Stop virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
force = false # bool | Force stop VM (optional) (default to false)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.stop_virtual_machine(customer_id, cloudspace_id, vm_id, force=force, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->stop_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **force** | **bool**| Force stop VM | [optional] [default to false]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **take_disk_snapshot**
> str take_disk_snapshot(customer_id, location, disk_id, snapshot_name, all_vm_disks=all_vm_disks)



Take Disk snapshot

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
snapshot_name = 'snapshot_name_example' # str | Snapshot Name
all_vm_disks = true # bool | Take Snapshots of All VM disks (optional)

try:
    api_response = api_instance.take_disk_snapshot(customer_id, location, disk_id, snapshot_name, all_vm_disks=all_vm_disks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->take_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **snapshot_name** | **str**| Snapshot Name | 
 **all_vm_disks** | **bool**| Take Snapshots of All VM disks | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unexpose_disk**
> SuccessModel unexpose_disk(customer_id, cloudspace_id, disk_id, x_fields=x_fields)



Unexpose an exposed disk

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
disk_id = 56 # int | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.unexpose_disk(customer_id, cloudspace_id, disk_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->unexpose_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **disk_id** | **int**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upate_objectspace_note**
> SuccessModel upate_objectspace_note(customer_id, objectspace_id, note_id, payload, x_fields=x_fields)



Update objectspace note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
objectspace_id = 'objectspace_id_example' # str | 
note_id = 'note_id_example' # str | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.upate_objectspace_note(customer_id, objectspace_id, note_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->upate_objectspace_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **objectspace_id** | **str**|  | 
 **note_id** | **str**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate**
> Certificates update_certificate(customer_id, domain, payload, x_fields=x_fields)



Update certificate information

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
domain = 'domain_example' # str | 
payload = pc4g.CreateCustomerCertificate() # CreateCustomerCertificate | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_certificate(customer_id, domain, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **domain** | **str**|  | 
 **payload** | [**CreateCustomerCertificate**](CreateCustomerCertificate.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Certificates**](Certificates.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloudspace_anti_affinity_group**
> SuccessModel update_cloudspace_anti_affinity_group(customer_id, cloudspace_id, group_id, spread, x_fields=x_fields)



Update anti-affinity group rules

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
group_id = 'group_id_example' # str | 
spread = 56 # int | Amount of physical nodes to spread vms over. Set to -1 for infinite spread
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_cloudspace_anti_affinity_group(customer_id, cloudspace_id, group_id, spread, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_cloudspace_anti_affinity_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **group_id** | **str**|  | 
 **spread** | **int**| Amount of physical nodes to spread vms over. Set to -1 for infinite spread | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloudspace_external_network_metric**
> update_cloudspace_external_network_metric(customer_id, cloudspace_id, metric, external_network_ip, external_network_id)



Update cloudspace external network metric

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
metric = 56 # int | external network metric(low priority is highest priority)if omitted lowest priority is used
external_network_ip = 'external_network_ip_example' # str | optional ip address inside the external network
external_network_id = 56 # int | optional id to take ip address from.If omited will search for available network

try:
    api_instance.update_cloudspace_external_network_metric(customer_id, cloudspace_id, metric, external_network_ip, external_network_id)
except ApiException as e:
    print("Exception when calling CustomersApi->update_cloudspace_external_network_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **metric** | **int**| external network metric(low priority is highest priority)if omitted lowest priority is used | 
 **external_network_ip** | **str**| optional ip address inside the external network | 
 **external_network_id** | **int**| optional id to take ip address from.If omited will search for available network | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloudspace_note**
> SuccessModel update_cloudspace_note(customer_id, cloudspace_id, note_id, payload, x_fields=x_fields)



Update cloudspace note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
note_id = 'note_id_example' # str | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_cloudspace_note(customer_id, cloudspace_id, note_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_cloudspace_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **note_id** | **str**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloudspace_quota**
> SuccessModel update_cloudspace_quota(customer_id, cloudspace_id, vcpu_quota=vcpu_quota, vdisk_space_quota=vdisk_space_quota, memory_quota=memory_quota, public_ip_quota=public_ip_quota, external_network_quota=external_network_quota, x_fields=x_fields)



Update cloudspace quota

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vcpu_quota = 56 # int | VCPU Quota. If omitted the account will be able to provision an unlimited amount of VCPUs. (optional)
vdisk_space_quota = 56 # int | VDisk Quota, If omitted the account will be able to provision an unlimited amount of VDisks. (optional)
memory_quota = 8.14 # float | Memory Quota, If omitted the account will be able to provision an unlimited amount of Memory. (optional)
public_ip_quota = 56 # int | Public IP Quota, If omitted the account will be able to provision an unlimited amount of Public IPs. (optional)
external_network_quota = 56 # int | External Network Transfer Quota (GB), If omitted the account will be able to provision an unlimited amount of External network transfers. (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_cloudspace_quota(customer_id, cloudspace_id, vcpu_quota=vcpu_quota, vdisk_space_quota=vdisk_space_quota, memory_quota=memory_quota, public_ip_quota=public_ip_quota, external_network_quota=external_network_quota, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_cloudspace_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vcpu_quota** | **int**| VCPU Quota. If omitted the account will be able to provision an unlimited amount of VCPUs. | [optional] 
 **vdisk_space_quota** | **int**| VDisk Quota, If omitted the account will be able to provision an unlimited amount of VDisks. | [optional] 
 **memory_quota** | **float**| Memory Quota, If omitted the account will be able to provision an unlimited amount of Memory. | [optional] 
 **public_ip_quota** | **int**| Public IP Quota, If omitted the account will be able to provision an unlimited amount of Public IPs. | [optional] 
 **external_network_quota** | **int**| External Network Transfer Quota (GB), If omitted the account will be able to provision an unlimited amount of External network transfers. | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> str update_customer(customer_id, payload)



Update customer info

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
payload = pc4g.CustomerUpdate() # CustomerUpdate | 

try:
    api_response = api_instance.update_customer(customer_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **payload** | [**CustomerUpdate**](CustomerUpdate.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disk_model**
> ChangedModel update_disk_model(customer_id, location, disk_id, model, x_fields=x_fields)



Update Disk Model

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
model = 'model_example' # str | the new NIC model
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_disk_model(customer_id, location, disk_id, model, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_disk_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **model** | **str**| the new NIC model | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ChangedModel**](ChangedModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disk_note**
> SuccessModel update_disk_note(customer_id, location, disk_id, note_id, payload, x_fields=x_fields)



Update disk note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
location = 'location_example' # str | 
disk_id = 56 # int | 
note_id = 'note_id_example' # str | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_disk_note(customer_id, location, disk_id, note_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_disk_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **location** | **str**|  | 
 **disk_id** | **int**|  | 
 **note_id** | **str**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_interface_model**
> ChangedModel update_network_interface_model(customer_id, cloudspace_id, vm_id, mac_address, model, x_fields=x_fields)



Update virtual machine network interface model

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
mac_address = 'mac_address_example' # str | 
model = 'model_example' # str | the new NIC model
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_network_interface_model(customer_id, cloudspace_id, vm_id, mac_address, model, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_network_interface_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **mac_address** | **str**|  | 
 **model** | **str**| the new NIC model | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ChangedModel**](ChangedModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portforward**
> SuccessModel update_portforward(customer_id, cloudspace_id, portforward_id, local_port, public_port, protocol, vm_id=vm_id, nested_cs_id=nested_cs_id, x_fields=x_fields)



Update cloudspace port forward

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
portforward_id = 'portforward_id_example' # str | 
local_port = 56 # int | Local port
public_port = 56 # int | Public port
protocol = 'protocol_example' # str | Protocol for port forwarding
vm_id = 56 # int | Virtual Machine ID (optional)
nested_cs_id = 56 # int | Nested Cloudspace ID (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_portforward(customer_id, cloudspace_id, portforward_id, local_port, public_port, protocol, vm_id=vm_id, nested_cs_id=nested_cs_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_portforward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **portforward_id** | **str**|  | 
 **local_port** | **int**| Local port | 
 **public_port** | **int**| Public port | 
 **protocol** | **str**| Protocol for port forwarding | 
 **vm_id** | **int**| Virtual Machine ID | [optional] 
 **nested_cs_id** | **int**| Nested Cloudspace ID | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> update_role(customer_id, role_id, payload)



Update customer role

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
payload = pc4g.CustomerRoleCreate() # CustomerRoleCreate | 

try:
    api_instance.update_role(customer_id, role_id, payload)
except ApiException as e:
    print("Exception when calling CustomersApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **payload** | [**CustomerRoleCreate**](CustomerRoleCreate.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_grants**
> update_role_grants(customer_id, role_id, payload)



Add/remove role access to a cloud resource

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
payload = pc4g.CustomerRoleResourceGrant() # CustomerRoleResourceGrant | 

try:
    api_instance.update_role_grants(customer_id, role_id, payload)
except ApiException as e:
    print("Exception when calling CustomersApi->update_role_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **payload** | [**CustomerRoleResourceGrant**](CustomerRoleResourceGrant.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_machine_description**
> VmIdModel update_virtual_machine_description(customer_id, cloudspace_id, vm_id, description=description, x_fields=x_fields)



Update virtual machine description

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
description = 'description_example' # str | Virtual Machine Description (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_virtual_machine_description(customer_id, cloudspace_id, vm_id, description=description, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_virtual_machine_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **description** | **str**| Virtual Machine Description | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VmIdModel**](VmIdModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_machine_note**
> SuccessModel update_virtual_machine_note(customer_id, cloudspace_id, vm_id, note_id, payload, x_fields=x_fields)



Update virtual machine note

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
note_id = 'note_id_example' # str | 
payload = pc4g.MenejaStructsVcoDataclassesNotesNoteInputsStruct() # MenejaStructsVcoDataclassesNotesNoteInputsStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_virtual_machine_note(customer_id, cloudspace_id, vm_id, note_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_virtual_machine_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **note_id** | **str**|  | 
 **payload** | [**MenejaStructsVcoDataclassesNotesNoteInputsStruct**](MenejaStructsVcoDataclassesNotesNoteInputsStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_file**
> SuccessModel write_file(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)



Write to file inside virtual machine

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.CustomersApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
vm_id = 56 # int | 
payload = pc4g.MenejaStructsVcoDataclassesVmVMWriteFileStruct() # MenejaStructsVcoDataclassesVmVMWriteFileStruct | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.write_file(customer_id, cloudspace_id, vm_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->write_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **vm_id** | **int**|  | 
 **payload** | [**MenejaStructsVcoDataclassesVmVMWriteFileStruct**](MenejaStructsVcoDataclassesVmVMWriteFileStruct.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

