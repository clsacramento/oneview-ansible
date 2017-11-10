# Playbooks examples

Tasks that Will be used as building blocks to achieve example use cases such as obtain the power state from a server profile.


## How to use this task

These tasks were created to be directly included on a playbook. These files should not be executed with ansible-playbook directly. Here is an exemble of the playbook to list hardware available:
~~~
###
# Lists all the server hardware that is available
# Sets a fact containing on array with the names (string) of the servers
# A server hardware is considered available when it does not have a
# profile applied to it.
# Usage example: ansible-playbook -i hosts playbooks/hardware_list_available.yaml
---
- hosts: all
  vars:
    - config: "{{ config_path }}"
  tasks:
    - include_tasks: ../servers_tasks/hardware_available_list.yaml
    - include_tasks: ../servers_tasks/hardware_pick_one_available.yaml
~~~
The playbook include the tasks to find the list of server_hardwares that are available and select one from the list


## Notes
 - Be careful when assign profiles to servers. If a profile that already is assigned to a server is assigned to another hardware, it will be moved from the previous server to the new one. The server to which the profile assigned originally will become empty. When a profile is removed from a server it will power off. When a profile is assigned to a server it will power on.

 - When you try to unassign the server hardware from a server profile. If the profile does not exist, the playbook will fail with a very misleading message: 
~~~        
fatal: [localhost -> localhost]: FAILED! => {"changed": false, "failed": true, "msg": "The value specified for the server hardware type null is not valid or not supported."}
~~~


 - It seems to playbooks that uses the oneview library cannot be executed at thte same time. Message got when tried to do so:
~~~
TASK [include_tasks] **************************************************************************************************************************************
fatal: [localhost]: FAILED! => {"failed": true, "reason": "no action detected in task. This often indicates a misspelled module name, or incorrect module path.\n\nThe error appears to have been in '/home/labtest/oneview-ansible/servers_tasks/profile_find_by_name.yaml': line 10, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n    - name: Gather facts about given server profile\n      ^ here\n\n\nThe error appears to have been in '/home/labtest/oneview-ansible/servers_tasks/profile_find_by_name.yaml': line 10, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n    - name: Gather facts about given server profile\n      ^ here\n\nexception type: <class 'ansible.errors.AnsibleParserError'>\nexception: no action detected in task. This often indicates a misspelled module name, or incorrect module path.\n\nThe error appears to have been in '/home/labtest/oneview-ansible/servers_tasks/profile_find_by_name.yaml': line 10, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n    - name: Gather facts about given server profile\n      ^ here\n"}
        to retry, use: --limit @/home/labtest/oneview-ansible/playbooks/unassign_hardware_from_profile.retry
~~~

 - The following message is misleading. This can happen sometimes if node is already on the state that is being applied such as power off a server already off. This should be a warning not an ERROR
~~~
TASK [Set power_state for server_hardware_name] ***************************************************************************************************************************************************************
fatal: [esx-synergyhost-04 -> localhost]: FAILED! => {"changed": false, "failed": true, "msg": "Unable to power off because the server hardware could not transition from the on state.; {u'errorSource': None, u'recommendedActions': [u'Refresh the server.  If the problem persists, remove and re-insert the server hardware.'], u'nestedErrors': [], u'errorCode': u'STATE_TRANSITION_ERROR_EXCEPTION', u'details': u'', u'message': u'Unable to power off because the server hardware could not transition from the on state.', u'data': {}}"}
changed: [localhost -> localhost]
~~~
