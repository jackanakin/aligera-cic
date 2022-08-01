# Aligera Cic Reader
Lê por SSH uso de canal, para isso carrega devices.json onde:
1. command - Comando que a ser executado por SSH
2. regex - Regex para extrair as estatísticas do resultado do comando SSH. 
    Ex: alguma coisa bla bla [0/3/1.30] e ta ta ta --> após regex \[\d\/\d\/\d.(\d{1,2})] --> [0/3/1.30]
3. cics:CIC_MATCH - Instrução de "comando_apos_regex".contem(CIC_MATCH) para ser vinculado
    Ex: [0/3/1.30] contem "0/3/1." então é LDN

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