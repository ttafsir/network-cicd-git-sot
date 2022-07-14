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


## Contributing

1. Clone the repo

```sh
git clone https://github.com/ttafsir/
```

### Install Requirements

1. Install Python Requirements

```sh
python -m venv .venv
source .venv/bin/activate
```

```sh
pip install -r requirements.txt
```

2. Install Ansible Galaxy Requirements

```sh
ansible-galaxy collection install -r roles/requirements.yml -p collections
```


### Create device configurations

The Arista AVD collection allows us to create device configurations based on intent data we've defined in the `data` directory.

To create the device configurations, we can use the `generate-configs.yaml` playbook or the `make configs` command.

```sh
ansible-playbook generate-configs.yaml -i inventory/ -e host_group="dc1:&env_dev"
```

Alternatively, we can use the `make configs` command. It will create the device configurations for the "dc1" host group in the "dev" environment.

```sh
make configs
```

You can type `make` to view the other available commands.

```sh
➜ make
build-eve-ng                   Build eve-ng lab from topology file
configs                        AVD configs
destroy-eve-ng                 Destroy eve-ng lab
test-inventory                 Create inventory file for test
```

### Build EVE-NG infrastructure

To test our generated configs, we can deploy them to a virtual infrastructure and test the network to assert that our deployment is working as intended. We use a [topology file](infra/eve-ng-fabric-topology.yml) to define the infrastructure. Each device in the topology has a configuration directive that points to generated config files. We use the [evengsdk](www.github/ttafsir/evengsdk) library to manage the virtual infrastructure.

To build the infrastructure, we can use the `build-eve-ng` command. Before running the command, we need to configuration environment variables for the evengsdk library.

Create a file called `.env` in the `infra` directory of the repo.

```txt
# infra/.env
export EVE_NG_HOST=<hostname or IP>
export EVE_NG_USERNAME=admin                    # EVE-NG API/GUI username
export EVE_NG_PASSWORD=<eve-ng API/GUI pass>    # EVE-NG API/GUI password
export EVE_NG_SSH_USERNAME=<eve-ng ssh user>    # EVE-NG SSH username
export EVE_NG_SSH_PASSWORD=<password>           # EVE-NG SSH password
```

Once the environment variables are set, we can run the `build-eve-ng` command.

```sh
make build-eve-ng
```

### Create inventory for testing

We use inventory plugins for our configure and manage our infrastructure. However, the ansible backend service for the [testinfra] pytest library does not seem to support inventory plugins. For that reason, we need to create an inventory file for testing.

```sh
make test-inventory
```

### Tear down the infrastructure

```sh
make destroy-eve-ng
```

## Testing

To test our infrastructure, we can use the pytest with the [testinfra] pytest library. `testinfra` provides a testing framework that allows use of different backends for testing, including Ansible. For our testing, we use the ansible backend to leverage the existing Ansible inventory and to also use ansible for the Arrange, and Act steps for our tests.

### Tox

To run the tests, we can use the [tox] library. You can use the `tox` command to run the tests.

```sh
tox
```

Our tox configuration file is located in the `tox.ini` file, and it allows us to run the tests in different environments and to pass arguments to Pytest, as needed.

For example, we can run just the BGP tests by filtering the tests using the `-k` option.

```sh
tox -- -k bgp
```

the `--` is a special option that tells tox that the following arguments are for Pytest.

Here's another example that shows how we can increase the number of workers for the tests.

```sh
tox -- -k bgp -n 10
```

In this case, the `-n` option tells tox to run the tests in parallel. The `10` argument is the number of workers. This option is provided by the `pytest-xdist` library.
