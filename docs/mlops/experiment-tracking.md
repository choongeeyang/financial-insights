# Experiment Tracking

!!! info "Planned Architecture (Future Phases)"
    MLflow experiment tracking and model registry are implemented in **Phase 6** (Weeks 21–24).

---

## Overview

<!-- Describe why experiment tracking matters: reproducibility, comparison, model rollback -->

---

## MLflow Setup

### Tracking Server

<!-- Describe MLflow server deployment: local for dev, remote backend store for production -->

```yaml
# MLflow backend store configuration
MLFLOW_TRACKING_URI: http://mlflow:5000
MLFLOW_ARTIFACT_ROOT: s3://finsight-mlflow-artifacts/
```

### Experiment Structure

<!-- Describe experiment hierarchy: project / model_type / run -->

---

## Logged Artifacts

| Artifact | Description |
|---|---|
| Parameters | Hyperparameters for each run |
| Metrics | Loss, accuracy, F1 per epoch |
| Model | Serialized model file |
| Feature importance | XGBoost feature charts |
| Confusion matrix | Classification diagnostics |

---

## Model Registry

<!-- Describe model lifecycle stages: Staging → Production → Archived -->

### Promotion Criteria

<!-- Describe what metric thresholds must be met to promote a model to production -->

### Version Pinning

<!-- Describe how the serving layer references a specific model version -->

---

## Integration with CI/CD

<!-- Describe how training runs are triggered by GitHub Actions on data updates or manual dispatch -->
