# Projeto Muliro

Um script Python simples para Windows que exibe uma imagem em intervalos aleatórios.

## Funcionalidades

- Exibe uma imagem específica em intervalos de tempo variados.
- Fecha a imagem automaticamente após um tempo definido.
- Ciclo contínuo.

## Como usar

1.  Certifique-se de ter o Python instalado.
2.  Coloque a imagem `muliro.jpeg` na mesma pasta do script (ou ajuste o caminho no código).
3.  Execute o script:
    ```bash
    python muliro.py
    ```
4.  Para parar, use `CTRL+C` no terminal.

## Configuração

Você pode ajustar o comportamento do script editando as variáveis dentro do arquivo `muliro.py`:    

- `caminho_imagem`: O caminho para a imagem que será exibida.
- `min_tempo_fechada`: Tempo mínimo (em segundos) de espera entre as exibições.
- `max_tempo_fechada`: Tempo máximo (em segundos) de espera entre as exibições.
- `tempo_aberta`: Quanto tempo a imagem permanece na tela antes de ser fechada.

## Requisitos

- Sistema Operacional: Windows (o script utiliza o comando `taskkill` e `os.startfile` que são nativos do Windows).
- Python 3.x

## Observação

O script tenta fechar a janela procurando pelo nome do arquivo no título. Se você estiver usando um visualizador de fotos que não coloca o nome do arquivo no título da janela, o fechamento automático pode falhar.
