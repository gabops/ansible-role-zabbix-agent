gabops.zabbix_agent
===================
[![Build Status](https://travis-ci.org/gabops/ansible-role-zabbix-agent.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-zabbix-agent)

Installs and configures Zabbix agent.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| zabbix_agent_service_enabled | true | Controls whether or not Zabbix agent service is enable. |
| zabbix_agent_service_state | started | Defines the state of the Zabbix agent service. Possible values should be `started` or `stopped`. |
| zabbix_agent_version | 4.0 | Defines the version of Zabbix agent to install. Possible values are `3.0`, `4.0`, `4.4` or `5.0`. |
| zabbix_agent_config_backup | false | Controls if the role should take a backup of `zabbix_agentd.conf` before applying any modification. |
| zabbix_agent_config | {} | Defines the configuration to be applied to the `zabbix_agentd.conf`. Note that if this parameter is empty as it is by default, the file `zabbix_agentd.conf` will not be modified at all and your installation will use the unmodified default config file. |

### Notes:

- This role installs the [Zabbix official repository](https://www.zabbix.com/documentation/4.0//manual/installation/install_from_packages) and then the Zabbix agent from it.

> For information about zabbix agent configuration parameters please visit Zabbix agent documentation ([3.0](https://www.zabbix.com/documentation/3.0/manual/appendix/config/zabbix_agentd), [4.0](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_agentd), [4.4](https://www.zabbix.com/documentation/4.4/manual/appendix/config/zabbix_agentd), [5.0](https://www.zabbix.com/documentation/5.0/manual/appendix/config/zabbix_agentd))

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: webservers
  vars:
    zabbix_agent_version: 4.4
    zabbix_agent_config:
      DebugLevel: 4
      Hostname: "{{ inventory_hostname }}"
      ListenIP: "{{ ansible_default_ipv4 }}"
      Server: 192.168.0.10
      StartAgents: 5
      HostMetadataItem: system.uname
      Timeout: 20
      TLSConnect: psk
      TLSAccept: psk
      TLSPSKIdentity: "{{ inventory_hostname }}"
      TLSPSKFile: /etc/zabbix/zabbix_agentd.psk
      Include:
        - /usr/local/etc/zabbix_agentd.userparams.conf
        - /opt/zabbix_custom/*.conf
  roles:
      - role: gabops.zabbix_agent
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
