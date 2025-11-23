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

Add Poetry p/ PATH (se nescessario):

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows (PowerShell)

``` powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
Se o comando `poetry` não for reconhecido, adicione-o manualmente ao PATH:

    C:\Users\<YOUR_USERNAME>\AppData\Roaming\Python\Scripts

------------------------------------------------------------------------

## 🚀 Rodando o Projeto

Clone the repository:

``` bash
https://github.com/GalaxyIgor/C07-Projeto-GestaoDeLivraria.git
cd C07-Projeto-GestaoDeLivraria
```

Instalando as dependências:

``` bash
poetry install
```

Ativiando ambiente virtual:

``` bash
poetry shell
```

------------------------------------------------------------------------

## 🧪 Rodando os Scripts

Rodadndo testes:

``` bash
poetry run pytest
```

Rodadndo apicações (exemplo):

``` bash
poetry run python src/C07-Projeto-GestaoDeLivraria/GestaoLivraria/src/main.py
```

------------------------------------------------------------------------
-   [Poetry Documentation](https://python-poetry.org/docs/)

------------------------------------------------------------------------
