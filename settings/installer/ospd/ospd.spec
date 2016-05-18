---
subparsers:
    ospd:
        formatter_class: RawTextHelpFormatter
        help: Installs openstack using OSP Director
        groups:
            - title: Introspection
              options:
                  instackenv-file:
                      type: Value
                      help: The path to the instackenv.json configuration file used for introspection.

            - title: Firewall
              options:
                  firewall:
                      type: YamlFile
                      help: The firewall configuration
                      default: default.yml

            - title: Product
              options:
                  product-version:
                      type: Value
                      help: The product version
                      choices: ["7", "8", "9"]
                      default: 8
                  product-build:
                      type: Value
                      help: The product build
                      default: latest
                  product-core-version:
                      type: Value
                      help: The product core version
                      choices: ["7", "8", "9"]
                      default: 8
                  product-core-build:
                      type: Value
                      help: The product core build
                      default: latest

            - title: Undercloud
              options:
                  undercloud-config:
                      type: YamlFile
                      help: The undercloud config details
                      default: default.yml

            - title: Nodes Deployment
              options:
                  nodes-controller:
                      type: Value
                      help: The amount of controller nodes to deploy
                      default: '1'
                  nodes-compute:
                      type: Value
                      help: The amount of compute nodes to deploy
                      default: '1'
                  nodes-storage:
                      type: Value
                      help: The amount of storage nodes to deploy
                      default: '0'

            - title: Overcloud
              options:
                  overcloud-ssl:
                      type: Value
                      help: Specifies whether ths SSL should be used for overcloud
                      default: 'no'

                  overcloud-deployment:
                      type: Value
                      help: |
                            The absolute path to the overcloud template folder you would like to use.
                            The template folder is where you keep the instackenv.json file +
                            network / storage templates you provide for the overcloud deployment.
                            Please see `settings/deployment/virthost` as reference.
                      required: yes

            - title: Overcloud Network Isolation
              options:
                  network-isolation:
                      type: Value
                      help: Whether we would like to use network isolation.
                      choices: ['no', 'single-nic-vlans', 'two-nics-vlans', 'three-nics-vlans']
                      required: yes

                  network-backend:
                      type: Value
                      help: The overcloud network backend.
                      choices: ['gre', 'vxlan', 'vlan']
                      default: vxlan

                  network-protocol:
                      type: Value
                      help: The overcloud network backend.
                      choices: ['ipv4', 'ipv6']
                      default: 'ipv4'

            - title: Overcloud storage
              options:
                storage:
                    type: YamlFile
                    help: The overcloud storage type
                    default: no-storage.yml

            - title: Overcloud images
              options:
                  images-task:
                      type: Value
                      help: Specifies whether the images should be built or imported
                      choices: [import, build, rpm]
                      default: import
                  images-url:
                      type: Value
                      help: Specifies the import image url. Required only when images task is 'import'

            - title: User
              options:
                  user-name:
                      type: Value
                      help: The installation user name
                      default: stack
                  user-password:
                      type: Value
                      help: The installation user password
                      default: stack

            - title: Loadbalancer
              options:
                  loadbalancer:
                      type: YamlFile
                      help: The loadbalancer to use

            - title: Workarounds
              options:
                  workarounds:
                      type: YamlFile
                      help: The list of workarounds to use during install

            - title: common
              options:
                  dry-run:
                      action: store_true
                      help: Only generate settings, skip the playbook execution stage
                  cleanup:
                      action: store_true
                      help: Clean given system instead of provisioning a new one
                  input:
                      action: append
                      type: str
                      short: i
                      help: Input settings file to be loaded before the merging of user args
                  output:
                      type: str
                      short: o
                      help: 'File to dump the generated settings into (default: stdout)'
                  extra-vars:
                      action: append
                      short: e
                      help: Extra variables to be merged last
                      type: str
                  from-file:
                      type: IniFile
                      help: the ini file with the list of arguments
                  generate-conf-file:
                      type: str
                      help: generate configuration file (ini) containing default values and exits. This file is than can be used with the from-file argument
