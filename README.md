<img src="https://user-images.githubusercontent.com/7189920/161707065-4bd60ae3-47f0-4426-92fe-1e07dd983897.png" alt="wiley" />

# ACME-CORP: Data center network automation

This repo contains the all of the intent and automation files to manage the ACME corporation's (a totally real company) datacenter networks. In this version of the automation, we're using Git, Github, and our developing version control skills to manage this repository and its Git database as our Source of Truth (SoT).

## Getting Started

[First Time Use](docs/first_time_use.md)

## Our Automation Stack

This list will evolve as we add more automation to the stack.

* Ansible
* Python
* Arista-AVD


## Testing the Infrastructure

### Create device configurations

```sh
ansible-playbook generate-configs.yaml -i inventory/ -e host_group="dc1:&env_dev"
```

### Build EVE-NG infrastructure

```sh
make build-eve-ng
```

### Create inventory for testing

```sh
make test-inventory
```

### Tear down the infrastructure

```sh
make destroy-eve-ng
```
