import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_groovy_installed(host):

    # Groovy expected version
    groovy_version = '3.0.2'

    # Groovy Home Path
    expected_groovy_home_path = '/opt/groovy/groovy-{}'\
                               .format(groovy_version)

    # Groovy archive file
    expected_groovy_archive_path = '/tmp/apache-groovy-sdk-{}.zip'\
                                  .format(groovy_version)

    # Check Groovy Home Path exists
    assert host.file(expected_groovy_home_path).exists
    assert host.file(expected_groovy_home_path).is_directory

    # Groovy Downloaded file
    groovy_archive = host.file(expected_groovy_archive_path)

    # Check that Groovy Archive exists
    assert groovy_archive.exists
    assert groovy_archive.is_file
