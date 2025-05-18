# Tech Challenge - Pós-Tech - IA For Devs - FIAP
# Fase 4 - Análise de vídeo com IA

## Alunos:

- André Mattos - RM358905
- Aurelio Thomasi Jr - RM358104
- Leonardo Ramires - RM358190
- Lucas Arruda - RM358628
- Pedro Marins - RM356883

## Evidências do projeto

- Link para o repositório:[Repositorio Git](https://github.com/acmattos/ia4devs/tree/main/module_04/04_Tech_Challenge)
- Link para o vídeo de apresentação: [Video Apresentação]
- Vosk Model: [Vosk Model](https://alphacephei.com/vosk/models)

## Passos para instalar Dlib e Tensorflow (Windows)

1. Instalar o [CUDA Toolkit 12.8](https://developer.nvidia.com/cuda-downloads)
2. Instalar o [cuDNN 9.10](https://developer.nvidia.com/cudnn-downloads)
   - Dúvidas no processo? [Veja mais](https://docs.nvidia.com/deeplearning/cudnn/installation/latest/windows.html)
3. Copie todos os arquivos `.dll` do diretório `/bin` do `CUDNN` 
   (C:\Program Files\NVIDIA\CUDNN\v9.1\bin\12.4) para dentro do `/bin` do `CUDA` 
   (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin)
4. Copie todos os arquivos do diretório `/include` do `CUDNN` 
   (C:\Program Files\NVIDIA\CUDNN\v9.1\include\12.4) para dentro do `/include` 
   do `CUDA` (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include)
5. Copie todos os arquivos do diretório `/lib/x64` do `CUDNN`
   (C:\Program Files\NVIDIA\CUDNN\v9.1\lib\12.4\x64) para dentro do `/lib/x64` do 
   `CUDA` (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64)
6. Clonar o repositório do [Dlib](https://github.com/davisking/dlib):

   ```bash
   git clone https://github.com/davisking/dlib.git
   ```

7. Entrar no diretório usando a janela de comandos:

   ```bash
   cd dlib
   ```

8. Instalar o Visual Studio Desktop Development com as ferramentas de C++
9. Instalar o [CMake](https://cmake.org/download)
10. Compilar o [DLib](https://learnopencv.com/install-dlib-on-windows/)
11. Instalar Dlib:

    ```bash
    python setup.py install
    ```

12. Instalar o Tensorflow:

    ```bash
    pip install tensorflow
    ```

## Passos para instalar o Modelo Vosk
Vosk Model - https://alphacephei.com/vosk/
1. Acessar [o documento de instalaçao do Vosk] (https://alphacephei.com/vosk/install)
2. Seguir os passos definidos.
3. Acessar [a página de modelos] (https://alphacephei.com/vosk/models).
4. Baixar vosk-model-en-us-0.22 ou similar.

## Descrição

Este Tech Challenge tem como objetivo de criar uma aplicação que utilize análise de vídeo com IA, para detectar os seguintes eventos:
- Reconhecimento facial: Identificar e marcar pessoas no vídeo
- Análise de expressões emocionais: Identificar e analise expressões dos rostos identificados
- Detecção de atividades: Detectar e categorizar atividades sendo realizadas no vídeo
- Geração de resumo: Um resumo automático das principais atividades e emoções detectadas no vídeo.

Após as detecções, os sistema irá gerar automaticamente um relatório com as principais atividades e emoções detectadas no vídeo.
O relatório deve incluir:
- Total de frames analisados
- Número de anomalias detectadas

## Detecção de rostos - reconhecimento facial

Esta parte do projeto foi desenvolvida utilizando a bibliotca Face

## Detecção de emoções - expressões faciais

## Transcrição de do vídeo

## Relatório

O relatório foi gerado utilizando a biblioteca Pandas, e foi gerado a partir dos dados coletados durante a análise do vídeo.
