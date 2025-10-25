🏥 ClinicHub
Um sistema de agendamento e gerenciamento de pacientes intuitivo, projetado para clínicas de pequeno porte.

🌟 Descrição do Projeto
O ClinicHub é uma aplicação de desktop desenvolvida em Python com a biblioteca PySide6 (Qt for Python), com o objetivo de facilitar a gestão diária de uma clínica de pequeno porte. Ele oferece uma interface gráfica amigável para visualizar o quadro de pacientes, o corpo clínico e o calendário de atividades, além de funcionalidades essenciais para o gerenciamento de consultas.

✨ Funcionalidades
O sistema está estruturado em torno de três telas principais, acessíveis através de um menu lateral:

Início (Dashboard):

Exibe cards de estatísticas rápidas: "Consultas Hoje", "Pacientes Ativos" e "Médicos".

Contém um calendário interativo (QCalendarWidget) para visualização e seleção de datas.

Botões de ação rápida: "Novo Paciente", "Adicionar Consulta" e "Cancelar".

Pacientes:

Lista todos os pacientes cadastrados através de cards informativos em uma área de rolagem.

Cada card de paciente exibe: Nome, ID e Condição atual.

Corpo Clínico (Médicos):

Lista todos os médicos da clínica em cards específicos.

Cada card de médico exibe: Nome, Especialidade e número do CRM.

🛠️ Tecnologias Utilizadas
Python: Linguagem de programação principal.

PySide6 (Qt for Python): Framework utilizado para a construção da interface gráfica (GUI).

Módulos PySide6 chave:

QtWidgets: Componentes de UI (janelas, botões, listas, layouts, etc.).

QtGui: Manipulação de fontes e cores.

QtCore: Sinais, slots e alinhamento.

⚙️ Estrutura do Código (ClinicHub.py)
O código está modularizado em classes PySide6, o que facilita a manutenção e a expansão do projeto.

1. Dados Iniciais
As listas MEDICOS_DATA e PACIENTES_DATA funcionam como um mock de banco de dados, armazenando as informações que são exibidas nas telas de Médicos e Pacientes.

2. Classes de UI Principal
MainWindow: A janela principal do aplicativo. Utiliza um QHBoxLayout para organizar o menu lateral (MenuLateral, assumido estar no módulo ia) e o QStackedWidget.

LoginWindow (Menu Lateral):

Configura o menu de navegação usando um QListWidget.

Controla a mudança de telas no QStackedWidget através do slot mudar_p.

QStackedWidget (self.stack): Gerencia as diferentes páginas de conteúdo, permitindo a transição entre PaginaInicio, Pacientes e Medicos.

3. Classes das Páginas
PaginaInicio: Contém o dashboard. A função criar_card é responsável pela criação dos widgets de estatísticas.

Pacientes: Responsável pela tela de listagem de pacientes. O método load_patient_cards itera sobre PACIENTES_DATA para gerar e adicionar os cards de pacientes (criar_card) dentro de um QScrollArea.

Medicos: Semelhante à classe Pacientes, carrega e exibe os cards do corpo clínico, utilizando MEDICOS_DATA.

4. Estilização (QSS)
A aplicação utiliza stylesheets (.setStyleSheet()) para aplicar um tema visual leve e moderno, com cores claras e bordas arredondadas, melhorando a experiência do usuário.

🚀 Como Executar o Projeto
Pré-requisitos: Certifique-se de ter o Python instalado.

Instalar PySide6:

Bash

pip install PySide6
Executar:

Bash

python ClinicHub.py
