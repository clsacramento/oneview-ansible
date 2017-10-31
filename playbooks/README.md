# Playbooks examples

Will use the tasks created to achieve example use cases such as obtain the power state from a server profile.


## Notes
 - Be careful when assign profiles to servers. If a profile that already is assigned to a server is assigned to another hardware, it will be moved from the previous server to the new one. The server to which the profile assigned originally will become empty. When a profile is removed from a server it will power off. When a profile is assigned to a server it will power on.
