# AI Bias & Ethics

Ensuring fairness, transparency, and ethical compliance in AI systems.

## Key Technologies
- AIF360, fairness metrics

## Example
```python
from aif360.sklearn.metrics import ClassificationMetric
metric = ClassificationMetric(data)
print(metric.statistical_parity_difference())
```

## Integration Notes
- Used for bias detection, mitigation, and ethical audits.
- See [explainable_ai.md](explainable_ai.md) for interpretability tools.
