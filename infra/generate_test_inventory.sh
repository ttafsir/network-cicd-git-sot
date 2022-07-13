(cd ../ansible && rm -rf inventory/hosts.yml)
(cd ../ansible && ansible-inventory  -i inventory/ --playbook-dir ./ --list -y) > ../ansible/inventory/hosts.yml
