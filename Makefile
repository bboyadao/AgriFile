build:
	pyinstaller --name=AgriFile manage.py

cc:
	python -m "PyInstaller AgriFile.spec -y"


run:
	 .\dist\AgriFile\AgriFile.exe runserver --noreload


