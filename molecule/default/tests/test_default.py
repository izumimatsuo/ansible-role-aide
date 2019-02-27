import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aide_is_installed(host):
    package = host.package("aide")
    assert package.is_installed
    assert package.version.startswith("0.15")


def test_aide_is_db_setupped(host):
    assert host.file("/var/lib/aide/aide.db.gz").exists


def test_aide_is_check_successful(host):
    assert host.run_test("aide --check")
