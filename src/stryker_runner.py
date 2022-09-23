import subprocess
import sys
import stryker_constants


class StrykerRunner:
    def __init__(self, stryker_config_file_path):
        self.stryker_config_file_path = stryker_config_file_path

    def run_mutation_for_project(self, project_name):
        project_command = self.get_mutation_command_for_project_name(
            project_name)

        process = subprocess.Popen(project_command.split(), stdout=sys.stdout)
        process.communicate()

    def get_mutation_command_for_project_name(self, project_name):
        config_file_arg = '{} {}'.format(
            stryker_constants.STRYKER_COMMAND_CONFIG_FILE_ARGUMENT_KEY, self.stryker_config_file_path)
        project_arg = '{} {}'.format(
            stryker_constants.STRYKER_COMMAND_PROJECT_ARGUMENT_KEY, project_name)
        return '{} {} {}'.format(stryker_constants.STRYKER_RUN_COMMAND, config_file_arg, project_arg)
