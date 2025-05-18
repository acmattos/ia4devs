# Tech Challenge - Pós-Tech - IA For Devs - FIAP

## Alunos:
- André Mattos - RM358905
- Aurelio Thomasi Jr - RM358104
- Leonardo Ramires - RM358190
- Lucas Arruda - RM358628
- Pedro Marins - RM356883
 
## Evidências do projeto
- Link para o repositório: Repositorio Git
- Link para o vídeo de apresentação: 

## Passos para instalar Dlib e Tensorflow 

1 Instalar o [CUDA Toolkit 12.8] (https://developer.nvidia.com/cuda-downloads).
2 Instalar o [cuDNN 9.10] (https://developer.nvidia.com/cudnn-downloads).
2.1 Dúvidas no processo? [Veja mais] (https://docs.nvidia.com/deeplearning/cudnn/installation/latest/windows.html).
3 Copie todos os arquivos `.dll` do diretório `/bin` do `CUDNN`. 
  (C:\Program Files\NVIDIA\CUDNN\v9.1\bin\12.4) para dentro do `/bin` do `CUDA` 
  (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin).
4 Copie todos os arquivos do diretório `/include` do `CUDNN`. 
  (C:\Program Files\NVIDIA\CUDNN\v9.1\include\12.4) para dentro do `/include` 
  do `CUDA`(C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include)
5 Copie todos os arquivos do diretório `/lib/x64` do `CUDNN`.
  (C:\Program Files\NVIDIA\CUDNN\v9.1\lib\12.4\x64) para dentro do `/lib/x64` do 
  `CUDA` (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64).
6 Clonar o repositório do [Dlib] (https://github.com/davisking/dlib): 
  `git clone https://github.com/davisking/dlib.git` 
7 Entrar no diretório usando a janela de comandos: `cd dlib`
8 Instalar o Visual Studio Desktop Development com as ferramentas de C++.
9 Instalar o [CMake] (https://cmake.org/download)
10 Compilar o [DLib] (https://learnopencv.com/install-dlib-on-windows/) 
11 Instalar Dlib: `python setup.py install`
12 Instalar o Tensorflow: `pip install tensorflow`

## Passos para instalar o Modelo Vosk  
Vosk Model - https://alphacephei.com/vosk/
1 Acessar [o documento de instalaçao do Vosk] (https://alphacephei.com/vosk/install)
2 Seguir os passos definidos.
3 Acessar [a página de modelos] (https://alphacephei.com/vosk/models).
4 Baixar vosk-model-en-us-0.22 ou similar.
