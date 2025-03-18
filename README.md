# 🏦 Sistema de Contas Bancárias

📌 **Status Atual:** Em desenvolvimento
📌 **Próximos passos:** Implementação da persistência de dados com JSON

Um **Sistema de Contas Bancárias** simples e funcional desenvolvido em **Python**. O sistema atualmente permite criar contas, realizar depósitos, saques e consultar saldo. O próximo passo será implementar a **persistência de dados em JSON**, garantindo que as contas sejam salvas e carregadas automaticamente.

## 🚀 Funcionalidades Implementadas
✅ Criar contas bancárias com titular e saldo inicial  
✅ Realizar depósitos  
✅ Realizar saques com validação de saldo  
✅ Consultar saldo da conta  

## 📌 Próximos Passos
🔹 Implementar a **persistência de dados** com JSON  
🔹 Criar um **menu interativo** no terminal  
🔹 Melhorar a **exibição de informações**  
🔹 Implementar **tratamento de erros** para evitar entradas inválidas  

## 📌 Tecnologias Utilizadas
- **Python 3**
- **Programação Orientada a Objetos (POO)**
- **Manipulação de arquivos JSON** (em andamento)
- **Estruturas de repetição e condicionais** para controle de fluxo

---

## 📂 Estrutura do Projeto
```
📦 Sistema-de-Contas-Bancarias
 ├── 📜 main.py          # Arquivo principal do programa
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

📌 **Obs:** A funcionalidade de persistência de dados em JSON ainda será implementada. No momento, os dados das contas não são salvos após o encerramento do programa.

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

## 🏗 **Trecho do Código (Exemplo da Classe ContaBancaria)**
```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo if saldo >= 0 else 0  # Evita saldo negativo inicial

    def __str__(self):
        return f"Conta de {self.titular} | Saldo: R$ {self.saldo:.2f}"
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

