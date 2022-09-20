import stryker_constants


class StrykerMutantReport:
    id = ''
    status = ''

    def __init__(self, mutant_json):
        self.id = mutant_json[stryker_constants.STRYKER_REPORT_FILE_MUTANTS_ID_JSON_KEY]
        self.status = mutant_json[stryker_constants.STRYKER_REPORT_FILE_MUTANTS_STATUS_JSON_KEY]

    def is_ignored(self):
        return self.status in stryker_constants.STRYKER_REPORT_IGNORED_STATUSES

    def is_killed(self):
        return self.status in stryker_constants.STRYKER_REPORT_KILLED_STATUS
