import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zabbix_process(host):
    s = host.service('zabbix-agent')

    assert s.is_enabled
    assert s.is_running


def test_zabbix_package(host):
    p = host.package("zabbix-agent")

    assert p.is_installed
    assert '5.0' in p.version
