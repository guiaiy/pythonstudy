#!/usr/bin/env python3
from collections import namedtuple

from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

Options = namedtuple('Options',
                     [
                         'connection',
                         'remote_user',
                         'ask_sudo_pass',
                         'verbosity',
                         'ask_pass',
                         'module_path',
                         'forks',
                         'become',
                         'become_method',
                         'become_user',
                         'check',
                         'listhosts',
                         'listtasks',
                         'listtags',
                         'syntax',
                         'sudo_user',
                         'sudo',
                         'diff'
                     ])

options = Options(
    connection='smart',
    remote_user=None,
    ask_pass=None,
    sudo_user=None,
    forks=5,
    sudo=None,
    ask_sudo_pass=False,
    verbosity=5,
    module_path=None,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    diff=False,
    listhosts=None,
    listtasks=None,
    listtags=None,
    syntax=None
)

loader = DataLoader()
passwords = dict()
inventory = InventoryManager(loader=loader, sources=['hosts'])
variable_manager = VariableManager(loader=loader, inventory=inventory)


def run_playbook(playbook_path):
    playbook = PlaybookExecutor(
        playbooks=playbook_path,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords
    )
    result = playbook.run()
    return result


if __name__ == '__main__':
    run_playbook(playbook_path=['lamp.yml'])
