#!/bin/bash
server_profile_name="esx-synergyhost-04"
provisioned_nic="ManagementNIC"
hostname_field="Hostname"
post_provisioning_tasks="../config_tasks/remove_host_from_vcenter.yaml"

#playbooks/get_provisioning_info.yaml
ansible-playbook -i hosts playbooks/remove_provisioned_server.yaml -e server_profile_name=$server_profile_name -e provisioned_nic=$provisioned_nic -e hostname_field=$hostname_field -e post_provisioning_tasks=$post_provisioning_tasks 
