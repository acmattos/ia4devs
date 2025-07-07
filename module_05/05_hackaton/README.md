Dataset original:
https://universe.roboflow.com/aws-icons/aws-icon-detector/dataset/4

O dataset original possui alguns problemas. O principal é não possuir nenhum 
exemplo para validação. Outro grande problema é a disparidade entre os exemplos.
Algumas classes possuem poucos exemplos como `ACM`, com 3 para treinar e 1 para 
teste, contrastando com `Lambda`, com 316 para treino e 10 para teste ou `EC2`, 
com 213 para treino e 40 para teste. Temos muitos casos, como 
`Analytics Services`, que possui apenas 1 exemplo para treino e mais nenhum para 
teste. 
Você pode verificar como o dataset original se distribui pelos diretórios de 
treino e teste, executando o seguinte script:

```bash
py dataset_report_samples_per_split.py 
```

A execução do script, no 
[dataset **original**](https://universe.roboflow.com/aws-icons/aws-icon-detector/dataset/),
mostra os seguintes valores por classe: 

```bash
Classe                     |    id | Train | Valid | Test
ACM                        |     0 |     3 |     0 |    1
ALB                        |     1 |    32 |     0 |    5
AMI                        |     2 |     4 |     0 |    0
API-Gateway                |     3 |   163 |     0 |    0
Active Directory Service   |     4 |     1 |     0 |    1
Airflow_                   |     5 |     2 |     0 |    0
Amplify                    |     6 |     8 |     0 |    0
Analytics Services         |     7 |     1 |     0 |    0
AppFlow                    |     8 |     1 |     0 |    0
Appsync                    |     9 |     5 |     0 |    0
Athena                     |    10 |    10 |     0 |    1
Aurora                     |    11 |    14 |     0 |    7
Auto Scaling               |    12 |    34 |     0 |    8
Auto Scaling Group         |    13 |     8 |     0 |    0
Automated Tests            |    14 |     6 |     0 |    0
Availability Zone          |    15 |     4 |     0 |    0
Backup                     |    16 |     2 |     0 |    0
Build Environment          |    17 |     3 |     0 |    0
CDN                        |    18 |     2 |     0 |    1
CUR                        |    19 |     3 |     0 |    0
Call Metrics               |    20 |     1 |     0 |    0
Call Recordings            |    21 |     1 |     0 |    0
Certificate Manager        |    22 |     7 |     0 |    1
Client                     |    23 |     7 |     0 |    0
Cloud Connector            |    24 |     2 |     0 |    0
Cloud Map                  |    25 |     1 |     0 |    0
Cloud Search               |    26 |     3 |     0 |    1
Cloud Trail                |    27 |    16 |     0 |    3
Cloud Watch                |    28 |    70 |     0 |    7
CloudFormation Stack       |    29 |    15 |     0 |    1
CloudHSM                   |    30 |     1 |     0 |    1
CloudWatch Alarm           |    31 |    11 |     0 |    0
Cloudfront                 |    32 |    52 |     0 |    9
CodeBuild                  |    33 |    21 |     0 |    1
CodeCommit                 |    34 |     8 |     0 |    1
CodeDeploy                 |    35 |     1 |     0 |    1
CodePipeline               |    36 |    20 |     0 |    0
Cognito                    |    37 |    51 |     0 |    1
Comprehend                 |    38 |     5 |     0 |    0
Config                     |    39 |     6 |     0 |    6
Connect                    |    40 |     1 |     0 |    0
Connect Contact Lens       |    41 |     1 |     0 |    0
Container                  |    42 |    68 |     0 |    1
Control Tower              |    43 |     1 |     0 |    0
Customer Gateway           |    44 |     7 |     0 |    0
DSI                        |    45 |     4 |     0 |    0
Data Pipeline              |    46 |     2 |     0 |    0
DataSync                   |    47 |     2 |     0 |    0
Deploy Stage               |    48 |     2 |     0 |    0
Direct Connect             |    50 |    14 |     0 |   11
Docker Image               |    52 |    13 |     0 |    2
Dynamo DB                  |    53 |   144 |     0 |   19
EBS                        |    54 |     8 |     0 |    4
EC2                        |    55 |   213 |     0 |   40
EFS                        |    56 |     9 |     0 |    5
EFS Mount Target           |    57 |     8 |     0 |    9
EKS                        |    58 |    15 |     0 |    0
ELB                        |    59 |    77 |     0 |   13
Edge Location              |    61 |     4 |     0 |    3
ElastiCache                |    62 |    21 |     0 |    5
Elastic Container Registry |    63 |    25 |     0 |    0
Elastic Container Service  |    64 |    38 |     0 |    2
Elastic Search             |    65 |    12 |     0 |    1
Elemental MediaConvert     |    66 |     3 |     0 |    1
Email                      |    68 |     3 |     0 |    1
Endpoint                   |    69 |     2 |     0 |    0
Event Bus                  |    70 |     1 |     0 |    0
EventBridge                |    71 |     3 |     0 |    5
Experiment Duration        |    72 |     1 |     0 |    0
Experiments                |    73 |     1 |     0 |    0
Fargate                    |    74 |    41 |     0 |    0
Fault Injection Simulator  |    75 |     3 |     0 |    0
Flask                      |    77 |     3 |     0 |    0
GameLift                   |    79 |     2 |     0 |    0
Git                        |    80 |     1 |     0 |    0
Github                     |    81 |    11 |     0 |    0
Glue                       |    83 |    10 |     0 |    2
Glue DataBrew              |    84 |     2 |     0 |    0
Grafana                    |    85 |     1 |     0 |    0
GuardDuty                  |    86 |     4 |     0 |    5
IAM                        |    87 |    27 |     0 |    9
IAM Role                   |    88 |    16 |     0 |    7
IOT Core                   |    89 |     7 |     0 |    1
Image                      |    90 |     6 |     0 |    0
Image Builder              |    91 |     1 |     0 |    0
Ingress                    |    92 |     1 |     0 |    0
Instances                  |    94 |     2 |     0 |    0
Internet                   |    95 |    41 |     0 |    8
Internet Gateway           |    96 |    19 |     0 |    4
Jenkins                    |    97 |     2 |     0 |    0
Key Management Service     |    98 |    13 |     0 |    3
Kibana                     |    99 |     1 |     0 |    0
Kinesis Data Streams       |   100 |    21 |     0 |    4
Kubernetes                 |   101 |     1 |     0 |    0
Lambda                     |   102 |   316 |     0 |   10
Lex                        |   103 |     1 |     0 |    0
MQ                         |   104 |     9 |     0 |    0
Machine Learning           |   105 |     4 |     0 |    0
Macie                      |   106 |     5 |     0 |    4
Marketplace                |   107 |     2 |     0 |    0
Memcached                  |   108 |     2 |     0 |    2
Mobile Client              |   109 |    28 |     0 |    4
Mongo DB                   |   110 |     6 |     0 |    0
MySQL                      |   111 |     1 |     0 |    0
NAT Gateway                |   112 |    36 |     0 |    8
Neptune                    |   113 |     3 |     0 |    0
Network Adapter            |   114 |     1 |     0 |    0
Notebook                   |   116 |     1 |     0 |    0
Order Controller           |   117 |     1 |     0 |    0
Organization Trail         |   118 |     1 |     0 |    4
Parameter Store            |   119 |     2 |     0 |    0
Pinpoint                   |   120 |     1 |     0 |    0
PostgreSQL                 |   121 |     1 |     0 |    0
Private Link               |   122 |     7 |     0 |    0
Private Subnet             |   123 |   101 |     0 |   10
Prometheus                 |   124 |     1 |     0 |    0
Public Subnet              |   125 |    82 |     0 |   18
Quarkus                    |   126 |     1 |     0 |    0
Quicksight                 |   127 |     4 |     0 |    0
RDS                        |   128 |    70 |     0 |   14
React                      |   129 |     1 |     0 |    0
Redis                      |   130 |    11 |     0 |    1
Redshift                   |   131 |     6 |     0 |    1
Region                     |   132 |    28 |     0 |    2
Rekognition                |   133 |     2 |     0 |    0
Results                    |   134 |     1 |     0 |    0
Route 53                   |   135 |     2 |     0 |    1
Route53                    |   136 |    65 |     0 |    9
S3                         |   137 |   225 |     0 |   24
SAR                        |   138 |     1 |     0 |    0
SDK                        |   139 |    31 |     0 |    1
SES                        |   140 |    12 |     0 |    2
SNS                        |   141 |    30 |     0 |    3
SQS                        |   142 |    21 |     0 |    2
Sagemaker                  |   144 |    27 |     0 |    0
Secret Manager             |   145 |     4 |     0 |    1
Security Group             |   146 |     1 |     0 |    1
Security Hub               |   147 |     1 |     0 |    5
Server                     |   148 |    19 |     0 |   12
Service Catalog            |   149 |     6 |     0 |    0
Shield                     |   150 |     3 |     0 |    1
Slack                      |   152 |     2 |     0 |    0
Stack                      |   154 |     2 |     0 |    0
Step Function              |   155 |     3 |     0 |    3
SwaggerHub                 |   157 |     1 |     0 |    0
Systems Manager            |   158 |     3 |     0 |    2
TV                         |   159 |     1 |     0 |    0
Table                      |   160 |    19 |     0 |    0
Task Runner                |   161 |     1 |     0 |    0
Terraform                  |   162 |     3 |     0 |    0
Text File                  |   163 |     9 |     0 |    0
Textract                   |   164 |     1 |     0 |    0
Transcribe                 |   165 |     1 |     0 |    0
Transfer Family            |   166 |     6 |     0 |    0
Transit Gateway            |   167 |     2 |     0 |    0
Translate                  |   168 |     3 |     0 |    0
Trusted Advisor            |   169 |     2 |     0 |    0
Twilio                     |   170 |     1 |     0 |    0
Users                      |   171 |    95 |     0 |   13
VDA                        |   172 |     1 |     0 |    0
VP Gateway                 |   173 |     4 |     0 |    1
VPC Router                 |   174 |    11 |     0 |    6
VPN Connection             |   175 |     5 |     0 |    1
WAF                        |   176 |    14 |     0 |    1
Web Clients                |   177 |    36 |     0 |    7
Websites                   |   178 |     4 |     0 |    0
X-Ray                      |   179 |    12 |     0 |    0
aws                        |   180 |   136 |     0 |   13
cache Worker               |   181 |     2 |     0 |    0
```

Mas será que estes são os únicos problemas do dataset? O script abaixo faz 
algumas análises úteis:

```bash
py dataset_validation.py
```

Verificamos que o `nc` corresponde ao total de classes declaradas. No momento, 
temos 210 imagens e 210 labels.
Não há nomes de classes duplicados, ne, imagens sem labels ou memso labels sem 
imagens. O resultado do script pode ser visto abaixo:

```bash
── Passo 1: contagens ───────────────────────────────────────────────────────
nc declarado:       182
len(names):         182
total imagens:      210
total labels:       210
✅ nc == len(names)
✅ #imagens == #labels

── Passo 2: duplicatas em names ─────────────────────────────────────────────
✅ Nenhuma duplicata em names

── Passo 3: consistência labels x names x imagens ──────────────────────────
✅ Todos os class_id em labels têm names associados

✅ Todas as imagens têm .txt correspondente
✅ Todos os labels têm imagem correspondente

✅ Todas as classes em names têm pelo menos 1 exemplo
```

Se decidirmos treinar o modelo com o dataset incompleto (isto é, com 
`valid/images` e `valid/labels` vazios), notaremos duas coisas:


```bash
[1]
WARNING Box and segment counts should be equal, but got len(segments) = 502, 
len(boxes) = 3108. To resolve this only boxes will be used and all segments will 
be removed. To avoid this please supply either a detect or segment dataset, not 
a detect-segment mixed dataset.
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, 
blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', 
num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
[2]
Traceback (most recent call last):
  File "D:\ia4devs\module_05\05_hackaton\.venv\Lib\site-packages\ultralytics\data\base.py", 
  line 178, in get_img_files
    assert im_files, f"{self.prefix}No images found in {img_path}. {FORMATS_HELP_MSG}"
           ^^^^^^^^
AssertionError: val: No images found in D:\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\images. 
Supported formats are:
images: {'heic', 'jpg', 'pfm', 'dng', 'mpo', 'bmp', 'jpeg', 'png', 'tiff', 'webp', 'tif'}
videos: {'mov', 'mkv', 'gif', 'asf', 'ts', 'm4v', 'mpeg', 'webm', 'wmv', 'mpg', 'mp4', 'avi'}
```

[1] - Temos um aviso de que alguns rótulos nos arquivos de `label` estão 
inadequados. O formato de segmentação foi encontrado e o yolo vai descartar 
estas marcações.

[2] - O diretório `valid` deve conter imagens e labels.

Para corrigir [1], precisamos rodar o script:

```bash 
py dataset_fix_labels.py
```

Para que ele detecte e corrija os rótulos inadequados. O resultado final será 
visto a seguir:

```bash
Fixed segments in: index101_jpg.rf.86ebe1a7bcfdd3fa92ef93ba5bfd2d19.txt
Fixed segments in: index108_png.rf.c04ccc21c4ad1c3f1ca51903606f7f0c.txt
Fixed segments in: index121_png.rf.71f9a36ddec18e197b04cc9cfc9e33c0.txt
Fixed segments in: index126_png.rf.a27b004ecd3aaae4b1d3a4747b69d613.txt
Fixed segments in: index136_png.rf.fd69f2a7634f5d83d4b09ace2ed4e8cd.txt
Fixed segments in: index137_jpg.rf.4a31794a0730be847e886f42f0fb7c94.txt
Fixed segments in: index154_jpg.rf.77cf8cc45b8a14d6fe9ea46e7f476f96.txt
Fixed segments in: index156_png.rf.b5d9270f67fd558d8e9036f3dfd575c0.txt
Fixed segments in: index161_png.rf.6c17459407b2e312e7adcc5649873ef9.txt
Fixed segments in: index177_png.rf.0cbfadbf1c1f8a322c3fcc7dd55e46a2.txt
Fixed segments in: index190_png.rf.ff2f24ed464240039309195bf0a73958.txt
Fixed segments in: index200_png.rf.3e34f6ab90231de27051ce831507656f.txt
Fixed segments in: index60_png.rf.1e092d82c19763160ffbb6b2fdbf68fe.txt
Fixed segments in: index62_png.rf.a1dc5d4beaf0dce66f55b97b7218aa5a.txt
Fixed segments in: index67_png.rf.6101eff034895460da133f0a0c7bb7e9.txt
Fixed segments in: index69_png.rf.f31ae1094002aac0abf4942427ce17c3.txt
Fixed segments in: index72_png.rf.946082aea49f9d39dbfc714ab9a7becf.txt
Fixed segments in: index76_jpg.rf.acd014a7447bfd032a059df9a3c42ed2.txt
Fixed segments in: index78_jpg.rf.41ff895dc95a8301b653232b1f6076f7.txt
Fixed segments in: index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af.txt
Fixed segments in: index80_jpg.rf.ff8325243baab715ecc57e8b2816b32c.txt
Fixed segments in: index82_png.rf.59d98bc77a90b37701036d534176c12b.txt
Fixed segments in: index86_png.rf.1f930ebaa16216d58c45b42eed1980ff.txt
Fixed segments in: index87_png.rf.340a2720a19109394b7209a44a0a0560.txt
Fixed segments in: index93_png.rf.1b8824bdce863db0c370aa9e08dc6025.txt
Fixed segments in: index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601.txt
Fixed segments in: index97_png.rf.c7f0f49920f42b2c1ff635062a6db557.txt
Total files fixed: 27/189
Fixed segments in: index32_png.rf.1f5e0fbbf9b24e978afe47ad026cd451.txt
Fixed segments in: index40_png.rf.c25d82eaf131a966b05189d26ad5bcba.txt
Fixed segments in: index42_png.rf.fe55375b35dcd8d5acb87b455aefe16a.txt
Fixed segments in: index43_jpg.rf.57e2088b019cbe2301f88be96faa8caf.txt
Fixed segments in: index45_png.rf.b8216c6948f9c7338bbc2d54c154b512.txt
Fixed segments in: index46_png.rf.a43f82f889300675176613a33f4e8168.txt
Fixed segments in: index5_png.rf.88b49ae013835d02145d6c80bce061fd.txt
Fixed segments in: index6_jpg.rf.f5a1f31d53e0577b2a9745e1f9b4f77b.txt
Total files fixed: 8/21
Total files fixed: 0/0
```

Para corrigir [2], precisamos rodar o script:

```bash 
py dataset_rebalance_oversample.py
```
O script faz basicamente três coisas — geração de exemplos via oversampling, 
realocação para garantir ao menos um número mínimo de amostras em valid e em 
test, sempre mantendo sincronizados os arquivos de imagem e os de label.
Na fase 1, garante no mínimo MIN_TRAIN instâncias de cada classe em train, 
duplicando (com oversampling) de forma round-robin pelas `bases` disponíveis.
A cada nova imagem criada, também incrementa o contador e adiciona o novo 
`basename` ao conjunto.
Na fase 2, garante pelo menos MIN_VALID instâncias em valid, movendo pares 
imagem+label de train (preferência) ou test.
Na fase 3, aAssegura pelo menos MIN_TEST instâncias em test, movendo pares 
imagem+label de train (preferência) ou valid.

Abaixo, um log de exemplo da execução do script:

```bash
=== Phase 1: Oversampling → TRAIN ===

Class   0: train has 70, target 70 → need 0
  → OK, não precisa oversample

Class   1: train has 48, target 70 → need 22
  → usando fonte train para oversample

(...)

Class 181: train has 2, target 70 → need 68
  → usando fonte train para oversample

=== Phase 2: Rebalance → VALID ===

Class   0: valid has 0, min 15 → need 15
  → movendo de train para valid
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_5 from train → valid
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_5 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_24 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_24 from train → valid
  → movendo de train para valid
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_20 from train → valid
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_20 from train → valid
  → movendo de train para valid
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_58 from train → valid
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_58 from train → valid
  → movendo de train para valid
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_16 from train → valid
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_16 from train → valid
  → movendo de train para valid
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_19 from train → valid
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_19 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_57 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_57 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_9 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_9 from train → valid
  → movendo de train para valid
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_11 from train → valid
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_11 from train → valid
  → movendo de train para valid
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_56 from train → valid
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_56 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_0 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_0 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_36 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_36 from train → valid
  → movendo de train para valid
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_55 from train → valid
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_55 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_27 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_27 from train → valid
  → movendo de train para valid
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_48 from train → valid
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_48 from train → valid

(...)

Class 181: valid has 0, min 15 → need 15
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
    Moved IMAGE  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_29 from train → valid
    Moved LABEL  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_29 from train → valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid
    Moved IMAGE  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_61 from train → valid
    Moved LABEL  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_61 from train → valid
  → movendo de train para valid
  → movendo de train para valid
  → movendo de train para valid

=== Phase 3: Rebalance → TEST ===

Class   0: test has 1, min 15 → need 14
  → movendo 'index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_60' de train para test
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_60 from train → test
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_60 from train → test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_28' de train para test
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_28 from train → test
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_28 from train → test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025' de train para test
  → movendo 'index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_48' de train para test
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_48 from train → test
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_48 from train → test
  → movendo 'index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_50' de train para test
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_50 from train → test
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_50 from train → test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_40' de train para test
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_40 from train → test
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_40 from train → test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_49' de train para test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_37' de train para test
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_37 from train → test
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_37 from train → test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_4' de train para test
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_4 from train → test
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_4 from train → test
  → movendo 'index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_2' de train para test
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_2 from train → test
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_2 from train → test
  → movendo 'index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_26' de train para test
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_26 from train → test
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_26 from train → test
  → movendo 'index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_41' de train para test
    Moved IMAGE  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_41 from train → test
    Moved LABEL  index151_jpg.rf.9e63372d562634afb9a7d4bcef7c59f6_os_41 from train → test
  → movendo 'index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_6' de train para test
    Moved IMAGE  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_6 from train → test
    Moved LABEL  index79_jpg.rf.4546d4d5cf54f6ddfb791a379783d3af_os_6 from train → test
  → movendo 'index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_19' de train para test
    Moved IMAGE  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_19 from train → test
    Moved LABEL  index93_png.rf.1b8824bdce863db0c370aa9e08dc6025_os_19 from train → test
  → test agora tem 15 para classe 0

(...)

Class 181: test has 0, min 15 → need 15
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_39' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_30' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_8' de train para test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_23' de train para test
    Moved IMAGE  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_23 from train → test
    Moved LABEL  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_23 from train → test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_31' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_36' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_6' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_16' de train para test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_19' de train para test
    Moved IMAGE  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_19 from train → test
    Moved LABEL  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_19 from train → test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_33' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_38' de train para test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_67' de train para test
    Moved IMAGE  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_67 from train → test
    Moved LABEL  index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_67 from train → test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_3' de train para test
  → movendo 'index161_png.rf.6c17459407b2e312e7adcc5649873ef9_os_27' de train para test
  → movendo 'index96_png.rf.50a8179a165b9e4dfa62dadcb03a7601_os_34' de train para test
  → test agora tem 15 para classe 181

=== Summary ===
Oversampled → TRAIN : 10484
Moved to VALID     : 2730
Moved to TEST      : 2345
```
S
🎯 Test Metrics (mean per class):
  Precision:    0.470
  Recall:       0.317
  mAP@0.5:      0.318
  mAP@0.5:0.95: 0.257



```commandline
RESULTADO FINAL
```


## Treinamento do Yolo 11 Modelo N

```bash
Ultralytics 8.3.162  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, 
auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, 
classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, 
copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, 
degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, 
dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, 
flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, 
hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, 
kobj=1.0, line_width=None, lr0=0.0005, lrf=0.05, mask_ratio=4, max_det=300, 
mixup=0.5, mode=train, model=./data/model/yolo11n.pt, momentum=0.937, 
mosaic=1.0, multi_scale=True, name=yolo11n_custom_100, nbs=64, nms=False, 
opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=10, 
perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, 
project=None, rect=False, resume=False, retina_masks=False, save=True, 
save_conf=False, save_crop=False, 
save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100, 
save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, 
seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, 
simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, 
task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, 
verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, 
warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=182

            from  n    params  module                                arguments
  0           -1  1       464  ultralytics.nn.modules.conv.Conv      [3, 16, 3, 2]
  1           -1  1      4672  ultralytics.nn.modules.conv.Conv      [16, 32, 3, 2]
  2           -1  1      6640  ultralytics.nn.modules.block.C3k2     [32, 64, 1, False, 0.25]
  3           -1  1     36992  ultralytics.nn.modules.conv.Conv      [64, 64, 3, 2]
  4           -1  1     26080  ultralytics.nn.modules.block.C3k2     [64, 128, 1, False, 0.25]
  5           -1  1    147712  ultralytics.nn.modules.conv.Conv      [128, 128, 3, 2]
  6           -1  1     87040  ultralytics.nn.modules.block.C3k2     [128, 128, 1, True]
  7           -1  1    295424  ultralytics.nn.modules.conv.Conv      [128, 256, 3, 2]
  8           -1  1    346112  ultralytics.nn.modules.block.C3k2     [256, 256, 1, True]
  9           -1  1    164608  ultralytics.nn.modules.block.SPPF     [256, 256, 5]
 10           -1  1    249728  ultralytics.nn.modules.block.C2PSA    [256, 256, 1]
 11           -1  1         0  torch.nn.modules.upsampling.Upsample  [None, 2, 'nearest']
 12      [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat    [1]
 13           -1  1    111296  ultralytics.nn.modules.block.C3k2     [384, 128, 1, False]
 14           -1  1         0  torch.nn.modules.upsampling.Upsample  [None, 2, 'nearest']
 15      [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat    [1]
 16           -1  1     32096  ultralytics.nn.modules.block.C3k2     [256, 64, 1, False]
 17           -1  1     36992  ultralytics.nn.modules.conv.Conv      [64, 64, 3, 2]
 18     [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat    [1]
 19           -1  1     86720  ultralytics.nn.modules.block.C3k2     [192, 128, 1, False]
 20           -1  1    147712  ultralytics.nn.modules.conv.Conv      [128, 128, 3, 2]
 21     [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat    [1]
 22           -1  1    378880  ultralytics.nn.modules.block.C3k2     [384, 256, 1, True]
 23 [16, 19, 22]  1    521278  ultralytics.nn.modules.head.Detect    [182, [64, 128, 256]]
YOLO11n summary: 181 layers, 2,680,446 parameters, 2,680,430 gradients, 6.9 GFLOPs

Transferred 448/499 items from pretrained weights
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed
train: Fast image access  (ping: 0.00.0 ms, read: 2741.9957.6 MB/s, size: 410.9 KB)
train: Scanning D:\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 3457 images, 0 backgrounds, 0 c
val: Fast image access  (ping: 0.00.0 ms, read: 977.6420.3 MB/s, size: 204.4 KB)
val: Scanning D:\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 1488 images, 0 backgrounds, 0 cor
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\labels.jpg...
optimizer: AdamW(lr=0.0005, momentum=0.937) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/100      6.44G      1.233      3.756     0.9746         32        864: 100%|██████████| 433/433 [00:54<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:23
                   all       1488      30084      0.385     0.0828     0.0319     0.0239

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/100      6.12G       1.14      2.761     0.9666        125        320: 100%|██████████| 433/433 [00:48<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:09
                   all       1488      30084      0.643      0.138       0.12     0.0872

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/100       4.7G      1.075      2.182     0.9515         24        480: 100%|██████████| 433/433 [00:47<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:09
                   all       1488      30084      0.609      0.248      0.258      0.196

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/100      4.43G      1.049      1.896     0.9445         98        608: 100%|██████████| 433/433 [00:47<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.585      0.324      0.354      0.269

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/100      5.45G      1.005      1.644     0.9351         78        640: 100%|██████████| 433/433 [00:46<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.643      0.426      0.461      0.361

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/100      5.35G     0.9933        1.5     0.9282         30        896: 100%|██████████| 433/433 [00:46<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.624      0.515       0.57      0.441

 (...)     

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/100      5.61G     0.7054     0.5857      0.862         23        896: 100%|██████████| 433/433 [00:48<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.954      0.982      0.981      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/100      5.03G     0.7039     0.5761     0.8637         43        928: 100%|██████████| 433/433 [00:50<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.951      0.989      0.981      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/100      3.88G     0.7042     0.5848     0.8582         17        416: 100%|██████████| 433/433 [00:48<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.955      0.986       0.98      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/100      3.89G     0.6942     0.5689      0.863         41        832: 100%|██████████| 433/433 [00:49<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.955      0.987       0.98      0.876

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/100      3.91G     0.6947     0.5699     0.8605         91        960: 100%|██████████| 433/433 [00:48<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.959      0.983      0.981      0.878

(...)

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     98/100      3.61G     0.4652     0.2971     0.8127         18        416: 100%|██████████| 433/433 [00:46<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084       0.96      0.995      0.983      0.911

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     99/100      3.61G     0.4553     0.2923     0.8131         30        896: 100%|██████████| 433/433 [00:46<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.961      0.994      0.984      0.911

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    100/100      3.61G     0.4588     0.2938     0.8114         22        960: 100%|██████████| 433/433 [00:45<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 93/93 [00:08
                   all       1488      30084      0.961      0.994      0.983      0.912

100 epochs completed in 1.622 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\best.pt, 5.7MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\best.pt...
Ultralytics 8.3.162  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
                     Class  Images Instances  Box(P      R  mAP50mAP50-95): 100%|██████████| 93/93 [00:12
                       all    1488     30084  0.957  0.994  0.984    0.892
                       ACM      62        62  0.989      1  0.995    0.958
                       ALB     228       332  0.992      1  0.994    0.862
                       AMI      29        44  0.982      1  0.995    0.943
               API-Gateway     774      1178  0.997  0.983  0.995    0.909
  Active Directory Service      31        31  0.984      1  0.995    0.954
                  Airflow_      15        30  0.983      1  0.995    0.898
                   Amplify      84        84   0.99      1  0.995    0.833
        Analytics Services      15        15  0.969      1  0.995    0.897
                   AppFlow      15        15  0.969      1  0.995    0.897
                   Appsync      61        61  0.989      1  0.995    0.824
                    Athena     143       148      1  0.995  0.995     0.91
                    Aurora      89       126  0.963      1  0.982    0.935
              Auto Scaling     173       307  0.984  0.993  0.995     0.83
        Auto Scaling Group      35        88  0.992      1  0.995     0.82
           Automated Tests      64        98  0.995      1  0.995    0.917
         Availability Zone      24        48  0.989      1  0.995    0.898
                    Backup      15        30  0.984      1  0.995    0.995
         Build Environment      44        44  0.848      1  0.995    0.862
                       CDN      20        20   0.89      1  0.966    0.921
                       CUR      42        42  0.988      1  0.995    0.751
              Call Metrics      15        15   0.97      1  0.995    0.887
           Call Recordings      15        15  0.973      1  0.995    0.793
       Certificate Manager      98        98  0.994      1  0.995    0.945
                    Client      16        61  0.671  0.702   0.74    0.649
           Cloud Connector      16        32  0.982      1  0.995    0.877
                 Cloud Map      15        15  0.968      1  0.995    0.995
              Cloud Search      56        56  0.801      1  0.995    0.893
               Cloud Trail     187       192  0.997      1  0.995    0.903
               Cloud Watch     543       644  0.986      1  0.995    0.906
      CloudFormation Stack     150       168  0.995      1  0.995    0.929
                  CloudHSM      34        34  0.983      1  0.995    0.916
          CloudWatch Alarm      87       121  0.996      1  0.995    0.882
                Cloudfront     401       427  0.997  0.998  0.995      0.9
                 CodeBuild     157       245  0.997      1  0.995     0.94
                CodeCommit      68        80  0.992      1  0.995    0.941
                CodeDeploy      17        17  0.971      1  0.995    0.995
              CodePipeline     214       220  0.998      1  0.995    0.915
                   Cognito     346       391  0.971  0.927  0.982    0.898
                Comprehend      72        72  0.992      1  0.995    0.959
                    Config     103       178  0.903  0.993  0.982    0.873
                   Connect      15        15  0.969      1  0.995    0.962
      Connect Contact Lens      15        15  0.964      1  0.995    0.902
                 Container      79       346  0.964  0.997  0.995    0.834
             Control Tower      17        17  0.973      1  0.995    0.986
          Customer Gateway      38        74  0.996      1  0.995    0.905
                       DSI      34        68  0.993      1  0.995    0.858
             Data Pipeline      23        23  0.978      1  0.995    0.914
                  DataSync      32        32  0.985      1  0.995    0.995
              Deploy Stage      30        30  0.978      1  0.995    0.848
                 Detective      15        15  0.967      1  0.995    0.922
            Direct Connect      91       126  0.995      1  0.995    0.939
              Distribution      15        15  0.603      1  0.947    0.927
              Docker Image      56       179  0.953  0.904  0.983    0.744
                 Dynamo DB     660       979  0.997      1  0.995    0.915
                       EBS      92       147  0.936  0.993  0.995    0.846
                       EC2     707      1935  0.982  0.997  0.995    0.892
                       EFS     100       133  0.995      1  0.995    0.928
          EFS Mount Target      99       129  0.995      1  0.995    0.877
                       EKS     161       184  0.996      1  0.995    0.926
                       ELB     425       583  0.997  0.966   0.97    0.907
                       EMR      15        15  0.968      1  0.995    0.922
             Edge Location      20        42  0.989      1  0.995    0.978
               ElastiCache     138       170  0.989      1  0.995    0.882
Elastic Container Registry     235       235  0.979  0.996  0.995    0.936
 Elastic Container Service     258       331  0.998      1  0.995    0.866
            Elastic Search     142       147  0.995      1  0.995    0.882
    Elemental MediaConvert      49        66  0.898  0.802  0.961    0.951
    Elemental MediaPackage      15        15  0.467      1  0.669    0.669
                     Email      25        25   0.98      1  0.995    0.912
                  Endpoint      27        27  0.973      1  0.995    0.815
                 Event Bus      16        16  0.962      1  0.995    0.995
               EventBridge      60       120  0.915      1  0.994     0.89
       Experiment Duration      17        17  0.565      1  0.772    0.597
               Experiments      17        17  0.561      1  0.641    0.585
                   Fargate     193       427  0.999      1  0.995    0.885
 Fault Injection Simulator      49        49   0.99      1  0.995    0.918
          Firewall Manager      15        15  0.968      1  0.995    0.922
                     Flask      15        45  0.977  0.956  0.984    0.726
                 Flow logs      15        60  0.985      1  0.995    0.745
                  GameLift      17        17  0.973      1  0.995     0.93
                       Git      15        15   0.97      1  0.995    0.904
                    Github      81        95  0.986      1  0.995    0.911
                   Glacier      15        15  0.967      1  0.995      0.9
                      Glue      58       116      1  0.979  0.995    0.876
             Glue DataBrew      26        26  0.982      1  0.995    0.969
                   Grafana      20        20  0.977      1  0.995    0.995
                 GuardDuty      72       132  0.996      1  0.995    0.843
                       IAM     201       334   0.83      1  0.985    0.844
                  IAM Role      98       207  0.823  0.965  0.971    0.776
                  IOT Core      40        54  0.991      1  0.995    0.969
                     Image      74        74  0.992      1  0.995    0.821
             Image Builder      15        15  0.964      1  0.995    0.995
                   Ingress      15        15   0.97      1  0.995    0.989
           Inspector Agent      15        15  0.969      1  0.995    0.834
                 Instances      19        38  0.554   0.98  0.661    0.587
                  Internet     240       345  0.949      1  0.994    0.907
          Internet Gateway     167       247  0.965      1  0.995    0.836
                   Jenkins      15        30  0.984      1  0.995     0.97
    Key Management Service     127       155  0.997      1  0.995    0.915
                    Kibana      15        15   0.97      1  0.995    0.845
      Kinesis Data Streams     150       198  0.986      1  0.995    0.937
                Kubernetes      15        15   0.97      1  0.995    0.918
                    Lambda     945      2489  0.994  0.997  0.995    0.919
                       Lex      16        16   0.97      1  0.995    0.995
                        MQ      25        57  0.991      1  0.995    0.869
          Machine Learning      56        56  0.832      1   0.98    0.947
                     Macie      65       146   0.99      1  0.995    0.832
               Marketplace      21        21  0.981      1  0.995    0.662
                 Memcached      18        36  0.976      1  0.995    0.923
             Mobile Client     198       249  0.975  0.984  0.989    0.831
                  Mongo DB      26        70  0.971  0.957  0.994    0.775
                     MySQL      15        15  0.973      1  0.995    0.844
               NAT Gateway     187       375  0.999      1  0.995    0.913
                   Neptune      42        42  0.991      1  0.995    0.679
           Network Adapter      15        15  0.916      1  0.995    0.995
          Network Firewall      15        15  0.968      1  0.995    0.986
                  Notebook      18        18  0.974      1  0.995    0.982
          Order Controller      18        18  0.973      1  0.995     0.91
        Organization Trail      32        77  0.992      1  0.995    0.873
           Parameter Store      26        26   0.98      1  0.995     0.92
                  Pinpoint      16        16   0.97      1  0.995    0.973
                PostgreSQL      15        15  0.964      1  0.995    0.911
              Private Link      89        89  0.994      1  0.995    0.912
            Private Subnet     368       930  0.982  0.967  0.986    0.798
                Prometheus      20        20  0.976      1  0.995    0.922
             Public Subnet     338       841   0.98  0.987  0.993     0.79
                   Quarkus      20        20  0.976      1  0.995    0.966
                Quicksight      41        51  0.972      1  0.995     0.92
                       RDS     345       685  0.985  0.987  0.994     0.89
                     React      15        15  0.852      1  0.995    0.815
                     Redis      49       100      1  0.995  0.995     0.91
                  Redshift      73        80  0.994      1  0.995    0.868
                    Region     183       269  0.994      1  0.995    0.828
               Rekognition      33        33  0.984      1  0.995    0.973
                   Results      17        17  0.564      1  0.737    0.681
                  Route 53      53        53  0.987      1  0.995     0.97
                   Route53     428       611  0.995      1  0.995    0.918
                        S3     977      2096  0.995  0.999  0.995    0.894
                       SAR      18        18  0.974      1  0.995    0.989
                       SDK     123       403  0.972  0.995  0.995     0.89
                       SES      72        87  0.994      1  0.995    0.895
                       SNS     258       279  0.994      1  0.995    0.954
                       SQS     189       199  0.997      1  0.995    0.913
                 SSM Agent      15        15  0.969      1  0.995    0.967
                 Sagemaker      81       267  0.985      1  0.995    0.731
            Secret Manager      46        46  0.987      1  0.995    0.924
            Security Group      15        15  0.967      1  0.995    0.995
              Security Hub      31        91  0.955      1  0.995    0.812
                    Server     101       193  0.989      1  0.995     0.91
           Service Catalog      40        91  0.994      1  0.995    0.885
                    Shield      58        58  0.991      1  0.995    0.966
                   Sign-On      15        15  0.969      1  0.995     0.91
                     Slack      37        37  0.984      1  0.995    0.923
                  Snowball      15        15  0.969      1  0.995    0.984
                     Stack      22        22  0.977      1  0.995    0.862
             Step Function      32        96  0.994      1  0.995    0.909
           Storage Gateway      15        15  0.966      1  0.995    0.902
                SwaggerHub      15        15  0.966      1  0.995     0.96
           Systems Manager      61        76   0.99      1  0.995    0.949
                        TV      22        22  0.976      1  0.995    0.897
                     Table      88       196      1      1  0.995    0.847
               Task Runner      18        18   0.97      1  0.995    0.905
                 Terraform      32        32  0.986      1  0.995    0.874
                 Text File      54       122  0.946      1  0.994    0.881
                  Textract      17        17  0.971      1  0.995    0.966
                Transcribe      17        17  0.972      1  0.995    0.909
           Transfer Family      68        68  0.993      1  0.995    0.954
           Transit Gateway      35        35  0.964      1  0.995    0.927
                 Translate      49        49   0.99      1  0.995     0.96
           Trusted Advisor      36        36  0.987      1  0.995    0.952
                    Twilio      15        15  0.969      1  0.995    0.987
                     Users     574       790  0.994  0.971  0.992     0.87
                       VDA      16        16  0.964      1  0.995    0.895
                VP Gateway      30        36   0.99      1  0.995     0.85
                VPC Router      50       102  0.933      1  0.995    0.894
            VPN Connection      21        57   0.99      1  0.995    0.917
                       WAF     112       131  0.996      1  0.995    0.917
               Web Clients     213       248  0.784      1  0.983    0.826
                  Websites      31        31  0.985      1  0.995    0.933
                     X-Ray      83        95  0.995      1  0.995    0.911
                       aws     971      1219  0.981  0.991  0.994    0.841
              cache Worker      36        36  0.982      1  0.995    0.933
Speed: 0.1ms preprocess, 4.4ms inference, 0.0ms loss, 1.1ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\best.pt
Ultralytics 8.3.162  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 627.2396.8 MB/s, size: 365.8 KB)
val: Scanning D:\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels... 1327 images, 0 backgrounds, 0 corrupt: 1
val: New cache created: D:\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache
                     Class Images Instances  Box(P      R  mAP50 mAP50-95): 100%|██████████| 166/166 [00:
                       all   1327     26828  0.957  0.992  0.979     0.911
                       ACM     42        42  0.984      1  0.995      0.99
                       ALB    206       292  0.968  0.983  0.993     0.891
                       AMI     24        39  0.985      1  0.995     0.956
               API-Gateway    707      1063      1  0.981  0.995      0.93
  Active Directory Service     29        29  0.982      1  0.995     0.985
                  Airflow_     15        30  0.983      1  0.995     0.901
                   Amplify     76        76  0.998      1  0.995     0.894
        Analytics Services     15        15  0.967      1  0.995     0.978
                   AppFlow     15        15  0.968      1  0.995     0.986
                   Appsync     50        50  0.972      1  0.995     0.817
                    Athena    133       141      1  0.979  0.995     0.939
                    Aurora     79       112  0.983  0.964  0.968     0.933
              Auto Scaling    126       211  0.996  0.976  0.989     0.826
        Auto Scaling Group     25        58  0.988      1  0.995     0.848
           Automated Tests     58        89  0.996      1  0.995      0.95
         Availability Zone     23        46  0.987      1  0.995     0.935
                    Backup     16        32  0.983      1  0.995     0.995
         Build Environment     34        34   0.89      1  0.995     0.845
                       CDN     21        21  0.974      1  0.995     0.976
                       CUR     35        35  0.985      1  0.995      0.79
              Call Metrics     15        15  0.965      1  0.995     0.863
           Call Recordings     15        15  0.976      1  0.995     0.859
       Certificate Manager    103       103  0.995      1  0.995     0.987
                    Client     16        61  0.559   0.82  0.686     0.612
           Cloud Connector     14        28  0.979      1  0.995     0.919
                 Cloud Map     15        15  0.966      1  0.995     0.995
              Cloud Search     48        48  0.761      1  0.995      0.93
               Cloud Trail    140       142  0.996      1  0.995     0.944
               Cloud Watch    468       566  0.997      1  0.995     0.924
      CloudFormation Stack    124       138  0.988      1  0.995     0.981
                  CloudHSM     33        33  0.981      1  0.995     0.977
          CloudWatch Alarm     75       106  0.995      1  0.995     0.886
                Cloudfront    346       366  0.996      1  0.995      0.91
                 CodeBuild    140       208  0.997      1  0.995     0.963
                CodeCommit     52        66  0.992      1  0.995     0.983
                CodeDeploy     13        13   0.96      1  0.995     0.988
              CodePipeline    183       190  0.993      1   0.99     0.916
                   Cognito    310       354  0.969  0.935  0.975     0.927
                Comprehend     73        73  0.993      1  0.995      0.95
                    Config     72       147  0.912  0.983  0.986     0.889
                   Connect     15        15  0.967      1  0.995     0.984
      Connect Contact Lens     15        15   0.97      1  0.995     0.942
                 Container     86       403  0.988      1  0.995     0.861
             Control Tower     14        14  0.964      1  0.995     0.976
          Customer Gateway     35        62  0.996      1  0.995     0.929
                       DSI     31        62  0.992      1  0.995     0.854
             Data Pipeline     22        22  0.975      1  0.995     0.995
                  DataSync     30        30  0.982      1  0.995     0.995
              Deploy Stage     27        27  0.979      1  0.995     0.863
                 Detective     15        15  0.963      1  0.995     0.922
            Direct Connect     77       112  0.995  0.991  0.995     0.914
              Distribution     15        15  0.594      1  0.849     0.822
              Docker Image     44       174  0.993  0.877  0.984      0.76
                 Dynamo DB    619       958  0.997  0.993  0.995     0.921
                       EBS     65       107  0.931  0.963  0.992     0.825
                       EC2    609      1692  0.982  0.987  0.994     0.904
                       EFS     90       116  0.986  0.983  0.989     0.931
          EFS Mount Target     95       128      1  0.925  0.981     0.905
                       EKS    147       164  0.996      1  0.995     0.956
                       ELB    379       521  0.996  0.956   0.97     0.912
                       EMR     15        15  0.966      1  0.995      0.98
             Edge Location     15        27  0.982      1  0.995      0.94
               ElastiCache    101       121  0.994  0.967  0.971     0.871
Elastic Container Registry    212       212  0.998      1  0.995     0.957
 Elastic Container Service    236       302  0.995      1  0.995       0.9
            Elastic Search    116       117  0.984      1  0.995      0.89
    Elemental MediaConvert     49        64  0.853  0.938   0.97     0.955
    Elemental MediaPackage     15        15  0.498      1  0.563     0.563
                     Email     29        29   0.98  0.966  0.969     0.871
                  Endpoint     22        22  0.975      1  0.995     0.846
                 Event Bus     15        15  0.963      1  0.995     0.995
               EventBridge     41       101  0.912   0.99  0.993     0.923
       Experiment Duration     14        14  0.552   0.88  0.559     0.489
               Experiments     14        14  0.513      1  0.692     0.666
                   Fargate    180       423  0.999      1  0.995     0.923
 Fault Injection Simulator     45        45  0.989      1  0.995     0.931
          Firewall Manager     15        15  0.966      1  0.995     0.915
                     Flask     17        51  0.996   0.98  0.994     0.742
                 Flow logs     15        60  0.992      1  0.995      0.81
                  GameLift     15        15  0.966      1  0.995     0.933
                       Git     17        17  0.974      1  0.995     0.964
                    Github     73        90  0.995      1  0.995     0.928
                   Glacier     15        15  0.967      1  0.995     0.989
                      Glue     59       118      1  0.964  0.995     0.923
             Glue DataBrew     22        22  0.976      1  0.995     0.995
                   Grafana     14        14  0.966      1  0.995     0.995
                 GuardDuty     57       117  0.998      1  0.995     0.904
                       IAM    180       335  0.921  0.994  0.991     0.889
                  IAM Role     78       185  0.843  0.984   0.98     0.816
                  IOT Core     46        52      1  0.991  0.995     0.988
                     Image     63        63   0.99      1  0.995     0.843
             Image Builder     15        15  0.966      1  0.995     0.984
                   Ingress     17        17  0.971      1  0.995     0.995
           Inspector Agent     15        15  0.968      1  0.995     0.995
                 Instances     16        32  0.517      1  0.536     0.476
                  Internet    201       272  0.947  0.993  0.993     0.915
          Internet Gateway    133       200  0.996   0.99  0.995     0.836
                   Jenkins     15        30  0.982      1  0.995     0.969
    Key Management Service    111       139  0.997      1  0.995     0.965
                    Kibana     18        18  0.983      1  0.995     0.899
      Kinesis Data Streams    156       207  0.995  0.986  0.995     0.946
                Kubernetes     17        17  0.971      1  0.995     0.957
                    Lambda    830      2220  0.995  0.995  0.995     0.939
                       Lex     18        18  0.971      1  0.995     0.995
                        MQ     34        86  0.994      1  0.995     0.899
          Machine Learning     47        47  0.805      1  0.981     0.933
                     Macie     56       119  0.983  0.977  0.994     0.911
               Marketplace     19        19  0.979      1  0.995     0.689
                 Memcached     11        22  0.895      1  0.995     0.943
             Mobile Client    150       196  0.987   0.98  0.986     0.848
                  Mongo DB     26        62      1  0.986  0.995     0.783
                     MySQL     15        15  0.974      1  0.995       0.9
               NAT Gateway    147       293  0.987  0.986  0.988     0.919
                   Neptune     35        35  0.988      1  0.995     0.708
           Network Adapter     15        15  0.949      1  0.995     0.995
          Network Firewall     15        15  0.966      1  0.995     0.995
                  Notebook     15        15  0.965      1  0.995     0.995
          Order Controller     17        17   0.97      1  0.995     0.905
        Organization Trail     26        71  0.992      1  0.995     0.934
           Parameter Store     27        27  0.978      1  0.995      0.94
                  Pinpoint     16        16  0.969      1  0.995     0.995
                PostgreSQL     15        15  0.962      1  0.995     0.919
              Private Link     87        87  0.994      1  0.995     0.967
            Private Subnet    335       936  0.994  0.966  0.985      0.83
                Prometheus     14        14  0.964      1  0.995     0.995
             Public Subnet    299       715  0.995  0.976  0.994     0.823
                   Quarkus     14        14  0.962      1  0.995     0.995
                Quicksight     40        50  0.986      1  0.995     0.966
                       RDS    266       551  0.972  0.975  0.977     0.898
                     React     15        15  0.838  0.933  0.973     0.756
                     Redis     47        98      1  0.996  0.995     0.975
                  Redshift     65        72  0.993      1  0.995     0.945
                    Region    161       243      1      1  0.995     0.876
               Rekognition     37        37  0.986      1  0.995     0.981
                   Results     14        14  0.517      1  0.555     0.525
                  Route 53     39        39  0.957      1  0.993      0.98
                   Route53    376       532  0.992  0.991  0.993     0.926
                        S3    867      1862  0.999  0.995  0.995     0.916
                       SAR     14        14  0.964      1  0.995      0.99
                       SDK     98       301  0.974  0.999  0.993     0.887
                       SES     69        84  0.991  0.988  0.995     0.932
                       SNS    232       254  0.998  0.996  0.995     0.967
                       SQS    184       197  0.997      1  0.995     0.956
                 SSM Agent     15        15  0.966      1  0.995     0.995
                 Sagemaker     76       241  0.999      1  0.995     0.736
            Secret Manager     44        44  0.986      1  0.995     0.957
            Security Group     16        16  0.969      1  0.995     0.966
              Security Hub     25        85  0.994      1  0.995     0.897
                    Server     88       165  0.995      1  0.995     0.904
           Service Catalog     30        72  0.994      1  0.995     0.907
                    Shield     52        52  0.991      1  0.995     0.963
                   Sign-On     15        15  0.966      1  0.995     0.934
                     Slack     30        30   0.98      1  0.995     0.983
                  Snowball     15        15  0.968      1  0.995     0.995
                     Stack     14        14  0.967      1  0.995     0.908
             Step Function     30        90  0.994      1  0.995      0.92
           Storage Gateway     15        15  0.965      1  0.995      0.97
                SwaggerHub     15        15  0.971      1  0.995     0.965
           Systems Manager     53        68  0.987      1  0.995      0.99
                        TV     12        12  0.956      1  0.995     0.912
                     Table     72       154  0.991  0.987  0.995      0.88
               Task Runner     17        17   0.97      1  0.995     0.995
                 Terraform     38        38  0.989      1  0.995     0.864
                 Text File     49        99  0.949  0.899   0.97     0.866
                  Textract     14        14  0.965      1  0.995     0.995
                Transcribe     19        19  0.974      1  0.995     0.995
           Transfer Family     67        67  0.993      1  0.995     0.985
           Transit Gateway     31        31  0.962      1  0.995     0.895
                 Translate     53        53   0.99      1  0.995     0.959
           Trusted Advisor     13        13  0.958      1  0.995     0.964
                    Twilio     18        18  0.971      1  0.995      0.98
                     Users    486       656  0.995   0.98  0.987     0.893
                       VDA     14        14  0.966      1  0.995     0.912
                VP Gateway     27        39  0.989  0.974  0.984     0.841
                VPC Router     39        80   0.98      1  0.995     0.879
            VPN Connection     21        48  0.997      1  0.995      0.91
                       WAF     99       109  0.995      1  0.995     0.968
               Web Clients    202       268  0.795      1  0.971      0.84
                  Websites     34        34   0.99      1  0.995     0.953
                     X-Ray     88       112      1  0.988  0.995     0.953
                       aws    845      1067  0.982  0.986  0.992      0.87
              cache Worker     26        26  0.981      1  0.995     0.995
Speed: 0.2ms preprocess, 2.7ms inference, 0.0ms loss, 1.0ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.957
  Recall:       0.992
  mAP@0.5:      0.979
  mAP@0.5:0.95: 0.911

image 1/1 D:\ia4devs\module_05\05_hackaton\data\sample\aws_02.png: 576x640 
1 ALB, 1 Auto Scaling, 1 Auto Scaling Group, 2 Cloud Watchs, 1 Cloudfront, 4 EC2s, 
1 EFS, 1 Key Management Service, 2 NAT Gateways, 3 Private Subnets, 3 Public Subnets, 
1 RDS, 1 Region, 1 Users, 2 WAFs, 1 aws, 47.2ms
Speed: 3.3ms preprocess, 47.2ms inference, 5.2ms postprocess per image at shape (1, 3, 576, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict\labels
✅ Detailed JSON saved to data\reports\yolo11n_custom_100\results.json
✅ Summary JSON saved to data\reports\yolo11n_custom_100\report.json
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
(...)
obb: None
(...)
path: 'D:\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict'
speed: {'preprocess': 3.2868999987840652, 'inference': 47.22200002288446, 'postprocess': 5.245600012131035}]
```
####################################################################

## Treinamento do Yolo 11 Modelo S

```bash


```
Report
```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\report.py 

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 1 Dynamo DB, 5 Lambdas, 1 S3, 1 SNS, 2 Userss, 1 aws, 55.0ms
Speed: 2.3ms preprocess, 55.0ms inference, 67.7ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict2
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict2\labels
✅ Detailed JSON saved to data\reports\yolo11s_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11s_custom_200\report.json
Reports generated: data/reports/yolo11s_custom_200
```
####################################################################

## Treinamento do Yolo 11 Modelo M

```bash
New https://pypi.org/project/ultralytics/8.3.162 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=5, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.001, lrf=0.05, mask_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11m.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11m_custom_100, nbs=64, nms=False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=10, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=182

                   from  n    params  module                                       arguments
  0                  -1  1      1856  ultralytics.nn.modules.conv.Conv             [3, 64, 3, 2]
  1                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]
  2                  -1  1    111872  ultralytics.nn.modules.block.C3k2            [128, 256, 1, True, 0.25]
  3                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]
  4                  -1  1    444928  ultralytics.nn.modules.block.C3k2            [256, 512, 1, True, 0.25]
  5                  -1  1   2360320  ultralytics.nn.modules.conv.Conv             [512, 512, 3, 2]
  6                  -1  1   1380352  ultralytics.nn.modules.block.C3k2            [512, 512, 1, True]
  7                  -1  1   2360320  ultralytics.nn.modules.conv.Conv             [512, 512, 3, 2]
  8                  -1  1   1380352  ultralytics.nn.modules.block.C3k2            [512, 512, 1, True]
  9                  -1  1    656896  ultralytics.nn.modules.block.SPPF            [512, 512, 5]
 10                  -1  1    990976  ultralytics.nn.modules.block.C2PSA           [512, 512, 1]
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 13                  -1  1   1642496  ultralytics.nn.modules.block.C3k2            [1024, 512, 1, True]
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 16                  -1  1    542720  ultralytics.nn.modules.block.C3k2            [1024, 256, 1, True]
 17                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 19                  -1  1   1511424  ultralytics.nn.modules.block.C3k2            [768, 512, 1, True]
 20                  -1  1   2360320  ultralytics.nn.modules.conv.Conv             [512, 512, 3, 2]
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 22                  -1  1   1642496  ultralytics.nn.modules.block.C3k2            [1024, 512, 1, True]
 23        [16, 19, 22]  1   1551346  ultralytics.nn.modules.head.Detect           [182, [256, 512, 512]]
YOLO11m summary: 231 layers, 20,193,330 parameters, 20,193,314 gradients, 69.0 GFLOPs

Transferred 643/649 items from pretrained weights
ClearML Task: created new task id=c53aa96e93fb49c0b91c34ae4a338b50
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/c53aa96e93fb49c0b91c34ae4a338b50/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed
train: Fast image access  (ping: 0.00.0 ms, read: 612.0463.1 MB/s, size: 416.9 KB)
train: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 5276
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
val: Fast image access  (ping: 0.00.0 ms, read: 593.9560.5 MB/s, size: 226.2 KB)
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 393 ima
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\labels.jpg...
optimizer: AdamW(lr=0.001, momentum=0.937) with parameter groups 106 weight(decay=0.0), 113 weight(decay=0.0005078125), 112 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/100      6.46G      1.193      2.857       0.98        239        320:  30%|██▉       | 316/1056 [01:41<06:06, ClearML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start
      1/100      6.75G      1.094      1.993     0.9566         30        640: 100%|██████████| 1056/1056 [04:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.697      0.619      0.726      0.549

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/100      4.42G      1.043      1.287     0.9084        461        768:   0%|          | 3/1056 [00:00<03:02,  5ClearML Monitor: Reporting detected, reverting back to iteration based reporting
      2/100      7.19G     0.9908      1.147     0.9267         82        640: 100%|██████████| 1056/1056 [03:14<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029       0.82      0.811        0.9      0.718

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/100      6.91G     0.9351     0.9351     0.9137         13        832: 100%|██████████| 1056/1056 [03:05<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.877       0.88      0.945       0.76

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/100      7.23G     0.8734     0.7724     0.9015         49        864: 100%|██████████| 1056/1056 [03:13<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.915       0.93       0.97      0.795

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/100      7.55G     0.8409     0.7045     0.8901         55        960: 100%|██████████| 1056/1056 [03:08<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.931      0.936      0.979      0.831

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/100      6.82G     0.8017     0.6497      0.883         21        800: 100%|██████████| 1056/1056 [03:12<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.933      0.966      0.982      0.846

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/100      6.92G     0.7742     0.5974     0.8762         22        544: 100%|██████████| 1056/1056 [03:11<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.926      0.965      0.982      0.852

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/100      6.83G     0.7408     0.5563     0.8671         81        896: 100%|██████████| 1056/1056 [03:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.946      0.937      0.982      0.854

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/100      7.09G     0.7228     0.5456     0.8614         58        544: 100%|██████████| 1056/1056 [03:08<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.933      0.975      0.981      0.862

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     10/100      6.92G     0.7015     0.5088     0.8559         16        544: 100%|██████████| 1056/1056 [03:05<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.966      0.976      0.988      0.885

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     11/100       6.9G     0.6991     0.5237     0.8566         57        608: 100%|██████████| 1056/1056 [03:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.937      0.976      0.987      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     12/100       6.8G     0.6717     0.4893     0.8512         28        352: 100%|██████████| 1056/1056 [03:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.952      0.974      0.988      0.884

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     13/100      6.82G      0.659     0.4768     0.8455        151        608: 100%|██████████| 1056/1056 [03:07<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.969      0.975       0.99      0.902

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     14/100       7.4G      0.641     0.4608     0.8445         28        480: 100%|██████████| 1056/1056 [03:09<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.921      0.988      0.978      0.885

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     15/100      7.22G     0.6289     0.4469     0.8418        149        416: 100%|██████████| 1056/1056 [03:08<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.975      0.959      0.988      0.902

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     16/100       6.8G       0.62     0.4387     0.8396         84        384: 100%|██████████| 1056/1056 [03:07<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.969      0.966      0.989      0.903

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     17/100      6.82G     0.6105     0.4393      0.837         53        384: 100%|██████████| 1056/1056 [03:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.964      0.978      0.987      0.905

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     18/100      6.81G     0.5999      0.427     0.8356        142        576: 100%|██████████| 1056/1056 [03:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.944      0.983      0.986      0.913

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     19/100      6.94G     0.5897     0.4176     0.8326         57        320: 100%|██████████| 1056/1056 [03:04<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.944      0.988       0.99      0.914

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     20/100      6.91G     0.5823     0.4032     0.8318         16        672: 100%|██████████| 1056/1056 [03:09<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.956       0.98      0.989      0.919

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     21/100      6.63G     0.5769     0.4045     0.8317         71        896: 100%|██████████| 1056/1056 [03:11<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029       0.97      0.976       0.99      0.914

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     22/100      6.82G     0.5702     0.3989     0.8285        100        896: 100%|██████████| 1056/1056 [03:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029       0.98      0.966       0.99      0.917

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     23/100      6.66G     0.5639     0.3895     0.8279         66        672: 100%|██████████| 1056/1056 [03:19<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.976      0.964       0.99      0.918

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     24/100      6.98G     0.5502      0.376     0.8249         76        928: 100%|██████████| 1056/1056 [03:18<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.979      0.965      0.989      0.926

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     25/100       7.3G     0.5483     0.3835     0.8257         20        480: 100%|██████████| 1056/1056 [03:48<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.963      0.971       0.99      0.925

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     26/100      7.04G     0.5466     0.3841     0.8231         21        608: 100%|██████████| 1056/1056 [03:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.969      0.981       0.99      0.926

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     27/100      6.74G     0.5343     0.3665     0.8234         85        416: 100%|██████████| 1056/1056 [03:21<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.973      0.971      0.991       0.93

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     28/100      6.55G     0.5297     0.3633     0.8215        145        672: 100%|██████████| 1056/1056 [03:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.933      0.993      0.984      0.925

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     29/100      7.17G     0.5261     0.3673     0.8194         19        864: 100%|██████████| 1056/1056 [03:16<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:05
                   all        393       9029      0.959      0.981      0.989      0.924

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     30/100      6.97G     0.5165     0.3544     0.8207         41        704: 100%|██████████| 1056/1056 [03:29<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.981      0.963      0.988      0.931

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     31/100      6.84G     0.5232     0.3579      0.817         31        320: 100%|██████████| 1056/1056 [05:53<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:11
                   all        393       9029      0.966      0.965       0.98      0.922

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     32/100      6.84G      0.509     0.3443     0.8172         95        640: 100%|██████████| 1056/1056 [06:22<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:11
                   all        393       9029      0.954      0.981      0.984      0.928

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     33/100      6.83G     0.5035      0.346     0.8173         53        352: 100%|██████████| 1056/1056 [07:16<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029       0.95      0.985      0.984       0.93

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     34/100      7.07G     0.5018     0.3405     0.8169         22        928: 100%|██████████| 1056/1056 [03:41<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.974      0.976      0.991       0.94

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     35/100      6.82G     0.5005     0.3409     0.8166         59        512: 100%|██████████| 1056/1056 [03:14<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.963      0.982       0.99      0.936

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     36/100      6.97G     0.5004     0.3416     0.8142         95        544: 100%|██████████| 1056/1056 [03:17<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.945       0.99      0.988      0.935

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     37/100      7.04G     0.4899     0.3288     0.8142         21        832: 100%|██████████| 1056/1056 [03:12<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.943      0.995      0.989      0.935

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     38/100      7.37G      0.492     0.3322     0.8141         41        352: 100%|██████████| 1056/1056 [03:16<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:05
                   all        393       9029      0.966      0.983       0.99      0.939

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     39/100      7.05G     0.4803     0.3258     0.8123         11        384: 100%|██████████| 1056/1056 [03:37<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:05
                   all        393       9029      0.968      0.985       0.99      0.937

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/100      7.63G     0.4807     0.3261     0.8128         20        320: 100%|██████████| 1056/1056 [03:38<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.972      0.985       0.99      0.941

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     41/100      6.87G     0.4758     0.3167     0.8116         58        448: 100%|██████████| 1056/1056 [03:11<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029       0.98      0.965      0.989      0.939

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     42/100      6.93G      0.472     0.3148     0.8102         27        896: 100%|██████████| 1056/1056 [03:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.979      0.968       0.99      0.942

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     43/100      6.83G     0.4671     0.3141     0.8101         37        416: 100%|██████████| 1056/1056 [03:15<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029       0.95       0.99       0.99      0.943

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     44/100      7.29G     0.4632      0.308     0.8106         37        320: 100%|██████████| 1056/1056 [03:30<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.985      0.966       0.99      0.945

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     45/100      6.57G     0.4668     0.3155     0.8087         81        576: 100%|██████████| 1056/1056 [03:23<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:05
                   all        393       9029      0.977      0.965      0.985       0.94

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     46/100      7.05G     0.4576     0.3057     0.8082         94        832: 100%|██████████| 1056/1056 [03:15<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.977       0.97      0.987      0.943

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     47/100      6.71G     0.4602     0.3081     0.8077         61        672: 100%|██████████| 1056/1056 [03:11<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.978      0.966      0.985      0.939

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/100      7.16G     0.4572     0.3066     0.8104        219        512: 100%|██████████| 1056/1056 [03:16<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.968      0.979      0.991      0.946

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/100      6.57G      0.462     0.3137      0.809         57        928: 100%|██████████| 1056/1056 [03:14<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.959      0.984       0.99      0.946

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/100      7.29G      0.451     0.3046     0.8072         87        512: 100%|██████████| 1056/1056 [03:13<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.951      0.988       0.99      0.944

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/100      7.04G     0.4445        0.3     0.8059         73        864: 100%|██████████| 1056/1056 [03:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.972      0.985      0.991      0.949

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/100      6.81G      0.447     0.3008     0.8072         86        576: 100%|██████████| 1056/1056 [03:32<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.981      0.965       0.99      0.948

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     53/100      7.12G     0.4393     0.2907     0.8047         35        960: 100%|██████████| 1056/1056 [03:14<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.949      0.994      0.991      0.951

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     54/100      6.83G     0.4436     0.2962     0.8059         91        480: 100%|██████████| 1056/1056 [03:15<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.984      0.965       0.99      0.949

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     55/100      6.94G     0.4301     0.2867     0.8051         74        672: 100%|██████████| 1056/1056 [03:40<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.977      0.969       0.99      0.949

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     56/100         7G     0.4394     0.2921     0.8047         30        736: 100%|██████████| 1056/1056 [03:11<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.985      0.964      0.991       0.95

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     57/100      6.77G      0.426     0.2826     0.8042         18        960: 100%|██████████| 1056/1056 [03:30<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.986      0.966       0.99      0.951

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     58/100      6.52G     0.4285     0.2871     0.8043         95        672: 100%|██████████| 1056/1056 [03:19<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.984      0.965      0.991       0.95

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     59/100      6.85G     0.4279     0.2848     0.8033         57        576: 100%|██████████| 1056/1056 [03:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.984      0.969      0.991       0.95

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     60/100      7.49G     0.4274     0.2841     0.8018         71        512: 100%|██████████| 1056/1056 [03:16<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.984      0.969       0.99      0.952

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     61/100      7.16G     0.4219     0.2819     0.8031         36        736: 100%|██████████| 1056/1056 [03:24<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.983      0.967      0.991      0.952

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     62/100      6.84G     0.4225     0.2823     0.8031         67        608: 100%|██████████| 1056/1056 [03:12<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029       0.96      0.991      0.991      0.952

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     63/100      6.89G     0.4173     0.2765      0.801        162        672: 100%|██████████| 1056/1056 [03:06<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.983      0.971      0.991      0.954

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     64/100      6.79G     0.4107     0.2679     0.7999         95        864: 100%|██████████| 1056/1056 [03:08<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.984      0.969      0.991      0.956

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     65/100      6.82G     0.4087     0.2684     0.7991         75        384: 100%|██████████| 1056/1056 [03:07<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.984      0.967       0.99      0.953

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     66/100      7.33G     0.4111     0.2699     0.8007         33        960: 100%|██████████| 1056/1056 [03:09<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.981      0.969      0.991      0.953

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     67/100      7.58G     0.4104     0.2707     0.8006         96        416: 100%|██████████| 1056/1056 [04:38<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.986      0.964       0.99      0.953

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     68/100       6.6G     0.4055     0.2694     0.7999         72        544: 100%|██████████| 1056/1056 [03:18<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.984      0.967      0.991      0.952

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     69/100      6.96G     0.4049     0.2651     0.7987         67        320: 100%|██████████| 1056/1056 [03:20<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:05
                   all        393       9029      0.983      0.969      0.991      0.953

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     70/100      6.79G     0.3993     0.2623     0.7995         59        960: 100%|██████████| 1056/1056 [03:18<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.981      0.969       0.99      0.952

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     71/100      7.05G     0.3993      0.262     0.7985         80        768: 100%|██████████| 1056/1056 [03:22<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.979      0.968       0.99      0.954

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     72/100      7.07G     0.3977      0.261     0.7991         70        864: 100%|██████████| 1056/1056 [03:31<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:05
                   all        393       9029      0.985      0.967      0.991      0.954

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     73/100       6.5G     0.3936      0.259     0.7979         83        544: 100%|██████████| 1056/1056 [03:19<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:03
                   all        393       9029      0.984      0.967       0.99      0.954

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     74/100      6.81G     0.3928     0.2573     0.7972         15        800: 100%|██████████| 1056/1056 [03:09<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:04
                   all        393       9029      0.984      0.969      0.991      0.955
EarlyStopping: Training stopped early as no improvement observed in last 10 epochs. Best results observed at epoch 64, best model saved as best.pt.
To update EarlyStopping(patience=10) pass a new patience value, i.e. `patience=300` or use `patience=0` to disable EarlyStopping.

74 epochs completed in 4.345 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\last.pt, 40.8MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\best.pt, 40.8MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\best.pt...
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11m summary (fused): 125 layers, 20,170,354 parameters, 0 gradients, 68.4 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 40/40 [00:09
                   all        393       9029      0.985      0.968      0.991      0.937
                   ACM         40         40      0.996          1      0.995      0.995
                   ALB         67         83      0.994      0.988      0.995      0.914
                   AMI          7         12      0.974          1      0.995      0.956
           API-Gateway        200        304          1      0.985      0.995      0.949
Active Directory Service         36         36      0.995          1      0.995      0.995
              Airflow_          3          6      0.967          1      0.995      0.995
               Amplify         16         16          1          1      0.995      0.881
    Analytics Services          5          5      0.974          1      0.995      0.995
               AppFlow         25         25      0.993          1      0.995      0.983
               Appsync          6          6      0.972          1      0.995      0.673
                Athena         36         37      0.992          1      0.995      0.948
                Aurora         44         54      0.989          1      0.995      0.885
          Auto Scaling         48         73      0.999          1      0.995        0.9
    Auto Scaling Group          4         10      0.987          1      0.995       0.88
       Automated Tests         15         20      0.991          1      0.995      0.937
     Availability Zone         12         24      0.994          1      0.995      0.941
                Backup          3          6      0.972          1      0.995      0.995
     Build Environment          7          7      0.984          1      0.995      0.846
                   CDN          5          5      0.968          1      0.995      0.995
                   CUR          5          5      0.966          1      0.995      0.722
          Call Metrics         25         25      0.995          1      0.995      0.944
       Call Recordings         25         25      0.994          1      0.995      0.898
   Certificate Manager         43         43      0.996          1      0.995      0.973
                Client          3         13          1      0.598       0.99      0.969
       Cloud Connector         11         22      0.992          1      0.995       0.98
             Cloud Map          5          5      0.968          1      0.995      0.995
          Cloud Search         19         19      0.991          1      0.995      0.967
           Cloud Trail         53         53      0.978      0.981      0.986      0.972
           Cloud Watch        113        135      0.999          1      0.995      0.948
  CloudFormation Stack         32         37      0.996          1      0.995      0.989
              CloudHSM         30         30          1      0.975      0.995      0.925
      CloudWatch Alarm         18         23      0.994          1      0.995      0.929
            Cloudfront        102        108          1      0.999      0.995      0.948
             CodeBuild         30         50      0.998          1      0.995      0.959
            CodeCommit         17         17       0.99          1      0.995      0.995
            CodeDeploy          5          5      0.969          1      0.995      0.979
          CodePipeline         43         43      0.996          1      0.995        0.9
               Cognito         90        104       0.96      0.962      0.966      0.945
            Comprehend         25         25      0.993          1      0.995      0.995
                Config         38        163      0.987          1      0.983      0.913
               Connect         25         25      0.993          1      0.995      0.975
  Connect Contact Lens         25         25      0.994          1      0.995      0.975
             Container         17         66          1          1      0.995      0.919
         Control Tower          5          5       0.97          1      0.995      0.939
      Customer Gateway          8         11      0.986          1      0.995      0.956
                   DSI          5         10      0.991          1      0.995      0.841
         Data Pipeline          5          5      0.971          1      0.995      0.945
              DataSync          5          5      0.968          1      0.995      0.995
          Deploy Stage         10         10      0.985          1      0.995      0.737
             Detective         25         25          1          1      0.995      0.939
        Direct Connect         21         21      0.992          1      0.995      0.964
          Distribution          5          5          1       0.68      0.995      0.995
          Docker Image         21         72      0.986      0.955      0.993      0.876
             Dynamo DB        169        263          1      0.994      0.995      0.947
                   EBS         27         37      0.997          1      0.995      0.948
                   EC2        179        418      0.992      0.964      0.992      0.924
                   EFS         22         30      0.966      0.949      0.956      0.922
      EFS Mount Target         52        102      0.971       0.99      0.985      0.839
                   EKS         53         59      0.999          1      0.995      0.968
                   ELB        111        150      0.991      0.947      0.966       0.94
                   EMR         10         10      0.983          1      0.995      0.995
         Edge Location          5          7      0.978          1      0.995      0.964
           ElastiCache         22         26      0.994          1      0.995      0.961
Elastic Container Registry         43         43      0.995          1      0.995      0.965
Elastic Container Service         50         60      0.983      0.989      0.995       0.87
        Elastic Search         38         38      0.996          1      0.995      0.913
Elemental MediaConvert         16         18          1      0.923      0.992      0.973
Elemental MediaPackage          5          5          1      0.908      0.995      0.995
                 Email          5          5      0.972          1      0.995      0.944
              Endpoint          5          5      0.968          1      0.995      0.901
             Event Bus          5          5      0.969          1      0.995      0.995
           EventBridge         35        135      0.999          1      0.995      0.877
   Experiment Duration          7          7          1          0      0.995      0.918
           Experiments          7          7          1          0      0.906      0.824
               Fargate         29         71      0.998          1      0.995      0.929
Fault Injection Simulator         15         15      0.995          1      0.995      0.888
      Firewall Manager         25         25      0.993          1      0.995      0.972
                 Flask          8         24      0.993          1      0.995      0.875
             Flow logs         25        100      0.999          1      0.995      0.873
              GameLift          5          5      0.961          1      0.995      0.905
                   Git          8          8      0.983          1      0.995      0.984
                Github         17         18      0.991          1      0.995      0.958
               Glacier         10         10          1          1      0.995      0.995
                  Glue         19         38      0.996          1      0.995      0.959
         Glue DataBrew          7          7      0.977          1      0.995      0.995
               Grafana         10         10      0.981          1      0.995      0.995
             GuardDuty         34        134      0.999          1      0.995      0.885
                   IAM         66        207          1      0.982      0.995      0.897
              IAM Role         41        169      0.987      0.976      0.991      0.808
              IOT Core         13         17      0.989          1      0.995      0.988
                 Image         11         11      0.984          1      0.995      0.862
         Image Builder          5          5      0.966          1      0.995      0.978
               Ingress          5          5      0.972          1      0.995      0.995
       Inspector Agent         25         25          1          1      0.995       0.99
             Instances          3          6      0.534       0.39      0.663      0.564
              Internet         59         82       0.92          1      0.992      0.948
      Internet Gateway         51         87          1          1      0.995      0.859
               Jenkins          3          6      0.972          1      0.995      0.969
Key Management Service         47         75      0.997          1      0.995      0.986
                Kibana          7          7      0.979          1      0.995      0.903
  Kinesis Data Streams         72         85      0.986      0.988      0.988      0.962
            Kubernetes          8          8       0.98          1      0.995      0.972
                Lambda        255        675          1      0.993      0.995      0.935
                   Lex          5          5          1          1      0.995      0.995
                    MQ          6         12      0.989          1      0.995      0.919
      Machine Learning          9          9      0.956          1      0.995      0.982
                 Macie         45        110      0.999          1      0.995      0.939
           Marketplace          5          5       0.99          1      0.995      0.862
             Memcached          5         10      0.981          1      0.995      0.955
         Mobile Client         36         41          1      0.971      0.995      0.919
              Mongo DB         11         23      0.989          1      0.995      0.873
                 MySQL          7          7      0.985          1      0.995      0.926
           NAT Gateway         44         85      0.996          1      0.995      0.951
               Neptune          5          5      0.971          1      0.995      0.545
       Network Adapter          5          5      0.971          1      0.995      0.949
      Network Firewall         25         25      0.993          1      0.995      0.913
              Notebook          5          5          1          1      0.995      0.983
      Order Controller          5          5      0.971          1      0.995      0.923
    Organization Trail         30        105      0.999          1      0.995      0.872
       Parameter Store          7          7      0.977          1      0.995      0.995
              Pinpoint          5          5      0.968          1      0.995      0.995
            PostgreSQL          7          7      0.981          1      0.995      0.934
          Private Link         25         25          1          1      0.995      0.969
        Private Subnet        106        263      0.963      0.988       0.99      0.887
            Prometheus         10         10      0.983          1      0.995      0.995
         Public Subnet        104        216      0.982      0.987      0.994      0.871
               Quarkus         10         10      0.983          1      0.995      0.972
            Quicksight         32         34      0.995          1      0.995      0.988
                   RDS         93        197      0.999          1      0.995      0.967
                 React          3          3      0.961          1      0.995      0.895
                 Redis         10         21      0.992          1      0.995      0.978
              Redshift         45         46          1      0.985      0.995      0.961
                Region         36         53      0.997          1      0.995      0.907
           Rekognition         14         14      0.987          1      0.995      0.995
               Results          7          7          1          0      0.906      0.878
              Route 53         40         40      0.996          1      0.995      0.947
               Route53         87        138      0.999          1      0.995      0.964
                    S3        260        514      0.996      0.996      0.993      0.925
                   SAR          5          5          1          1      0.995      0.979
                   SDK         26         88          1      0.946      0.995      0.946
                   SES         14         17      0.991          1      0.995      0.982
                   SNS         62         69      0.998      0.986      0.995      0.973
                   SQS         43         44      0.997          1      0.995      0.969
             SSM Agent         25         25          1          1      0.995      0.926
             Sagemaker         18         61          1      0.553      0.966      0.752
        Secret Manager         30         30      0.991          1      0.995      0.973
        Security Group          5          5       0.97          1      0.995      0.995
          Security Hub         30        130      0.999          1      0.995      0.841
                Server         27         42      0.997          1      0.995      0.939
       Service Catalog          8         23      0.994          1      0.995      0.951
                Shield         31         31      0.995          1      0.995      0.991
               Sign-On         25         25      0.993          1      0.995      0.989
                 Slack         12         12      0.987          1      0.995      0.977
              Snowball         10         10      0.983          1      0.995      0.995
                 Stack          5          5      0.971          1      0.995      0.917
         Step Function          7         21      0.992          1      0.995      0.969
       Storage Gateway         10         10          1          1      0.995      0.995
            SwaggerHub          3          3          1          1      0.995      0.951
       Systems Manager         39         64      0.997          1      0.995      0.962
                    TV          5          5      0.968          1      0.995      0.995
                 Table         20         40      0.996          1      0.995      0.943
           Task Runner          5          5          1          1      0.995      0.975
             Terraform         13         13      0.989          1      0.995      0.995
             Text File         14         32          1       0.91      0.993       0.92
              Textract          3          3      0.951          1      0.995      0.995
            Transcribe          9          9      0.981          1      0.995      0.995
       Transfer Family         16         16       0.99          1      0.995      0.991
       Transit Gateway         10         10      0.985          1      0.995       0.98
             Translate         19         19       0.99          1      0.995      0.995
       Trusted Advisor          5          5      0.972          1      0.995      0.949
                Twilio          7          7          1          1      0.995      0.995
                 Users        152        204      0.995          1      0.995      0.925
                   VDA         11         11      0.985          1      0.995      0.975
            VP Gateway          6          7       0.98          1      0.995        0.9
            VPC Router          9         16       0.99          1      0.995      0.962
        VPN Connection          5          8      0.983          1      0.995      0.961
                   WAF         43         46          1      0.945      0.995      0.971
           Web Clients         45         62          1      0.794      0.991      0.882
              Websites          5          5      0.979          1      0.995      0.927
                 X-Ray         16         20      0.992          1      0.995      0.961
                   aws        240        322      0.993      0.997      0.995      0.904
          cache Worker          8          8      0.979          1      0.995      0.958
Speed: 0.2ms preprocess, 18.7ms inference, 0.0ms loss, 1.3ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\best.pt
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11m summary (fused): 125 layers, 20,170,354 parameters, 0 gradients, 68.4 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 195.2112.9 MB/s, size: 766.9 KB)
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache... 386 imag
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 49/49 [00:05
█████████▉                        31% | 12.03/38.9 MB [00:20<00:47,  1.77s/MB]:                    all        386       7672      0.941      0.985      0.985      0.953.3 MB [00:00<00:00,  2.01s/MB]:
                   ACM         22         22          1          1      0.995      0.995
                   ALB         58         74      0.979      0.973      0.994      0.936:  98%|█████████▊| 48/49 [00:05
                   AMI          8         13      0.948          1      0.995      0.995
           API-Gateway        201        304      0.978          1      0.995      0.978
Active Directory Service         15         15      0.954          1      0.995      0.995
              Airflow_          3          6      0.896          1      0.995      0.995
               Amplify         18         18      0.958          1      0.995       0.96
    Analytics Services          5          5          1          1      0.995      0.995
               AppFlow         12         12      0.944          1      0.995      0.995
               Appsync          8          8      0.919          1      0.995      0.919
                Athena         32         33      0.954          1      0.995      0.989
                Aurora         27         36      0.951      0.889      0.926       0.91
          Auto Scaling         45         75      0.992          1      0.995      0.928
    Auto Scaling Group          3          8          1          1      0.995      0.854
       Automated Tests         12         17       0.96          1      0.995      0.939
     Availability Zone         10         20      0.965          1      0.995      0.982
                Backup          3          6      0.896          1      0.995      0.995
     Build Environment          6          6      0.897          1      0.995      0.793
                   CDN          7          7      0.908          1      0.995       0.96
                   CUR          6          6          1          1      0.995      0.963
          Call Metrics         12         12      0.944          1      0.995      0.982
       Call Recordings         12         12      0.945          1      0.995      0.973
   Certificate Manager         28         28      0.975          1      0.995      0.995
                Client          3          8      0.374          1      0.734       0.72
       Cloud Connector          7         14      0.952          1      0.995      0.995
             Cloud Map          5          5      0.877          1      0.995      0.995
          Cloud Search         14         14      0.952          1      0.995      0.983
           Cloud Trail         39         41      0.958      0.976      0.984      0.962
           Cloud Watch        126        151      0.977          1      0.995      0.956
  CloudFormation Stack         38         45      0.984          1      0.995      0.985
              CloudHSM         13         13          1      0.983      0.995      0.986
      CloudWatch Alarm         18         23       0.97          1      0.995      0.938
            Cloudfront         97        101      0.983          1      0.995      0.968
             CodeBuild         33         53      0.987          1      0.995      0.982
            CodeCommit         15         15      0.954          1      0.995      0.988
            CodeDeploy          5          5      0.878          1      0.995      0.944
          CodePipeline         43         43       0.96          1      0.988      0.956
               Cognito         85        100      0.983       0.98      0.988      0.985
            Comprehend         27         27      0.974          1      0.995      0.995
                Config         25         65       0.96          1      0.967      0.959
               Connect         12         12          1          1      0.995      0.995
  Connect Contact Lens         12         12      0.944          1      0.995      0.982
             Container         18         81       0.98          1      0.995      0.939
         Control Tower          7          7      0.909          1      0.995      0.995
      Customer Gateway          5         11      0.939          1      0.995      0.973
                   DSI          5         10      0.935          1      0.995      0.832
         Data Pipeline          5          5      0.879          1      0.995      0.965
              DataSync          5          5      0.878          1      0.995      0.995
          Deploy Stage          7          7       0.91          1      0.995      0.832
             Detective          8          8      0.919          1      0.995      0.995
        Direct Connect         19         26       0.97      0.962      0.976      0.897
          Distribution          5          5      0.765          1      0.962      0.962
          Docker Image         18         61      0.973      0.967      0.977      0.883
             Dynamo DB        174        270          1       0.97      0.988      0.961
                   EBS         24         36      0.979      0.972      0.994      0.947
                   EC2        166        406      0.985       0.97      0.989      0.927
                   EFS         28         36      0.931      0.917      0.904      0.879
      EFS Mount Target         35         54      0.944      0.926      0.929      0.908
                   EKS         51         58      0.984          1      0.995      0.983
                   ELB        104        149      0.966      0.956       0.98      0.951
                   EMR          5          5      0.877          1      0.995      0.995
         Edge Location          3          5          1          1      0.995      0.817
           ElastiCache         25         31      0.976      0.935      0.962      0.942
Elastic Container Registry         51         51      0.962          1      0.995      0.994
Elastic Container Service         50         62      0.967          1      0.995      0.908
        Elastic Search         32         33      0.896          1      0.995      0.951
Elemental MediaConvert         17         20      0.833      0.998      0.987      0.985
Elemental MediaPackage          5          5      0.664          1      0.766      0.766
                 Email          5          5          1      0.947      0.995      0.835
              Endpoint          6          6      0.898          1      0.995      0.893
             Event Bus          5          5      0.878          1      0.995      0.995
           EventBridge         21         53      0.985          1      0.995      0.991
   Experiment Duration          5          5          1      0.551      0.839      0.755
           Experiments          5          5          1      0.256      0.928      0.892
               Fargate         30         72      0.989          1      0.995      0.956
Fault Injection Simulator         12         12          1      0.996      0.995      0.914
      Firewall Manager          8          8      0.919          1      0.995      0.995
                 Flask          6         18      0.964          1      0.995      0.929
             Flow logs          8         32      0.978          1      0.995      0.964
              GameLift          5          5      0.876          1      0.995      0.972
                   Git          6          6      0.896          1      0.995      0.995
                Github         20         25      0.972          1      0.995      0.945
               Glacier          5          5          1          1      0.995      0.995
                  Glue         15         30      0.977          1      0.995      0.964
         Glue DataBrew          7          7      0.908          1      0.995      0.995
               Grafana          8          8      0.918          1      0.995      0.995
             GuardDuty         17         49      0.985          1      0.995      0.984
                   IAM         51        104      0.957      0.971      0.982      0.957
              IAM Role         25         68       0.94          1      0.987      0.884
              IOT Core         12         14      0.951          1      0.995      0.983
                 Image         13         13      0.946          1      0.995      0.898
         Image Builder          5          5      0.877          1      0.995      0.995
               Ingress          5          5      0.878          1      0.995      0.995
       Inspector Agent          8          8          1          1      0.995      0.995
             Instances          3          6      0.596          1       0.68      0.642
              Internet         63         86      0.941      0.988      0.984      0.947
      Internet Gateway         32         50      0.982          1      0.995      0.949
               Jenkins          3          6      0.895          1      0.995      0.995
Key Management Service         29         40      0.986          1      0.995      0.992
                Kibana          7          7      0.911          1      0.995      0.913
  Kinesis Data Streams         50         66      0.985      0.967      0.985      0.978
            Kubernetes          6          6          1          1      0.995      0.995
                Lambda        243        673      0.997          1      0.995       0.98
                   Lex          5          5          1          1      0.995      0.995
                    MQ          5         11      0.939          1      0.995      0.908
      Machine Learning         11         11      0.817          1      0.988      0.975
                 Macie         27         70       0.99          1      0.995      0.984
           Marketplace          5          5      0.887          1      0.995      0.676
             Memcached          6         12      0.938          1      0.995      0.922
         Mobile Client         40         49          1          1      0.995      0.918
              Mongo DB          9         21      0.968          1      0.995      0.905
                 MySQL          7          7      0.912          1      0.995      0.955
           NAT Gateway         46         88      0.972      0.966      0.985       0.96
               Neptune          6          6      0.896          1      0.995      0.875
       Network Adapter          5          5      0.876          1      0.995      0.995
      Network Firewall          8          8      0.919          1      0.995      0.995
              Notebook          5          5          1          1      0.995      0.975
      Order Controller          5          5      0.872          1      0.995      0.967
    Organization Trail         17         41      0.983          1      0.995      0.959
       Parameter Store          7          7      0.908          1      0.995      0.975
              Pinpoint          5          5          1          1      0.995      0.995
            PostgreSQL          7          7       0.91          1      0.995      0.995
          Private Link         24         24      0.972          1      0.995       0.99
        Private Subnet         89        208      0.961      0.971       0.98      0.916
            Prometheus          8          8          1          1      0.995      0.995
         Public Subnet         90        203      0.985      0.968      0.987      0.892
               Quarkus          8          8      0.919          1      0.995      0.995
            Quicksight         19         21      0.967          1      0.995      0.992
                   RDS         83        163      0.943      0.939      0.969      0.945
                 React          4          4      0.856          1      0.995      0.895
                 Redis         10         25      0.984          1      0.995      0.981
              Redshift         27         29          1      0.991      0.995       0.99
                Region         36         52      0.987          1      0.995      0.918
           Rekognition         14         14          1          1      0.995      0.995
               Results          5          5          1      0.681      0.865      0.865
              Route 53         21         21      0.924          1      0.989      0.989
               Route53         98        167      0.975      0.994      0.992      0.969
                    S3        256        520      0.994      0.994      0.995      0.966
                   SAR          5          5          1          1      0.995      0.995
                   SDK         24         80      0.948          1      0.989      0.954
                   SES         17         20      0.957          1      0.995      0.982
                   SNS         63         69      0.987          1      0.995      0.987
                   SQS         49         50      0.985          1      0.995      0.975
             SSM Agent          8          8          1          1      0.995      0.995
             Sagemaker         16         59        0.7          1      0.982       0.84
        Secret Manager         14         14      0.937          1      0.995      0.995
        Security Group          5          5      0.876          1      0.995      0.901
          Security Hub         13         45      0.985          1      0.995      0.988
                Server         20         32      0.956          1      0.995      0.903
       Service Catalog         10         31      0.978          1      0.995      0.987
                Shield         15         15      0.947          1      0.995      0.995
               Sign-On          8          8      0.918          1      0.995      0.995
                 Slack         13         13      0.948          1      0.995      0.983
              Snowball          5          5          1          1      0.995      0.995
                 Stack          5          5       0.88          1      0.995      0.946
         Step Function          8         24      0.971          1      0.995      0.931
       Storage Gateway          5          5          1          1      0.995      0.995
            SwaggerHub          5          5          1          1      0.995      0.995
       Systems Manager         20         28      0.975          1      0.995      0.993
                    TV          6          6      0.896          1      0.995      0.981
                 Table         23         46      0.973          1      0.995      0.986
           Task Runner          5          5          1          1      0.995      0.995
             Terraform         11         11      0.941          1      0.995       0.99
             Text File         11         28      0.815          1      0.939      0.913
              Textract          5          5      0.877          1      0.995      0.995
            Transcribe          9          9          1          1      0.995      0.995
       Transfer Family         15         15      0.954          1      0.995      0.986
       Transit Gateway         12         12       0.93          1      0.995      0.995
             Translate         19         19      0.963          1      0.995      0.991
       Trusted Advisor          6          6      0.897          1      0.995      0.995
                Twilio          7          7      0.908          1      0.995      0.995
                 Users        144        196          1          1      0.995      0.952
                   VDA          7          7      0.877          1      0.995      0.995
            VP Gateway          5          6      0.879      0.833      0.872      0.858
            VPC Router          8         16      0.957          1      0.995      0.913
        VPN Connection          3          9          1      0.984      0.995      0.966
                   WAF         25         28          1      0.964      0.995      0.978
           Web Clients         50         62      0.895      0.984      0.988      0.911
              Websites          9          9      0.929          1      0.995      0.971
                 X-Ray         19         21      0.967          1      0.995      0.988
                   aws        243        326      0.945          1      0.995      0.939
          cache Worker          7          7      0.908          1      0.995      0.981
Speed: 0.3ms preprocess, 9.4ms inference, 0.0ms loss, 0.9ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.941
  Recall:       0.985
  mAP@0.5:      0.985
  mAP@0.5:0.95: 0.953

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_02.png: 576x640 1 Auto Scaling, 2 Cloud Watchs, 1 Cloudfront, 4 EC2s, 1 ElastiCache, 1 IOT Core, 3 Private Subnets, 3 Public Subnets, 2 RDSs, 1 Region, 1 SES, 1 Users, 2 WAFs, 1 aws, 59.5ms
Speed: 3.7ms preprocess, 59.5ms inference, 4.0ms postprocess per image at shape (1, 3, 576, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict3
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict3\labels
✅ Detailed JSON saved to data\reports\yolo11m_custom_100\results.json
✅ Summary JSON saved to data\reports\yolo11m_custom_100\report.json
([ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'ACM', 1: 'ALB', 2: 'AMI', 3: 'API-Gateway', 4: 'Active Directory Service', 5: 'Airflow_', 6: 'Amplify', 7: 'Analytics Services', 8: 'AppFlow', 9: 'Appsync', 10: 'Athena', 11: 'Aurora', 12: 'Auto Scaling', 13: 'Auto Scaling Group', 14: 'Automated Tests', 15: 'Availability Zone', 16: 'Backup', 17: 'Build Environment', 18: 'CDN', 19: 'CUR', 20: 'Call Metrics', 21: 'Call Recordings', 22: 'Certificate Manager', 23: 'Client', 24: 'Cloud Connector', 25: 'Cloud Map', 26: 'Cloud Search', 27: 'Cloud Trail', 28: 'Cloud Watch', 29: 'CloudFormation Stack', 30: 'CloudHSM', 31: 'CloudWatch Alarm', 32: 'Cloudfront', 33: 'CodeBuild', 34: 'CodeCommit', 35: 'CodeDeploy', 36: 'CodePipeline', 37: 'Cognito', 38: 'Comprehend', 39: 'Config', 40: 'Connect', 41: 'Connect Contact Lens', 42: 'Container', 43: 'Control Tower', 44: 'Customer Gateway', 45: 'DSI', 46: 'Data Pipeline', 47: 'DataSync', 48: 'Deploy Stage', 49: 'Detective', 50: 'Direct Connect', 51: 'Distribution', 52: 'Docker Image', 53: 'Dynamo DB', 54: 'EBS', 55: 'EC2', 56: 'EFS', 57: 'EFS Mount Target', 58: 'EKS', 59: 'ELB', 60: 'EMR', 61: 'Edge Location', 62: 'ElastiCache', 63: 'Elastic Container Registry', 64: 'Elastic Container Service', 65: 'Elastic Search', 66: 'Elemental MediaConvert', 67: 'Elemental MediaPackage', 68: 'Email', 69: 'Endpoint', 70: 'Event Bus', 71: 'EventBridge', 72: 'Experiment Duration', 73: 'Experiments', 74: 'Fargate', 75: 'Fault Injection Simulator', 76: 'Firewall Manager', 77: 'Flask', 78: 'Flow logs', 79: 'GameLift', 80: 'Git', 81: 'Github', 82: 'Glacier', 83: 'Glue', 84: 'Glue DataBrew', 85: 'Grafana', 86: 'GuardDuty', 87: 'IAM', 88: 'IAM Role', 89: 'IOT Core', 90: 'Image', 91: 'Image Builder', 92: 'Ingress', 93: 'Inspector Agent', 94: 'Instances', 95: 'Internet', 96: 'Internet Gateway', 97: 'Jenkins', 98: 'Key Management Service', 99: 'Kibana', 100: 'Kinesis Data Streams', 101: 'Kubernetes', 102: 'Lambda', 103: 'Lex', 104: 'MQ', 105: 'Machine Learning', 106: 'Macie', 107: 'Marketplace', 108: 'Memcached', 109: 'Mobile Client', 110: 'Mongo DB', 111: 'MySQL', 112: 'NAT Gateway', 113: 'Neptune', 114: 'Network Adapter', 115: 'Network Firewall', 116: 'Notebook', 117: 'Order Controller', 118: 'Organization Trail', 119: 'Parameter Store', 120: 'Pinpoint', 121: 'PostgreSQL', 122: 'Private Link', 123: 'Private Subnet', 124: 'Prometheus', 125: 'Public Subnet', 126: 'Quarkus', 127: 'Quicksight', 128: 'RDS', 129: 'React', 130: 'Redis', 131: 'Redshift', 132: 'Region', 133: 'Rekognition', 134: 'Results', 135: 'Route 53', 136: 'Route53', 137: 'S3', 138: 'SAR', 139: 'SDK', 140: 'SES', 141: 'SNS', 142: 'SQS', 143: 'SSM Agent', 144: 'Sagemaker', 145: 'Secret Manager', 146: 'Security Group', 147: 'Security Hub', 148: 'Server', 149: 'Service Catalog', 150: 'Shield', 151: 'Sign-On', 152: 'Slack', 153: 'Snowball', 154: 'Stack', 155: 'Step Function', 156: 'Storage Gateway', 157: 'SwaggerHub', 158: 'Systems Manager', 159: 'TV', 160: 'Table', 161: 'Task Runner', 162: 'Terraform', 163: 'Text File', 164: 'Textract', 165: 'Transcribe', 166: 'Transfer Family', 167: 'Transit Gateway', 168: 'Translate', 169: 'Trusted Advisor', 170: 'Twilio', 171: 'Users', 172: 'VDA', 173: 'VP Gateway', 174: 'VPC Router', 175: 'VPN Connection', 176: 'WAF', 177: 'Web Clients', 178: 'Websites', 179: 'X-Ray', 180: 'aws', 181: 'cache Worker'}
obb: None
orig_img: array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
orig_shape: (993, 1167)
path: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict3'
speed: {'preprocess': 3.6726000253111124, 'inference': 59.52100001741201, 'postprocess': 4.0268999873660505}],
 [{'boxes': [{'class': 176,
              'confidence': 0.9660469889640808,
              'coordinates': [650.2527465820312,
                              37.864471435546875,
                              741.7692260742188,
                              130.70510864257812],
              'name': 'WAF'},
             {'class': 125,
              'confidence': 0.932704508304596,
              'coordinates': [401.23101806640625,
                              314.9771423339844,
                              446.1429748535156,
                              360.016845703125],
              'name': 'Public Subnet'},
             {'class': 128,
              'confidence': 0.9263925552368164,
              'coordinates': [416.1855773925781,
                              758.3898315429688,
                              497.5505065917969,
                              841.7466430664062],
              'name': 'RDS'},
             {'class': 28,
              'confidence': 0.9221709370613098,
              'coordinates': [972.3582763671875,
                              624.7167358398438,
                              1056.1219482421875,
                              710.4908447265625],
              'name': 'Cloud Watch'},
             {'class': 128,
              'confidence': 0.9207841753959656,
              'coordinates': [257.0060729980469,
                              758.1612548828125,
                              337.86962890625,
                              841.6099853515625],
              'name': 'RDS'},
             {'class': 171,
              'confidence': 0.9153991341590881,
              'coordinates': [130.25099182128906,
                              48.012657165527344,
                              198.9364471435547,
                              116.34870910644531],
              'name': 'Users'},
             {'class': 125,
              'confidence': 0.9127123951911926,
              'coordinates': [691.2793579101562,
                              314.8809814453125,
                              736.4474487304688,
                              360.0815124511719],
              'name': 'Public Subnet'},
             {'class': 132,
              'confidence': 0.9112388491630554,
              'coordinates': [83.55904388427734,
                              188.04554748535156,
                              123.74624633789062,
                              230.89031982421875],
              'name': 'Region'},
             {'class': 55,
              'confidence': 0.9109958410263062,
              'coordinates': [760.1375732421875,
                              758.5093383789062,
                              848.84521484375,
                              847.3902587890625],
              'name': 'EC2'},
             {'class': 55,
              'confidence': 0.9061219692230225,
              'coordinates': [483.89202880859375,
                              563.2224731445312,
                              573.9852294921875,
                              653.192138671875],
              'name': 'EC2'},
             {'class': 125,
              'confidence': 0.9045307040214539,
              'coordinates': [135.26507568359375,
                              320.60418701171875,
                              179.8280029296875,
                              364.8290100097656],
              'name': 'Public Subnet'},
             {'class': 180,
              'confidence': 0.892848789691925,
              'coordinates': [70.28880310058594,
                              145.2466278076172,
                              113.20043182373047,
                              191.1332244873047],
              'name': 'aws'},
             {'class': 89,
              'confidence': 0.8835115432739258,
              'coordinates': [969.0076293945312,
                              498.90728759765625,
                              1056.57666015625,
                              585.2077026367188],
              'name': 'IOT Core'},
             {'class': 28,
              'confidence': 0.8819605112075806,
              'coordinates': [969.5029296875,
                              213.13211059570312,
                              1056.387939453125,
                              299.4565734863281],
              'name': 'Cloud Watch'},
             {'class': 123,
              'confidence': 0.8803290724754333,
              'coordinates': [400.7654724121094,
                              453.84027099609375,
                              445.5066833496094,
                              494.1293029785156],
              'name': 'Private Subnet'},
             {'class': 140,
              'confidence': 0.8799541592597961,
              'coordinates': [969.0143432617188,
                              767.47216796875,
                              1057.012939453125,
                              856.7139892578125],
              'name': 'SES'},
             {'class': 123,
              'confidence': 0.8694849014282227,
              'coordinates': [690.9721069335938,
                              453.1850891113281,
                              735.8294067382812,
                              495.0124206542969],
              'name': 'Private Subnet'},
             {'class': 123,
              'confidence': 0.8522970676422119,
              'coordinates': [136.60072326660156,
                              454.017333984375,
                              178.5751495361328,
                              496.0107116699219],
              'name': 'Private Subnet'},
             {'class': 55,
              'confidence': 0.8064488172531128,
              'coordinates': [762.9654541015625,
                              561.7301635742188,
                              851.2537231445312,
                              652.2162475585938],
              'name': 'EC2'},
             {'class': 55,
              'confidence': 0.7948201298713684,
              'coordinates': [196.136474609375,
                              558.6541137695312,
                              286.9456481933594,
                              649.6227416992188],
              'name': 'EC2'},
             {'class': 176,
              'confidence': 0.7853794693946838,
              'coordinates': [385.1454162597656,
                              38.46767044067383,
                              474.0307312011719,
                              130.90625],
              'name': 'WAF'},
             {'class': 12,
              'confidence': 0.748910129070282,
              'coordinates': [778.5922241210938,
                              688.5576782226562,
                              824.1015625,
                              734.7759399414062],
              'name': 'Auto Scaling'},
             {'class': 32,
              'confidence': 0.7255633473396301,
              'coordinates': [503.5216064453125,
                              40.24740982055664,
                              598.1478271484375,
                              129.8302459716797],
              'name': 'Cloudfront'},
             {'class': 62,
              'confidence': 0.7224067449569702,
              'coordinates': [547.9291381835938,
                              756.753173828125,
                              632.2969970703125,
                              842.6041259765625],
              'name': 'ElastiCache'}],
   'path': 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'}])
████████████████████████████████ 100% | 38.90/38.9 MB [01:25<00:00,  2.20s/MB]:
Skipping upload, could not find object file 'C:\Users\acmattos\AppData\Local\Temp\tmpto9olqpe.png'
Skipping upload, could not find object file 'C:\Users\acmattos\AppData\Local\Temp\tmpjlmnq_h6.png'
Skipping upload, could not find object file 'C:\Users\acmattos\AppData\Local\Temp\tmpq_h0rljf.png'
████████████████████████████████ 100% | 0.31/0.31 MB [05:03<00:00, 979.43s/MB]:
████████████████████████████████ 100% | 0.30/0.3 MB [05:03<00:00, 1012.03s/MB]:
███████████████████████████████ 100% | 0.26/0.26 MB [05:03<00:00, 1167.70s/MB]:
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton> cd D:\ia4devs\module_05\05_hackaton
(.venv) PS D:\ia4devs\module_05\05_hackaton> py .\model.py
New https://pypi.org/project/ultralytics/8.3.162 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=6, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.0005, lrf=0.05, mask_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11m.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11m_custom_100, nbs=64, nms=False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=10, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=182

                   from  n    params  module                                       arguments
  0                  -1  1      1856  ultralytics.nn.modules.conv.Conv             [3, 64, 3, 2]
  1                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]
  2                  -1  1    111872  ultralytics.nn.modules.block.C3k2            [128, 256, 1, True, 0.25]
  3                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]
  4                  -1  1    444928  ultralytics.nn.modules.block.C3k2            [256, 512, 1, True, 0.25]
  5                  -1  1   2360320  ultralytics.nn.modules.conv.Conv             [512, 512, 3, 2]
  6                  -1  1   1380352  ultralytics.nn.modules.block.C3k2            [512, 512, 1, True]
  7                  -1  1   2360320  ultralytics.nn.modules.conv.Conv             [512, 512, 3, 2]
  8                  -1  1   1380352  ultralytics.nn.modules.block.C3k2            [512, 512, 1, True]
  9                  -1  1    656896  ultralytics.nn.modules.block.SPPF            [512, 512, 5]
 10                  -1  1    990976  ultralytics.nn.modules.block.C2PSA           [512, 512, 1]
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 13                  -1  1   1642496  ultralytics.nn.modules.block.C3k2            [1024, 512, 1, True]
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 16                  -1  1    542720  ultralytics.nn.modules.block.C3k2            [1024, 256, 1, True]
 17                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 19                  -1  1   1511424  ultralytics.nn.modules.block.C3k2            [768, 512, 1, True]
 20                  -1  1   2360320  ultralytics.nn.modules.conv.Conv             [512, 512, 3, 2]
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 22                  -1  1   1642496  ultralytics.nn.modules.block.C3k2            [1024, 512, 1, True]
 23        [16, 19, 22]  1   1551346  ultralytics.nn.modules.head.Detect           [182, [256, 512, 512]]
YOLO11m summary: 231 layers, 20,193,330 parameters, 20,193,314 gradients, 69.0 GFLOPs

Transferred 643/649 items from pretrained weights
ClearML Task: created new task id=4d88d8495b224537b71cc9f78d532fad
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/4d88d8495b224537b71cc9f78d532fad/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed
train: Fast image access  (ping: 0.20.1 ms, read: 900.8340.6 MB/s, size: 1118.3 KB)
train: Scanning D:\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 3457 images, 0 backgrounds, 0 c
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
val: Fast image access  (ping: 0.10.1 ms, read: 432.2297.8 MB/s, size: 607.4 KB)
val: Scanning D:\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 1488 images, 0 backgrounds, 0 cor
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\labels.jpg...
optimizer: AdamW(lr=0.0005, momentum=0.937) with parameter groups 106 weight(decay=0.0), 113 weight(decay=0.000515625), 112 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/100      7.37G      1.421      5.513      1.155        253        384:   2%|▏         | 10/577 [00:04<03:27,  
      1/100      7.55G      1.108      2.564     0.9695        242        576:  67%|██████▋   | 388/577 [02:18<00:49, 
      1/100      7.55G      1.071      2.245     0.9587         29        544: 100%|██████████| 577/577 [03:18<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   7%|▋         | 9/124 [00:01
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.695      0.418      0.493      0.376

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/100      7.54G     0.9569      1.188     0.9321         25        672: 100%|██████████| 577/577 [02:54<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.754      0.715      0.794      0.612

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/100      7.86G     0.9032     0.9137     0.9158          9        672: 100%|██████████| 577/577 [02:38<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.842      0.836      0.915      0.727

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/100      7.69G     0.8737     0.8256     0.9097         12        736: 100%|██████████| 577/577 [03:48<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.863      0.886      0.939      0.764

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/100      7.72G     0.8313     0.7116     0.9021         24        896: 100%|██████████| 577/577 [04:20<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.899      0.929      0.969      0.803

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/100      7.78G     0.7875     0.6362     0.8858         80        768: 100%|██████████| 577/577 [04:44<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.945      0.962      0.978      0.836

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/100      7.69G     0.7651     0.6092     0.8865         27        960: 100%|██████████| 577/577 [03:57<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.928      0.977       0.98      0.853

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/100      7.64G       0.73      0.556     0.8752         16        864: 100%|██████████| 577/577 [02:39<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.932       0.98       0.98       0.85

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/100      7.76G     0.7183     0.5498     0.8703         29        640: 100%|██████████| 577/577 [02:51<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.955      0.976      0.982      0.872

(...)

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/100      8.05G     0.4519     0.3103     0.8122          5        384: 100%|██████████| 577/577 [06:15<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.953      0.999      0.982      0.948

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/100      7.66G     0.4436     0.3047     0.8118         52        608: 100%|██████████| 577/577 [03:15<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.951      0.999      0.984      0.948

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/100      7.56G     0.4367     0.3027     0.8113         32        928: 100%|██████████| 577/577 [04:10<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.971       0.99      0.982      0.947

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/100      7.54G      0.438      0.303     0.8122         54        736: 100%|██████████| 577/577 [03:39<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.959      0.993      0.983      0.948

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/100      7.87G     0.4401     0.3049     0.8098         48        864: 100%|██████████| 577/577 [02:46<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.958      0.994      0.984      0.949

(...)

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     81/100       7.8G     0.3734     0.2554      0.799         68        320: 100%|██████████| 577/577 [04:41<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.959      0.997      0.982      0.956

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     82/100      8.03G     0.3781     0.2593     0.7981         21        320: 100%|██████████| 577/577 [02:51<00:00,
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                   all       1488      30084      0.955      0.998      0.982      0.957
EarlyStopping: Training stopped early as no improvement observed in last 10 epochs. Best results observed at epoch 72, best model saved as best.pt.
To update EarlyStopping(patience=10) pass a new patience value, i.e. `patience=300` or use `patience=0` to disable EarlyStopping.

82 epochs completed in 5.280 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\last.pt, 40.8MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\best.pt, 40.8MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\best.pt...
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11m summary (fused): 125 layers, 20,170,354 parameters, 0 gradients, 68.4 GFLOPs
                     Class  Images Instances  Box(P      R  mAP50  mAP50-95): 100%|██████████| 124/124 [00:
                       all    1488     30084  0.955  0.995  0.984      0.936
                       ACM      62        62   0.99      1  0.995      0.953
                       ALB     228       332  0.998      1  0.995      0.947
                       AMI      29        44  0.986      1  0.995      0.979
               API-Gateway     774      1178  0.968      1  0.995      0.958
  Active Directory Service      31        31  0.981      1  0.995      0.978
                  Airflow_      15        30   0.98      1  0.995      0.984
                   Amplify      84        84  0.993      1  0.995      0.895
        Analytics Services      15        15  0.962      1  0.995      0.988
                   AppFlow      15        15  0.961      1  0.995      0.995
                   Appsync      61        61  0.991      1  0.995      0.826
                    Athena     143       148   0.84      1   0.99      0.965
                    Aurora      89       126  0.995      1  0.995      0.982
              Auto Scaling     173       307  0.995      1  0.995      0.929
        Auto Scaling Group      35        88  0.993      1  0.995      0.841
           Automated Tests      64        98  0.994      1  0.995      0.974
         Availability Zone      24        48  0.987      1  0.995      0.956
                    Backup      15        30   0.98      1  0.995      0.995
         Build Environment      44        44  0.975      1  0.995      0.868
                       CDN      20        20  0.884      1  0.995      0.975
                       CUR      42        42  0.987      1  0.995      0.801
              Call Metrics      15        15  0.961      1  0.995      0.963
           Call Recordings      15        15  0.961      1  0.995       0.91
       Certificate Manager      98        98  0.994      1  0.995      0.988
                    Client      16        61  0.669      1  0.742      0.667
           Cloud Connector      16        32  0.981      1  0.995       0.94
                 Cloud Map      15        15  0.961      1  0.995      0.995
              Cloud Search      56        56  0.989      1  0.995       0.96
               Cloud Trail     187       192  0.996      1  0.995      0.972
               Cloud Watch     543       644  0.999      1  0.995      0.949
      CloudFormation Stack     150       168  0.994      1  0.995      0.961
                  CloudHSM      34        34  0.982      1  0.995      0.916
          CloudWatch Alarm      87       121  0.995      1  0.995      0.942
                Cloudfront     401       427  0.926  0.995  0.995      0.962
                 CodeBuild     157       245  0.998      1  0.995      0.961
                CodeCommit      68        80  0.992      1  0.995      0.979
                CodeDeploy      17        17  0.965      1  0.995      0.995
              CodePipeline     214       220  0.861      1  0.995      0.934
                   Cognito     346       391  0.846      1  0.984      0.952
                Comprehend      72        72  0.991      1  0.995      0.994
                    Config     103       178  0.982   0.92  0.991      0.903
                   Connect      15        15      1      1  0.995      0.995
      Connect Contact Lens      15        15  0.961      1  0.995      0.987
                 Container      79       346  0.984      1  0.995      0.903
             Control Tower      17        17  0.965      1  0.995      0.995
          Customer Gateway      38        74  0.992      1  0.995      0.965
                       DSI      34        68  0.991      1  0.995      0.884
             Data Pipeline      23        23  0.973      1  0.995      0.928
                  DataSync      32        32  0.981      1  0.995      0.991
              Deploy Stage      30        30   0.98      1  0.995      0.924
                 Detective      15        15  0.961      1  0.995      0.915
            Direct Connect      91       126  0.995      1  0.995      0.958
              Distribution      15        15  0.609      1  0.895      0.887
              Docker Image      56       179  0.912      1  0.995      0.836
                 Dynamo DB     660       979  0.957      1  0.995      0.964
                       EBS      92       147  0.996      1  0.995      0.953
                       EC2     707      1935  0.986      1  0.995      0.936
                       EFS     100       133  0.995      1  0.995      0.945
          EFS Mount Target      99       129  0.995      1  0.995      0.958
                       EKS     161       184  0.997      1  0.995      0.977
                       ELB     425       583  0.994  0.969  0.975      0.944
                       EMR      15        15  0.961      1  0.995      0.895
             Edge Location      20        42  0.985      1  0.995      0.982
               ElastiCache     138       170  0.996      1  0.995      0.954
Elastic Container Registry     235       235  0.997      1  0.995      0.958
 Elastic Container Service     258       331  0.909      1  0.994      0.901
            Elastic Search     142       147  0.996      1  0.995      0.948
    Elemental MediaConvert      49        66  0.952  0.788  0.965      0.951
    Elemental MediaPackage      15        15  0.462      1  0.605      0.605
                     Email      25        25  0.977      1  0.995      0.987
                  Endpoint      27        27  0.979      1  0.995      0.927
                 Event Bus      16        16  0.963      1  0.995      0.995
               EventBridge      60       120  0.971      1  0.995      0.881
       Experiment Duration      17        17   0.56      1  0.612      0.588
               Experiments      17        17  0.559      1  0.675      0.675
                   Fargate     193       427  0.981      1  0.995      0.925
 Fault Injection Simulator      49        49  0.988      1  0.995      0.919
          Firewall Manager      15        15      1      1  0.995      0.914
                     Flask      15        45  0.964      1  0.995      0.868
                 Flow logs      15        60   0.99      1  0.995      0.848
                  GameLift      17        17  0.966      1  0.995      0.924
                       Git      15        15  0.961      1  0.995      0.968
                    Github      81        95  0.993      1  0.995      0.962
                   Glacier      15        15      1      1  0.995      0.978
                      Glue      58       116  0.993      1  0.995      0.933
             Glue DataBrew      26        26  0.977      1  0.995      0.995
                   Grafana      20        20      1      1  0.995      0.995
                 GuardDuty      72       132  0.995      1  0.995      0.928
                       IAM     201       334  0.894      1  0.991        0.9
                  IAM Role      98       207  0.872      1   0.98      0.836
                  IOT Core      40        54  0.989      1  0.995      0.978
                     Image      74        74  0.992      1  0.995      0.876
             Image Builder      15        15  0.961      1  0.995      0.995
                   Ingress      15        15  0.961      1  0.995      0.985
           Inspector Agent      15        15  0.961      1  0.995      0.878
                 Instances      19        38   0.57  0.488  0.651      0.561
                  Internet     240       345      1  0.965  0.994      0.963
          Internet Gateway     167       247  0.998      1  0.995      0.936
                   Jenkins      15        30   0.98      1  0.995      0.945
    Key Management Service     127       155  0.996      1  0.995       0.99
                    Kibana      15        15  0.962      1  0.995      0.923
      Kinesis Data Streams     150       198  0.996      1  0.995      0.968
                Kubernetes      15        15  0.962      1  0.995       0.96
                    Lambda     945      2489  0.948      1  0.995      0.954
                       Lex      16        16  0.963      1  0.995      0.995
                        MQ      25        57   0.99      1  0.995      0.916
          Machine Learning      56        56  0.829      1  0.982      0.923
                     Macie      65       146  0.996      1  0.995       0.95
               Marketplace      21        21  0.974      1  0.995      0.634
                 Memcached      18        36  0.983      1  0.995       0.98
             Mobile Client     198       249  0.985      1  0.995       0.93
                  Mongo DB      26        70  0.929      1  0.995      0.904
                     MySQL      15        15  0.961      1  0.995       0.99
               NAT Gateway     187       375  0.998      1  0.995      0.962
                   Neptune      42        42    0.6      1  0.995      0.764
           Network Adapter      15        15  0.961      1  0.995      0.995
          Network Firewall      15        15  0.961      1  0.995      0.961
                  Notebook      18        18  0.967      1  0.995      0.995
          Order Controller      18        18  0.967      1  0.995      0.989
        Organization Trail      32        77  0.992      1  0.995      0.854
           Parameter Store      26        26  0.977      1  0.995      0.995
                  Pinpoint      16        16  0.963      1  0.995      0.995
                PostgreSQL      15        15  0.961      1  0.995      0.986
              Private Link      89        89  0.985      1  0.995      0.949
            Private Subnet     368       930  0.973  0.982  0.986      0.864
                Prometheus      20        20  0.969      1  0.995      0.995
             Public Subnet     338       841  0.995      1  0.995      0.865
                   Quarkus      20        20   0.97      1  0.995      0.984
                Quicksight      41        51  0.988      1  0.995      0.986
                       RDS     345       685  0.999      1  0.995       0.95
                     React      15        15  0.961      1  0.995      0.814
                     Redis      49       100  0.994      1  0.995      0.975
                  Redshift      73        80  0.992      1  0.995      0.951
                    Region     183       269  0.997      1  0.995      0.879
               Rekognition      33        33  0.982      1  0.995      0.992
                   Results      17        17  0.558      1  0.901      0.901
                  Route 53      53        53  0.989      1  0.995      0.995
                   Route53     428       611  0.999      1  0.995      0.957
                        S3     977      2096   0.94      1  0.995      0.943
                       SAR      18        18      1      1  0.995      0.995
                       SDK     123       403      1  0.975  0.995      0.965
                       SES      72        87  0.992      1  0.995      0.951
                       SNS     258       279  0.998      1  0.995      0.977
                       SQS     189       199  0.997      1  0.995      0.968
                 SSM Agent      15        15  0.961      1  0.995      0.865
                 Sagemaker      81       267  0.718      1  0.968      0.809
            Secret Manager      46        46  0.987      1  0.995      0.926
            Security Group      15        15      1      1  0.995      0.995
              Security Hub      31        91  0.994      1  0.995      0.895
                    Server     101       193  0.997      1  0.995      0.953
           Service Catalog      40        91  0.993      1  0.995      0.936
                    Shield      58        58   0.99      1  0.995      0.994
                   Sign-On      15        15   0.96      1  0.995      0.995
                     Slack      37        37  0.984      1  0.995      0.979
                  Snowball      15        15  0.961      1  0.995      0.995
                     Stack      22        22  0.973      1  0.995      0.901
             Step Function      32        96  0.994      1  0.995      0.914
           Storage Gateway      15        15  0.961      1  0.995      0.995
                SwaggerHub      15        15  0.961      1  0.995      0.995
           Systems Manager      61        76  0.992      1  0.995      0.956
                        TV      22        22  0.974      1  0.995      0.936
                     Table      88       196  0.997      1  0.995      0.957
               Task Runner      18        18  0.968      1  0.995      0.986
                 Terraform      32        32  0.981      1  0.995      0.935
                 Text File      54       122  0.943      1  0.994      0.964
                  Textract      17        17  0.965      1  0.995      0.995
                Transcribe      17        17  0.965      1  0.995      0.995
           Transfer Family      68        68  0.991      1  0.995      0.976
           Transit Gateway      35        35  0.983      1  0.995      0.978
                 Translate      49        49  0.987      1  0.995       0.99
           Trusted Advisor      36        36  0.983      1  0.995      0.995
                    Twilio      15        15  0.961      1  0.995      0.995
                     Users     574       790  0.994  0.996  0.995      0.922
                       VDA      16        16  0.964      1  0.995      0.964
                VP Gateway      30        36  0.984      1  0.995      0.959
                VPC Router      50       102  0.994      1  0.995      0.962
            VPN Connection      21        57  0.989      1  0.995      0.984
                       WAF     112       131  0.995      1  0.995      0.962
               Web Clients     213       248   0.82      1  0.984      0.904
                  Websites      31        31   0.98      1  0.995      0.956
                     X-Ray      83        95  0.972      1  0.995      0.968
                       aws     971      1219  0.997      1  0.995      0.899
              cache Worker      36        36  0.983      1  0.995      0.995
Speed: 0.2ms preprocess, 12.1ms inference, 0.0ms loss, 1.0ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11m_custom_100\weights\best.pt
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11m summary (fused): 125 layers, 20,170,354 parameters, 0 gradients, 68.4 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 713.9422.1 MB/s, size: 628.8 KB)
val: Scanning D:\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache... 1327 images, 0 backgrounds, 0 corr
                     Class Images Instances   Box(P      R   mAP50  mAP50-95): 100%|██████████| 166/166 [00:
                       all   1327     26828   0.958  0.989    0.98      0.957: 100%|██████████| 166/166 [00:
                       ACM     42        42   0.985      1   0.995      0.995
                       ALB    206       292       1  0.989   0.995       0.96
                       AMI     24        39   0.984      1   0.995      0.995
               API-Gateway    707      1063   0.973      1   0.995       0.98
  Active Directory Service     29        29    0.98      1   0.995      0.995
                  Airflow_     15        30    0.98      1   0.995      0.988
                   Amplify     76        76   0.994      1   0.995      0.925
        Analytics Services     15        15   0.961      1   0.995      0.995
                   AppFlow     15        15    0.96      1   0.995      0.995
                   Appsync     50        50   0.989      1   0.995      0.857
                    Athena    133       141   0.914      1   0.995      0.979
                    Aurora     79       112   0.994  0.964   0.978      0.975
              Auto Scaling    126       211   0.999      1   0.995      0.949
        Auto Scaling Group     25        58    0.99      1   0.995      0.931
           Automated Tests     58        89   0.993      1   0.995      0.974
         Availability Zone     23        46   0.987      1   0.995      0.995
                    Backup     16        32   0.981      1   0.995      0.995
         Build Environment     34        34   0.979      1   0.995      0.852
                       CDN     21        21   0.971      1   0.995      0.983
                       CUR     35        35   0.984      1   0.995      0.865
              Call Metrics     15        15   0.961      1   0.995      0.995
           Call Recordings     15        15   0.961      1   0.995      0.921
       Certificate Manager    103       103   0.994      1   0.995      0.995
                    Client     16        61     0.5      1   0.616      0.562
           Cloud Connector     14        28   0.978      1   0.995      0.974
                 Cloud Map     15        15   0.908      1   0.995      0.995
              Cloud Search     48        48   0.987      1   0.995      0.993
               Cloud Trail    140       142   0.995      1   0.995      0.988
               Cloud Watch    468       566   0.999      1   0.995      0.972
      CloudFormation Stack    124       138   0.995      1   0.995      0.994
                  CloudHSM     33        33   0.981      1   0.995      0.995
          CloudWatch Alarm     75       106   0.994      1   0.995      0.954
                Cloudfront    346       366   0.941      1   0.995      0.975
                 CodeBuild    140       208   0.997      1   0.995      0.978
                CodeCommit     52        66   0.991      1   0.995      0.994
                CodeDeploy     13        13   0.949      1   0.995       0.99
              CodePipeline    183       190   0.851      1   0.992      0.956
                   Cognito    310       354   0.893  0.992   0.989      0.977
                Comprehend     73        73   0.992      1   0.995      0.995
                    Config     72       147   0.995  0.898    0.99      0.966
                   Connect     15        15       1      1   0.995      0.995
      Connect Contact Lens     15        15   0.961      1   0.995      0.995
                 Container     86       403   0.994      1   0.995       0.95
             Control Tower     14        14   0.958      1   0.995      0.995
          Customer Gateway     35        62    0.99      1   0.995      0.974
                       DSI     31        62   0.991      1   0.995      0.888
             Data Pipeline     22        22   0.972      1   0.995      0.995
                  DataSync     30        30       1      1   0.995      0.995
              Deploy Stage     27        27   0.978      1   0.995      0.873
                 Detective     15        15   0.961      1   0.995      0.995
            Direct Connect     77       112   0.994  0.991   0.995      0.972
              Distribution     15        15   0.855  0.333   0.888      0.888
              Docker Image     44       174   0.977  0.983   0.989      0.891
                 Dynamo DB    619       958   0.976  0.992   0.995      0.971
                       EBS     65       107   0.995  0.991   0.995       0.95
                       EC2    609      1692   0.982  0.994   0.994      0.967
                       EFS     90       116   0.991  0.971   0.988      0.983
          EFS Mount Target     95       128       1  0.974   0.984      0.971
                       EKS    147       164   0.995      1   0.995      0.981
                       ELB    379       521   0.981  0.964   0.975       0.96
                       EMR     15        15       1      1   0.995      0.995
             Edge Location     15        27   0.977      1   0.995      0.967
               ElastiCache    101       121   0.993  0.983    0.99      0.978
Elastic Container Registry    212       212   0.998      1   0.995       0.98
 Elastic Container Service    236       302   0.918      1   0.995      0.937
            Elastic Search    116       117   0.995      1   0.995      0.962
    Elemental MediaConvert     49        64   0.965  0.797   0.965      0.965
    Elemental MediaPackage     15        15   0.493      1   0.568      0.568
                     Email     29        29       1  0.987   0.995      0.986
                  Endpoint     22        22   0.974      1   0.995      0.942
                 Event Bus     15        15    0.96      1   0.995      0.995
               EventBridge     41       101   0.994      1   0.995      0.992
       Experiment Duration     14        14   0.512      1   0.642      0.634
               Experiments     14        14   0.511      1   0.647      0.647
                   Fargate    180       423   0.992      1   0.995      0.964
 Fault Injection Simulator     45        45   0.987      1   0.995      0.957
          Firewall Manager     15        15   0.962      1   0.995      0.995
                     Flask     17        51   0.985      1   0.995      0.882
                 Flow logs     15        60    0.99      1   0.995      0.946
                  GameLift     15        15   0.959      1   0.995      0.941
                       Git     17        17   0.965      1   0.995      0.939
                    Github     73        90   0.993      1   0.995       0.98
                   Glacier     15        15       1      1   0.995      0.995
                      Glue     59       118   0.995      1   0.995      0.967
             Glue DataBrew     22        22   0.973      1   0.995      0.995
                   Grafana     14        14   0.958      1   0.995      0.995
                 GuardDuty     57       117   0.995      1   0.995      0.984
                       IAM    180       335   0.911  0.997   0.991      0.967
                  IAM Role     78       185    0.86      1   0.984      0.903
                  IOT Core     46        52       1  0.994   0.995      0.995
                     Image     63        63   0.991      1   0.995      0.914
             Image Builder     15        15   0.956      1   0.995      0.995
                   Ingress     17        17   0.965      1   0.995      0.995
           Inspector Agent     15        15   0.961      1   0.995      0.995
                 Instances     16        32   0.515  0.438   0.589      0.584
                  Internet    201       272   0.992  0.945   0.993      0.975
          Internet Gateway    133       200   0.992      1   0.995      0.942
                   Jenkins     15        30   0.979      1   0.995      0.995
    Key Management Service    111       139   0.995      1   0.995      0.994
                    Kibana     18        18   0.967      1   0.995      0.932
      Kinesis Data Streams    156       207       1  0.989   0.995       0.99
                Kubernetes     17        17   0.967      1   0.995      0.995
                    Lambda    830      2220   0.974      1   0.995      0.982
                       Lex     18        18   0.967      1   0.995      0.995
                        MQ     34        86   0.993      1   0.995      0.974
          Machine Learning     47        47   0.803      1   0.979      0.976
                     Macie     56       119   0.995      1   0.995      0.985
               Marketplace     19        19   0.972      1   0.995      0.689
                 Memcached     11        22   0.973      1   0.995      0.967
             Mobile Client    150       196   0.995  0.996   0.995      0.942
                  Mongo DB     26        62    0.99      1   0.995      0.903
                     MySQL     15        15   0.961      1   0.995      0.986
               NAT Gateway    147       293   0.999   0.99   0.995      0.988
                   Neptune     35        35   0.973      1   0.995      0.755
           Network Adapter     15        15    0.96      1   0.995      0.995
          Network Firewall     15        15       1      1   0.995      0.995
                  Notebook     15        15   0.961      1   0.995      0.995
          Order Controller     17        17   0.924      1   0.995      0.995
        Organization Trail     26        71   0.992      1   0.995      0.977
           Parameter Store     27        27   0.978      1   0.995      0.995
                  Pinpoint     16        16   0.963      1   0.995      0.995
                PostgreSQL     15        15   0.961      1   0.995      0.957
              Private Link     87        87   0.983      1   0.995      0.995
            Private Subnet    335       936   0.983  0.981   0.987      0.926
                Prometheus     14        14   0.958      1   0.995      0.995
             Public Subnet    299       715   0.999  0.992   0.995      0.925
                   Quarkus     14        14   0.958      1   0.995      0.995
                Quicksight     40        50   0.988      1   0.995      0.995
                       RDS    266       551   0.984  0.985   0.984      0.967
                     React     15        15   0.961      1   0.995       0.96
                     Redis     47        98       1  0.996   0.995      0.989
                  Redshift     65        72   0.991      1   0.995      0.995
                    Region    161       243   0.997      1   0.995      0.931
               Rekognition     37        37   0.984      1   0.995      0.995
                   Results     14        14   0.509      1   0.572      0.572
                  Route 53     39        39    0.96      1   0.995      0.995
                   Route53    376       532   0.997  0.998   0.995      0.979
                        S3    867      1862   0.957  0.991   0.994      0.971
                       SAR     14        14   0.957      1   0.995      0.995
                       SDK     98       301   0.991  0.963   0.993      0.976
                       SES     69        84   0.993  0.988   0.994      0.988
                       SNS    232       254   0.999      1   0.995       0.99
                       SQS    184       197   0.997      1   0.995      0.981
                 SSM Agent     15        15   0.961      1   0.995      0.995
                 Sagemaker     76       241   0.746  0.986   0.951      0.819
            Secret Manager     44        44   0.986      1   0.995      0.995
            Security Group     16        16   0.963      1   0.995      0.985
              Security Hub     25        85   0.994      1   0.995      0.989
                    Server     88       165   0.996      1   0.995      0.952
           Service Catalog     30        72   0.992      1   0.995      0.977
                    Shield     52        52   0.988      1   0.995      0.995
                   Sign-On     15        15    0.96      1   0.995      0.995
                     Slack     30        30    0.98      1   0.995      0.995
                  Snowball     15        15   0.961      1   0.995      0.995
                     Stack     14        14       1      1   0.995      0.991
             Step Function     30        90   0.993      1   0.995      0.926
           Storage Gateway     15        15    0.96      1   0.995      0.995
                SwaggerHub     15        15    0.96      1   0.995      0.995
           Systems Manager     53        68   0.991      1   0.995      0.995
                        TV     12        12   0.957      1   0.995       0.97
                     Table     72       154   0.993      1   0.995      0.952
               Task Runner     17        17       1      1   0.995      0.995
                 Terraform     38        38   0.984      1   0.995      0.994
                 Text File     49        99   0.913      1   0.975      0.965
                  Textract     14        14   0.957      1   0.995      0.995
                Transcribe     19        19   0.968      1   0.995      0.995
           Transfer Family     67        67   0.991      1   0.995      0.988
           Transit Gateway     31        31    0.96      1   0.995      0.992
                 Translate     53        53   0.988      1   0.995      0.995
           Trusted Advisor     13        13   0.956      1   0.995       0.99
                    Twilio     18        18   0.967      1   0.995      0.995
                     Users    486       656   0.999  0.991   0.995       0.96
                       VDA     14        14   0.958      1   0.995      0.995
                VP Gateway     27        39       1  0.992   0.995      0.957
                VPC Router     39        80   0.992      1   0.995      0.962
            VPN Connection     21        48   0.989      1   0.995      0.993
                       WAF     99       109   0.994      1   0.995      0.992
               Web Clients    202       268    0.83      1   0.973      0.917
                  Websites     34        34   0.981      1   0.995      0.995
                     X-Ray     88       112   0.992      1   0.995      0.994
                       aws    845      1067   0.991  0.998   0.994       0.94
              cache Worker     26        26   0.977      1   0.995      0.995
Speed: 0.2ms preprocess, 8.5ms inference, 0.0ms loss, 0.8ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.958
  Recall:       0.989
  mAP@0.5:      0.980
  mAP@0.5:0.95: 0.957

image 1/1 D:\ia4devs\module_05\05_hackaton\data\sample\aws_02.png: 576x640 
3 ALBs, 1 Auto Scaling, 1 Cloud Trail, 1 Cloud Watch, 1 Cloudfront, 4 EC2s, 
3 Private Subnets, 3 Public Subnets, 2 RDSs, 1 Region, 1 S3, 1 SES, 1 Users, 
2 WAFs, 1 aws, 50.6ms
Speed: 3.2ms preprocess, 50.6ms inference, 3.6ms postprocess per image at shape (1, 3, 576, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict\labels
✅ Detailed JSON saved to data\reports\yolo11m_custom_100\results.json
✅ Summary JSON saved to data\reports\yolo11m_custom_100\report.json
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
(...)
obb: None
(...)
orig_shape: (993, 1167)
path: 'D:\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict'
speed: {'preprocess': 3.1897000153549016, 'inference': 50.62539997743443, 'postprocess': 3.644100041128695}]
████████████████████████████████ 100% | 38.90/38.9 MB [01:27<00:00,  2.24s/MB]:
(.venv) PS D:\ia4devs\module_05\05_hackaton>
```
