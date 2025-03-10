#!/usr/bin/python
import paramiko

"""
Script para conexão SSH e execução de comandos remotamente.

COMO EXECUTAR:
1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca necessária com: pip install paramiko
3. Execute o script no terminal com: python nome_do_arquivo.py
4. Insira os dados quando solicitado:
   - IP do servidor remoto
   - Nome de usuário SSH
   - Senha do usuário
   - Comando a ser executado no servidor
5. O script se conectará ao servidor, executará o comando e exibirá a saída.

OBSERVAÇÕES:
- O servidor SSH precisa estar configurado e acessível.
- Caso tenha problemas de permissão, use uma chave SSH em vez de senha.
- Este script aceita automaticamente chaves de host desconhecidas.
"""

# Solicita as informações ao usuário
ip = input('Qual IP? ')
username = input('Qual username? ')  
password = input('Qual a senha? ')
comando = input('Qual comando deseja executar? ')

# Cria um cliente SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Aceita automaticamente chaves desconhecidas

try:
    # Conecta ao servidor
    ssh.connect(ip, username=username, password=password)
    
    # Executa o comando
    stdin, stdout, stderr = ssh.exec_command(comando)

    # Exibe a saída do comando
    print("\nSaída do comando:")
    print(stdout.read().decode())  # Decodifica para string legível

    # Exibe erros, se houver
    erro = stderr.read().decode()
    if erro:
        print("\nErro:", erro)

except Exception as e:
    print(f"\nErro ao conectar ou executar comando: {e}")

finally:
    ssh.close()  # Fecha a conexão para evitar problemas
