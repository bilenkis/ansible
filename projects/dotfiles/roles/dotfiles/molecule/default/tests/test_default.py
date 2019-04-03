import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_home_files(host):
    f = host.file('~/.tmux.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
    'vim',
    'tmux',
    'mosh',
])
def test_installed_packages(host, pkg):
    p = host.package(pkg)
    assert p.is_installed
