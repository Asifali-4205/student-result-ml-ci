import json
import sys

MINIMUM_ACCURACY = 0.85


def main():
    print("Reading model evaluation metrics...")

    try:
        with open("metrics.json", "r", encoding="utf-8") as file:
            metrics = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"Unable to read metrics.json: {error}")
        sys.exit(1)

    if "accuracy" not in metrics:
        print("QUALITY GATE FAILED")
        print("The metrics file does not contain an accuracy value.")
        sys.exit(1)

    accuracy = float(metrics["accuracy"])

    print("Model Accuracy :", round(accuracy, 4))
    print("Required Accuracy:", MINIMUM_ACCURACY)

    if accuracy < MINIMUM_ACCURACY:
        print("QUALITY GATE FAILED")
        print("Model performance is below the required threshold.")
        sys.exit(1)

    print("QUALITY GATE PASSED")
    print("Model performance satisfies the required threshold.")
    sys.exit(0)


if __name__ == "__main__":
    main()
