# Model Deployment

!!! info "Planned Architecture (Future Phases)"
    Production model deployment and CI/CD pipeline are implemented in **Phase 6** (Weeks 21–24).

---

## Overview

<!-- Describe the deployment strategy: containerized model server behind FastAPI, loaded from MLflow registry -->

---

## Model Serving

### Integration with FastAPI

<!-- Describe how the ML model is loaded at startup and exposed via a /v1/predict endpoint -->

```python
import mlflow.pyfunc

model = mlflow.pyfunc.load_model("models:/FinSightSentiment/Production")
```

### Inference Endpoint

<!-- Describe the prediction endpoint: input schema, output schema, latency SLA -->

---

## Fallback Strategy

<!-- Describe model fallback: if production model fails validation, auto-revert to previous version -->

---

## CI/CD Pipeline

```mermaid
flowchart LR
    A[Push to main] --> B[GitHub Actions]
    B --> C[Run Tests]
    C --> D[Build Docker Image]
    D --> E[Push to Registry]
    E --> F[Deploy to Cloud]
    F --> G[Health Check]
```

### GitHub Actions Workflow

<!-- Describe workflow stages: test → build → push → deploy → smoke test -->

---

## Docker

<!-- Describe Dockerfile for the ML service, multi-stage build to keep image size minimal -->

---

## Monitoring in Production

<!-- Describe model performance monitoring: data drift detection, prediction distribution tracking, retraining triggers -->

---

## Infrastructure

<!-- Describe cloud deployment target, container orchestration (Docker Compose / Kubernetes), auto-scaling -->
