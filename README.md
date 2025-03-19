# 🏦 Sistema de Contas Bancárias

📌 **Status Atual:** Persistência de dados implementada!
📌 **Próximos passos:** Criar menu interativo para interação do usuário

Um **Sistema de Contas Bancárias** simples e funcional desenvolvido em **Python**. O sistema permite criar contas, realizar depósitos, saques, consultar saldo e agora **salva e carrega contas automaticamente** com **JSON**.

## 🚀 Funcionalidades Implementadas
✅ Criar contas bancárias com titular e saldo inicial  
✅ Realizar depósitos  
✅ Realizar saques com validação de saldo  
✅ Consultar saldo da conta  
✅ Salvar contas automaticamente em JSON  
✅ Carregar contas salvas ao iniciar o programa  

## 📌 Próximos Passos
🔹 Criar um **menu interativo** no terminal para facilitar a navegação  
🔹 Melhorar a **exibição de informações** das contas  
🔹 Implementar **tratamento de erros** para evitar entradas inválidas  

## 📌 Tecnologias Utilizadas
- **Python 3**
- **Programação Orientada a Objetos (POO)**
- **Manipulação de arquivos JSON**
- **Estruturas de repetição e condicionais** para controle de fluxo

---

## 📂 Estrutura do Projeto
```
📦 Sistema-de-Contas-Bancarias
 ├── 📜 main.py          # Arquivo principal do programa
 ├── 📜 contas.json      # Armazena as contas registradas
 ├── 📜 README.md        # Documentação do projeto
```

---

## 🔧 **Pré-requisitos**
Antes de começar, verifique se você tem os seguintes requisitos instalados:

- **Python 3.x** instalado na máquina

Para verificar a instalação do Python:
```sh
python --version  # Ou python3 --version
```

---

## 💻 **Como Executar o Projeto**

1️⃣ **Clone o repositório:**
```sh
git clone https://github.com/Thiago-c-souza/Sistema-de-Contas-Bancarias.git
```

2️⃣ **Acesse a pasta do projeto:**
```sh
cd Sistema-de-Contas-Bancarias
```

3️⃣ **Execute o programa:**
```sh
python main.py
```

📌 **Obs:** O arquivo `contas.json` será criado automaticamente ao adicionar contas. Caso já existam contas registradas, elas serão carregadas ao iniciar o programa.

---

## 🛠 **Como Usar**
Quando o programa for executado, o seguinte menu aparecerá:
```
🏦 Sistema de Contas Bancárias
1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Consultar Saldo
5 - Sair
```

🔹 **Opções disponíveis:**
- **1:** Criar uma nova conta bancária.
- **2:** Digitar o valor e depositar na conta.
- **3:** Digitar o valor e sacar da conta (se houver saldo suficiente).
- **4:** Exibir o saldo atual da conta.
- **5:** Encerrar o programa.

---

## 🏗 **Trecho do Código (Exemplo da Persistência de Dados)**
```python
import json

def salvar_contas(contas):
    with open("contas.json", "w") as arquivo:
        json.dump([conta.__dict__ for conta in contas], arquivo, indent=4)

def carregar_contas():
    try:
        with open("contas.json", "r") as arquivo:
            contas_dados = json.load(arquivo)
            return [ContaBancaria(**conta) for conta in contas_dados]
    except FileNotFoundError:
        return []
```

---

## 📌 **Possíveis Melhorias Futuras**
🔹 Implementar múltiplas contas para um único usuário  
🔹 Criar um histórico de transações  
🔹 Implementar autenticação com senha  
🔹 Criar interface gráfica com Tkinter ou PyQt  
🔹 Integrar com um banco de dados (SQLite ou PostgreSQL)  

---

## 🤝 **Contribuição**
Se quiser contribuir para o projeto:
1. **Faça um fork** do repositório
2. **Crie uma branch** com a nova funcionalidade: `git checkout -b minha-feature`
3. **Faça um commit das alterações**: `git commit -m 'Adicionando nova feature'`
4. **Envie para o GitHub**: `git push origin minha-feature`
5. **Abra um Pull Request`

---

📌 **Criado por Thiago Caixeta de Souza** 🚀

