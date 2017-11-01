# Playbooks examples

Will use the tasks created to achieve example use cases such as obtain the power state from a server profile.


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
