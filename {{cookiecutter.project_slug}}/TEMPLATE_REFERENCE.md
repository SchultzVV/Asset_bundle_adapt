# Cookiecutter Template: Databricks Asset Bundle + CI/CD

Each section is a file that will be generated in your new repo. Variables like {{cookiecutter.project_slug}} will be replaced with your chosen values.

- README.md
- pyproject.toml
- databricks.yml
- .gitignore
- .env.example
- Makefile
- .devcontainer/devcontainer.json
- .github/workflows/databricks-ci.yml (optional)
- azure-pipelines.yml (optional)
- src/{{cookiecutter.project_slug}}/__init__.py
- src/{{cookiecutter.project_slug}}/mock.py
- src/{{cookiecutter.project_slug}}/main.py
- tests/test_mock.py

See the template repo for details.
