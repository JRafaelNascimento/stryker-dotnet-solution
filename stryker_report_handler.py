import os
import shutil
import fnmatch
import stryker_constants
import stryker_report


class StrykerReportHandler:
    stryker_report_folder_path = ''

    def __init__(self, stryker_report_folder_path):
        self.stryker_report_folder_path = stryker_report_folder_path

    def get_last_report(self):
        report_file_name = self.get_last_report_file_name()
        if report_file_name == '':
            return None

        return stryker_report.StrykerReport(report_file_name)

    def get_last_report_file_name(self):
        reports = self.get_all_report_file_names()
        if len(reports) == 0:
            return ''

        return sorted(reports)[-1]

    def get_all_report_file_names(self):
        result = []
        for root, dirs, files in os.walk(self.stryker_report_folder_path):
            for name in files:
                if fnmatch.fnmatch(name, stryker_constants.STRYKER_REPORT_FILE_NAME):
                    result.append(os.path.join(root, name))

        return result

    def clean_all_reports(self):
        if os.path.exists(self.stryker_report_folder_path):
            shutil.rmtree(self.stryker_report_folder_path)
