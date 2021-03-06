# Example playbooks to perform common tasks on Oneview

These playbooks uses the server_tasks files to build on more complete use cases. By including a number of tasks in a certain order, interesting functionality is achieved.

## How to use these examples

### Requirements

- Be sure to have git, ansible, python and python-pip installed in your system.

- Install the Oneview Python SDK using the instructions found [here](https://github.com/HewlettPackard/python-hpOneView#installation).

- Clone this repository:

~~~
git clone https://github.com/clsacramento/oneview-ansible.git
~~~

- Configure the OneView library environment variables pointing to the library directory from this repository. As in this [example](https://github.com/HewlettPackard/oneview-ansible#2-configure-the-ansible_library-environmental-variable).


- For the vCenter automation, install the govc utility following their [official instructions](https://github.com/vmware/govmomi/tree/master/govc#installation).

### Configure environment specific information:

#### File group_vars/all
~~~
#JSON file containing Oneview API endpoint details
config: /home/ubuntu/config.json
#Environment file used to perform tasks on vCenter
vsphere_env: /home/ubuntu/vsphere.env
#Weather vMotion is available. If false will power off VMs before migrating
vmotion_available: False
#Username that will be used to connect to hosts. Should be same one configure on server profile template.
user: root
#Passwod configured for that user. Requiered for SSH into hosts. Cannot be obtained from API
password: Synergy!
~~~

#### File config.json for oneview api connection
~~~
{
  "ip": "10.0.0.1",
  "credentials": {
    "userName": "administrator",
    "authLoginDomain": "",
    "password": "password"
  },
  "api_version": 500
}
~~~

#### File vsphere.env
~~~
export GOVC_USERNAME='administrator@vsphere.local'
export GOVC_PASSWORD='password'
export GOVC_URL='vcenter.example.domain'
export GOVC_INSECURE='true'
export GOVC_DATACENTER='DC'
export GOVC_CLUSTER='Cluster'
export GOVC_PORTGROUP='PG'
export GOVC_VSWITCH='vSwitch1'
export GOVC_VLAN='343'
~~~ 


## Running the playbooks
From the main directory of this repository:
~~~
cd oneview-ansible
~~~
Simply use the ansible-playbook command:
~~~
ansible-playbook -i hosts playbooks/hardware_list_available.yaml
~~~

Some playbooks require arguments. They can be passed with '-e' option:
~~~
ansible-playbook -i hosts playbooks/profile_power_state.yaml -e server_profile_name=myprofile -e ps=On
~~~

## Shell wrappers for adding/removing ESX hosts
As the playbooks to create and delete nodes on ESX became a bit longer, new_esx.sh and delete_esx.sh shell wrappers can be used. Have a look at their contents:
~~~
$ cat new_esx.sh
#!/bin/bash
server_profile_name="esx-synergyhost-04"
profile_template_name="ESXi-host-profile-template 1.2"
post_provisioning_tasks="../config_tasks/add_host_to_vcenter.yaml"

ansible-playbook -i hosts playbooks/provision_new_server.yaml -e server_profile_name=$server_profile_name -e profile_template_name="'$profile_template_name'" -e post_provisioning_tasks=$post_provisioning_tasks

$ cat delete_esx.sh
#!/bin/bash
server_profile_name="esx-synergyhost-04"
post_provisioning_tasks="../config_tasks/remove_host_from_vcenter.yaml"

ansible-playbook -i hosts playbooks/remove_provisioned_server.yaml -e server_profile_name=$server_profile_name -e post_provisioning_tasks=$post_provisioning_tasks
~~~

To use them, modify the values for profile and template accordingly, then execute:
~~~
$ ./new_esx.sh
$ ./delete_esx.sh
~~~

## In case of issue

If new_esh.sh fails but server profile was successfully created. You can run the following playbook to re-run only the configuration tasks:
~~~
ansible-playbook -i hosts playbooks/provision_retry.yaml --extra-vars '{"server_profile_name":"esx-synergyhost-04"}'
~~~

In case of issue when running delete_esx.sh, you may need to clean the host from the vCenter manually. In that case, the profile can be deleted from the oneview freeing up the node with the following playbook:
~~~
ansible-playbook -i hosts playbooks/profile_delete.yaml --extra-vars '{"server_profile_name":"esx-synergyhost-04"}'
~~~
