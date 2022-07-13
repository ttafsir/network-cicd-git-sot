.DEFAULT_GOAL := help

SCRIPTS_DIR = "infra"
EVEN_NG_TOPOLOGY_FILE ?= "eve-ng-fabric-topology.yml"
HOST_GROUP ?= "dc1"

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build-eve-ng:	## Build eve-ng lab from topology file
	(cd infra && ./build_dev_fabric.sh ${EVEN_NG_TOPOLOGY_FILE})

destroy-eve-ng:	## Destroy eve-ng lab
	export LAB_NAME=$(grep -m 1 "name:" ${SCRIPTS_DIR}/${EVEN_NG_TOPOLOGY_FILE} | cut -d: -f 2) | \
	tr -d "[:space:]"; \
	eve-ng lab delete --path $(LAB_NAME)

test-inventory:	## Create inventory file for test
	(cd infra && ./generate_test_inventory.sh)

configs:	## AVD configs
	(cd ansible && ansible-playbook -i inventory/ generate-configs.yaml -e "host_group=${HOST_GROUP}")
