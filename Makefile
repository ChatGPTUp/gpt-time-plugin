.PHONY: setup run clean

setup: requirements.txt
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run: setup
	. .venv/bin/activate && uvicorn main:app --reload --port 1037

clean: 
	rm -rf .venv