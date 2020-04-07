# Loja_de_Aluguel

Simples API de controle de aluguel de itens

#### Estrutura do projeto
-----------------
::

    Loja_de_Aluguel
    ├── modulos               - estrutura do codigo fonte de end-points.
    │   ├── Aluga             - sub-modulo reponsavél por resava direta de item.
    │   ├── Cancela_Reserva   - sub-modulo reponsável por cancelar só reservas de itens reservados.
    │   ├── Cliente           - sub-modulo responsável de cadastro de clientes.
    │   ├── Devolucao_Item    - sub-modulo responsável pela devolução de item de reserva ou aluguel direto.
    │   ├── Item              - sub-modulo responsável cadastro de tipo de item e item.
    │   ├── Reserva           - sub-modulo responsável reserva de item para cliente.
    ├── Modelos               - modulo responsável por criação do modelo do banco de dados.
    
    
#### Requerimentos
-----------------
* Versão do python:

      PYTHON >= 3.6
 
* Versão virtualenv

      VIRTUALENV >= 20.0
      
* Versão docker

      DOCKER >= 18.06
 

#### Executando a API com virtualenv
-----------------
* Instale o vitualenv execute o seguinte comando:

      sudo pip install virtualenv
      
* No diretório raiz execute o seguinte comando e ative o ambiente:

      source ven_loja/bin/activate
