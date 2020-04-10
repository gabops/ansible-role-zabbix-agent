gabops.zabbix_agent
===================
[![Build Status](https://travis-ci.org/gabops/ansible-role-zabbix-agent.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-zabbix-agent)

Installs and configures Zabbix agent.

Table of Contents
-----------------

- [Requirements](#requirements)
- [Role Variables](#role-variables)
  - [Main variables](#main-variables)
  - [Agent configuration](#agent-configuration)
  - [Agent TLS configuration](#agent-tls-configuration)
- [Dependencies](#dependencies)
- [Example Playbook](#example-playbook)
- [License](#license)
- [Author Information](#author-information)

Requirements
------------

None.

Role Variables
--------------

### Main variables:

#### zabbix_agent_version
Default value: `4.0`

Defines the version of Zabbix agent to be installed. Possible values are `3.0`, `4.0`, `4.4` or `5.0`.

#### zabbix_agent_service_enabled
Default value: `true`

Controls whether or not Zabbix agent service is enable.

#### zabbix_agent_service_state
Default value: `started`

Defines the state of the Zabbix agent service. Possible values should be `started` or `stopped`.

#### zabbix_agent_config_backup
Default value: `false`

Controls if the role should take a backup of `zabbix_agentd.conf` before applying any modification.

### Agent configuration

#### zabbix_agent_pidfile
Default value: `/var/run/zabbix/ zabbix_agentd.pid`

Name of PID file.

#### zabbix_agent_hostinterface
Default value: `""`

Optional parameter that defines host interface. Host interface is used at host autoregistration process. **Only available since 4.4**

#### zabbix_agent_hostinterfaceitem
Default value: `""`

Optional parameter that defines an item used for getting host interface. Host interface is used at host autoregistration process. **Only available since 4.4**

#### zabbix_agent_logtype
Default value: `file`

Log output type.

#### zabbix_agent_logfile 
Default value: `""`

Name of log file.

#### zabbix_agent_logfilesize 
Default value: `""`

Maximum size of log file in MB.

#### zabbix_agent_debuglevel
Default value: `3`

Specifies debug level.

#### zabbix_agent_sourceip
Default value: `""`

Source IP address for outgoing connections.

#### zabbix_agent_denykey
Default value: `system.run[*]`

Allow execution of items keys matching pattern. Only available when Zabbix agent version `5.0`

#### zabbix_agent_allowkey
Default value: `system.run[*]`

Deny execution of items keys matching pattern. Only available when Zabbix agent version `5.0`

#### zabbix_agent_enableremotecommands
Default value: `0`

Whether remote commands from Zabbix server are allowed.

#### zabbix_agent_logremotecommands
Default value: `0`

Enable logging of executed shell commands as warnings.

#### zabbix_agent_server
Default value: `127.0.0.1`

List of comma delimited IP addresses, optionally in CIDR notation, or hostnames of Zabbix servers and Zabbix proxies.  Incoming connections will be accepted only from the hosts listed here.

#### zabbix_agent_listenport
Default value: `10050`

Agent will listen on this port for connections from the server.

#### zabbix_agent_listenip
Default value: `0.0.0.0`

List of comma delimited IP addresses that the agent should listen on.

#### zabbix_agent_startagents
Default value: `3`

Number of pre-forked instances of zabbix_agentd that process passive checks.

#### zabbix_agent_serveractive
Default value: `127.0.0.1`

IP:port (or hostname:port) of Zabbix server or Zabbix proxy for active checks. Multiple comma-delimited addresses can be provided to use several independent Zabbix servers in parallel. Spaces are allowed.

#### zabbix_agent_hostname
Default value: `Zabbix server`

Unique, case sensitive hostname. Required for active checks and must match hostname as configured on the server.

#### zabbix_agent_hostnameitem
Default value: `system.hostname`

Optional parameter that defines a Zabbix agent item used for getting host name. This option is only used when Hostname is not defined.

#### zabbix_agent_hostmetadata
Default value: `""`

Optional parameter that defines host metadata. Host metadata is used only at host auto-registration process (active agent).

#### zabbix_agent_hostmetadataitem
Default value: `""`

Optional parameter that defines a Zabbix agent item used for getting host metadata. This option is only used when HostMetadata is not defined.

#### zabbix_agent_refreshactivechecks
Default value: `120`

How often list of active checks is refreshed, in seconds.

#### zabbix_agent_buffersend
Default value: `5`

Do not keep data longer than N seconds in buffer.

#### zabbix_agent_buffersize
Default value: `100`

Maximum number of values in a memory buffer.

#### zabbix_agent_maxlinespersecond
Default value: `20`

Maximum number of new lines the agent will send per second to Zabbix server or proxy when processing 'log' and 'eventlog' active checks.

#### zabbix_agent_alias
Default value: `[]`

Sets an alias for an item key.

#### zabbix_agent_timeout
Default value: `3`

Spend no more than Timeout seconds on processing.

#### zabbix_agent_allowroot
Default value: `0`

Allow the agent to run as 'root'.

#### zabbix_agent_user
Default value: `zabbix`

Drop privileges to a specific, existing user on the system. Only has effect if run as 'root' and AllowRoot is disabled.

#### zabbix_agent_include
Default value: `['/etc/zabbix/zabbix_agentd.d/*.conf']`

You may include individual files or all files in a directory in the configuration file.

#### zabbix_agent_unsafeuserparameters
Default value: `0`

Allow all characters to be passed in arguments to user-defined parameters.

#### zabbix_agent_userparameter
Default value: `[]`

User-defined parameter to monitor. There can be several user-defined parameters. Format: UserParameter=<key>,<shell command>

#### zabbix_agent_loadmodulepath
Default value: `${libdir}/modules`

Full path to location of agent modules.

#### zabbix_agent_loadmodule
Default value: `[]`

Module to load at agent startup. Modules are used to extend functionality of the agent. Formats: "LoadModule=<module.so>", "LoadModule=<path/module.so>".

### Agent TLS configuration

#### zabbix_agent_tlsconnect
Default value: `unencrypted`

How the agent should connect to Zabbix server or proxy. Used for active checks. Possible values are `unencrypted`, `psk`, `cert`.

#### zabbix_agent_tlsaccept
Default value: `""`

What incoming connections to accept. Used for a passive checks. Possible values are `unencrypted`, `psk`, `cert`.

#### zabbix_agent_tlscafile
Default value: `""`

Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.

#### zabbix_agent_tlscrlfile
Default value: `""`

Full pathname of a file containing revoked certificates.

#### zabbix_agent_tlsservercertissuer
Default value: `""`

Allowed server (proxy) certificate issuer.

#### zabbix_agent_tlsservercertsubject
Default value: `""`

Allowed server (proxy) certificate subject.

#### zabbix_agent_tlscertfile
Default value: `""`

Full pathname of a file containing the agent certificate or certificate chain.

#### zabbix_agent_tlskeyfile
Default value: `""`

Full pathname of a file containing the agent private key used for encrypted communications with Zabbix components.

#### zabbix_agent_tlspskidentity
Default value: `""`

Pre-shared key identity string, used for encrypted communications with Zabbix server.

#### zabbix_agent_tlspskfile
Default value: `""`

Full pathname of a file containing the agent pre-shared key used for encrypted communications with Zabbix components.

#### zabbix_agent_tlsciphercert13
Default value: `""`

Cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate-based encryption. Not available when version is `3.0`.

#### zabbix_agent_tlsciphercert
Default value: `""`

GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate-based encryption. Not available when version is `3.0`.

#### zabbix_agent_tlscipherpsk13
Default value: `""`

Cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Not available when version is `3.0`.

#### zabbix_agent_tlscipherpsk
Default value: `""`

GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for PSK-based encryption. Not available when version is `3.0`.

#### zabbix_agent_tlscipherall13
Default value: `""`

Cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption. Not available when version is `3.0`.

#### zabbix_agent_tlscipherall
Default value: `""`

GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate and PSK-based encryption. Not available when version is `3.0`.

> For information about zabbix agent configuration parameters please visit Zabbix agent documentation ([3.0](https://www.zabbix.com/documentation/3.0/manual/appendix/config/zabbix_agentd), [4.0](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_agentd), [4.4](https://www.zabbix.com/documentation/4.4/manual/appendix/config/zabbix_agentd), [5.0](https://www.zabbix.com/documentation/5.0/manual/appendix/config/zabbix_agentd))

Dependencies
------------

- [gabops.zabbix_repo](https://galaxy.ansible.com/gabops/zabbix_repo)

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
    zabbix_agent_include:
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
