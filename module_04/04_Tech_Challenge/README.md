# Tech Challenge - Pós-Tech - IA For Devs - FIAP
# Fase 4 - Análise de vídeo com IA

## 1. Alunos:

- André Mattos - RM358905
- Aurelio Thomasi Jr - RM358104
- Leonardo Ramires - RM358190
- Lucas Arruda - RM358628
- Pedro Marins - RM356883

## 2. Evidências do projeto

- Link para o repositório:[Repositorio Git](https://github.com/acmattos/ia4devs/tree/main/module_04/04_Tech_Challenge)
- Link para o vídeo de apresentação: [Video Apresentação]
- Vosk Model: [Vosk Model](https://alphacephei.com/vosk/models)

## 3. Bibliotecas utilizadas

- Principais bibliotecas:
  - **OpenCV (cv2)**: Biblioteca utilizada para processamento de vídeo, detecção de rostos e manipulação de imagens
  - **DeepFace**: Biblioteca utilizada para análise de emoções faciais (feliz, triste, etc.)
  - **MediaPipe**: Biblioteca utilizada para detecção de movimentos(pose corporal, movimentos das mãos, etc.)

- Bibliotecas de suporte:
  - **Dlib**: Biblioteca base para o face_recognition, utilizada para detecção e codificação de rostos
  - **Tensorflow**: Dependência do DeepFace para análise de emoções
  - **Vosk**: Biblioteca utilizada para transcrição de áudio do vídeo para texto
  - **Pandas**: Biblioteca utilizada para geração de relatórios e análise dos dados coletados
  - **NumPy**: Biblioteca utilizada para operações matemáticas e manipulação de arrays
  - **tqdm**: Biblioteca utilizada para exibir barras de progresso durante o processamento do vídeo que está sendo analisado.

## 4. Instalar Dlib e Tensorflow (Windows)

Durante o desenvolvimento do projeto, foi necessário instalar o Dlib e o Tensorflow para a utilização de CUDA, para processar os vídeos com GPU e consequentemente melhorar o desempenho do processamento.
No final desta documentação, será apresentado o passo a passo para instalar o Dlib e o Tensorflow para o ambiente Windows (ambiente de desenvolvimento utilizado).

**CUDA**: É uma biblioteca de software utilizada em hardware de computação gráfica da empresa NVIDIA, que permite a utilização de GPUs para acelerar o processamento de cálculos matemáticos (Por exemplo, matrizes, cálculos de IA, etc.)

## 6. Descrição

Este Tech Challenge tem como objetivo de criar uma aplicação que utilize análise de vídeo com IA, para detectar os seguintes eventos:
- Reconhecimento facial: Identificar e marcar pessoas no vídeo
- Análise de expressões emocionais: Identificar e analise expressões dos rostos identificados
- Detecção de atividades: Detectar e categorizar atividades sendo realizadas no vídeo
- Geração de resumo: Um resumo automático das principais atividades e emoções detectadas no vídeo.

Após as detecções, os sistema irá gerar automaticamente um relatório com as principais atividades e emoções detectadas no vídeo.
O relatório deve incluir:
- Total de frames analisados
- Número de anomalias detectadas

## 7. Detecção de rostos - reconhecimento facial

Esta parte do projeto foi desenvolvida utilizando a bibliotca **OpenCV** para realizar o processamento.
Os seguintes passos são realizados neste processo:

1. Carregar o modelo de detecção de rostos
2. Carregar o vídeo
3. Processar o vídeo frame a frame
4. Detectar rostos no frame
5. Desenhar retângulos ao redor dos rostos detectados
6. Identificar nome de pessoas de acordo com imagens de referência que estão salvas no diretório `images`
7. Salvar o frame com os retângulos desenhados
8. Atualizar o relatório com os dados coletados

### 7.1 Imagens de referência

As imagens de referência foram salvas no diretório `images` e foram utilizadas para identificar as pessoas no vídeo.
As seguintes imagens foram utilizadas:

- **Ann** (01Ann_A01.png)
- **Brunna** (01Brunna_B01.png)
- **Charles** (01Charles_C01.png)
- **Danielle** (01Danielle_D01.png)
- **Ed** (02Ed_E01.png)
- **Faith** (04Faith_F01.png)
- **Garth** (05Garth_G01.png)
- **Harry** (06Harry_H01.png)
- **Ivy** (07Ivy_I01.png)
- **John** (08John_J01.png)
- **Kay** (12Kay_K01.png)
- **Lana** (13Lana_L01.png)
- **Mark** (14Mark_M01.png)
- **Noah** (15Noah_N01.png)
- **Oswald** (17Oswald_O01.png)
- **Paula** (17Paula_P01.png)
- **Rita** (17Rita_R01.png)
- **Saul** (17Saul_S01.png)
- **Thor** (18Thor_T01.png)

### 7.2 Processamento do vídeo e parâmetros

A função `face_detection_and_recognition` é responsável por realizar o reconhecimento facial no vídeo. O processo consiste em:

1. **Carregamento de Dados**:
   - Carrega as imagens de referência do diretório especificado
   - Inicializa o vídeo de entrada e cria o arquivo de saída
   - Prepara as estruturas de dados para armazenar os resultados

2. **Processamento Frame a Frame**:
   - Para cada frame do vídeo:
     - Converte o frame para RGB (necessário para o `face_recognition`)
     - Detecta rostos e gera codificações faciais
     - Compara com as imagens de referência
     - Desenha retângulos e nomes ao redor dos rostos identificados
     - Salva os resultados para análise posterior

3. **Geração de Relatório**:
   - Cria um arquivo CSV com os resultados
   - Gera um resumo da análise com estatísticas

4. **Anomalias**:
   - Se o nome da pessoa não for encontrado nas imagens de referência, o sistema irá marcar a pessoa como "Anônimo"

#### 7.2.1 Parâmetros da Função

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `images_path` | str | Caminho para o diretório contendo as imagens de referência |
| `video_in_path` | str | Caminho do arquivo de vídeo de entrada |
| `video_out_path` | str | Caminho onde será salvo o vídeo processado |

#### 7.2.2 Parâmetros Internos

| Parâmetro | Valor Padrão | Descrição |
|-----------|--------------|-----------|
| `number_of_times_to_upsample` | 5 | Número de vezes que a imagem é redimensionada para detectar rostos menores |
| `model` | "cnn" | Modelo de detecção facial ("cnn" para GPU, "hog" para CPU) |
| `num_jitters` | 40 | Número de amostragens para gerar a codificação facial |
| `encoding_model` | "large" | Modelo de codificação facial ("large" para 128 pontos, "small" para 5 pontos) |

#### 7.2.3 Saídas

1. **Vídeo Processado**:
   - Arquivo MP4 com os rostos identificados
   - Retângulos coloridos ao redor dos rostos
   - Nomes das pessoas identificadas

2. **Arquivo CSV**:
   - Frame ID
   - Nome da pessoa identificada
   - Timestamp do frame

3. **Resumo da Análise**:
   - Total de frames processados
   - Estatísticas de detecção por pessoa
   - Tempo total de processamento

## 8. Detecção de emoções - expressões faciais

Esta parte do projeto foi desenvolvida utilizando a biblioteca **DeepFace** para realizar a análise de emoções. O processo consiste em:

1. **Carregamento de Dados**:
   - Inicializa o vídeo de entrada
   - Prepara o arquivo de saída para o vídeo processado
   - Configura as estruturas de dados para armazenar os resultados

2. **Processamento Frame a Frame**:
   - Para cada frame do vídeo:
     - Detecta rostos usando OpenCV (DNN ou cascatas Haar)
     - Analisa as emoções de cada rosto detectado usando DeepFace
     - Desenha retângulos e emoções ao redor dos rostos identificados
     - Salva os resultados para análise posterior

3. **Geração de Relatório**:
   - Cria um arquivo CSV com os resultados
   - Gera um resumo da análise com estatísticas de emoções

#### 8.1 Parâmetros da Função

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `video_in_path` | str | Caminho do arquivo de vídeo de entrada |
| `video_out_path` | str | Caminho onde será salvo o vídeo processado |

#### 8.2 Parâmetros Internos

| Parâmetro | Valor Padrão | Descrição |
|-----------|--------------|-----------|
| `actions` | ['emotion'] | Lista de ações a serem analisadas pelo DeepFace |
| `detector_backend` | 'centerface' | Backend de detecção facial ('opencv', 'mtcnn', 'skip', 'mediapipe' ou 'centerface') |
| `enforce_detection` | False | Se deve forçar a detecção mesmo com baixa confiança |
| `anti_spoofing` | False | Se deve verificar se o rosto é real ou uma foto |

#### 8.3 Emoções Detectadas

O sistema é capaz de detectar as seguintes emoções:
- **Feliz** (happy)
- **Triste** (sad)
- **Neutro** (neutral)
- **Surpreso** (surprise)
- **Com medo** (fear)
- **Irritado** (angry)
- **Desconhecido** (unknown) - quando não é possível detectar a emoção

#### 8.4 Saídas

1. **Vídeo Processado**:
   - Arquivo MP4 com os rostos e emoções identificados
   - Retângulos coloridos ao redor dos rostos
   - Emoção detectada para cada rosto

2. **Arquivo CSV**:
   - Frame ID
   - Emoções detectadas (até 4 emoções por frame)
   - Timestamp do frame

3. **Resumo da Análise**:
   - Total de frames processados
   - Estatísticas de cada emoção detectada
   - Tempo total de processamento

## 9. Transcrição do vídeo

Esta parte do projeto foi desenvolvida utilizando as bibliotecas **MoviePy** e **Vosk** para realizar a transcrição do áudio do vídeo. Isso não é um requisito para o projeto, mas foi uma opção considerada para o desenvolvimento porque é uma análise útil e faz parte da fase atual da Pos-Tech. O processo consiste em:

1. **Extração do Áudio**:
   - Carrega o arquivo de vídeo usando MoviePy
   - Extrai a faixa de áudio do vídeo
   - Salva o áudio em formato WAV com qualidade CD (44.1kHz, 16-bit, mono)

2. **Processamento do Áudio**:
   - Carrega o arquivo de áudio extraído
   - Converte o áudio para o formato adequado para reconhecimento de fala
   - Utiliza o modelo Vosk para transcrição offline

3. **Geração da Transcrição**:
   - Realiza o reconhecimento de fala
   - Salva o texto transcrito em um arquivo
   - Exibe o progresso durante o salvamento

#### 9.1 Parâmetros da Função

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `video_in_path` | str | Caminho do arquivo de vídeo de entrada |
| `audio_out_path` | str | Caminho onde será salvo o arquivo de áudio extraído |
| `text_out_path` | str | Caminho onde será salva a transcrição em texto |

#### 9.2 Parâmetros Internos

| Parâmetro | Valor Padrão | Descrição |
|-----------|--------------|-----------|
| `fps` | 44100 | Taxa de amostragem do áudio (Hz) |
| `nbytes` | 2 | Profundidade de bits (2 = 16-bit) |
| `codec` | 'pcm_s16le' | Codec de áudio (WAV 16-bit) |
| `ffmpeg_params` | ["-ac", "1"] | Parâmetros para forçar saída mono |

#### 9.3 Requisitos

1. **Modelo Vosk**:
   - É necessário baixar e instalar o modelo de linguagem Vosk

2. **Dependências**:
   - **MoviePy**: Biblioteca utilizada para manipulação de vídeo e áudio
   - **SpeechRecognition**: Biblioteca utilizada para interface com o Vosk
   - **FFmpeg**: Biblioteca utilizada para processamento de áudio

#### 9.4 Saídas

1. **Arquivo de Áudio**:
   - Formato WAV
   - Qualidade CD (44.1kHz)
   - Áudio mono
   - 16-bit de profundidade

2. **Arquivo de Transcrição**:
   - Formato texto (.txt)
   - Codificação UTF-8
   - Texto transcrito do áudio
   - Salvo em chunks para melhor performance

3. **Feedback**:
   - Barra de progresso durante o processamento
   - Mensagens de status no console
   - Transcrição exibida no terminal

## 10. Relatório

O projeto gera três tipos principais de relatórios através de diferentes módulos:
- Reconhecimento Facial (`face_detection_recognition.py`)
- Análise de Emoções (`face_expression.py`)
- Análise de Movimentos Corporais (`pose_activity.py`)

Cada módulo gera relatórios específicos que são consolidados em um arquivo de resumo (`summary_analysis.txt`), que foi utilizado para gerar esta documentação.

### 10.1 Relatório de Reconhecimento Facial
**Arquivo:** `tc4_video_fr.mp4.csv`
**Módulo:** `face_detection_recognition.py`

#### Top 5 Resultados:
| Pessoa | Aparições |
|--------|-----------|
| Ivy_I | 6 |
| Danielle_D | 3 |
| Ann_A | 2 |
| Harry_H | 2 |
| John_J | 2 |

**Detalhes:**
- O relatório identifica pessoas conhecidas no vídeo
- Registra o número de aparições de cada pessoa identificada
- Pessoas não reconhecidas são marcadas como "Unknown"

### 10.2 Relatório de Análise de Emoções
**Arquivo:** `tc4_video_fe.mp4.csv`
**Módulo:** `face_expression.py`

#### Top 5 Resultados:
| Emoção | Aparições |
|--------|-----------|
| fear | 19 |
| happy | 17 |
| neutral | 14 |
| sad | 12 |
| angry | 9 |

**Detalhes:**
- Analisa as emoções dominantes em cada face detectada
- Utiliza o modelo DeepFace para classificação de emoções
- Registra a frequência de cada emoção detectada
- Emoções analisadas: 
  - **medo**
  - **felicidade**
  - **neutralidade**
  - **tristeza**
  - **raiva**
  - **surpresa**

### 10.3 Relatório de Movimentos Corporais
**Arquivo:** `tc4_video_pa.mp4.csv`
**Módulo:** `pose_activity.py`

#### Top 5 Resultados:
| Atividade | Ocorrências |
|-----------|-------------|
| Movimentos da mão esquerda | 27 |
| Movimentos da mão direita | 26 |
| Movimentos dos braços | 17 |
| Boca fechada | 35 |
| Boca aberta | 13 |

**Detalhes:**
- Analisa movimentos corporais e expressões faciais
- Total de frames analisados: 3.326
- Anomalias detectadas: 183
- Monitora:
  - Movimentos dos braços
  - Movimentos das mãos
  - Toques no rosto
  - Expressões faciais (boca aberta/fechada, sorriso)

### 10.4 Transcrição do Vídeo
**Arquivo:** `tc4_video_transcription.txt`
**Módulo:** `video_transcription.py`

Este arquivo contém a transcrição do áudio do vídeo, permitindo análise do conteúdo verbal em conjunto com as análises visuais.

### 10.5 Arquivos de Relatório Detalhado
Para análises mais detalhadas, os seguintes arquivos CSV estão disponíveis:
- `tc4_video_fr.mp4.csv`: Dados brutos de reconhecimento facial
- `tc4_video_fe.mp4.csv`: Dados brutos de análise de emoções
- `tc4_video_pa.mp4.csv`: Dados brutos de movimentos corporais

### 10.6 Resumo Consolidado
**Arquivo:** `summary_analysis.txt`

Este arquivo apresenta um resumo consolidado de todas as análises, incluindo:
- Contagem de aparições de pessoas
- Distribuição de emoções
- Estatísticas de atividades e movimentos
- Detecção de anomalias

### 10.7 Observações Técnicas
- Todos os relatórios são gerados automaticamente durante o processamento do vídeo
- Os dados são salvos em formato CSV para fácil análise posterior
- O sistema utiliza múltiplos modelos de deep learning para diferentes análises
- Os relatórios podem ser usados em conjunto para uma análise mais completa do comportamento

### 10.8 Links para Arquivos
- [Resumo da Análise](./doc/videos/result/summary_analysis.txt)
- [Relatório de Reconhecimento Facial](./doc/videos/result/tc4_video_fr.mp4.csv)
- [Relatório de Emoções](./doc/videos/result/tc4_video_fe.mp4.csv)
- [Relatório de Atividades](./doc/videos/result/tc4_video_pa.mp4.csv)
- [Transcrição do Vídeo](./doc/videos/result/tc4_video_transcription.txt)

## (Extra) Instalação de dependências para rodar o projeto

### 11.1 Instalação do Dlib e Tensorflow

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

### 11.2 Instalação do Modelo Vosk

Vosk Model - https://alphacephei.com/vosk/
1. Acessar [o documento de instalaçao do Vosk] (https://alphacephei.com/vosk/install)
2. Seguir os passos definidos.
3. Acessar [a página de modelos] (https://alphacephei.com/vosk/models).
4. Baixar vosk-model-en-us-0.22 ou similar.
