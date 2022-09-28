import stryker_config
import stryker_multi_project_config
import stryker_runner
import stryker_report_handler
import stryker_directory_handler
import stryker_argument_handler
import stryker_constants


class StrykerMultiProjectRunner:
    def __init__(self):
        self.stryker_argument_handler = stryker_argument_handler.StrykerArgumentHandler()
        self.stryker_multi_project_config = stryker_multi_project_config.StrykerMultiProjectsConfig(
            self.stryker_argument_handler.config_file)
        self.stryker_directory_handler = stryker_directory_handler.StrykerDirectoryHandler(
            self.stryker_argument_handler.config_file, self.stryker_multi_project_config.test_project_path, self.stryker_multi_project_config.stryker_config_file)

        self.stryker_directory_handler.go_to_config_multi_project_directory()
        self.stryker_config = stryker_config.StrykerConfig(
            self.stryker_multi_project_config.stryker_config_file)
        self.stryker_directory_handler.go_to_work_directory()

        self.stryker_report_handler = stryker_report_handler.StrykerReportHandler(
            self.stryker_directory_handler.stryker_output_directory)
        self.stryker_runner = stryker_runner.StrykerRunner(
            self.stryker_directory_handler.stryker_config_path)

    def run(self):
        self.stryker_config.print_config()
        self.stryker_multi_project_config.print_config()
        self.stryker_report_handler.clean_all_reports()

        self.stryker_directory_handler.go_to_test_project_directory()
        for project_name in self.stryker_multi_project_config.projects_to_test:
            self.run_for_project(project_name)
        self.stryker_directory_handler.go_to_work_directory()

    def run_for_project(self, project_name):
        self.stryker_runner.run_mutation_for_project(project_name)

        report = self.stryker_report_handler.get_last_report()
        self.validate_report(report)
        self.rename_last_html_report_file_name(project_name)

        if not self.is_report_successful(project_name, report):
            self.run_failed()

    def validate_report(self, report):
        if report == None:
            self.print_error('Failed to load reports')
            self.run_failed()

    def rename_last_html_report_file_name(self, project_name):
        new_report_file_name = '{}.{}'.format(
            project_name, stryker_constants.STRYKER_REPORT_HTML_FILE_EXTENSION)
        self.stryker_report_handler.rename_last_html_report_file_name(
            new_report_file_name)

    def print_error(self, msg):
        print('ERR: {}'.format(msg))

    def run_failed(self):
        self.stryker_directory_handler.go_to_work_directory()
        exit(1)

    def is_report_successful(self, project_name, report):
        mutation_score = report.get_mutation_score()
        self.print_result(project_name, mutation_score)

        return self.is_mutation_score_successful(mutation_score)

    def print_result(self, project_name, mutation_score):
        print('Result:')
        print('\tProject Name: {}'.format(project_name))
        print('\tMutation Score: {}%'.format(str(round(mutation_score, 2))))

        if not self.is_mutation_score_successful(mutation_score):
            print('\tStatus: Failed')
            return

        print('\tStatus: Success')

    def is_mutation_score_successful(self, mutation_score):
        return mutation_score >= self.stryker_config.threshold_break
