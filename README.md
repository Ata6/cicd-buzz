# Automation - Ata6

De buzz-generator uit het werkboek, met Flask als webapp.
Bij het verversen krijg je steeds een andere zin.

Starten met `python app.py` en dan naar http://localhost:5000 gaan.
Installeer eerst de packages met `pip install -r requirements.txt`.

De drie tests staan in `tests/test_generator.py`:

```sh
python -m pytest -v tests/test_generator.py
```

GitHub Actions draait flake8 en deze tests bij een push naar main.
Het Dockerfile is voor de containeropdracht.
