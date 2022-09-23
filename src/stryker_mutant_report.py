import stryker_constants


class StrykerMutantReport:
    def __init__(self, mutant_json):
        self.id = mutant_json[stryker_constants.STRYKER_REPORT_FILE_MUTANTS_ID_JSON_KEY]
        self.status = mutant_json[stryker_constants.STRYKER_REPORT_FILE_MUTANTS_STATUS_JSON_KEY]

    def is_detected(self):
        return self.status in stryker_constants.STRYKER_REPORT_MUTANT_DETECTED_STATUSES

    def is_undetected(self):
        return self.status in stryker_constants.STRYKER_REPORT_MUTANT_UNDETECTED_STATUSES
