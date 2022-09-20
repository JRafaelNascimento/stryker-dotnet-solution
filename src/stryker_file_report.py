import stryker_mutant_report
import stryker_constants


class StrykerFileReport:
    file_name = ''
    mutants = []

    def __init__(self, file_name, file_json):
        self.file_name = file_name
        for mutant_json in file_json[stryker_constants.STRYKER_REPORT_FILE_MUTANTS_JSON_KEY]:
            self.mutants.append(
                stryker_mutant_report.StrykerMutantReport(mutant_json))

    def get_killed_mutants_count(self):
        count = 0
        for mutant_report in self.mutants:
            if mutant_report.is_killed():
                count += 1

        return count

    def get_considered_mutants_count(self):
        count = 0
        for mutant_report in self.mutants:
            if not mutant_report.is_ignored():
                count += 1

        return count
