import stryker_constants
import os


class StrykerDirectoryHandler:
    def __init__(self, config_file_path, test_project_file_path, stryker_config_file_path):
        self.work_directory = os.getcwd()
        self.config_multi_project_path = os.path.abspath(config_file_path)
        self.config_multi_project_directory = os.path.dirname(
            self.config_multi_project_path)

        self.go_to_config_multi_project_directory()

        self.stryker_config_path = os.path.abspath(stryker_config_file_path)
        self.stryker_config_directory = os.path.dirname(
            self.stryker_config_path)
        self.test_project_directory = os.path.abspath(test_project_file_path)
        self.stryker_output_directory = os.path.abspath(
            '{}/{}'.format(test_project_file_path, stryker_constants.STRYKER_REPORT_FOLDER_NAME))

        self.go_to_work_directory()

    def go_to_config_multi_project_directory(self):
        os.chdir(self.config_multi_project_directory)

    def go_to_test_project_directory(self):
        os.chdir(self.test_project_directory)

    def go_to_work_directory(self):
        os.chdir(self.work_directory)

    def print_directories(self):
        print('Stryker Directories:')
        print('\tWork Directory: {}'.format(self.work_directory))
        print('\tStryker Config Path: {}'.format(self.stryker_config_path))
        print('\tStryker Config Directory: {}'.format(
            self.stryker_config_directory))
        print('\tStryker Output Directory: {}'.format(
            self.stryker_output_directory))
        print('\tConfig Multi Project Path: {}'.format(
            self.config_multi_project_path))
        print('\tConfig Multi Project Directory: {}'.format(
            self.config_multi_project_directory))
        print('\tTest Project Directory: {}'.format(
            self.test_project_directory))
