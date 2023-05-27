import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Inicializar o reconhecimento de voz
recognizer = sr.Recognizer()

# Inicializar o mecanismo de texto para voz
engine = pyttsx3.init()

# Definir a voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Índice 0 é a voz masculina

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.pause_threshold = 0.5  # Pausa de 1 segundo para finalizar a fala
        audio = recognizer.listen(source)

    try:
        print("Reconhecendo...")
        comando = recognizer.recognize_google(audio, language='pt-BR''en-US')
        print(f"Você disse: {comando}\n")
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender.")
        comando = ouvir()

    return comando

def verificar_ativacao(comando):
    ativacao = 'jarvis'  # Comando de ativação por voz
    if ativacao in comando:
        falar("Como posso ajudar?")
        while True:
            comando = ouvir().lower()
            executar_comando(comando)

def executar_comando(comando):
    if 'horas' in comando:
        agora = datetime.datetime.now().strftime("%H:%M")
        falar(f"São {agora} horas.")
    elif 'pesquisa' in comando:
        falar("O que você gostaria de pesquisar?")
        termo = ouvir()
        resultados = wikipedia.search(termo)
        if len(resultados) > 0:
            pagina = wikipedia.page(resultados[0])
            falar(pagina.summary)
        else:
            falar("Nenhum resultado encontrado para esse termo.")
    elif 'site' in comando:
        falar("Qual site você gostaria de abrir?")
        site = ouvir()
        webbrowser.open(f"https://www.{site}.com")
    elif 'tocar música' in comando:
        caminho_musica = 'caminho/para/música.mp3'
        os.system(f"start {caminho_musica}")
    elif 'sair' in comando:
        falar("Até logo!")
        exit()
        
    elif 'spotify' in comando:
        falar("Tudo bem !.")
        os.system("start spotify:")    
    elif 'word' in comando:
        falar("Tudo bem!.")
        os.system("start winword")    
    elif 'excel' in comando:
        falar("Tudo bem!.")
        os.system("start excel")      
        ouvir()
    elif 'desligar' in comando:
     falar("Desligando o computador.")
     os.system("shutdown /s /t 0")
     exit()
     
# Função principal
def main():
    falar("")
    ativado = False
    while not ativado:
        comando = ouvir().lower()
        if 'jarvis' in comando:
            ativado = True
            verificar_ativacao(comando)

if __name__ == "__main__":
    main()
