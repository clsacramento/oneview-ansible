#!/bin/bash
server_profile_name="esx-synergyhost-04"
post_provisioning_tasks="../config_tasks/remove_host_from_vcenter.yaml"

ansible-playbook -i hosts playbooks/remove_provisioned_server.yaml -e server_profile_name=$server_profile_name -e post_provisioning_tasks=$post_provisioning_tasks 
