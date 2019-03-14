Ansible role that adds Ceph RBD
=========

This role adds Ceph RBD persistent volume to k8s cluster.
Note: rbd sercrets will be installed in kube-system namespace.
The origin for templates is https://github.com/kubernetes-incubator/external-storage/tree/master/ceph/rbd/deploy/rbac

Requirements
------------

1. Installed and worked Kubernetes cluster
2. Installed and worked Ceph monitor e.g. *ceph-mon*
3. pip install -r requirements.txt

Role Variables
--------------

The role uses variables defined in defaults. You can override them by using group_vars or host_vars

Dependencies
------------

None

Example Playbook
----------------

Here as a small example playbook:

```yaml
  - name: Add Ceph RBD to k8s
    hosts: localhost
    roles:
       - bilenkis.k8s_ceph_rbd
```

You can run it with:

```sh
ansible-playbook -i k8s_ceph_rbd/tests/inventory k8s_ceph_rbd/tests/test.yml
```

License
-------

## see [ Apache License 2.0 ]( LICENSE )

Author Information
------------------

Feel free to open issues or MRs if you find problems or have ideas for improvements.
