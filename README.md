# Instalacja

W jednym z zadań będziemy używać Selenium.

Selenium wymaga zainstalowania sterownika dla zaintalowanej przeglądarki. Proszę skorzytać z listy i instrukcji na tej stronie: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

# Jak uruchomić testy

## Przed uruchomieniem

Używamy Python 3.9, ale prawdopodobnie każda wersja powyżej 3.7 zadziała.

### Pipenv

Jeśli używasz Pipenv

```bash
pipenv install --dev
pipenv shell
```

Jeśli używasz MacOS i nie można zainstalować `numpy`: `export SYSTEM_VERSION_COMPAT=1` przed `pipenv install --dev`

### Jeśli używasz Python virtual env

```bash
python3 -m venv ven
source ven/bin/activate
pip3 install -r requirements.txt
```

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