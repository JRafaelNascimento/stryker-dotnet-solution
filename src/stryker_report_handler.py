import os
import shutil
import fnmatch
import stryker_constants
import stryker_report


class StrykerReportHandler:
    def __init__(self, stryker_report_folder_path):
        self.stryker_report_folder_path = stryker_report_folder_path

    def get_last_report(self):
        report_file_name = self.get_last_json_report_file_name()
        if report_file_name == '':
            return None

        return stryker_report.StrykerReport(report_file_name)

    def get_last_json_report_file_name(self):
        reports = self.get_all_json_reports_file_name()
        if len(reports) == 0:
            return ''

        return sorted(reports)[-1]

    def get_all_json_reports_file_name(self):
        return self.get_all_reports_with_file_name(stryker_constants.STRYKER_REPORT_FILE_NAME_JSON)

    def get_all_reports_with_file_name(self, file_name):
        result = []
        for root, dirs, files in os.walk(self.stryker_report_folder_path):
            for name in files:
                if fnmatch.fnmatch(name, file_name):
                    result.append(os.path.join(root, name))

        return result

    def rename_last_html_report_file_name(self, file_name):
        report_file_name = self.get_last_html_report_file_name()
        report_file_path = os.path.dirname(report_file_name)
        new_report_file_name = '{}/{}'.format(report_file_path, file_name)
        os.rename(report_file_name, new_report_file_name)

    def get_last_html_report_file_name(self):
        reports = self.get_all_html_reports_file_name()
        if len(reports) == 0:
            return ''

        return sorted(reports)[-1]

    def get_all_html_reports_file_name(self):
        return self.get_all_reports_with_file_name(stryker_constants.STRYKER_REPORT_FILE_NAME_HTML)

    def clean_all_reports(self):
        if os.path.exists(self.stryker_report_folder_path):
            shutil.rmtree(self.stryker_report_folder_path)
