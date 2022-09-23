## Stryker .NET Mutation Test Solution

Python Script to run Stryker .NET for a solution.

## Usage
Runs the following bash command:
```bash
python3 src/stryker.py --config-file stryker-multi-project-config.json
```

Parameters include:
- **--config-file**: Path to Stryker .NET Solution configuration file.

## Configuration
- **stryker-multi-projects-config**
  - **projects-to-test**
    - Project list to be mutated, should be include only the .csproj filename.
  - **test-project-path**
    - Root path of unit test project.
  - **stryker-config-file**
    - Configuration file path of Stryker. [Read More](https://stryker-mutator.io/docs/stryker-net/configuration/)

### Restrictions to Stryker Configuration
- **project**
  - This configuration shouldn't be used as it will be configured by the Python Script.
- **reporters**
  - Must add **json** for report as it will be used by Python Script to calculate mutation score, no matter others.

## Release notes

**New in 1.0.0**
- Runs Stryker .NET Mutation tests for all configured projects.

## Related Links

- [Stryker VSS Extension Repository](https://github.com/JRafaelNascimento/stryker-vss-ext)