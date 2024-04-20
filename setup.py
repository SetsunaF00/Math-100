from cx_Freeze import setup, Executable

# Ścieżka do pliku ikony
icon_file = "resources/favicon.ico"

setup(
    name="Math100",
    version="0.1",
    description="Prosta gra matematyczna",
    executables=[Executable("Math100.py", base="Win32GUI", icon=icon_file)],
)
