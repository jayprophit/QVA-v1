# Explainable AI (XAI)

Explainable AI provides transparency and interpretability for model predictions.

## Key Technologies
- SHAP, LIME

## Example
```python
import shap
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)
```

## Integration Notes
- Used for auditability, compliance, and user trust.
- Closely linked with AI ethics (see [bias_ethics.md](bias_ethics.md)).
