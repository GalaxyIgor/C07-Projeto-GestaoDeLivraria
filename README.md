# 📦 Projeto Gestão De Livraria

Este respositorio esta destinado so projeto de C07 - Disciplina de Bancos de Dados do INATEL, o projeto em si aborda um sistema de gerenciamento de uma livraria utilizando o BD MySQL
A dependencia de ambiente utilizada é o **Poetry**.

------------------------------------------------------------------------

## ⚙️ Requisitos

Antes de instalar, verifique se vc tem as seguintes ferramentas:
-   [Python 3.10+](https://www.python.org/downloads/)
-   [Poetry](https://python-poetry.org/docs/#installation)

------------------------------------------------------------------------

## 📥 Instalando o Poetry

### Linux / macOS

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to PATH (if needed):

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows (PowerShell)

``` powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

If the `poetry` command is not recognized, manually add it to PATH:

    C:\Users\<YOUR_USERNAME>\AppData\Roaming\Python\Scripts

------------------------------------------------------------------------

## 🚀 Running the project

Clone the repository:

``` bash
https://github.com/GalaxyIgor/C07-Projeto-GestaoDeLivraria.git
cd C07-Projeto-GestaoDeLivraria
```

Install dependencies:

``` bash
poetry install
```

Activate the virtual environment:

``` bash
poetry shell
```

------------------------------------------------------------------------

## 🧪 Running scripts

Run tests:

``` bash
poetry run pytest
```

Run application (example):

``` bash
poetry run python src/C07-Projeto-GestaoDeLivraria/GestaoLivraria/src/main.py
```

------------------------------------------------------------------------
-   [Poetry Documentation](https://python-poetry.org/docs/)

------------------------------------------------------------------------
