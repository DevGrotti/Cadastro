🪪**SISTEMA DE CADASTRO**

📃Um sistema para gerenciamento de registros de pessoas, utilizando SQLite para modular o banco de dados, Python e a biblioteca Tkinter para interface gráfica.

⚙️Pré-requisitos

* **Visual Studio Code:** Certifique-se de ter o VS Code instalado.
* **Python:** O Python deve estar instalado no seu sistema. Você pode baixá-lo em [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **Extensão Python para VS Code:** Instale a extensão Python no VS Code para suporte completo à linguagem.

🛠️Instalação

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/mathgrotti/Cadastro.git](https://github.com/mathgrotti/Cadastro.git)
    ```

2.  **Abra o projeto no VS Code:**

    * Abra o VS Code.
    * Vá em "File" -> "Open Folder" e selecione a pasta onde você clonou o repositório.

3.  **Crie um ambiente virtual (recomendado):**

    * Abra o terminal integrado no VS Code (View -> Terminal).
    * Execute o seguinte comando para criar um ambiente virtual:

        ```bash
        python -m venv venv
        ```

    * Ative o ambiente virtual:

        * No Windows:

            ```bash
            venv\Scripts\activate
            ```

        * No macOS/Linux:

            ```bash
            source venv/bin/activate
            ```

4.  **Instale as dependências:**

        ```bash
        pip install -r requirements.txt
        ```

5.  **Execute o projeto:**

    * No terminal, execute o seguinte comando para executar o arquivo principal do projeto:

        ```bash
        python main.py
        ```


📲Uso

  • 👤Para **criar** um novo usuário, preencha **todas** as informações dos campos solicitados: <br><br>
     ![image](https://media.discordapp.net/attachments/782794257085366274/1342885469545041940/gif1Dados.gif?ex=67bb430d&is=67b9f18d&hm=a5e8e4e22dfbb121168db697106d9ae6807cbcc4e27b2abf5c628a23c352c6da&=&width=682&height=468) <br><br>

  Obs: Caso algum campo não seja preenchido, resultará em erro ao adicionar! <br><br>
      ![image](https://media.discordapp.net/attachments/782794257085366274/1342885583525122118/gif6error.gif?ex=67bb4328&is=67b9f1a8&hm=5f522a4fffa498a6738bcbcf4bfec7c69d51515efb63309e30d08ce777e16b83&=&width=656&height=468) <br><br>
  

  • ⤴️Após preencher os campos de texto, **anexe uma foto do usuário** clicando no botão "Fazer Upload": <br><br>
      ![image](https://media.discordapp.net/attachments/782794257085366274/1342885504026411140/gif2addfoto.gif?ex=67bb4315&is=67b9f195&hm=ff449fcbfde3fb72f73f0b41b7de7e16d0d116d84c5d3639cd74edb7c2ea86ec&=&width=680&height=468) <br><br>

  • ✅**Clique em "Adicionar"** para registrar o usuário no banco de dados: <br><br>
      ![image](https://media.discordapp.net/attachments/782794257085366274/1342885526549692438/gif3seeUser.gif?ex=67bb431b&is=67b9f19b&hm=199bbd616b436ff162328eaf98d0b6095b0094b23a0458b5af47bca472a94a1b&=&width=669&height=468) <br><br>

  • 🔄️**Para alterar algum dado de usuário**, selecione o usuário na tabela e clique em "Atualizar". Após as mudanças, clique no botão "Confirmar": <br><br>
      ![image](https://media.discordapp.net/attachments/782794257085366274/1342885545310687296/gif4attUser.gif?ex=67bb431f&is=67b9f19f&hm=271faccc65d8b4f6a07a5d2c69cd29dfcbbefb833199db79236dc27996cc9344&=&width=662&height=468) <br><br>

  • ❌Caso deseje **deletar** algum usuário, selecione-o na tabela e clique em "Deletar": <br><br>
      ![image](https://media.discordapp.net/attachments/782794257085366274/1342885566093463683/gif5delUser.gif?ex=67bb4324&is=67b9f1a4&hm=5473ee1d5b45304056ea25fd73c47bf2eadeea901c177cc40da37e60ca2ade99&=&width=668&height=468) <br><br>
      

