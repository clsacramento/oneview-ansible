# Example playbooks to perform common tasks on Oneview

These playbooks uses the server_tasks files to build on more complete use cases. By including a number of tasks in a certain order, interesting functionality is achieved.

## How to use these examples

First of all be sure to follow oneview-ansible main page instructions on how to install the library on your environment: [Ansible Modules for HPE OneView](https://github.com/HewlettPackard/oneview-ansible)


Configure environment specific information:

### File group_vars/all
~~~
#JSON file containing Oneview API endpoint details
config: /home//config.json
#Environment file used to perform tasks on vCenter
vsphere_env: /home/telia/vsphere.env
#Weather vMotion is available. If false will power off VMs before migrating
vmotion_available: False
#Username that will be used to connect to hosts. Should be same one configure on server profile template.
user: root
#Passwod configured for that user. Requiered for SSH into hosts. Cannot be obtained from API
password: Synergy!
~~~

### File config.json for oneview api connection
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

### File vsphere.env
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
