# Adhyaya 9: Explainable AI (XAI)

---

### **Mangala Shloka (Invocation)**

```text
Om! May the light of explanation dispel the darkness of uncertainty and foster trust in intelligence.
```

---

## **Shloka 9.1: Principle**
Explainable AI provides transparency and interpretability for model predictions.

## **Shloka 9.2: Key Technologies**
- SHAP, LIME

## **Shloka 9.3: Example**
```python
import shap
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)
```

## **Shloka 9.4: Integration Commentary**
- Used for auditability, compliance, and user trust.
- Closely linked with AI ethics (see [bias_ethics.md](bias_ethics.md)).

---

### **Phala Shruti (Result)**
- Increases transparency and accountability in AI-driven systems.

---

### **Prasthana (Closing Invocation)**

```text
May this explanation module reveal the reasons behind every decision. Om Shanti!
```
