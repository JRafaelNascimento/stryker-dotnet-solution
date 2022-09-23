import argparse


class StrykerArgumentHandler:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Run Stryker Multi Project.')
        parser.add_argument(
            '--config-file', help='JSON configuration file path', required=True)

        args = parser.parse_args()
        self.config_file = args.config_file
