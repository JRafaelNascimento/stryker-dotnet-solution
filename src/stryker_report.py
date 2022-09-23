import json
import stryker_file_report
import stryker_constants


class StrykerReport:
    def __init__(self, report_file_name):
        report_json = self.get_json_from_file(report_file_name)

        self.schema_version = report_json[stryker_constants.STRYKER_REPORT_SCHEMA_VERSION_JSON_KEY]
        self.threshold_high = report_json[stryker_constants.STRYKER_REPORT_THRESHOLDS_JSON_KEY][
            stryker_constants.STRYKER_REPORT_THRESHOLDS_HIGH_JSON_KEY]
        self.threshold_low = report_json[stryker_constants.STRYKER_REPORT_THRESHOLDS_JSON_KEY][
            stryker_constants.STRYKER_REPORT_THRESHOLDS_LOW_JSON_KEY]

        self.file_reports = []
        for file_name in report_json[stryker_constants.STRYKER_REPORT_FILE_JSON_KEY].keys():
            self.file_reports.append(stryker_file_report.StrykerFileReport(
                file_name, report_json[stryker_constants.STRYKER_REPORT_FILE_JSON_KEY][file_name]))

    def get_json_from_file(self, report_file_name):
        with open(report_file_name) as report_file:
            return json.load(report_file)

    def get_mutation_score(self):
        detected_mutants_count = self.get_detected_mutants_count()
        undetected_mutants_count = self.get_undetected_mutants_count()
        total_mutants_count = detected_mutants_count + undetected_mutants_count
        if total_mutants_count == 0:
            return 100.0

        return (float(detected_mutants_count)/total_mutants_count) * 100.0

    def get_detected_mutants_count(self):
        count = 0
        for file_report in self.file_reports:
            count += file_report.get_detected_mutants_count()

        return count

    def get_undetected_mutants_count(self):
        count = 0
        for file_report in self.file_reports:
            count += file_report.get_undetected_mutants_count()

        return count
