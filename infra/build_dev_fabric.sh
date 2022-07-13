#!/bin/bash
# Track setup script
# -e - exit on any error
# -u - fail on unbound or unknown vars
# -x - verbose output
# -o pipefail - ensure pipes catch errors (not true by default)
set -euo pipefail

echo "Export the environment variables"
source .env

set +euo pipefail
echo "Get EVE-NG node details"
eveng lab create-from-topology -t $1
set -euo pipefail

echo "Get EVE-NG node details"
eveng node list --output json | yq -P > nodes.yml

echo "Start the lab"
export LAB_NAME=$(grep -m 1 "name:" $1 | cut -d: -f 2); \
eveng lab start --path ${LAB_NAME}

cat > ansible-hosts << EOF
[all]
eve_ng_host  ansible_host=${EVE_NG_HOST} ansible_user=${EVE_NG_SSH_USERNAME} ansible_pass=${EVE_NG_SSH_PASSWORD}
EOF

cat > ansible.cfg << EOF
[defaults]
host_key_checking   = False

retry_files_enabled     = False
interpreter_python      = /usr/bin/python
force_valid_group_names = ignore
gathering               = smart
stdout_callback         = debug
EOF

set +euo pipefail

echo "Build the NAT configuration for virtual devices"
echo ${PWD}
ansible-playbook -i ansible-hosts pb-configure-nat.yml -vv

echo "Clean up"
rm ansible-hosts
rm nodes.yml
