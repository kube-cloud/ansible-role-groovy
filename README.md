# Ansible Linux based Groovy role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-groovy.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-groovy.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-groovy)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/41894.svg?style=flat)](https://galaxy.ansible.com/jetune/groovy)

Ansible role used to install Groovy on Linux based Operating System.

<a href="https://www.kube-cloud.com/"><img width="300" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="200" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://groovy.apache.org/"><img width="250" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Groovy-logo.svg/1280px-Groovy-logo.svg.png" /></a>

# Supported Version

* Apache Groovy 2.x/3.x

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Trusty/Xenial/Bionic
* Debian Jessie/Strech

# Depend On

* jetune.java

# Usage

* Install Role ``` ansible-galaxy install jetune.groovy ```
* use in your playbook
```
---
- hosts: all

  roles:
   - role: jetune.java
     vars:
      from_repo: false
      implementation: OPENJDK
      v_major: 11
      v_minor: 0.1
      build: 13
      os: linux
      arch: x64
      checksum: sha256:7a6bb980b9c91c478421f865087ad2d69086a0583aeeb9e69204785e8e97dcfd
      alternative_priority: 300
      is_default: true

   - role: jetune.groovy
     vars:
      groovy_version: 3
      groovy_is_default: true
      groovy_settings_directory: "~/.m2/"
      groovy_local_repository: "/opt/groovy/repository"
      groovy_proxies:
       - id: "cntlm_groovy_proxy"
         active: true
         protocol: "http"
         username: "jetune"
         password: "mypassword"
         host: "localhost"
         port: 3286
         exclusions: "localhost|127.0.0.1|some.other.host"
      groovy_servers:
       - id: "sonatype-nexus"
         username: "admin"
         password: "admin"
       - id: "bitbucket"
         privateKey: "/opt/security/key"
         passphrase: "p@ssw0rd"
      groovy_mirrors:
       - id: "mirror-central"
         name: "Central groovy repository mirror"
         target: "central"
         url: "https://artifact.lab.kube-cloud.be/repository/groovy-central/"

```

* You can install more than one Groovy version
