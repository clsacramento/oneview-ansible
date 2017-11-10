#!/bin/bash
server_profile_name="esx-synergyhost-04"
profile_template_name="ESXi-host-profile-template 1.2"
post_provisioning_tasks="../config_tasks/add_host_to_vcenter.yaml"

ansible-playbook -i hosts playbooks/provision_new_server.yaml -e server_profile_name=$server_profile_name -e profile_template_name="'$profile_template_name'" -e post_provisioning_tasks=$post_provisioning_tasks 
