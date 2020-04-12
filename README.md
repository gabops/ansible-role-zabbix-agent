gabops.zabbix_agent
===================
[![Build Status](https://travis-ci.org/gabops/ansible-role-zabbix-agent.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-zabbix-agent)

Installs and configures Zabbix agent.

Requirements
------------

None.

Role Variables
--------------

### BASIC PARAMETERS
| Variable | Default value | Description |
| :--- | :--- | :--- |
| zabbix_agent_service_enabled | true | Controls whether or not Zabbix agent service is enable. |
| zabbix_agent_service_state | started | Defines the state of the Zabbix agent service. Possible values should be `started` or `stopped`. |
| zabbix_agent_version | 4.0 | Defines the version of Zabbix agent to install. Possible values are `3.0`, `4.0`, `4.4` or `5.0`. |
| zabbix_agent_config_backup | false | Controls if the role should take a backup of `zabbix_agentd.conf` before applying any modification. |

### AGENT CONFIGURATION:
#### GENERAL PARAMETERS
| Variable | Default value | Description |
| :--- | :--- | :--- |

#### ADVANCED PARAMETERS
| Variable | Default value | Description |
| :--- | :--- | :--- |

#### USER-DEFINED MONITORED PARAMETERS
| Variable | Default value | Description |
| :--- | :--- | :--- |

#### LOADABLE MODULES
| Variable | Default value | Description |
| :--- | :--- | :--- |

#### TLS-RELATED PARAMETERS
| Variable | Default value | Description |
| :--- | :--- | :--- |

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
    zabbix_agent_debuglevel: 4
    zabbix_agent_hostname: "{{ inventory_hostname }}"
    zabbix_agent_listenip: "{{ ansible_default_ipv4 }}"
    zabbix_agent_server: 192.168.0.10
    zabbix_agent_startagents: 5
    zabbix_agent_hostmetadataItem: system.uname
    zabbix_agent_timeout: 20
    zabbix_agent_tlsconnect: psk
    zabbix_agent_tlsaccept: psk
    zabbix_agent_tlkspkidentity: "{{ inventory_hostname }}"
    zabbix_agent_tlspskfile: /etc/zabbix/zabbix_agentd.psk
    zabbix_agebt_include:
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
