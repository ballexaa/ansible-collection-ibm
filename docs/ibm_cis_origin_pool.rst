
ibm_cis_origin_pool -- Configure IBM Cloud 'ibm_cis_origin_pool' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_origin_pool' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  notification_email (False, str, None)
    None


  origins (False, list, None)
    (Required for new resource)


  healthy (False, str, None)
    None


  modified_on (False, str, None)
    None


  name (False, str, None)
    (Required for new resource) name


  check_regions (False, list, None)
    (Required for new resource)


  description (False, str, None)
    None


  minimum_origins (False, int, 1)
    None


  cis_id (False, str, None)
    (Required for new resource) CIS instance crn


  enabled (False, bool, None)
    (Required for new resource)


  monitor (False, str, None)
    None


  created_on (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

