import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# instalação das bibliotecas
install('pyautogui')
install('pyperclip')

# importar bibliotecas




import getpass
import time
import pyautogui
import pyperclip
idioma=[ ]

if pyautogui.confirm(text='language', buttons=['português', 'english'])== 'português':
    idioma = ['escolha o navegador de preferencia.','outro','insira o nome desse outro navegador--->','vai encaminhar as mensagens acompanhadas do nome da pessoa ??','FUNCIONAMENTO','sim','não','antes do nome','completa',"Insira a sua mensagem ","(digite /n para quebras de linha, porem sem o espaço): ","Insira a sua mensagem depois do nome (digite /n para quebras de linha): ","insira o link da sua pesquisa--->",'insira os nomes --->','insira os numeros--->','abrir os programas é uma parte essencial e pode apresentar erros se não for executado.','PROGRAMAS',"posicione o mouse em cima da barra de mensagens do whatssap e aperte enter em seguida.","foi negada a inicialização dos aplicativos",'Para começar a rodar confirme','CONFIRMAÇÃO','faltam ',' segundos para começar',"TERMINOU","não foi altorizado a rodar o programa","não foi possivel rodar o código pois o quantidade de números e de nomes são diferentes",'chave de segurança invalida','recomendado']

else:
    idioma = ['choose your preferred browser.','other','insert the name of this other browser--->',"will you forward messages accompanied by the person's name??",'OPERATION','yes',' no','before the name','complete',"Enter your message ","(type /n for line breaks, but without the space): ","Insert your message after the name (type /n for line breaks): ","insert your search link--->",'insert names--->','insert numbers--->','opening programs is an essential part and may present errors if not executed.','PROGRAMS',"position the mouse over the WhatsApp message bar and then press enter.","applications were denied initialization",'To start running, confirm' ,'CONFIRMATION','missing','seconds to start',"FINISHED","was not allowed to run the program","it was not possible to run the code because the number of numbers and names are different",'key security invalid','recommended']
print(idioma)
senha = "" #defina sua senha de segurança para que outras pessoas não acessem/usem o programa de forma a enhviar mensagens aleatorias para pessoas aleatorias
if input("password  ") == senha:#linhas utilizada para testar se a senha e valida se não for valida retorna a não ativação do codigo e retorna a mensagem da ultima linha
    # variaveis """utilizadas para armazenar valores"""
    indice = 0  # indice usado para poder acessar o nome da pessoa que é dona do numero de telefone
    navegador =  pyautogui.confirm(text=idioma[0], title='NAVEGADOR', buttons=[f'chrome({idioma[27]})', 'edge', idioma[1]])
    if navegador == idioma[1]:
        navegador = input(idioma[2])
    elif navegador == 'chrome(RECOMENDADO)':
        navegador = 'chrome'
    funcionamento= pyautogui.confirm(text=idioma[3], title=idioma[4], buttons=[idioma[5],idioma[6]])
    inicial = idioma[7] if funcionamento == idioma[5]  else idioma[8]
    #input("insira o nome do navegador escolhido --->") #onde coloca o nome do navegador que sera utilizado para o programa rodar
    mensagem_inicial = input(idioma[9] + inicial + idioma[10]) #mensagem que deve ser escrita antes do nome
    mensagem_inicial = mensagem_inicial.replace('/n', '\n')
    if funcionamento == idioma[5]:
        mensagem_final = input(idioma[11]) #mensagem que deve ser escrita depois do nome
        mensagem_final = mensagem_final.replace('/n', '\n')
        link = input(idioma[12]) # link do formulário é dispensavel se já tiver inserido anteriormente na mensaegem
    timer = 5 #contagem regressiva em segundos para a inicialização do programa após confirmação
    # listas
    numero = ' ' #variavel utilizada para adicionar os números a lista numeros
    numeros = [] #lista onde ficarão armazenado os números
    dado = ' ' #variavel utilizada para adicionar os nomes a lista numeros
    dados = [] #lista onde ficarão armazenados os nomess
    if funcionamento == idioma[5]:
        while dado: #laço de repetição para adição dos nomes a lista
            dado = input(idioma[13]) #linha de codigo de inserção do nome
            dados.append(dado) #adição a lista
        dados.remove('')
    while numero: #laço de repetição para adição dos números a lista
        numero = input(idioma[14]) #inserção do número
        numeros.append(numero) #adição a lista
    numeros.remove('')
    confirmação_1=pyautogui.confirm(text=idioma[15], title=idioma[16], buttons=[idioma[5], idioma[6]]) #confirmação
    if len(dados) ==len(numeros) or funcionamento == idioma[6]:
      if confirmação_1 == idioma[5]: #se confirmado o que está dentro do if sera executado
          # abre o whatsapp
          pyautogui.press('win') #abre o menu
          pyautogui.write('whatsapp') # pesquisa no menu o nome do aplicativo de envio (whatsapp)
          time.sleep(.5) #tempo para processar
          pyautogui.press('enter') # abre o aplitivo
          time.sleep(5) #tempo para abrir
          pyautogui.hotkey('win', 'up') #deixa em tela cheia
          pyautogui.alert(idioma[17])
          mouse = pyautogui.position() #re3colhe a posição da caixa de mensagens
          # abre o navegador de escolha
          pyautogui.press('win') #abre o menu
          pyautogui.write(navegador) #digita o navegador escolhido anteriormente
          time.sleep(.5) #tempo para processar
          pyautogui.press('enter') #abre o aplicativo
          time.sleep(5)#tempo para abrir
          pyautogui.hotkey('win', 'up') #tela cheia
          time.sleep(.5) #tempo para processar
          pyautogui.keyDown('alt') #deixa a tecla alt pressionada
          pyautogui.press('tab') #troca de aplicativo
          pyautogui.press('tab')#troca de aplicativo
          pyautogui.press('alt')#confirma a troca de aplicativo
      else:
          pyautogui.alert(idioma[18]) #caso não seja altorizado a inicialixzação dos aplicativos e mostrada essa mensagem
      confirmação_2=pyautogui.confirm(text=idioma[19], title=idioma[20], buttons=[idioma[5], idioma[6]]) #PEDE CONFIRMAÇÃO
      if confirmação_2 == idioma[5]: #caso seja confirmado sera executado o código
          while timer >=1: #timer de inicialização
              print(idioma[21]+ str(timer) +idioma[22]) #mostra a contagem regressiva
              time.sleep(1) #intervalo de tempo de inicialização
              timer = timer - 1 # redução do tempo remanecente
          pyautogui.keyDown('alt') #deixa tecla alt pressionada
          pyautogui.press('tab')# troca de aplicativo
          pyautogui.press('alt')#confirma troca
          for num in numeros: #laço para envio das mensagens
              time.sleep(1) # tempo para processar
              pyautogui.hotkey('ctrl', 't')  # abrir uma nova guia
              time.sleep(1)  # tempo para processar
              pyautogui.write("wa.me/")  # escrever o link
              pyautogui.write(num)  # escrever o numero da pessoa
              time.sleep(.5) # tempo para processar
              pyautogui.press('enter')  # acionar o link
              time.sleep(2)# tempo para processar
              # esperasse que tenha sido redirecionado para o whatssap
              pyautogui.click(mouse.x, mouse.y)# abrir a caixa para escrever a mensagem
              time.sleep(1) # tempo para processar
              pyperclip.copy(mensagem_inicial + ' ')
              time.sleep(.1)
              pyautogui.hotkey('ctrl','v')
              if funcionamento == idioma[5]:
                  pyperclip.copy(dados[indice])
                  time.sleep(.1)
                  pyautogui.hotkey('ctrl', 'v')
                  pyperclip.copy(" " + mensagem_final)
                  time.sleep(.1)
                  pyautogui.hotkey('ctrl', 'v')
                  pyperclip.copy(" " + link)
                  time.sleep(.1)
                  pyautogui.hotkey('ctrl', 'v')
              
              time.sleep(1) #tempo para processar
              pyautogui.press('enter')  # enviar a mensagem
              time.sleep(.1)
              pyautogui.keyDown('alt') #deixa tecla alt pressionada
              pyautogui.press('tab') #troca de aplicativo
              pyautogui.press('alt')# confirma troca
              pyautogui.hotkey('ctrl', 'w')  # fechar aba
              indice = indice + 1 #adiciona 1 ao indice para que os nomes sejam correspondentes ao número
          pyautogui.hotkey('ctrl','w')
          pyautogui.hotkey('win', 'm') #minimiza todas as abas após terminar
          pyautogui.alert(idioma[23]) #emite alerta de termino
      else:
        pyautogui.alert(idioma[24])  # caso seja negado a inicialização
    else:
          print(idioma[25])

else:
    print(idioma[26]) # caso a senha de validação seja invalida emite essa reposta no terminal
