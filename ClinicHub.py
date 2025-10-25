from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QStackedWidget, QFrame,
    QCalendarWidget, QScrollArea, QSizePolicy
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys

from ia import MenuLateral

MEDICOS_DATA = [
    ("Dr. Arthur Mendes Lima", "Cardiologia", "CRM 15487"),
    ("Dra. Beatriz Almeida Rocha", "Dermatologia", "CRM 29012"),
    ("Dr. Carlos Eduardo Silva", "Ortopedia", "CRM 05367"),
    ("Dra. Denise Ferreira Gomes", "Pediatria", "CRM 41259"),
    ("Dr. Ernesto Ricardo Borges", "Neurologia", "CRM 11094"),
    ("Dra. Fernanda Lemos Vaz", "Ginecologia", "CRM 33701"),
    ("Dr. Gustavo Henrique Mota", "Oftalmologia", "CRM 08520"),
    ("Dra. Helena Souza Nunes", "Endocrinologia", "CRM 22468"),
    ("Dr. Ivan Pereira Santos", "Cirurgia Geral", "CRM 19345"),
    ("Dra. Juliana C. Oliveira", "Psiquiatria", "CRM 50123"),
    ("Dr. Klaus Weber Müller", "Urologia", "CRM 17654"),
    ("Dra. Lívia Dantas Morais", "Reumatologia", "CRM 38901"),
    ("Dr. Marcelo Augusto Costa", "Infectologia", "CRM 02077"),
    ("Dra. Natália E. Barbosa", "Geriatria", "CRM 45610"),
    ("Dr. Osvaldo Guedes Pinto", "Anestesiologia", "CRM 09876"),
    ("Dra. Patrícia Queiroz Cruz", "Medicina Esportiva", "CRM 25032"),
]

PACIENTES_DATA = [
    ("Ana Clara dos Santos", "P001", "Febre Alta, Sem Diagnóstico"),
    ("Rafaela Lins de Queiroz", "P002", "Pós-Operatório de Apendicite"),
    ("Lucas Vinícius de Sousa", "P003", "Fratura Exposta na Tíbia"),
    ("Gabriel Fernandes Matos", "P004", "Gripe H1N1"),
    ("Isabella Rocha Dantas", "P005", "Exames de Rotina (Internada)"),
    ("Pedro Henrique Azevedo", "P006", "Insuficiência Renal Crônica"),
    ("Mariana Silva Oliveira", "P007", "Reabilitação Fisioterapêutica"),
    ("João Paulo Ferreira", "P008", "Câncer de Pulmão (Estágio II)"),
    ("Laura Beatriz Costa", "P009", "Infecção Urinária"),
    ("Felipe Eduardo Borges", "P010", "Acompanhamento Neurológico"),
    ("Sofia Gomes Almeida", "P011", "Enxaqueca Severa"),
    ("Ricardo Alves Lima", "P012", "Procedimento Eletivo"),
]


class LoginWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(250)
        self.setStyleSheet("""
            QFrame {
                background-color: #f1f4f9;
                border-right: 1px solid #6a99b8;
            }
            QListWidget {
                background-color: #f1f4f9;
                border: none;
                outline: none;
            }
            QListWidget::item {
                color: #000000;
                padding: 15px 20px;
                border-bottom: 1px solid #000000;
            }
            QListWidget::item:hover {
                background-color: #f1f4f9;
                color: white;
            }
            QListWidget::item:selected {
                background-color: #000000;
                color: white;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.lista = QListWidget()
        for item_t in ["Início", "Pacientes", "Médicos"]:
            item = QListWidgetItem(item_t)
            item.setFont(QFont("Arial", 12))
            self.lista.addItem(item)

        self.lista.currentRowChanged.connect(self.mudar_p)
        layout.addWidget(self.lista)
        self.setLayout(layout)

    def mudar_p(self, index):
        self.stack_widget.setCurrentIndex(index)


class PaginaInicio(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 20, 50, 20)
        main_layout.setSpacing(30)

        # Título centralizado
        titulo = QLabel("Início")
        titulo.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 26px;
                font-weight: bold;
            }
        """)
        main_layout.addWidget(titulo, alignment=Qt.AlignHCenter)

        # Layout para os cards de estatísticas
        stats_container = QHBoxLayout()
        stats_container.setSpacing(20)
        stats_container.addWidget(self.criar_card("Consultas Hoje", "8"))
        stats_container.addWidget(self.criar_card("Pacientes Ativos", "27"))
        stats_container.addWidget(self.criar_card("Médicos", "15"))
        main_layout.addLayout(stats_container)

        # Layout para botões e calendário
        content_layout = QHBoxLayout()
        content_layout.setSpacing(30)

        # Lado esquerdo - Botões
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(15)
        
        self.btn_p = QPushButton("Novo Paciente")
        self.btn_p.setFixedSize(170, 40)
        self.btn_p.setStyleSheet("""
            QPushButton { 
                background-color: #6fa5c7; 
                border-radius: 18px; 
                font-size: 14px;
                color: white;
            }
            QPushButton:hover {
                background-color: #a1b5c2;
            }
        """)

        self.btn_add = QPushButton("Adicionar Consulta")
        self.btn_add.setFixedSize(170, 40)
        self.btn_add.setStyleSheet("""
            QPushButton { 
                background-color: #6fa5c7; 
                border-radius: 18px; 
                font-size: 14px;
                color: white;
            }
            QPushButton:hover {
                background-color: #a1b5c2;
            }
        """)

        self.btn_can = QPushButton("Cancelar")
        self.btn_can.setFixedSize(170, 40)
        self.btn_can.setStyleSheet("""
            QPushButton { 
                background-color: #6fa5c7; 
                border-radius: 18px; 
                font-size: 14px;
                color: white;
            }
            QPushButton:hover {
                background-color: #a1b5c2;
            }
        """)

        buttons_layout.addWidget(self.btn_p)
        buttons_layout.addWidget(self.btn_add)
        buttons_layout.addWidget(self.btn_can)
        buttons_layout.addStretch()

        # Lado direito - Calendário
        calendar_container = QVBoxLayout()
        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setStyleSheet("""
            background-color: #ffffff;
            color: #000000;
            selection-background-color: #000000;
        """)
        self.calendario.clicked.connect(self.data_selecionada)

        self.label_data = QLabel()
        self.label_data.setStyleSheet("color: #000000; font-size: 14px;")
        self.label_data.setAlignment(Qt.AlignHCenter)

        calendar_container.addWidget(self.calendario)
        calendar_container.addWidget(self.label_data)

        content_layout.addLayout(buttons_layout)
        content_layout.addLayout(calendar_container)
        main_layout.addLayout(content_layout)

    def data_selecionada(self, date):
        self.label_data.setText(f"Data selecionada: {date.toString('dd/MM/yyyy')}")

    def criar_card(self, titulo, valor):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #dee1e3;
                border-radius: 15px;
                border: 1px solid #dcdcdc;
            }
        """)

        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignCenter)

        label_titulo = QLabel(titulo)
        label_titulo.setFont(QFont("Arial", 12, QFont.Bold))
        label_titulo.setAlignment(Qt.AlignHCenter)
        
        label_valor = QLabel(valor)
        label_valor.setFont(QFont("Arial", 18))
        label_valor.setAlignment(Qt.AlignHCenter)

        card_layout.addWidget(label_titulo)
        card_layout.addWidget(label_valor)
        card.setLayout(card_layout)
        card.setFixedSize(180, 100)
        return card


class Pacientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 20, 50, 20)
        main_layout.setSpacing(20)

        # Título centralizado
        titulo = QLabel("Pacientes")
        titulo.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 26px;
                font-weight: bold;
            }
        """)
        main_layout.addWidget(titulo, alignment=Qt.AlignHCenter)

        # Área de rolagem para os cards
        self.scroll_content_widget = QWidget()
        self.cards_layout = QVBoxLayout(self.scroll_content_widget)
        self.cards_layout.setAlignment(Qt.AlignTop)
        self.cards_layout.setSpacing(10)
        self.cards_layout.setContentsMargins(10, 10, 10, 10)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_content_widget)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)

        main_layout.addWidget(self.scroll_area)
        self.load_patient_cards()

    def criar_card(self, nome, id_num, condicao):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setFrameShadow(QFrame.Shadow.Raised)
        card.setStyleSheet("""
            QFrame {
                background-color: #dee1e3;
                border-radius: 15px;
                border: 1px solid #dcdcdc;
            }
        """)

        card.setFixedHeight(100)
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(15, 15, 15, 15)

        label_nome = QLabel(nome)
        label_nome.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        label_id = QLabel(f"ID: {id_num}")
        label_id.setFont(QFont("Arial", 10))

        label_condicao = QLabel(f"Condição: {condicao}")
        label_condicao.setFont(QFont("Arial", 11))

        card_layout.addWidget(label_nome)
        card_layout.addWidget(label_id)
        card_layout.addWidget(label_condicao)
        card_layout.addStretch(1)

        card.setLayout(card_layout)
        return card

    def load_patient_cards(self):
        for nome, id_num, condicao in PACIENTES_DATA:
            card = self.criar_card(nome, id_num, condicao)
            self.cards_layout.addWidget(card)
        self.cards_layout.addStretch(1)


class Medicos(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 20, 50, 20)
        main_layout.setSpacing(20)

        # Título centralizado
        titulo = QLabel("Corpo Clínico")
        titulo.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 26px;
                font-weight: bold;
            }
        """)
        main_layout.addWidget(titulo, alignment=Qt.AlignHCenter)

        # Área de rolagem para os cards
        self.scroll_content_widget = QWidget()
        self.cards_layout = QVBoxLayout(self.scroll_content_widget)
        self.cards_layout.setAlignment(Qt.AlignTop)
        self.cards_layout.setSpacing(10)
        self.cards_layout.setContentsMargins(10, 10, 10, 10)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_content_widget)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)

        main_layout.addWidget(self.scroll_area)
        self.load_doctor_cards()

    def criar_card(self, nome, especialidade, crm):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setFrameShadow(QFrame.Shadow.Raised)
        card.setStyleSheet("""
            QFrame {
                background-color: #e0f7fa;
                border-radius: 15px;
                border: 1px solid #00bcd4;
            }
        """)

        card.setFixedHeight(100)
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(15, 15, 15, 15)

        label_nome = QLabel(nome)
        label_nome.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        label_nome.setStyleSheet("color: #00796b;")

        label_especialidade = QLabel(f"Especialidade: {especialidade}")
        label_especialidade.setFont(QFont("Arial", 11))

        label_crm = QLabel(crm)
        label_crm.setFont(QFont("Arial", 10))

        card_layout.addWidget(label_nome)
        card_layout.addWidget(label_especialidade)
        card_layout.addWidget(label_crm)
        card_layout.addStretch(1)

        card.setLayout(card_layout)
        return card

    def load_doctor_cards(self):
        for nome, especialidade, crm in MEDICOS_DATA:
            card = self.criar_card(nome, especialidade, crm)
            self.cards_layout.addWidget(card)
        self.cards_layout.addStretch(1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ClinicHub")
        self.setFixedSize(930, 710)
        self.setup_ui()

    def setup_ui(self):
        container = QWidget()
        main_layout = QHBoxLayout(container)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.stack = QStackedWidget()
        self.stack.addWidget(PaginaInicio())
        self.stack.addWidget(Pacientes())
        self.stack.addWidget(Medicos())

        self.menu = MenuLateral(self.stack)

        main_layout.addWidget(self.menu)
        main_layout.addWidget(self.stack)

        self.setCentralWidget(container)
        self.setStyleSheet("background-color: #f1f4f9;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())