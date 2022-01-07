initialise:
    pip install -r requirements.txt

run-tests:
    python -m pytest ./tests/

run:
    python bmi_calculator/__init__.py