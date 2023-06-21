PYTHON_INTERPRETER = python3
MAIN_FILE = VMTranslator.py
OUTPUT_FILE = VMTranslator
OUTPUT_DIR = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
EXECUTABLE = $(OUTPUT_DIR)$(OUTPUT_FILE)
REQUIREMENTS_FILE = requirements.txt

all: VMTranslator

VMTranslator:
	${PYTHON_INTERPRETER} -m pip install -r $(REQUIREMENTS_FILE)
	$(PYTHON_INTERPRETER) -m PyInstaller --onefile $(MAIN_FILE) --distpath $(OUTPUT_DIR) --name $(OUTPUT_FILE)
	chmod +x $(EXECUTABLE)

clean:
	rm -rf build
	rm -f $(EXECUTABLE)
	rm -f $(EXECUTABLE).spec
