• Desenvolvendo uma Assistente Virtual em Python com base em códigos de outros Devs •

• Sobre o requirements.txt

    O comando de instalação automático padrão é o pip install -r requirements.txt

    Sinto informar, mas a depender da sua versão do python alguns listados não seram instalados.
    Como uma das soluções vale repassar o comando checando um por um, por exemplo: pip install pyttsx3==2.90 
    Após isso, verifique o status da instalação e faça o mesmo com os próximos na lista, os que estiverem dando erro faça o seguinte procedimento.
    Retire o '==versão' e rode apenas ex: pip install pyttsx3 
    Faça esse procedimento para todos que apresentarem erro. 
    OBS: essa forma de correção pode fazer algumas partes do código não funcionarem bem, mas é a menos trabalhosa. 
