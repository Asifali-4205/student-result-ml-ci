# Student Result Prediction ML CI

This practical demonstrates a small machine-learning pipeline with GitHub Actions.

## What it does
- Generates a reproducible dataset containing 300 student records.
- Trains a scikit-learn Logistic Regression model using attendance, internal marks, assignment marks, and previous score.
- Evaluates the model and saves accuracy metrics.
- Runs seven automated tests on the generated dataset, model, metrics, and predictions.

## Run locally
```bash
python -m pip install -r requirements.txt
python train_model.py
python -m unittest discover -v
```

## GitHub Actions
The workflow in `.github/workflows/ml-ci.yml` runs on pushes and pull requests to `main`, and can also be started manually from the Actions tab.

Generated files (`student_results.csv`, `student_result_model.pkl`, and `metrics.json`) are created in the workflow runner and are not committed automatically.
