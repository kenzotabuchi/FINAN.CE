
# FINAN.CE
Sistema web de finanças pessoais.

## Como rodar o projeto
### 1 - Clonar o repositório
```
git clone https://github.com/kenzotabuchi/FINAN.CE.git
cd seu-repositorio
```

### 2 - Instalar o Python e o Pip
Verifique se você tem o Python (versão 3+) e o Pip (versão 24+) instalado no seu computador
```
python --version
pip --version
```

Caso não estejam instalados, baixe e instale o Python em:
https://www.python.org/downloads/

E instale o pip seguindo a documentação:
https://pip.pypa.io/en/stable/installation/

### 3 - Criar um ambiente virtual
No diretório onde você clonou o repositório, crie um ambiente virtual com os seguintes comandos
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

Faça isso no terminal no seu sistema ou IDE.

### 4 - Instalar dependências
No terminal execute
```
pip install -r requirements.txt
```

Assim você irá instalar todos os pacotes necessários para o funcionamento do projeto.

### 5 - Rodar o projeto
Com o ambiente virtual ativo, faça as migrações do projeto Django
```
python manage.py migrate  # Aplicar migrações do banco de dados
python manage.py runserver  # Iniciar o servidor local
```
Acesse o projeto em: http://127.0.0.1:8000/








