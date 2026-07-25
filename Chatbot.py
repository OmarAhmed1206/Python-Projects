from google import genai
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

app = QApplication([])

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gemini ChatBot")
        self.resize(1000, 700)

        self.vertical_layout = QVBoxLayout()

        userBox = QHBoxLayout()
        buttonBox = QHBoxLayout()

        self.userTextBox = QLineEdit()
        self.userTextBox.setPlaceholderText("Enter your message here...")
        self.sendButton = QPushButton("Enter")
        self.sendButton.clicked.connect(self.chatbot)
        self.endProgram = QPushButton("End Program")
        self.endProgram.clicked.connect(self.close)

        userBox.addWidget(self.userTextBox)
        buttonBox.addWidget(self.sendButton)
        buttonBox.addWidget(self.endProgram)


        botBox = QHBoxLayout()
        self.botAnswer = QTextEdit()
        self.botAnswer.setReadOnly(True)

        botBox.addWidget(self.botAnswer)


        self.vertical_layout.addLayout(botBox)
        self.vertical_layout.addLayout(userBox)
        self.vertical_layout.addLayout(buttonBox)

        self.setStyleSheet("""
        QWidget {
            background-color: #1e1e2f;
            color: white;
            font-size: 14px;
        }

        QPushButton {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 8px;
        }
        
        QPushButton:hover {
            background-color: #45a049;
        }
        
        QLineEdit {
            background: white;
            color: black;
            border: 2px solid #4CAF50;
            border-radius: 8px;
            padding: 5px;
        }
        
        QTextEdit {
            background: #2c2c3c;
            color: white;
            border-radius: 10px;
        }
        """)

        self.setLayout(self.vertical_layout)


    def chatbot(self):
        user_input = self.userTextBox.text()
        client  = genai.Client(api_key = api_key)

        interaction = client.interactions.create(
            model = "gemini-3.6-flash",
            input = user_input
        )
        self.botAnswer.setPlainText(interaction.output_text)
        self.userTextBox.clear()


window = MainWindow()
window.show()
app.exec()

