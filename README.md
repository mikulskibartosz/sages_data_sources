# Jak uruchomić testy

## Przed uruchomieniem

```bash
pipenv install --dev
pipenv shell
```

Jeśli używasz MacOS i nie można zainstalować `numpy`: `export SYSTEM_VERSION_COMPAT=1` przed `pipenv install --dev`

## Uruchamianie testów

```bash
pytest
```

## Uruchomienie jednego pliku

Przykład:

```bash
pytest tests/csv/test_load_csv.py
```

## Uruchomienie jednego testu

```bash
pytest -k nazwa_testu
```