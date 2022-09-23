import json
import stryker_constants


class StrykerMultiProjectsConfig:
    def __init__(self, config_file_path):
        with open(config_file_path) as config_file:
            config_json = json.load(config_file)

        self.projects_to_test = config_json[stryker_constants.STRYKER_MULTI_PROJECTS_CONFIG_JSON_KEY][
            stryker_constants.STRYKER_MULTI_PROJECTS_CONFIG_PROJECTS_TO_TEST_JSON_KEY]
        self.test_project_path = config_json[stryker_constants.STRYKER_MULTI_PROJECTS_CONFIG_JSON_KEY][
            stryker_constants.STRYKER_MULTI_PROJECTS_CONFIG_TEST_PROJECT_PATH_JSON_KEY]
        self.stryker_config_file = config_json[stryker_constants.STRYKER_MULTI_PROJECTS_CONFIG_JSON_KEY][
            stryker_constants.STRYKER_MULTI_PROJECTS_CONFIG_STRYKER_CONFIG_FILE_JSON_KEY]

    def print_config(self):
        print('Stryker Multi Project Config:')
        print('\tProjects to Test: {}'.format(self.projects_to_test))
        print('\tTest Project Path: {}'.format(
            self.test_project_path))
        print('\tStryker Config File: {}'.format(self.stryker_config_file))
