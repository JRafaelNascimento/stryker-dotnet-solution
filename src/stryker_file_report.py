import stryker_mutant_report
import stryker_constants


class StrykerFileReport:
    def __init__(self, file_name, file_json):
        self.file_name = file_name
        self.mutants = []
        for mutant_json in file_json[stryker_constants.STRYKER_REPORT_FILE_MUTANTS_JSON_KEY]:
            self.mutants.append(
                stryker_mutant_report.StrykerMutantReport(mutant_json))

    def get_detected_mutants_count(self):
        count = 0
        for mutant_report in self.mutants:
            if mutant_report.is_detected():
                count += 1

        return count

    def get_undetected_mutants_count(self):
        count = 0
        for mutant_report in self.mutants:
            if mutant_report.is_undetected():
                count += 1

        return count
