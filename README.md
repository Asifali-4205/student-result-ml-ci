# Student Result Prediction ML CI

This practical demonstrates a small machine-learning pipeline with a model-quality gate using GitHub Actions.

## What it does
- Generates a reproducible dataset containing 300 student records.
- Trains a scikit-learn Logistic Regression model using attendance, internal marks, assignment marks, and previous score.
- Evaluates the model and saves accuracy metrics to `metrics.json`.
- Runs a quality gate that requires at least **0.85 (85%) accuracy**.
- Stops the workflow before automated tests if the model accuracy is below the threshold.
- Runs seven automated tests when the quality gate passes.

## Pipeline flow
1. Install Python dependencies.
2. Train the student-result model.
3. Generate `metrics.json`.
4. Run `quality_gate.py` to compare accuracy with the 0.85 threshold.
5. If the gate passes, run automated ML tests; if it fails, stop the workflow.

## Run locally
```bash
python -m pip install -r requirements.txt
python train_model.py
python quality_gate.py
python -m unittest discover -v
```

## GitHub Actions
The workflow in `.github/workflows/ml-ci.yml` runs on pushes and pull requests to `main`, and can also be started manually from the Actions tab.

Generated files (`student_results.csv`, `student_result_model.pkl`, and `metrics.json`) are created in the workflow runner and are not committed automatically.

## Demonstrating a failure
For a controlled demonstration, temporarily change `MINIMUM_ACCURACY` in `quality_gate.py` from `0.85` to `0.99`, commit the change, and inspect the failed Actions run. Restore `0.85` afterward and verify that the workflow succeeds again.
