# importar bibliotecas
import getpass
import time
import pyautogui
import pyperclip

senha = "" #defina sua senha de segurança para que outras pessoas não acessem/usem o programa de forma a enhviar mensagens aleatorias para pessoas aleatorias
if input("insira a senha  ") == senha:#linhas utilizada para testar se a senha e valida se não for valida retorna a não ativação do codigo e retorna a mensagem da ultima linha
    # variaveis """utilizadas para armazenar valores"""
    indice = 0  # indice usado para poder acessar o nome da pessoa que é dona do numero de telefone
    navegador =  pyautogui.confirm(text='escolha o navegador de preferencia.', title='NAVEGADOR', buttons=['chrome(RECOMENDADO)', 'edge', 'outro'])
    if navegador == 'outro':
        navegador = input('insira o nome desse outro navegador--->')
    elif navegador == 'chrome(RECOMENDADO)':
        navegador = 'chrome'
    funcionamento= pyautogui.confirm(text='vai encaminhar as mensagens acompanhadas do nome da pessoa ??', title='FUNCIONAMENTO', buttons=['sim', 'não'])
    inicial = 'antes do nome' if funcionamento == 'sim'  else 'completa'
    #input("insira o nome do navegador escolhido --->") #onde coloca o nome do navegador que sera utilizado para o programa rodar
    mensagem_inicial = input("Insira a sua mensagem " + inicial + "(digite /n para quebras de linha, porem sem o espaço): ") #mensagem que deve ser escrita antes do nome
    mensagem_inicial = mensagem_inicial.replace('/n', '\n')
    if funcionamento == "sim":
        mensagem_final = input("Insira a sua mensagem depois do nome (digite /n para quebras de linha): ") #mensagem que deve ser escrita depois do nome
        mensagem_final = mensagem_final.replace('/n', '\n')
        link = input("insira o link da sua pesquisa--->") # link do formulário é dispensavel se já tiver inserido anteriormente na mensaegem
    timer = 5 #contagem regressiva em segundos para a inicialização do programa após confirmação
    # listas
    numero = ' ' #variavel utilizada para adicionar os números a lista numeros
    numeros = [] #lista onde ficarão armazenado os números
    dado = ' ' #variavel utilizada para adicionar os nomes a lista numeros
    dados = [] #lista onde ficarão armazenados os nomess
    if funcionamento == 'sim':
        while dado: #laço de repetição para adição dos nomes a lista
            dado = input('insira os nomes --->') #linha de codigo de inserção do nome
            dados.append(dado) #adição a lista
        dados.remove('')
    while numero: #laço de repetição para adição dos números a lista
        numero = input('insira os numeros--->') #inserção do número
        numeros.append(numero) #adição a lista
    numeros.remove('')
    confirmação_1=pyautogui.confirm(text='abrir os programas é uma parte essencial e pode apresentar erros se não for executado.', title='PROGRAMAS', buttons=['SIM', 'não']) #confirmação
    if len(dados) ==len(numeros) or funcionamento == 'não':
      if confirmação_1 == "SIM": #se confirmado o que está dentro do if sera executado
          # abre o whatsapp
          pyautogui.press('win') #abre o menu
          pyautogui.write('whatsapp') # pesquisa no menu o nome do aplicativo de envio (whatsapp)
          time.sleep(.5) #tempo para processar
          pyautogui.press('enter') # abre o aplitivo
          time.sleep(5) #tempo para abrir
          pyautogui.hotkey('win', 'up') #deixa em tela cheia
          pyautogui.alert("posicione o mouse em cima da barra de mensagens do whatssap e aperte enter em seguida.")
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
          pyautogui.alert("foi negada a inicialização dos aplicativos") #caso não seja altorizado a inicialixzação dos aplicativos e mostrada essa mensagem
      confirmação_2=pyautogui.confirm(text='Para começar a rodar confirme', title='CONFIRMAÇÃO', buttons=['COMEÇAR', 'CANCELAR']) #PEDE CONFIRMAÇÃO
      if confirmação_2 == "COMEÇAR": #caso seja confirmado sera executado o código
          while timer >=1: #timer de inicialização
              print('faltam ' + str(timer) +' segundos para começar') #mostra a contagem regressiva
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
              if funcionamento == "sim":
                  pyperclip.copy(dados[indice])
                  time.sleep(.1)
                  pyautogui.hotkey('ctrl', 'v')
                  pyperclip.copy(" " + mensagem_final)
                  time.sleep(.1)
                  pyautogui.hotkey('ctrl', 'v')
                  pyperclip.copy(" " + link)
                  time.sleep(.1)
                  pyautogui.hotkey('ctrl', 'v')
              #pyautogui.write(mensagem_inicial + " " + dados[indice] + " " + mensagem_final + " " + link)  # escreve a mensagem
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
          pyautogui.alert("TERMINOU") #emite alerta de termino
      else:
        pyautogui.alert("não foi altorizado a rodar o programa")  # caso seja negado a inicialização
    else:
          print("não foi possivel rodar o código pois o quantidade de números e de nomes são diferentes")

else:
    print('chave de segurança invalida') # caso a senha de validação seja invalida emite essa reposta no terminal
