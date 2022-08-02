# Aligera Cic Reader
Lê por SSH uso de canal, para isso carrega "json/devices.json" onde:
1. command - Comando que a ser executado por SSH
2. regex - Regex para extrair as estatísticas do resultado do comando SSH. 
    Ex: alguma coisa bla bla [0/3/1.30] e ta ta ta --> após regex \[\d\/\d\/\d.(\d{1,2})] --> [0/3/1.30]
3. cics:CIC_MATCH - Instrução de "comando_apos_regex".contem(CIC_MATCH) para ser vinculado
    Ex: [0/3/1.30] contem "0/3/1." então é LDN

### Rodando/Deploy

## 1. Docker

> docker run -d -it -p 8000:8000 -v "$(pwd)"/json:/opt/json jackanakin/aligera-cic

## 2. Manual

Cria ambiente virtual do python para não misturar dependências instaladas na máquina local
> python3 -m venv venv

Ativa o ambiente virtual do python criado acima
> source venv/bin/activate

Atualiza o versão do pip para a mais recente
> pip install --upgrade pip

Instala as dependências do programa com o pip
> pip install -r pip_install.txt

Executar
> python src/http-server.py

## 3. Acessando

http://localhost:8000

## 4. Resultado

![alt text](https://github.com/jackanakin/aligera-cic/blob/main/result.png?raw=true)