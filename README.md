[![CI](https://github.com/Ibrahim-56/Quality-Excellence-through-Agentic-AI/actions/workflows/tests.yml/badge.svg)](https://github.com/Ibrahim-56/Quality-Excellence-through-Agentic-AI/actions/workflows/tests.yml)

# Quality Excellence through Agentic AI

A small Python prototype exploring a rule-based quality-monitoring workflow. It evaluates quality metrics against thresholds and generates simple follow-up recommendations.

## Current implementation

- `QualityMetric` stores a metric name, value, and threshold.
- `MonitoringAgent` flags metrics whose values fall below their thresholds.
- `RecommendationAgent` produces a text recommendation for each alert.
- `app.py` includes a sample run with illustrative metric values.
- `test_app.py` contains unit tests for alert detection and recommendation generation.

Despite the project name, the current code is a basic rule-based prototype; it does not yet implement autonomous AI agents, integrations, compliance engines, or root-cause analysis.

## Run

Requires Python 3.10 or later. No third-party packages are needed for the current prototype.

```bash
python app.py
python -m unittest discover -v
```

## Continuous integration

GitHub Actions runs the unit tests on pushes and pull requests targeting `main`.

## Next steps

- Define metric sources and data validation.
- Separate rules from reporting.
- Add tests for missing, invalid, and boundary values.
- Document any future AI or external-service integrations only after implementation.
