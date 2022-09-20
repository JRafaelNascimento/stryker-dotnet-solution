import json
import stryker_constants


class StrykerConfig:
    threshold_break = 0

    def __init__(self, config_file_path):
        with open(config_file_path) as config_file:
            config_json = json.load(config_file)

        self.threshold_break = config_json[stryker_constants.STRYKER_CONFIG_JSON_KEY][
            stryker_constants.STRYKER_CONFIG_THRESHOLDS_JSON_KEY][stryker_constants.STRYKER_CONFIG_THRESHOLDS_BREAK_JSON_KEY]

    def print_config(self):
        print('Stryker Config:')
        print('\tThreshold Break: {}'.format(self.threshold_break))
