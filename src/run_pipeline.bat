@echo off

REM IMPORTANT: This batch file must be located in the 'src' folder
REM (e.g., newsapi-keyword-ranker/src/run_pipeline.bat)

REM Get the directory where this batch file (run_pipeline.bat) is located.
set "BATCH_FILE_DIR=%~dp0"

REM Navigate UP one level to the project root (newsapi-keyword-ranker).
REM This changes the current working directory for the subsequent python command.
cd /d "%BATCH_FILE_DIR%.."

REM Execute the Python script.
REM Now, the Python script's CWD will be the project root.
REM So, 'charts/' will correctly refer to newsapi-keyword-ranker/charts/.
REM Ensure the path to your python.exe is correct.
REM The path to daily_keyword_pipeline.py is relative to the new CWD (the project root).
"C:\YourPythonEnvironmentFolder\python.exe" "src\daily_keyword_pipeline.py"

REM Optional: Keep the window open if there are errors (for testing)
pause