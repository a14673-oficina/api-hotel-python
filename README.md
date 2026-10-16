# API Hotel Python 🏨

Uma API básica desenvolvida em Python para a gestão de um sistema de hotel, permitindo o controlo de quartos, clientes e reservas.

## 🚀 Funcionalidades

* **Gestão de Quartos:** Cadastro, visualização e atualização de status dos quartos (disponível, ocupado, manutenção).
* **Gestão de Hóspedes:** Registo e consulta de dados de clientes.
* **Sistema de Reservas:** Criação, cancelamento e verificação de disponibilidade de reservas.

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem principal)
* **Framework:** *[Ex: Flask]*
* **Base de Dados:** *[Ex: SQLite/ MySQL]*

## 📦 Como Executar o Projeto

### Pré-requisitos
Antes de começar, certifica-te de que tens o **Python 3.x** e o **pip** instalados na tua máquina.

### Passos para instalação:

1. **Clona o repositório:**
   ```bash
   git clone https://github.com
   cd api-hotel-python
   ```

2. **Cria e ativa um ambiente virtual (opcional, mas recomendado):**
   ```bash
   # No Linux/macOS:
   python3 -m venv venv
   source venv/bin/activate

   # No Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instala as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executa a aplicação:**
   ```bash
   python main.py
   ```
   *(Nota: Substitui `main.py` pelo ficheiro principal do teu projeto, se for diferente).*

## 📌 Rotas da API (Exemplos)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| **GET** | `/quartos` | Listar todos os quartos |
| **POST** | `/reservas` | Criar uma nova reserva |
| **GET** | `/hospedes` | Listar clientes registados |

---
Desenvolvido como parte do projeto de oficina.
