## Os comandos listados são executados na raíz do projeto, aqui onde este arquivo README.md está localizado
> Configurações de acesso aos equipamentos colocar no arquivo '.env', seguir o exemplo do arquivo '.env.example'

### 1. Para instalar as dependências do Python
Cria ambiente virtual do python para não misturar dependências instaladas na máquina local
> python3 -m venv venv

Ativa o ambiente virtual do python criado acima
> source venv/bin/activate

Atualiza o versão do pip para a mais recente
> pip install --upgrade pip

Instala as dependências do programa com o pip
> pip install -r pip_install.txt

### 2. Rodando
Ativa o ambiente virtual do python
> source venv/bin/activate

Executar
> python src/run.py 