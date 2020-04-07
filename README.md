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
    
