import json
import stryker_file_report
import stryker_constants


class StrykerReport:
    schema_version = ''
    threshold_high = 0
    threshold_low = 0
    file_reports = []

    def __init__(self, report_file_name):
        report_json = self.get_json_from_file(report_file_name)

        self.schema_version = report_json[stryker_constants.STRYKER_REPORT_SCHEMA_VERSION_JSON_KEY]
        self.threshold_high = report_json[stryker_constants.STRYKER_REPORT_THRESHOLDS_JSON_KEY][
            stryker_constants.STRYKER_REPORT_THRESHOLDS_HIGH_JSON_KEY]
        self.threshold_low = report_json[stryker_constants.STRYKER_REPORT_THRESHOLDS_JSON_KEY][
            stryker_constants.STRYKER_REPORT_THRESHOLDS_LOW_JSON_KEY]

        for file_name in report_json[stryker_constants.STRYKER_REPORT_FILE_JSON_KEY].keys():
            self.file_reports.append(stryker_file_report.StrykerFileReport(
                file_name, report_json[stryker_constants.STRYKER_REPORT_FILE_JSON_KEY][file_name]))

    def get_json_from_file(self, report_file_name):
        with open(report_file_name) as report_file:
            return json.load(report_file)

    def get_mutation_score(self):
        considered_mutants_count = self.get_considered_mutants_count()
        if considered_mutants_count == 0:
            return 100.0

        killed_mutants_count = self.get_killed_mutants_count()
        return (float(killed_mutants_count)/considered_mutants_count) * 100.0

    def get_killed_mutants_count(self):
        count = 0
        for file_report in self.file_reports:
            count += file_report.get_killed_mutants_count()

        return count

    def get_considered_mutants_count(self):
        count = 0
        for file_report in self.file_reports:
            count += file_report.get_considered_mutants_count()

        return count
