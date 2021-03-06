#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster
short_description: Configure IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.5
    - Terraform v0.12.20

options:
    kube_version:
        description:
            - None
        required: False
        type: str
    ingress_secret:
        description:
            - None
        required: False
        type: str
    ingress_hostname:
        description:
            - None
        required: False
        type: str
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: False
        type: str
    region:
        description:
            - The cluster region
        required: False
        type: str
    disk_encryption:
        description:
            - None
        required: False
        type: bool
        default: True
    subnet_id:
        description:
            - None
        required: False
        type: list
        elements: str
    public_vlan_id:
        description:
            - None
        required: False
        type: str
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    public_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: False
        type: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    private_vlan_id:
        description:
            - None
        required: False
        type: str
    no_subnet:
        description:
            - None
        required: False
        type: bool
        default: False
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    machine_type:
        description:
            - None
        required: False
        type: str
    billing:
        description:
            - None
        required: False
        type: str
    is_trusted:
        description:
            - None
        required: False
        type: bool
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    worker_num:
        description:
            - Number of worker nodes
        required: False
        type: int
        default: 0
    update_all_workers:
        description:
            - None
        required: False
        type: bool
        default: False
    server_url:
        description:
            - None
        required: False
        type: str
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    hardware:
        description:
            - (Required for new resource) 
        required: False
        type: str
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
    ('datacenter', 'str'),
    ('hardware', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'kube_version',
    'ingress_secret',
    'ingress_hostname',
    'public_service_endpoint',
    'private_service_endpoint',
    'resource_crn',
    'name',
    'region',
    'disk_encryption',
    'subnet_id',
    'public_vlan_id',
    'wait_time_minutes',
    'public_service_endpoint_url',
    'resource_controller_url',
    'resource_status',
    'datacenter',
    'default_pool_size',
    'private_vlan_id',
    'no_subnet',
    'org_guid',
    'albs',
    'private_service_endpoint_url',
    'resource_group_name',
    'workers_info',
    'machine_type',
    'billing',
    'is_trusted',
    'tags',
    'worker_pools',
    'worker_num',
    'update_all_workers',
    'server_url',
    'space_guid',
    'gateway_enabled',
    'crn',
    'resource_name',
    'hardware',
    'webhook',
    'resource_group_id',
    'account_guid',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    kube_version=dict(
        required=False,
        type='str'),
    ingress_secret=dict(
        required=False,
        type='str'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    resource_crn=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    subnet_id=dict(
        required=False,
        elements='',
        type='list'),
    public_vlan_id=dict(
        required=False,
        type='str'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    default_pool_size=dict(
        default=1,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='str'),
    no_subnet=dict(
        default=False,
        type='bool'),
    org_guid=dict(
        required=False,
        type='str'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    workers_info=dict(
        required=False,
        elements='',
        type='list'),
    machine_type=dict(
        required=False,
        type='str'),
    billing=dict(
        required=False,
        type='str'),
    is_trusted=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    worker_num=dict(
        default=0,
        type='int'),
    update_all_workers=dict(
        default=False,
        type='bool'),
    server_url=dict(
        required=False,
        type='str'),
    space_guid=dict(
        required=False,
        type='str'),
    gateway_enabled=dict(
        default=False,
        type='bool'),
    crn=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    hardware=dict(
        required=False,
        type='str'),
    webhook=dict(
        required=False,
        elements='',
        type='list'),
    resource_group_id=dict(
        required=False,
        type='str'),
    account_guid=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.5',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
