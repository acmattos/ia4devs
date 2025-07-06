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




yolo11n
```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\model.py 
True
New https://pypi.org/project/ultralytics/8.3.157 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=200, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.05, mask_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11n.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11n_custom_200, nbs=64, nms=False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=40, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=182

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      6640  ultralytics.nn.modules.block.C3k2            [32, 64, 1, False, 0.25]      
  3                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
  4                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]     
  5                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
  6                  -1  1     87040  ultralytics.nn.modules.block.C3k2            [128, 128, 1, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1    249728  ultralytics.nn.modules.block.C2PSA           [256, 256, 1]                 
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1    111296  ultralytics.nn.modules.block.C3k2            [384, 128, 1, False]          
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 16                  -1  1     32096  ultralytics.nn.modules.block.C3k2            [256, 64, 1, False]           
 17                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 19                  -1  1     86720  ultralytics.nn.modules.block.C3k2            [192, 128, 1, False]          
 20                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 22                  -1  1    378880  ultralytics.nn.modules.block.C3k2            [384, 256, 1, True]           
 23        [16, 19, 22]  1    521278  ultralytics.nn.modules.head.Detect           [182, [64, 128, 256]]         
YOLO11n summary: 181 layers, 2,680,446 parameters, 2,680,430 gradients, 6.9 GFLOPs

Transferred 448/499 items from pretrained weights
ClearML Task: created new task id=63cd0f81cbeb4a03951f810806826bca
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/63cd0f81cbeb4a03951f810806826bca/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt'...
100%|██████████| 5.35M/5.35M [00:03<00:00, 1.77MB/s]
AMP: checks passed 
train: Fast image access  (ping: 0.00.0 ms, read: 97.760.3 MB/s, size: 80.2 KB)
train: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 478 images, 0 backgrounds, 0 corrupt: 100%|██████████| 478/478 [00:00<?, ?it/s]
WARNING Box and segment counts should be equal, but got len(segments) = 1356, len(boxes) = 7878. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 2 images, 0 backgrounds, 0 corrupt: 100%|██████████| 2/2 [00:00<?, ?it/s]
val: Fast image access  (ping: 0.00.0 ms, read: 118.261.5 MB/s, size: 235.6 KB)
WARNING Error decoding JSON from C:\Users\acmattos\AppData\Roaming\Ultralytics\persistent_cache.json. Starting with an empty dictionary.
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\labels.jpg... 
optimizer: AdamW(lr=0.01, momentum=0.937) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200
Starting training for 200 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/200      4.08G      1.446      4.368      1.207        189        352: 100%|██████████| 60/60 [00:42<00:00,  1.41it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  1.61it/s]
                   all          2         62          0          0          0          0
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/200      3.79G      1.451      3.408      1.246        230        800: 100%|██████████| 60/60 [00:26<00:00,  2.29it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.33it/s]
                   all          2         62     0.0963     0.0217    0.00837    0.00328

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/200      3.81G      1.408      3.163      1.282        248        768: 100%|██████████| 60/60 [00:24<00:00,  2.45it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  3.73it/s]
                   all          2         62     0.0844     0.0494     0.0392     0.0156

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/200      3.82G      1.351      2.954      1.222        225        480: 100%|██████████| 60/60 [00:23<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.09it/s]
                   all          2         62     0.0908      0.429       0.28      0.105
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/200      3.82G      1.337      2.841      1.211        262        480: 100%|██████████| 60/60 [00:21<00:00,  2.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.71it/s]
                   all          2         62      0.151      0.428       0.28      0.117

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/200      3.82G      1.332      2.677      1.224        169        512: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.69it/s]
                   all          2         62      0.455      0.337      0.349      0.145
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/200      3.84G      1.314       2.57      1.187        157        832: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  8.06it/s]
                   all          2         62      0.463      0.408      0.393      0.158

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/200      3.84G      1.302       2.47      1.206        306        640: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.13it/s]
                   all          2         62      0.228      0.761      0.499      0.217

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/200      3.84G       1.28      2.439      1.221        291        928: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.74it/s]
                   all          2         62      0.314      0.712      0.582      0.241
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     10/200      3.84G      1.255       2.35      1.202        234        704: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.02it/s]
                   all          2         62      0.579      0.405      0.463      0.178
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     11/200      3.84G      1.204      2.227      1.171        199        736: 100%|██████████| 60/60 [00:23<00:00,  2.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.45it/s]
                   all          2         62      0.256      0.606      0.529      0.239

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     12/200      3.84G      1.241      2.249      1.182        251        800: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.91it/s]
                   all          2         62      0.244      0.693      0.552      0.237
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     13/200      3.84G      1.196       2.17      1.194        240        896: 100%|██████████| 60/60 [00:23<00:00,  2.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.45it/s]
                   all          2         62      0.409      0.717      0.676      0.299

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     14/200      3.84G      1.229      2.179      1.189        301        608: 100%|██████████| 60/60 [00:22<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.71it/s]
                   all          2         62      0.531      0.739      0.766      0.362

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     15/200      3.84G      1.227      2.117      1.204        199        960: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.94it/s]
                   all          2         62      0.352      0.833       0.66      0.302
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     16/200      3.84G      1.203      2.005      1.163        209        640: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.58it/s]
                   all          2         62      0.753      0.427      0.635      0.278
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     17/200      3.85G      1.232      1.985      1.148        242        864: 100%|██████████| 60/60 [00:23<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.74it/s]
                   all          2         62      0.443      0.641      0.698      0.341
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     18/200      3.85G      1.204      1.989      1.167        237        704: 100%|██████████| 60/60 [00:22<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.61it/s]
                   all          2         62      0.413      0.842      0.797      0.383

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     19/200      3.85G      1.194      1.912      1.185        190        640: 100%|██████████| 60/60 [00:21<00:00,  2.74it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.55it/s]
                   all          2         62      0.292      0.674      0.587      0.264
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     20/200      3.85G      1.206      1.942      1.186        197        928: 100%|██████████| 60/60 [00:23<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.12it/s]
                   all          2         62      0.513      0.718      0.726      0.317

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     21/200      3.85G      1.192      1.892      1.148        270        832: 100%|██████████| 60/60 [00:22<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.63it/s]
                   all          2         62      0.635      0.576      0.786      0.391
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     22/200      3.85G      1.211      1.884      1.171        263        480: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.55it/s]
                   all          2         62      0.417      0.909      0.794       0.36
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     23/200      3.85G        1.2      1.844      1.145        127        736: 100%|██████████| 60/60 [00:22<00:00,  2.71it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.69it/s]
                   all          2         62      0.452      0.957      0.796      0.371

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     24/200      3.85G      1.161      1.779      1.108        312        480: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.11it/s]
                   all          2         62      0.378      0.957      0.826      0.387
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     25/200      4.18G      1.177      1.803       1.17        245        672: 100%|██████████| 60/60 [00:23<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.67it/s]
                   all          2         62      0.642      0.647      0.799      0.368
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     26/200      3.72G      1.208       1.82      1.162        384        544: 100%|██████████| 60/60 [00:23<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.52it/s]
                   all          2         62      0.574      0.796      0.789      0.374
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     27/200       4.3G      1.162      1.769      1.133        212        960: 100%|██████████| 60/60 [00:21<00:00,  2.77it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.78it/s]
                   all          2         62      0.438      0.834       0.75      0.336

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     28/200      3.71G      1.168      1.777      1.156        339        416: 100%|██████████| 60/60 [00:22<00:00,  2.67it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.59it/s]
                   all          2         62      0.623      0.681      0.805      0.374

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     29/200      3.96G      1.158       1.74      1.147        346        672: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.96it/s]
                   all          2         62      0.702      0.721      0.863      0.421
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     30/200      4.19G      1.174      1.765      1.139        331        480: 100%|██████████| 60/60 [00:22<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.31it/s]
                   all          2         62       0.55      0.812      0.808      0.382

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     31/200      3.85G      1.147      1.709      1.145        270        576: 100%|██████████| 60/60 [00:23<00:00,  2.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.41it/s]
                   all          2         62      0.648      0.593      0.775      0.367

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     32/200      3.86G      1.157      1.749      1.171        315        704: 100%|██████████| 60/60 [00:22<00:00,  2.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.46it/s]
                   all          2         62      0.608      0.734      0.837      0.406

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     33/200      4.23G      1.173      1.748      1.138        274        320: 100%|██████████| 60/60 [00:23<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.65it/s]
                   all          2         62       0.49      0.726      0.707      0.316
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     34/200      3.84G      1.143      1.668      1.129        220        960: 100%|██████████| 60/60 [00:22<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.92it/s]
                   all          2         62      0.637      0.726      0.836      0.395
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     35/200      3.85G      1.164      1.706      1.146        220        672: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.99it/s]
                   all          2         62      0.528      0.721      0.806       0.41

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     36/200      3.87G      1.168      1.666      1.131        197        352: 100%|██████████| 60/60 [00:21<00:00,  2.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.50it/s]
                   all          2         62      0.743      0.751      0.834      0.404

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     37/200      4.25G      1.177      1.672       1.17        263        896: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.84it/s]
                   all          2         62      0.486      0.902       0.82      0.386
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     38/200      4.07G      1.169      1.651      1.137        238        672: 100%|██████████| 60/60 [00:22<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.37it/s]
                   all          2         62      0.638      0.662      0.821      0.413
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     39/200       3.5G      1.134      1.606      1.132        260        544: 100%|██████████| 60/60 [00:24<00:00,  2.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.01it/s]
                   all          2         62      0.603      0.771      0.788      0.381

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/200      3.78G      1.154       1.59      1.156        248        704: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.31it/s]
                   all          2         62      0.567      0.748      0.804      0.371

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     41/200      4.16G      1.171      1.607      1.155        215        320: 100%|██████████| 60/60 [00:22<00:00,  2.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.65it/s]
                   all          2         62      0.653      0.718      0.768      0.367
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     42/200      4.15G      1.162      1.656      1.168        311        608: 100%|██████████| 60/60 [00:23<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.74it/s]
                   all          2         62      0.555      0.924      0.801      0.397

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     43/200      3.93G      1.149       1.57       1.13        184        768: 100%|██████████| 60/60 [00:22<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.73it/s]
                   all          2         62      0.681      0.701      0.845      0.421

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     44/200      4.22G      1.121      1.547      1.123        207        864: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.92it/s]
                   all          2         62      0.571      0.737      0.688      0.345

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     45/200      4.03G       1.13      1.575      1.127        197        544: 100%|██████████| 60/60 [00:21<00:00,  2.75it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.00it/s]
                   all          2         62      0.593      0.704      0.744      0.327

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     46/200      3.73G      1.136      1.607      1.145        209        960: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.96it/s]
                   all          2         62      0.704       0.68      0.877      0.411
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     47/200      4.01G      1.138      1.568      1.124        233        864: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.42it/s]
                   all          2         62      0.621       0.81      0.864      0.403
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/200      3.43G      1.122      1.559      1.099        291        576: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.79it/s]
                   all          2         62      0.517      0.902      0.864      0.379
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/200      3.68G      1.114      1.525      1.112        348        928: 100%|██████████| 60/60 [00:22<00:00,  2.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.48it/s]
                   all          2         62      0.635      0.717      0.821      0.378
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/200      3.69G      1.129      1.554      1.137        216        832: 100%|██████████| 60/60 [00:22<00:00,  2.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.77it/s]
                   all          2         62      0.666      0.671      0.783      0.388
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/200      4.25G      1.119      1.532      1.112        176        416: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.01it/s]
                   all          2         62      0.597      0.804      0.846      0.391
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/200      3.67G      1.118      1.534      1.106        232        768: 100%|██████████| 60/60 [00:23<00:00,  2.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.58it/s]
                   all          2         62      0.735       0.74      0.878      0.435
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     53/200      3.68G      1.126      1.517      1.126        195        544: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.06it/s]
                   all          2         62      0.665      0.822      0.854      0.421

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     54/200       3.7G      1.137      1.499      1.135        279        544: 100%|██████████| 60/60 [00:21<00:00,  2.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.97it/s]
                   all          2         62      0.751       0.71      0.917      0.464
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     55/200      4.04G       1.11      1.408      1.106        138        896: 100%|██████████| 60/60 [00:22<00:00,  2.65it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.74it/s]
                   all          2         62      0.788      0.728      0.876      0.408

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     56/200      3.55G      1.144      1.511      1.144        331        544: 100%|██████████| 60/60 [00:23<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.62it/s]
                   all          2         62      0.761      0.823        0.9       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     57/200      4.11G      1.117      1.424       1.12        196        640: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.11it/s]
                   all          2         62      0.866       0.68       0.86      0.421

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     58/200      3.89G      1.105      1.445      1.098        181        448: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.38it/s]
                   all          2         62      0.757      0.778      0.887      0.421
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     59/200      4.17G      1.124      1.484      1.114        253        704: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.60it/s]
                   all          2         62      0.633      0.848      0.907      0.457
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     60/200      3.48G      1.089      1.414      1.112        310        480: 100%|██████████| 60/60 [00:23<00:00,  2.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.51it/s]
                   all          2         62      0.632      0.761       0.88      0.404
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     61/200      3.71G      1.102      1.409      1.113        265        544: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.96it/s]
                   all          2         62      0.729      0.813      0.873      0.428
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     62/200      3.98G       1.14       1.48      1.129        242        800: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.55it/s]
                   all          2         62       0.72      0.772      0.886      0.437
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     63/200      4.65G      1.084      1.383      1.086        359        864: 100%|██████████| 60/60 [00:09<00:00,  6.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.89it/s]
                   all          2         62      0.683      0.799      0.906      0.452

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     64/200      3.92G      1.112      1.452      1.126        185        672: 100%|██████████| 60/60 [00:06<00:00,  8.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.41it/s]
                   all          2         62      0.737      0.803       0.88      0.431

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     65/200      3.93G       1.08      1.377       1.11        261        352: 100%|██████████| 60/60 [00:06<00:00,  8.91it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.78it/s]
                   all          2         62      0.652      0.872      0.929      0.454
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     66/200      3.93G      1.112      1.399       1.09        163        800: 100%|██████████| 60/60 [00:07<00:00,  8.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.76it/s]
                   all          2         62      0.637      0.869      0.923      0.449
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     67/200      4.26G      1.074       1.34      1.098        493        544: 100%|██████████| 60/60 [00:06<00:00,  8.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.02it/s]
                   all          2         62      0.672      0.861       0.89      0.402
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     68/200      4.32G      1.084      1.351      1.112        255        544: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.49it/s]
                   all          2         62      0.755        0.8       0.86      0.409
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     69/200      3.66G      1.103      1.435      1.099        169        544: 100%|██████████| 60/60 [00:06<00:00,  9.79it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.664      0.826      0.908      0.444
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     70/200      4.33G      1.084      1.368       1.13        391        928: 100%|██████████| 60/60 [00:07<00:00,  8.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.727      0.832      0.908      0.429

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     71/200      4.04G      1.078      1.351      1.102        189        640: 100%|██████████| 60/60 [00:07<00:00,  8.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 16.20it/s]
                   all          2         62      0.742       0.85      0.906      0.455
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     72/200      3.81G      1.068      1.308       1.09        186        384: 100%|██████████| 60/60 [00:07<00:00,  8.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.49it/s]
                   all          2         62      0.661       0.83      0.889      0.428
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     73/200      4.12G      1.079      1.397      1.093        279        896: 100%|██████████| 60/60 [00:06<00:00,  9.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.11it/s]
                   all          2         62      0.858      0.713      0.905      0.466
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     74/200      3.74G      1.107      1.385        1.1        228        800: 100%|██████████| 60/60 [00:06<00:00,  9.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.679      0.777      0.911      0.444
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     75/200      3.76G      1.095      1.353      1.112        357        608: 100%|██████████| 60/60 [00:06<00:00,  8.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 18.65it/s]
                   all          2         62      0.857      0.757      0.943      0.447
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     76/200      3.77G      1.069      1.289      1.111        363        672: 100%|██████████| 60/60 [00:07<00:00,  8.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 38.49it/s]
                   all          2         62      0.875       0.72      0.929      0.469
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     77/200      4.08G      1.106      1.377      1.098        263        640: 100%|██████████| 60/60 [00:06<00:00,  8.82it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.729      0.842      0.887       0.43
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     78/200      4.18G      1.096      1.394      1.101        265        480: 100%|██████████| 60/60 [00:06<00:00,  8.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.67it/s]
                   all          2         62      0.738       0.71      0.887      0.429
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     79/200      4.16G      1.085      1.309      1.095        238        800: 100%|██████████| 60/60 [00:07<00:00,  8.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.68it/s]
                   all          2         62      0.656      0.891      0.914       0.44
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     80/200      4.16G      1.072      1.317      1.092        188        672: 100%|██████████| 60/60 [00:06<00:00,  8.91it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 36.22it/s]
                   all          2         62      0.766      0.816      0.937      0.452

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     81/200      4.01G      1.098      1.343       1.12        302        896: 100%|██████████| 60/60 [00:07<00:00,  8.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.08it/s]
                   all          2         62       0.64      0.933      0.893      0.462

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     82/200      3.81G      1.075      1.339      1.095        314        672: 100%|██████████| 60/60 [00:06<00:00,  8.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.25it/s]
                   all          2         62      0.683       0.87       0.93      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     83/200      3.83G      1.104      1.422       1.14        323        640: 100%|██████████| 60/60 [00:07<00:00,  8.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.691      0.858      0.952      0.464
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     84/200      3.85G      1.088      1.375      1.112        266        704: 100%|██████████| 60/60 [00:06<00:00,  9.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.699      0.815      0.941      0.467

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     85/200      3.85G      1.097      1.327      1.092        225        544: 100%|██████████| 60/60 [00:06<00:00,  9.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.82it/s]
                   all          2         62      0.779      0.829      0.927      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     86/200      3.86G      1.078      1.357      1.106        326        544: 100%|██████████| 60/60 [00:06<00:00,  8.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.98it/s]
                   all          2         62      0.724      0.899       0.94      0.466

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     87/200      3.88G      1.102      1.318      1.079        315        608: 100%|██████████| 60/60 [00:06<00:00,  9.31it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.48it/s]
                   all          2         62      0.663       0.82      0.891      0.454

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     88/200      4.17G      1.069      1.319      1.094        183        640: 100%|██████████| 60/60 [00:06<00:00,  8.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.41it/s]
                   all          2         62      0.701      0.877      0.929      0.459
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     89/200      4.25G      1.052      1.333      1.109        277        832: 100%|██████████| 60/60 [00:07<00:00,  8.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.15it/s]
                   all          2         62      0.833      0.806      0.948      0.482
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     90/200      3.73G      1.072      1.314      1.091        187        480: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.80it/s]
                   all          2         62      0.748      0.899      0.934      0.463

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     91/200      3.98G       1.09       1.32      1.093        160        480: 100%|██████████| 60/60 [00:06<00:00,  8.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.43it/s]
                   all          2         62      0.767      0.755      0.917       0.44

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     92/200      4.26G      1.065      1.273      1.091        240        928: 100%|██████████| 60/60 [00:07<00:00,  8.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.715      0.857      0.921      0.464

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     93/200      3.89G      1.057      1.285       1.08        176        800: 100%|██████████| 60/60 [00:06<00:00,  8.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62       0.69      0.844      0.886      0.451

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     94/200      4.19G      1.051      1.266      1.099        216        512: 100%|██████████| 60/60 [00:07<00:00,  7.77it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 16.95it/s]
                   all          2         62      0.701      0.902      0.941      0.477

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     95/200      3.75G      1.068      1.286      1.102        302        384: 100%|██████████| 60/60 [00:07<00:00,  8.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.43it/s]
                   all          2         62      0.698       0.89       0.93      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     96/200      3.76G      1.083      1.355      1.089        312        640: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.66it/s]
                   all          2         62      0.792      0.819      0.905      0.448
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     97/200      3.77G      1.061      1.297      1.088        186        640: 100%|██████████| 60/60 [00:07<00:00,  8.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.09it/s]
                   all          2         62      0.671      0.889      0.916      0.433

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     98/200      3.77G      1.051       1.25      1.111        188        320: 100%|██████████| 60/60 [00:07<00:00,  7.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.64it/s]
                   all          2         62      0.742      0.908      0.952      0.459
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     99/200      3.79G      1.053        1.3      1.082        245        480: 100%|██████████| 60/60 [00:06<00:00,  8.78it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.31it/s]
                   all          2         62      0.696       0.87       0.93      0.478

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    100/200      4.12G      1.044       1.21      1.081        295        864: 100%|██████████| 60/60 [00:07<00:00,  8.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.95it/s]
                   all          2         62      0.689      0.778      0.926      0.454

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    101/200      4.39G      1.066      1.238      1.107        362        416: 100%|██████████| 60/60 [00:08<00:00,  7.48it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.18it/s]
                   all          2         62        0.7      0.886      0.917      0.447
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    102/200       3.3G      1.037       1.22      1.079        263        800: 100%|██████████| 60/60 [00:07<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.33it/s]
                   all          2         62      0.704      0.913      0.944      0.473

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    103/200      3.73G       1.04      1.193      1.092        249        640: 100%|██████████| 60/60 [00:07<00:00,  7.92it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.32it/s]
                   all          2         62      0.667      0.855      0.914       0.46
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    104/200      3.74G       1.05      1.242      1.106        332        864: 100%|██████████| 60/60 [00:07<00:00,  8.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.42it/s]
                   all          2         62      0.881      0.825      0.952      0.474

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    105/200      3.74G       1.05      1.258      1.079        223        832: 100%|██████████| 60/60 [00:07<00:00,  8.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.20it/s]
                   all          2         62      0.661      0.839      0.914      0.446

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    106/200      3.76G      1.063      1.207      1.093        281        640: 100%|██████████| 60/60 [00:07<00:00,  8.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.30it/s]
                   all          2         62      0.761      0.938      0.948      0.472
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    107/200      4.39G      1.054      1.226      1.077        305        640: 100%|██████████| 60/60 [00:07<00:00,  8.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.59it/s]
                   all          2         62      0.666      0.913      0.915      0.447

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    108/200      4.16G      1.047      1.226      1.083        333        832: 100%|██████████| 60/60 [00:07<00:00,  7.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 19.38it/s]
                   all          2         62       0.73      0.905      0.952      0.494
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    109/200      3.53G      1.055      1.213      1.043        276        320: 100%|██████████| 60/60 [00:06<00:00,  9.04it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.19it/s]
                   all          2         62      0.758      0.865      0.948      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    110/200      3.84G      1.038      1.185      1.089        223        384: 100%|██████████| 60/60 [00:07<00:00,  8.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.43it/s]
                   all          2         62      0.808      0.804      0.931      0.485
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    111/200      3.86G      1.038      1.223      1.097        236        416: 100%|██████████| 60/60 [00:06<00:00,  8.71it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62        0.8      0.785      0.923      0.456
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    112/200      3.87G      1.029       1.19      1.074        286        384: 100%|██████████| 60/60 [00:07<00:00,  8.49it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.673      0.874      0.906      0.469

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    113/200      3.87G      1.049       1.19       1.09        218        416: 100%|██████████| 60/60 [00:07<00:00,  8.09it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.48it/s]
                   all          2         62      0.722      0.931      0.933      0.451
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    114/200      3.88G      1.047      1.235      1.097        305        320: 100%|██████████| 60/60 [00:06<00:00,  8.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.47it/s]
                   all          2         62      0.773      0.935      0.942      0.465

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    115/200      4.26G      1.059       1.24      1.101        145        512: 100%|██████████| 60/60 [00:07<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.77it/s]
                   all          2         62      0.676      0.945      0.949      0.483

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    116/200       3.5G       1.05      1.214      1.077        242        320: 100%|██████████| 60/60 [00:07<00:00,  8.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.42it/s]
                   all          2         62      0.759      0.908      0.947      0.469

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    117/200      3.74G      1.034      1.173      1.073        162        672: 100%|██████████| 60/60 [00:07<00:00,  7.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.26it/s]
                   all          2         62      0.801       0.95      0.952      0.476

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    118/200      3.99G      1.035      1.193       1.09        229        832: 100%|██████████| 60/60 [00:07<00:00,  8.16it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.13it/s]
                   all          2         62      0.727      0.817      0.873      0.433
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    119/200      4.31G      1.028      1.164      1.084        296        480: 100%|██████████| 60/60 [00:07<00:00,  8.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.31it/s]
                   all          2         62      0.738      0.952      0.946      0.475
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    120/200      3.79G      1.012       1.13      1.089        265        672: 100%|██████████| 60/60 [00:07<00:00,  8.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.26it/s]
                   all          2         62      0.827      0.827      0.922      0.465
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    121/200      4.02G      1.014      1.144      1.061        328        960: 100%|██████████| 60/60 [00:07<00:00,  8.26it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.29it/s]
                   all          2         62      0.727      0.929      0.931       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    122/200      3.86G      1.065      1.222      1.084        222        896: 100%|██████████| 60/60 [00:07<00:00,  8.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.90it/s]
                   all          2         62      0.846      0.829      0.924      0.468

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    123/200      3.88G      1.048       1.22      1.087        204        864: 100%|██████████| 60/60 [00:06<00:00,  8.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.42it/s]
                   all          2         62      0.697      0.902      0.941      0.461
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    124/200      3.89G      1.028      1.148      1.075        290        576: 100%|██████████| 60/60 [00:07<00:00,  8.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.83it/s]
                   all          2         62      0.772       0.89      0.922      0.463

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    125/200      3.89G      1.054      1.219      1.097        237        448: 100%|██████████| 60/60 [00:07<00:00,  8.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.747      0.952      0.952       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    126/200      3.89G       1.04      1.187      1.074        187        672: 100%|██████████| 60/60 [00:06<00:00,  8.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 20.00it/s]
                   all          2         62       0.72      0.913      0.952      0.489
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    127/200      4.26G      1.041      1.196      1.083        167        352: 100%|██████████| 60/60 [00:07<00:00,  8.38it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.04it/s]
                   all          2         62      0.715      0.893       0.91      0.461
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    128/200      3.91G      1.043      1.157      1.074        371        352: 100%|██████████| 60/60 [00:07<00:00,  8.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.41it/s]
                   all          2         62       0.72      0.944      0.945      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    129/200      3.91G      1.024       1.14      1.068        198        960: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 17.13it/s]
                   all          2         62      0.732      0.917      0.921       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    130/200      3.93G      1.018       1.12      1.067        150        512: 100%|██████████| 60/60 [00:07<00:00,  7.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.98it/s]
                   all          2         62      0.749      0.849      0.915      0.446

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    131/200      4.19G      1.029      1.181      1.076        272        640: 100%|██████████| 60/60 [00:07<00:00,  8.04it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.98it/s]
                   all          2         62      0.803      0.883      0.922      0.452

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    132/200      3.67G      1.026      1.149      1.045        194        672: 100%|██████████| 60/60 [00:06<00:00,  9.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.97it/s]
                   all          2         62       0.84      0.786      0.927      0.473
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    133/200      3.97G       1.01      1.101      1.072        231        320: 100%|██████████| 60/60 [00:07<00:00,  8.15it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.862       0.79       0.92      0.458
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    134/200       4.3G      1.013      1.135      1.071        257        736: 100%|██████████| 60/60 [00:07<00:00,  8.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.765      0.894      0.934      0.475
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    135/200      3.85G      1.041      1.155      1.058        176        960: 100%|██████████| 60/60 [00:07<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.93it/s]
                   all          2         62      0.775      0.868      0.932      0.494
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    136/200      3.86G      1.034      1.183      1.068        254        672: 100%|██████████| 60/60 [00:06<00:00,  8.70it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.41it/s]
                   all          2         62      0.747      0.939      0.947      0.477

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    137/200      3.88G      1.018      1.141      1.034        333        512: 100%|██████████| 60/60 [00:06<00:00,  9.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.88it/s]
                   all          2         62      0.776      0.941      0.949      0.491
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    138/200      4.22G      1.025       1.14       1.05        229        800: 100%|██████████| 60/60 [00:07<00:00,  8.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.49it/s]
                   all          2         62      0.755      0.957      0.941      0.484
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    139/200      3.57G      1.008      1.097      1.057        221        320: 100%|██████████| 60/60 [00:07<00:00,  8.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.48it/s]
                   all          2         62      0.739      0.926      0.924      0.447
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    140/200      4.37G      1.038      1.172       1.09        236        928: 100%|██████████| 60/60 [00:07<00:00,  8.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.34it/s]
                   all          2         62      0.818      0.861      0.907      0.451

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    141/200       3.8G      1.011      1.102      1.078        276        608: 100%|██████████| 60/60 [00:07<00:00,  8.20it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.28it/s]
                   all          2         62      0.863      0.896      0.937      0.476
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    142/200      4.31G      1.005      1.112      1.063        225        448: 100%|██████████| 60/60 [00:07<00:00,  8.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.87it/s]
                   all          2         62       0.75      0.897      0.947      0.474
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    143/200      4.03G      1.009      1.083       1.06        295        704: 100%|██████████| 60/60 [00:07<00:00,  8.05it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.76it/s]
                   all          2         62      0.696      0.884      0.927      0.459

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    144/200       3.6G      1.003      1.076      1.043        299        320: 100%|██████████| 60/60 [00:07<00:00,  8.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.41it/s]
                   all          2         62      0.804      0.878      0.936      0.466
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    145/200      3.83G      1.037      1.163      1.061        307        576: 100%|██████████| 60/60 [00:06<00:00,  9.11it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.767      0.925      0.924      0.472

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    146/200      4.08G      1.003      1.065      1.031        255        704: 100%|██████████| 60/60 [00:06<00:00,  8.96it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.31it/s]
                   all          2         62      0.721      0.926      0.932      0.467
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    147/200      3.85G      1.034      1.177      1.076        213        800: 100%|██████████| 60/60 [00:06<00:00,  8.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.31it/s]
                   all          2         62      0.793      0.914      0.929      0.473
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    148/200      4.54G      1.026      1.105      1.077        326        864: 100%|██████████| 60/60 [00:07<00:00,  8.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.784      0.938      0.952      0.474
EarlyStopping: Training stopped early as no improvement observed in last 40 epochs. Best results observed at epoch 108, best model saved as best.pt.
To update EarlyStopping(patience=40) pass a new patience value, i.e. `patience=300` or use `patience=0` to disable EarlyStopping.

148 epochs completed in 0.611 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\last.pt, 5.6MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\best.pt, 5.6MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\best.pt...
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.05it/s]
                   all          2         62       0.74      0.901      0.952      0.483
           API-Gateway          2          4      0.613          1      0.995      0.298
               Amplify          2          2      0.771          1      0.995      0.497
               Appsync          2          2      0.793          1      0.995      0.427
                Athena          2          2      0.788          1      0.995      0.199
                   CUR          2          2      0.788          1      0.995      0.527
            Cloudfront          2          2      0.771          1      0.995      0.298
             CodeBuild          2          2      0.498          1      0.995      0.697
          CodePipeline          2          2      0.829          1      0.995      0.298
               Cognito          2          2          0          0      0.142     0.0426
                Config          2          2          1      0.841      0.995      0.497
             Dynamo DB          2          2      0.427          1      0.995      0.398
Elastic Container Registry          2          2      0.771          1      0.995      0.796
Elastic Container Service          2          2      0.516          1      0.995      0.398
        Elastic Search          2          2          1          0      0.995      0.796
               Fargate          2          2      0.783          1      0.995      0.398
                 Image          2          2      0.768          1      0.995      0.697
                Lambda          2          8      0.654      0.875      0.867      0.371
               Neptune          2          2      0.995          1      0.995      0.398
        Private Subnet          2          2      0.851          1      0.995      0.597
                    S3          2         10      0.835          1      0.995      0.296
                   SDK          2          2      0.968          1      0.995      0.597
                 Users          2          2      0.807          1      0.995      0.697
                   aws          2          2      0.785          1      0.995      0.895
Speed: 0.3ms preprocess, 71.8ms inference, 0.0ms loss, 1.4ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\best.pt
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 138.632.7 MB/s, size: 106.4 KB)
WARNING Box and segment counts should be equal, but got len(segments) = 233, len(boxes) = 426. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache... 21 images, 0 backgrounds, 0 corrupt: 100%|██████████| 21/21 [00:00<?, ?it/s]
                                            0% | 0.00/5.39 MB [00:00<?, ?MB/s]: 
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   0%|          | 0/3 [00:00<?, ?it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  33%|███▎      | 1/3 [00:00<00:00,  3.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  67%|██████▋   | 2/3 [00:00<00:00,  4.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 3/3 [00:00<00:00,  4.35it/s]
                   all         21        426      0.374      0.335      0.327      0.265
                   ACM          1          1          1          0          0          0
                   ALB          5          5      0.152        0.4      0.423      0.369
Active Directory Service          1          1          0          0          0          0
                Athena          1          1      0.786          1      0.995      0.895
                Aurora          4          7          0          0     0.0145    0.00145
          Auto Scaling          4          8       0.23       0.25      0.299      0.206
                   CDN          1          1      0.861          1      0.995      0.796
   Certificate Manager          1          1          0          0          0          0
          Cloud Search          1          1          1          0          0          0
           Cloud Trail          2          3      0.493      0.329      0.312      0.219
           Cloud Watch          5          7       0.27      0.857      0.804      0.731
  CloudFormation Stack          1          1      0.293          1      0.995      0.995
              CloudHSM          1          1          1          0          0          0
            Cloudfront          9          9      0.169      0.222      0.142      0.124
             CodeBuild          1          1      0.562          1      0.995      0.796
            CodeCommit          1          1      0.419          1      0.995      0.895
            CodeDeploy          1          1          1          1      0.995      0.796
               Cognito          1          1          0          0          0          0
                Config          1          6          0          0          0          0
             Container          1          1      0.317          1      0.995      0.697
             Detective          1          1          0          0          0          0
        Direct Connect          4         11      0.829      0.818       0.78      0.525
          Distribution          2          2          0          0          0          0
          Docker Image          1          2          1          0          0          0
             Dynamo DB          8         19      0.574      0.684      0.671      0.536
                   EBS          3          4          1          0      0.213      0.123
                   EC2         13         40      0.377      0.453      0.256      0.175
                   EFS          5          5     0.0592      0.071      0.047     0.0376
      EFS Mount Target          4          9      0.508      0.444      0.353      0.266
                   ELB         10         13       0.36      0.385      0.293      0.213
                   EMR          1          1          0          0          0          0
         Edge Location          1          3          0          0          0          0
           ElastiCache          3          5      0.573        0.4      0.297      0.232
Elastic Container Service          1          2      0.651          1      0.995      0.821
        Elastic Search          1          1          1          0      0.199      0.139
Elemental MediaConvert          1          1        0.5          1      0.995      0.796
Elemental MediaPackage          1          1          0          0          0          0
                 Email          1          1          1          0          0          0
           EventBridge          1          5          1          0          0          0
      Firewall Manager          1          1          0          0          0          0
             Flow logs          1          4          0          0          0          0
               Glacier          1          1          0          0          0          0
                  Glue          1          2      0.623          1      0.995      0.747
             GuardDuty          1          5          1          0          0          0
                   IAM          2          9       0.19      0.111      0.132     0.0846
              IAM Role          2          7      0.166      0.143      0.157     0.0472
              IOT Core          1          1      0.589          1      0.995      0.995
       Inspector Agent          1          1          0          0          0          0
              Internet          7          8      0.447      0.407      0.369      0.296
      Internet Gateway          3          4          0          0     0.0168    0.00337
Key Management Service          2          3          0          0          0          0
  Kinesis Data Streams          2          4      0.287          1      0.995      0.828
                Lambda          4         10      0.378        0.8      0.801       0.69
                 Macie          2          4      0.333       0.25      0.272      0.136
             Memcached          1          2          0          0          0          0
         Mobile Client          1          4      0.464          1      0.995      0.902
           NAT Gateway          4          8          0          0     0.0402     0.0141
      Network Firewall          1          1          0          0          0          0
    Organization Trail          1          4          0          0          0          0
        Private Subnet          3         10          0          0      0.027     0.0102
         Public Subnet          6         18      0.368      0.389      0.227      0.154
                   RDS          6         14      0.223        0.5      0.366      0.296
                 Redis          1          1      0.512          1      0.995      0.796
              Redshift          1          1          1          0      0.995      0.895
                Region          2          2          0          0          0          0
              Route 53          1          1          1          0          0          0
               Route53          9          9      0.274      0.333      0.346        0.3
                    S3         17         24       0.28      0.542      0.414      0.325
                   SDK          1          1      0.227          1      0.995      0.597
                   SES          2          2          0          0          0          0
                   SNS          3          3      0.334      0.667       0.67      0.637
                   SQS          2          2      0.342        0.5      0.253      0.253
             SSM Agent          1          1          0          0          0          0
        Secret Manager          1          1          0          0          0          0
        Security Group          1          1          0          0          0          0
          Security Hub          1          5          1          0          0          0
                Server          4         12      0.175       0.25      0.127     0.0862
                Shield          1          1          1          0          0          0
               Sign-On          1          1          0          0          0          0
              Snowball          1          1          0          0          0          0
         Step Function          1          3      0.789          1      0.995      0.895
       Storage Gateway          1          1          0          0          0          0
       Systems Manager          1          2          1          0          0          0
                 Users         11         13      0.509      0.462      0.325      0.207
            VP Gateway          1          1      0.628          1      0.995      0.796
            VPC Router          2          6      0.503      0.667      0.629       0.51
        VPN Connection          1          1      0.389          1      0.497      0.398
                   WAF          1          1          0          0          0          0
           Web Clients          2          7      0.234      0.143      0.149      0.119
                   aws         11         13      0.454      0.692      0.618      0.435
Speed: 1.4ms preprocess, 24.3ms inference, 0.0ms loss, 1.1ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.374
  Recall:       0.335
  mAP@0.5:      0.327
  mAP@0.5:0.95: 0.265

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 3 Cloud Watchs, 1 Dynamo DB, 5 Lambdas, 1 S3, 2 SNSs, 2 Userss, 46.3ms
Speed: 2.5ms preprocess, 46.3ms inference, 3.0ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict\labels
✅ Detailed JSON saved to data\reports\yolo11n_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11n_custom_200\report.json
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'ACM', 1: 'ALB', 2: 'AMI', 3: 'API-Gateway', 4: 'Active Directory Service', 5: 'Airflow_', 6: 'Amplify', 7: 'Analytics Services', 8: 'AppFlow', 9: 'Appsync', 10: 'Athena', 11: 'Aurora', 12: 'Auto Scaling', 13: 'Auto Scaling Group', 14: 'Automated Tests', 15: 'Availability Zone', 16: 'Backup', 17: 'Build Environment', 18: 'CDN', 19: 'CUR', 20: 'Call Metrics', 21: 'Call Recordings', 22: 'Certificate Manager', 23: 'Client', 24: 'Cloud Connector', 25: 'Cloud Map', 26: 'Cloud Search', 27: 'Cloud Trail', 28: 'Cloud Watch', 29: 'CloudFormation Stack', 30: 'CloudHSM', 31: 'CloudWatch Alarm', 32: 'Cloudfront', 33: 'CodeBuild', 34: 'CodeCommit', 35: 'CodeDeploy', 36: 'CodePipeline', 37: 'Cognito', 38: 'Comprehend', 39: 'Config', 40: 'Connect', 41: 'Connect Contact Lens', 42: 'Container', 43: 'Control Tower', 44: 'Customer Gateway', 45: 'DSI', 46: 'Data Pipeline', 47: 'DataSync', 48: 'Deploy Stage', 49: 'Detective', 50: 'Direct Connect', 51: 'Distribution', 52: 'Docker Image', 53: 'Dynamo DB', 54: 'EBS', 55: 'EC2', 56: 'EFS', 57: 'EFS Mount Target', 58: 'EKS', 59: 'ELB', 60: 'EMR', 61: 'Edge Location', 62: 'ElastiCache', 63: 'Elastic Container Registry', 64: 'Elastic Container Service', 65: 'Elastic Search', 66: 'Elemental MediaConvert', 67: 'Elemental MediaPackage', 68: 'Email', 69: 'Endpoint', 70: 'Event Bus', 71: 'EventBridge', 72: 'Experiment Duration', 73: 'Experiments', 74: 'Fargate', 75: 'Fault Injection Simulator', 76: 'Firewall Manager', 77: 'Flask', 78: 'Flow logs', 79: 'GameLift', 80: 'Git', 81: 'Github', 82: 'Glacier', 83: 'Glue', 84: 'Glue DataBrew', 85: 'Grafana', 86: 'GuardDuty', 87: 'IAM', 88: 'IAM Role', 89: 'IOT Core', 90: 'Image', 91: 'Image Builder', 92: 'Ingress', 93: 'Inspector Agent', 94: 'Instances', 95: 'Internet', 96: 'Internet Gateway', 97: 'Jenkins', 98: 'Key Management Service', 99: 'Kibana', 100: 'Kinesis Data Streams', 101: 'Kubernetes', 102: 'Lambda', 103: 'Lex', 104: 'MQ', 105: 'Machine Learning', 106: 'Macie', 107: 'Marketplace', 108: 'Memcached', 109: 'Mobile Client', 110: 'Mongo DB', 111: 'MySQL', 112: 'NAT Gateway', 113: 'Neptune', 114: 'Network Adapter', 115: 'Network Firewall', 116: 'Notebook', 117: 'Order Controller', 118: 'Organization Trail', 119: 'Parameter Store', 120: 'Pinpoint', 121: 'PostgreSQL', 122: 'Private Link', 123: 'Private Subnet', 124: 'Prometheus', 125: 'Public Subnet', 126: 'Quarkus', 127: 'Quicksight', 128: 'RDS', 129: 'React', 130: 'Redis', 131: 'Redshift', 132: 'Region', 133: 'Rekognition', 134: 'Results', 135: 'Route 53', 136: 'Route53', 137: 'S3', 138: 'SAR', 139: 'SDK', 140: 'SES', 141: 'SNS', 142: 'SQS', 143: 'SSM Agent', 144: 'Sagemaker', 145: 'Secret Manager', 146: 'Security Group', 147: 'Security Hub', 148: 'Server', 149: 'Service Catalog', 150: 'Shield', 151: 'Sign-On', 152: 'Slack', 153: 'Snowball', 154: 'Stack', 155: 'Step Function', 156: 'Storage Gateway', 157: 'SwaggerHub', 158: 'Systems Manager', 159: 'TV', 160: 'Table', 161: 'Task Runner', 162: 'Terraform', 163: 'Text File', 164: 'Textract', 165: 'Transcribe', 166: 'Transfer Family', 167: 'Transit Gateway', 168: 'Translate', 169: 'Trusted Advisor', 170: 'Twilio', 171: 'Users', 172: 'VDA', 173: 'VP Gateway', 174: 'VPC Router', 175: 'VPN Connection', 176: 'WAF', 177: 'Web Clients', 178: 'Websites', 179: 'X-Ray', 180: 'aws', 181: 'cache Worker'}
obb: None
orig_img: array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [ 39,  34,  33],
        [ 62,  55,  52],
        [ 54,  45,  42]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 254],
        [235, 228, 225],
        [ 67,  58,  55]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 254],
        [255, 255, 252],
        [ 41,  32,  29]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 248],
        [255, 255, 249],
        [ 49,  43,  36]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 248],
        [247, 239, 232],
        [ 53,  47,  40]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [ 44,  36,  29],
        [ 90,  80,  73],
        [ 51,  43,  36]]], dtype=uint8)
orig_shape: (597, 744)
path: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_01.jpg'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict'
speed: {'preprocess': 2.4835000513121486, 'inference': 46.330400044098496, 'postprocess': 3.0128000071272254}]
█████████████████████████████████ 100% | 5.39/5.39 MB [00:20<00:00,  3.83s/MB]: 

Process finished with exit code 0
```

Report:
```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\report.py 

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 3 Cloud Watchs, 1 Dynamo DB, 5 Lambdas, 1 S3, 2 SNSs, 2 Userss, 41.6ms
Speed: 2.2ms preprocess, 41.6ms inference, 86.1ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict7
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict7\labels
✅ Detailed JSON saved to data\reports\yolo11n_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11n_custom_200\report.json
Reports generated: data/reports/yolo11n_custom_200
```

yolo11s

```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\model.py 
New https://pypi.org/project/ultralytics/8.3.157 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=200, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.05, mask_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11s.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11s_custom_200, nbs=64, nms=False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=40, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=182

                   from  n    params  module                                       arguments                     
  0                  -1  1       928  ultralytics.nn.modules.conv.Conv             [3, 32, 3, 2]                 
  1                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  2                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]     
  3                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
  4                  -1  1    103360  ultralytics.nn.modules.block.C3k2            [128, 256, 1, False, 0.25]    
  5                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]              
  6                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]           
  7                  -1  1   1180672  ultralytics.nn.modules.conv.Conv             [256, 512, 3, 2]              
  8                  -1  1   1380352  ultralytics.nn.modules.block.C3k2            [512, 512, 1, True]           
  9                  -1  1    656896  ultralytics.nn.modules.block.SPPF            [512, 512, 5]                 
 10                  -1  1    990976  ultralytics.nn.modules.block.C2PSA           [512, 512, 1]                 
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1    443776  ultralytics.nn.modules.block.C3k2            [768, 256, 1, False]          
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 16                  -1  1    127680  ultralytics.nn.modules.block.C3k2            [512, 128, 1, False]          
 17                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 19                  -1  1    345472  ultralytics.nn.modules.block.C3k2            [384, 256, 1, False]          
 20                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]              
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 22                  -1  1   1511424  ultralytics.nn.modules.block.C3k2            [768, 512, 1, True]           
 23        [16, 19, 22]  1    889842  ultralytics.nn.modules.head.Detect           [182, [128, 256, 512]]        
YOLO11s summary: 181 layers, 9,498,226 parameters, 9,498,210 gradients, 21.9 GFLOPs

Transferred 493/499 items from pretrained weights
ClearML Task: created new task id=cdcfdb936c1b498e9d6aa6561e65c459
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/cdcfdb936c1b498e9d6aa6561e65c459/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed 
train: Fast image access  (ping: 0.00.0 ms, read: 783.6370.8 MB/s, size: 80.2 KB)
WARNING Box and segment counts should be equal, but got len(segments) = 1356, len(boxes) = 7878. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
train: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 478 images, 0 backgrounds, 0 corrupt: 100%|██████████| 478/478 [00:00<?, ?it/s]
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 2 images, 0 backgrounds, 0 corrupt: 100%|██████████| 2/2 [00:00<?, ?it/s]
val: Fast image access  (ping: 0.00.0 ms, read: 604.964.2 MB/s, size: 235.6 KB)
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200\labels.jpg... 
optimizer: AdamW(lr=0.01, momentum=0.937) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200
Starting training for 200 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/200      5.76G      1.454      3.696      1.238        189        352: 100%|██████████| 60/60 [00:14<00:00,  4.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.25it/s]
                   all          2         62          0          0          0          0

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/200      5.71G      1.435      2.942      1.282        230        800: 100%|██████████| 60/60 [00:10<00:00,  5.96it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  9.61it/s]
                   all          2         62          0          0          0          0

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/200      5.78G      1.424      2.801      1.308        248        768: 100%|██████████| 60/60 [00:10<00:00,  5.67it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 15.93it/s]
                   all          2         62     0.0281      0.109     0.0379     0.0121

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/200      5.34G      1.373      2.706      1.243        225        480: 100%|██████████| 60/60 [00:09<00:00,  6.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.03it/s]
                   all          2         62     0.0524      0.139     0.0873     0.0282

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/200      6.18G      1.336      2.547      1.215        262        480: 100%|██████████| 60/60 [00:09<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.39it/s]
                   all          2         62      0.286      0.648      0.525       0.24
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/200       5.5G      1.315      2.377      1.224        169        512: 100%|██████████| 60/60 [00:09<00:00,  6.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.91it/s]
                   all          2         62      0.461      0.406       0.45      0.197
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/200      5.47G      1.299      2.295      1.186        157        832: 100%|██████████| 60/60 [00:08<00:00,  7.00it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 17.38it/s]
                   all          2         62      0.156      0.322      0.218     0.0959
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/200      5.49G      1.274      2.197       1.19        306        640: 100%|██████████| 60/60 [00:09<00:00,  6.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.00it/s]
                   all          2         62      0.449      0.513      0.531      0.228
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/200      6.35G      1.274      2.163      1.211        291        928: 100%|██████████| 60/60 [00:20<00:00,  2.88it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.71it/s]
                   all          2         62      0.313      0.641      0.522      0.249
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     10/200      5.43G      1.256      2.078      1.189        234        704: 100%|██████████| 60/60 [00:22<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.87it/s]
                   all          2         62      0.331      0.752       0.65      0.324

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     11/200      5.96G      1.186      1.937      1.158        199        736: 100%|██████████| 60/60 [00:23<00:00,  2.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.58it/s]
                   all          2         62      0.346      0.848      0.745      0.365

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     12/200      5.65G      1.227      2.002       1.17        251        800: 100%|██████████| 60/60 [00:23<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.98it/s]
                   all          2         62      0.307      0.772      0.656      0.329

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     13/200      6.16G      1.181      1.877      1.185        240        896: 100%|██████████| 60/60 [00:24<00:00,  2.49it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.18it/s]
                   all          2         62      0.321      0.839      0.743      0.314
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     14/200      5.39G      1.208      1.913      1.174        301        608: 100%|██████████| 60/60 [00:23<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.59it/s]
                   all          2         62      0.574      0.772      0.788      0.385

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     15/200       5.9G      1.201      1.849      1.189        199        960: 100%|██████████| 60/60 [00:23<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.35it/s]
                   all          2         62      0.489      0.717       0.68      0.298

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     16/200      5.48G      1.162       1.72       1.14        209        640: 100%|██████████| 60/60 [00:22<00:00,  2.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.60it/s]
                   all          2         62      0.458      0.594      0.648      0.269

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     17/200      5.67G      1.215      1.721      1.137        242        864: 100%|██████████| 60/60 [00:23<00:00,  2.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.09it/s]
                   all          2         62      0.376      0.842      0.793      0.371

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     18/200      5.53G      1.189      1.718      1.157        237        704: 100%|██████████| 60/60 [00:23<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  3.91it/s]
                   all          2         62      0.489      0.674      0.615      0.269

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     19/200      5.88G       1.16      1.638      1.167        190        640: 100%|██████████| 60/60 [00:23<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.02it/s]
                   all          2         62      0.451      0.935      0.814       0.42
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     20/200      6.03G      1.165      1.667      1.165        197        928: 100%|██████████| 60/60 [00:23<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.52it/s]
                   all          2         62      0.426      0.957      0.895      0.445

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     21/200      6.14G      1.159      1.623      1.134        270        832: 100%|██████████| 60/60 [00:22<00:00,  2.65it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.50it/s]
                   all          2         62      0.376      0.859      0.733      0.365
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     22/200      5.45G      1.194      1.624       1.16        263        480: 100%|██████████| 60/60 [00:23<00:00,  2.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.58it/s]
                   all          2         62      0.616      0.809      0.885      0.437
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     23/200      5.52G      1.169      1.568      1.132        127        736: 100%|██████████| 60/60 [00:16<00:00,  3.75it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.39it/s]
                   all          2         62      0.688      0.674      0.856      0.419

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     24/200      5.59G      1.146      1.522      1.102        312        480: 100%|██████████| 60/60 [00:08<00:00,  7.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.72it/s]
                   all          2         62      0.555      0.776      0.851      0.435
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     25/200      5.69G      1.136      1.505      1.148        245        672: 100%|██████████| 60/60 [00:09<00:00,  6.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.70it/s]
                   all          2         62      0.571      0.868      0.878      0.444

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     26/200      5.84G      1.158      1.498      1.133        384        544: 100%|██████████| 60/60 [00:09<00:00,  6.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 20.23it/s]
                   all          2         62      0.737      0.677      0.774      0.377
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     27/200      6.05G      1.133      1.466      1.111        212        960: 100%|██████████| 60/60 [00:08<00:00,  7.03it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.18it/s]
                   all          2         62      0.676       0.79      0.889      0.426

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     28/200      5.54G      1.151      1.502      1.144        339        416: 100%|██████████| 60/60 [00:08<00:00,  7.06it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.49it/s]
                   all          2         62      0.722      0.647      0.873      0.415
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     29/200      5.54G      1.139      1.473      1.128        346        672: 100%|██████████| 60/60 [00:09<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 37.73it/s]
                   all          2         62      0.662      0.777      0.854      0.435

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     30/200      5.96G      1.126      1.465      1.111        331        480: 100%|██████████| 60/60 [00:08<00:00,  6.90it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.674      0.826      0.952       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     31/200      5.82G      1.106      1.392      1.115        270        576: 100%|██████████| 60/60 [00:09<00:00,  6.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.93it/s]
                   all          2         62      0.576      0.781      0.828      0.403

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     32/200      5.43G      1.123      1.439       1.15        315        704: 100%|██████████| 60/60 [00:09<00:00,  6.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.24it/s]
                   all          2         62      0.858      0.628      0.835      0.373

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     33/200      5.98G      1.133      1.443      1.121        274        320: 100%|██████████| 60/60 [00:08<00:00,  6.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.514      0.957      0.863       0.41
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     34/200      5.58G       1.12      1.391      1.125        220        960: 100%|██████████| 60/60 [00:09<00:00,  6.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 37.73it/s]
                   all          2         62      0.589      0.792      0.762      0.334
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     35/200      5.75G      1.156      1.455      1.145        220        672: 100%|██████████| 60/60 [00:08<00:00,  7.04it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.05it/s]
                   all          2         62      0.685      0.734      0.915      0.455

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     36/200      5.67G      1.151      1.428      1.123        197        352: 100%|██████████| 60/60 [00:08<00:00,  6.88it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.686      0.902      0.939      0.465
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     37/200      5.93G      1.168      1.432      1.159        263        896: 100%|██████████| 60/60 [00:09<00:00,  6.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.81it/s]
                   all          2         62      0.767      0.826      0.944       0.47

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     38/200      5.97G      1.134      1.417      1.126        238        672: 100%|██████████| 60/60 [00:08<00:00,  6.92it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.22it/s]
                   all          2         62       0.67      0.817      0.937      0.464
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     39/200      5.38G      1.088      1.339      1.111        260        544: 100%|██████████| 60/60 [00:08<00:00,  7.09it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 36.35it/s]
                   all          2         62      0.832      0.814       0.94      0.453
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/200       5.8G      1.116      1.321      1.136        248        704: 100%|██████████| 60/60 [00:09<00:00,  6.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.33it/s]
                   all          2         62      0.815      0.865      0.952      0.478
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     41/200       5.9G      1.121      1.326      1.129        215        320: 100%|██████████| 60/60 [00:09<00:00,  6.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.727      0.845      0.935      0.482
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     42/200      6.01G      1.116      1.394      1.145        311        608: 100%|██████████| 60/60 [00:10<00:00,  5.95it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.73it/s]
                   all          2         62      0.669      0.832      0.915       0.43

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     43/200      6.08G      1.114      1.326      1.114        184        768: 100%|██████████| 60/60 [00:08<00:00,  6.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.78it/s]
                   all          2         62      0.774      0.897      0.952      0.488

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     44/200      5.53G      1.084      1.287      1.102        207        864: 100%|██████████| 60/60 [00:09<00:00,  6.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 40.02it/s]
                   all          2         62      0.699      0.813      0.878      0.466
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     45/200      5.58G      1.101       1.32      1.117        197        544: 100%|██████████| 60/60 [00:08<00:00,  6.74it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.65it/s]
                   all          2         62      0.697      0.841       0.92      0.444
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     46/200      5.68G      1.102       1.35      1.127        209        960: 100%|██████████| 60/60 [00:10<00:00,  5.84it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.49it/s]
                   all          2         62      0.728      0.766      0.936      0.484
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     47/200      5.81G        1.1      1.325      1.109        233        864: 100%|██████████| 60/60 [00:09<00:00,  6.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.24it/s]
                   all          2         62      0.669      0.935      0.931      0.453

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/200      5.37G      1.078      1.273      1.077        291        576: 100%|██████████| 60/60 [00:08<00:00,  6.82it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.30it/s]
                   all          2         62      0.691      0.893      0.935      0.466
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/200      5.48G       1.08      1.281      1.096        348        928: 100%|██████████| 60/60 [00:08<00:00,  7.05it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.06it/s]
                   all          2         62      0.657      0.902      0.907      0.446

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/200      5.59G      1.104      1.333      1.126        216        832: 100%|██████████| 60/60 [00:08<00:00,  6.88it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.741      0.851       0.92       0.46
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/200      6.15G      1.086      1.292      1.096        176        416: 100%|██████████| 60/60 [00:08<00:00,  6.81it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.79it/s]
                   all          2         62      0.679      0.938      0.935      0.472

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/200      5.56G      1.083       1.27       1.09        232        768: 100%|██████████| 60/60 [00:08<00:00,  6.86it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.65it/s]
                   all          2         62      0.802      0.856      0.936      0.444
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     53/200      5.52G      1.078      1.265      1.104        195        544: 100%|██████████| 60/60 [00:08<00:00,  7.03it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.25it/s]
                   all          2         62      0.792      0.944      0.952      0.491
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     54/200      5.79G      1.085       1.26      1.117        279        544: 100%|██████████| 60/60 [00:09<00:00,  6.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.67it/s]
                   all          2         62      0.712      0.913      0.932      0.488

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     55/200      5.98G      1.048      1.172      1.074        138        896: 100%|██████████| 60/60 [00:09<00:00,  6.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.01it/s]
                   all          2         62      0.821      0.876      0.934      0.471

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     56/200      5.25G      1.088      1.268      1.118        331        544: 100%|██████████| 60/60 [00:09<00:00,  6.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.75it/s]
                   all          2         62      0.823      0.893      0.952      0.476

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     57/200      5.91G      1.068      1.202      1.098        196        640: 100%|██████████| 60/60 [00:09<00:00,  6.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.64it/s]
                   all          2         62      0.731      0.917      0.923       0.46
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     58/200       5.9G      1.063      1.209      1.081        181        448: 100%|██████████| 60/60 [00:09<00:00,  6.43it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.12it/s]
                   all          2         62      0.769      0.913      0.952      0.493

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     59/200      5.38G      1.084      1.254      1.098        253        704: 100%|██████████| 60/60 [00:09<00:00,  6.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.77it/s]
                   all          2         62      0.695      0.859       0.92      0.454
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     60/200      5.39G      1.046       1.19      1.093        310        480: 100%|██████████| 60/60 [00:08<00:00,  6.82it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.74it/s]
                   all          2         62      0.753      0.902      0.952      0.465

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     61/200       5.6G      1.064      1.199      1.095        265        544: 100%|██████████| 60/60 [00:09<00:00,  6.27it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 17.50it/s]
                   all          2         62      0.778      0.895      0.952      0.471
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     62/200      5.55G      1.095      1.272      1.117        242        800: 100%|██████████| 60/60 [00:09<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.778       0.87      0.952       0.49

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     63/200      6.03G      1.043      1.182      1.075        359        864: 100%|██████████| 60/60 [00:08<00:00,  6.71it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.33it/s]
                   all          2         62      0.656       0.87       0.92      0.474
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     64/200      5.83G      1.082      1.247      1.109        185        672: 100%|██████████| 60/60 [00:09<00:00,  6.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62       0.81      0.902      0.943      0.481

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     65/200      5.68G      1.042      1.151      1.091        261        352: 100%|██████████| 60/60 [00:09<00:00,  6.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 20.61it/s]
                   all          2         62       0.82      0.901      0.947      0.492
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     66/200      5.53G      1.068      1.145      1.072        163        800: 100%|██████████| 60/60 [00:09<00:00,  6.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.72it/s]
                   all          2         62      0.707      0.957      0.952      0.475
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     67/200      6.14G      1.033      1.116      1.083        493        544: 100%|██████████| 60/60 [00:09<00:00,  6.18it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.87it/s]
                   all          2         62      0.766      0.913      0.952      0.477

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     68/200      5.97G      1.045      1.125      1.093        255        544: 100%|██████████| 60/60 [00:09<00:00,  6.03it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.38it/s]
                   all          2         62       0.83      0.939      0.952      0.476
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     69/200       5.6G      1.061      1.194      1.083        169        544: 100%|██████████| 60/60 [00:08<00:00,  7.00it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.00it/s]
                   all          2         62      0.877      0.818      0.944      0.467
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     70/200      5.72G      1.043      1.134      1.106        391        928: 100%|██████████| 60/60 [00:10<00:00,  5.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.48it/s]
                   all          2         62      0.774      0.948      0.952      0.484
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     71/200      6.13G      1.032      1.109       1.08        189        640: 100%|██████████| 60/60 [00:09<00:00,  6.06it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.07it/s]
                   all          2         62      0.845      0.913      0.952       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     72/200       5.8G      1.016      1.078       1.07        186        384: 100%|██████████| 60/60 [00:09<00:00,  6.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 37.73it/s]
                   all          2         62      0.823      0.912      0.952      0.509
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     73/200      5.45G      1.038      1.168      1.077        279        896: 100%|██████████| 60/60 [00:08<00:00,  6.85it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.26it/s]
                   all          2         62      0.737      0.932      0.934      0.471

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     74/200       5.5G      1.061      1.161      1.076        228        800: 100%|██████████| 60/60 [00:08<00:00,  6.84it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.21it/s]
                   all          2         62      0.869      0.825      0.952      0.491

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     75/200       5.5G      1.043      1.135      1.085        357        608: 100%|██████████| 60/60 [00:09<00:00,  6.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 18.27it/s]
                   all          2         62       0.76      0.957      0.952      0.488

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     76/200      5.54G      1.029      1.092      1.092        363        672: 100%|██████████| 60/60 [00:09<00:00,  6.09it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.64it/s]
                   all          2         62      0.754      0.913      0.952      0.488
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     77/200      5.78G      1.056      1.147      1.078        263        640: 100%|██████████| 60/60 [00:09<00:00,  6.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.09it/s]
                   all          2         62       0.72      0.947      0.941       0.49
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     78/200      6.08G      1.036      1.155      1.075        265        480: 100%|██████████| 60/60 [00:09<00:00,  6.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.98it/s]
                   all          2         62      0.822      0.836      0.948      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     79/200      6.09G      1.027      1.067      1.067        238        800: 100%|██████████| 60/60 [00:09<00:00,  6.11it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 39.30it/s]
                   all          2         62      0.759       0.91      0.952      0.473

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     80/200      6.11G      1.032      1.107      1.076        188        672: 100%|██████████| 60/60 [00:09<00:00,  6.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.78it/s]
                   all          2         62      0.777      0.894      0.938      0.454
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     81/200      5.79G      1.049      1.104      1.099        302        896: 100%|██████████| 60/60 [00:09<00:00,  6.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 36.60it/s]
                   all          2         62      0.787      0.886       0.94      0.451
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     82/200      5.76G      1.033      1.121      1.076        314        672: 100%|██████████| 60/60 [00:09<00:00,  6.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.24it/s]
                   all          2         62      0.847      0.848      0.942      0.489

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     83/200      5.81G      1.056      1.175      1.118        323        640: 100%|██████████| 60/60 [00:09<00:00,  6.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.89it/s]
                   all          2         62      0.821      0.865      0.952      0.472
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     84/200      5.58G      1.045      1.154      1.093        266        704: 100%|██████████| 60/60 [00:09<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.94it/s]
                   all          2         62      0.783      0.946      0.937      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     85/200      5.81G      1.056      1.121      1.071        225        544: 100%|██████████| 60/60 [00:08<00:00,  6.88it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.26it/s]
                   all          2         62      0.744      0.946      0.942      0.469

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     86/200      5.63G      1.042      1.148      1.088        326        544: 100%|██████████| 60/60 [00:09<00:00,  6.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.69it/s]
                   all          2         62      0.818      0.946      0.952      0.495
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     87/200      5.37G       1.04      1.084      1.055        315        608: 100%|██████████| 60/60 [00:08<00:00,  7.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 17.39it/s]
                   all          2         62      0.708      0.942      0.952      0.484

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     88/200      5.65G       1.02      1.103      1.074        183        640: 100%|██████████| 60/60 [00:08<00:00,  6.74it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 20.19it/s]
                   all          2         62      0.765      0.945      0.952      0.483
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     89/200      5.73G      1.007       1.11      1.089        277        832: 100%|██████████| 60/60 [00:09<00:00,  6.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.90it/s]
                   all          2         62      0.798      0.941      0.952      0.491

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     90/200       5.4G      1.038      1.113      1.075        187        480: 100%|██████████| 60/60 [00:08<00:00,  6.75it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.74it/s]
                   all          2         62      0.884      0.907      0.952      0.473
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     91/200      5.65G      1.038      1.093       1.07        160        480: 100%|██████████| 60/60 [00:08<00:00,  6.82it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.715      0.932      0.941      0.481

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     92/200      5.88G      1.013      1.043      1.071        240        928: 100%|██████████| 60/60 [00:08<00:00,  6.75it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.79it/s]
                   all          2         62      0.813      0.853      0.937      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     93/200      5.99G      1.009      1.055      1.061        176        800: 100%|██████████| 60/60 [00:09<00:00,  6.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 19.61it/s]
                   all          2         62      0.795      0.892      0.942      0.476

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     94/200      6.22G      1.002      1.041      1.076        216        512: 100%|██████████| 60/60 [00:10<00:00,  5.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 13.64it/s]
                   all          2         62        0.8      0.944      0.952      0.469

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     95/200      5.56G      1.019      1.059      1.083        302        384: 100%|██████████| 60/60 [00:09<00:00,  6.27it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.05it/s]
                   all          2         62      0.833       0.89      0.952      0.473

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     96/200      5.46G      1.047      1.125      1.078        312        640: 100%|██████████| 60/60 [00:08<00:00,  7.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.29it/s]
                   all          2         62      0.868      0.956      0.952      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     97/200       5.8G      1.021      1.077      1.067        186        640: 100%|██████████| 60/60 [00:08<00:00,  6.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.99it/s]
                   all          2         62      0.894      0.903      0.952      0.499

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     98/200      6.32G      1.021      1.041      1.093        188        320: 100%|██████████| 60/60 [00:10<00:00,  5.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.33it/s]
                   all          2         62      0.746       0.93      0.931      0.483

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     99/200      5.52G      1.014       1.07      1.066        245        480: 100%|██████████| 60/60 [00:08<00:00,  7.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.23it/s]
                   all          2         62      0.796      0.913      0.952      0.494

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    100/200      5.92G     0.9921      1.002      1.056        295        864: 100%|██████████| 60/60 [00:09<00:00,  6.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.00it/s]
                   all          2         62      0.732      0.931      0.944      0.499

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    101/200      5.87G      1.019      1.023      1.083        362        416: 100%|██████████| 60/60 [00:10<00:00,  5.86it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 18.52it/s]
                   all          2         62      0.758      0.891      0.947      0.485
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    102/200       5.1G      1.001      1.019      1.063        263        800: 100%|██████████| 60/60 [00:09<00:00,  6.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.93it/s]
                   all          2         62      0.818      0.894      0.952      0.487

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    103/200      5.83G     0.9926     0.9774      1.069        249        640: 100%|██████████| 60/60 [00:10<00:00,  5.84it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62       0.77      0.943      0.952      0.467

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    104/200      5.98G      1.008      1.026      1.084        332        864: 100%|██████████| 60/60 [00:10<00:00,  5.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.29it/s]
                   all          2         62      0.831      0.854      0.952      0.518
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    105/200      5.62G      0.998      1.018      1.055        223        832: 100%|██████████| 60/60 [00:08<00:00,  6.98it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 14.84it/s]
                   all          2         62      0.719      0.915      0.938      0.464
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    106/200      5.98G      1.006     0.9857      1.067        281        640: 100%|██████████| 60/60 [00:09<00:00,  6.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 37.43it/s]
                   all          2         62      0.827      0.925      0.933      0.494
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    107/200       6.1G      0.997      1.017      1.056        305        640: 100%|██████████| 60/60 [00:09<00:00,  6.15it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.12it/s]
                   all          2         62      0.879      0.816      0.944      0.452
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    108/200      6.15G     0.9888      1.007      1.056        333        832: 100%|██████████| 60/60 [00:09<00:00,  6.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.729      0.942      0.938      0.486
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    109/200       5.2G      1.002      1.002      1.022        276        320: 100%|██████████| 60/60 [00:08<00:00,  7.38it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 19.24it/s]
                   all          2         62      0.759      0.941      0.938      0.455
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    110/200      5.49G     0.9911     0.9822      1.071        223        384: 100%|██████████| 60/60 [00:09<00:00,  6.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.83it/s]
                   all          2         62      0.826      0.915      0.939      0.475

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    111/200      5.36G     0.9937      1.024      1.078        236        416: 100%|██████████| 60/60 [00:09<00:00,  6.34it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.17it/s]
                   all          2         62      0.815      0.909      0.935      0.474

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    112/200      5.45G     0.9815     0.9913      1.049        286        384: 100%|██████████| 60/60 [00:09<00:00,  6.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.42it/s]
                   all          2         62      0.805      0.933      0.931       0.45
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    113/200      6.13G      1.006     0.9794      1.067        218        416: 100%|██████████| 60/60 [00:09<00:00,  6.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.791      0.921      0.928      0.476
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    114/200       5.7G     0.9953      1.012      1.075        305        320: 100%|██████████| 60/60 [00:09<00:00,  6.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.99it/s]
                   all          2         62      0.766      0.939      0.936      0.495

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    115/200      5.86G      1.003      1.032      1.077        145        512: 100%|██████████| 60/60 [00:09<00:00,  6.15it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.76it/s]
                   all          2         62      0.825      0.893       0.93      0.484
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    116/200      5.39G     0.9971     0.9972      1.053        242        320: 100%|██████████| 60/60 [00:08<00:00,  6.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.22it/s]
                   all          2         62      0.772      0.936      0.936      0.496

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    117/200      5.68G     0.9799     0.9625      1.052        162        672: 100%|██████████| 60/60 [00:09<00:00,  6.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.57it/s]
                   all          2         62       0.83       0.94      0.944      0.483

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    118/200      5.71G     0.9887     0.9772      1.069        229        832: 100%|██████████| 60/60 [00:09<00:00,  6.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.44it/s]
                   all          2         62      0.778      0.935      0.929      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    119/200      5.52G     0.9819     0.9599      1.062        296        480: 100%|██████████| 60/60 [00:09<00:00,  6.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.57it/s]
                   all          2         62      0.836      0.946      0.935      0.473
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    120/200      5.42G      0.971     0.9266      1.068        265        672: 100%|██████████| 60/60 [00:10<00:00,  5.90it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.78it/s]
                   all          2         62      0.817      0.875      0.928      0.454

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    121/200      5.15G     0.9684     0.9273      1.038        328        960: 100%|██████████| 60/60 [00:09<00:00,  6.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.11it/s]
                   all          2         62      0.808      0.941      0.952       0.49

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    122/200      5.76G       1.01     0.9926      1.059        222        896: 100%|██████████| 60/60 [00:09<00:00,  6.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.29it/s]
                   all          2         62      0.877      0.888      0.937       0.47

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    123/200      5.45G     0.9873     0.9788      1.058        204        864: 100%|██████████| 60/60 [00:09<00:00,  6.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.03it/s]
                   all          2         62       0.81      0.906      0.933      0.477
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    124/200      5.78G     0.9835     0.9388      1.053        290        576: 100%|██████████| 60/60 [00:09<00:00,  6.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.78it/s]
                   all          2         62      0.776      0.924      0.933      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    125/200      6.21G      0.996     0.9861       1.07        237        448: 100%|██████████| 60/60 [00:09<00:00,  6.09it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.93it/s]
                   all          2         62      0.828      0.923      0.936      0.481

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    126/200      5.24G     0.9736     0.9548      1.043        187        672: 100%|██████████| 60/60 [00:09<00:00,  6.48it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.852      0.917      0.937      0.493

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    127/200      5.49G     0.9811     0.9652      1.055        167        352: 100%|██████████| 60/60 [00:09<00:00,  6.34it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.66it/s]
                   all          2         62      0.861      0.929      0.937      0.487

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    128/200      5.67G     0.9861     0.9498       1.05        371        352: 100%|██████████| 60/60 [00:09<00:00,  6.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.849      0.935      0.947      0.494

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    129/200      5.52G     0.9668     0.9326      1.046        198        960: 100%|██████████| 60/60 [00:09<00:00,  6.34it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 36.77it/s]
                   all          2         62      0.734      0.946      0.943      0.486
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    130/200      5.38G     0.9523     0.9081       1.04        150        512: 100%|██████████| 60/60 [00:09<00:00,  6.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.12it/s]
                   all          2         62      0.855      0.864      0.944      0.487

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    131/200      5.67G     0.9759     0.9707       1.05        272        640: 100%|██████████| 60/60 [00:09<00:00,  6.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 36.46it/s]
                   all          2         62      0.838      0.903       0.94      0.468

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    132/200      5.37G     0.9757     0.9495      1.026        194        672: 100%|██████████| 60/60 [00:08<00:00,  7.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.72it/s]
                   all          2         62      0.821      0.946       0.94      0.485

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    133/200      5.94G     0.9578     0.9148      1.053        231        320: 100%|██████████| 60/60 [00:10<00:00,  5.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.79it/s]
                   all          2         62      0.804      0.925      0.935       0.47

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    134/200      5.67G     0.9598     0.9144      1.049        257        736: 100%|██████████| 60/60 [00:09<00:00,  6.26it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 20.78it/s]
                   all          2         62      0.885      0.941      0.944      0.491
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    135/200      5.88G      0.976     0.9319       1.03        176        960: 100%|██████████| 60/60 [00:09<00:00,  6.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.98it/s]
                   all          2         62       0.81      0.949      0.944       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    136/200      5.68G     0.9728     0.9466      1.042        254        672: 100%|██████████| 60/60 [00:09<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.33it/s]
                   all          2         62      0.881      0.895      0.931      0.471

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    137/200      5.08G     0.9564     0.9223      1.013        333        512: 100%|██████████| 60/60 [00:07<00:00,  7.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 18.77it/s]
                   all          2         62      0.831      0.946      0.939       0.48
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    138/200      5.64G     0.9693     0.9208      1.028        229        800: 100%|██████████| 60/60 [00:09<00:00,  6.34it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.42it/s]
                   all          2         62      0.881      0.947      0.941      0.485

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    139/200      5.81G     0.9398     0.8734       1.03        221        320: 100%|██████████| 60/60 [00:09<00:00,  6.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.67it/s]
                   all          2         62      0.821      0.876      0.922      0.459
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    140/200      6.26G     0.9731     0.9478      1.065        236        928: 100%|██████████| 60/60 [00:09<00:00,  6.10it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.61it/s]
                   all          2         62      0.747      0.939      0.942       0.49

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    141/200      5.58G      0.947     0.8999       1.05        276        608: 100%|██████████| 60/60 [00:10<00:00,  5.95it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.29it/s]
                   all          2         62      0.792      0.927      0.932       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    142/200      5.66G     0.9521     0.9091       1.04        225        448: 100%|██████████| 60/60 [00:09<00:00,  6.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.78it/s]
                   all          2         62      0.802      0.943      0.943      0.451
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    143/200      5.58G     0.9572     0.8712      1.039        295        704: 100%|██████████| 60/60 [00:09<00:00,  6.18it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.33it/s]
                   all          2         62      0.786      0.935      0.934      0.453

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    144/200      5.38G     0.9496     0.8755      1.024        299        320: 100%|██████████| 60/60 [00:09<00:00,  6.31it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.45it/s]
                   all          2         62      0.846      0.879      0.932      0.462
EarlyStopping: Training stopped early as no improvement observed in last 40 epochs. Best results observed at epoch 104, best model saved as best.pt.
To update EarlyStopping(patience=40) pass a new patience value, i.e. `patience=300` or use `patience=0` to disable EarlyStopping.

144 epochs completed in 0.460 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200\weights\last.pt, 19.3MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200\weights\best.pt, 19.3MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200\weights\best.pt...
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11s summary (fused): 100 layers, 9,483,234 parameters, 0 gradients, 21.7 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.05it/s]
                   all          2         62      0.862      0.913      0.952      0.523
           API-Gateway          2          4      0.918          1      0.995      0.351
               Amplify          2          2          1          1      0.995      0.497
               Appsync          2          2       0.87          1      0.995      0.497
                Athena          2          2      0.836          1      0.995      0.298
                   CUR          2          2      0.871          1      0.995      0.456
            Cloudfront          2          2      0.851          1      0.995      0.398
             CodeBuild          2          2      0.874          1      0.995      0.724
          CodePipeline          2          2      0.893          1      0.995      0.298
               Cognito          2          2          0          0          0          0
                Config          2          2          1          1      0.995      0.535
             Dynamo DB          2          2      0.472          1      0.995      0.457
Elastic Container Registry          2          2      0.937          1      0.995      0.748
Elastic Container Service          2          2      0.837          1      0.995      0.453
        Elastic Search          2          2      0.923          1      0.995      0.796
               Fargate          2          2      0.913          1      0.995      0.429
                 Image          2          2          1          1      0.995      0.796
                Lambda          2          8      0.932          1      0.995      0.442
               Neptune          2          2          1          0      0.995      0.497
        Private Subnet          2          2      0.945          1      0.995      0.548
                    S3          2         10      0.963          1      0.995       0.31
                   SDK          2          2      0.988          1      0.995      0.796
                 Users          2          2      0.867          1      0.995      0.895
                   aws          2          2      0.926          1      0.995      0.796
Speed: 0.2ms preprocess, 73.3ms inference, 0.0ms loss, 1.2ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_200\weights\best.pt
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11s summary (fused): 100 layers, 9,483,234 parameters, 0 gradients, 21.7 GFLOPs
val: Fast image access  (ping: 0.20.1 ms, read: 91.615.5 MB/s, size: 73.3 KB)
WARNING Box and segment counts should be equal, but got len(segments) = 233, len(boxes) = 426. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache... 21 images, 0 backgrounds, 0 corrupt: 100%|██████████| 21/21 [00:00<?, ?it/s]
                                           0% | 0.00/18.41 MB [00:00<?, ?MB/s]: 
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   0%|          | 0/3 [00:00<?, ?it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  33%|███▎      | 1/3 [00:00<00:00,  3.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  67%|██████▋   | 2/3 [00:00<00:00,  4.05it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 3/3 [00:00<00:00,  4.42it/s]
                   all         21        426       0.47      0.317      0.318      0.257
                   ACM          1          1          1          0          0          0
                   ALB          5          5      0.351        0.4      0.205      0.185
Active Directory Service          1          1          0          0          0          0
                Athena          1          1      0.463          1      0.995      0.796
                Aurora          4          7          0          0          0          0
          Auto Scaling          4          8      0.405       0.25      0.218      0.163
                   CDN          1          1          1          0      0.995      0.796
   Certificate Manager          1          1          1          0          0          0
          Cloud Search          1          1          1          0          0          0
           Cloud Trail          2          3      0.328      0.667      0.229       0.16
           Cloud Watch          5          7      0.583      0.857      0.757      0.704
  CloudFormation Stack          1          1      0.671          1      0.995      0.895
              CloudHSM          1          1          1          0          0          0
            Cloudfront          9          9      0.114      0.111      0.103     0.0871
             CodeBuild          1          1      0.809          1      0.995      0.796
            CodeCommit          1          1      0.782          1      0.995      0.995
            CodeDeploy          1          1          1          1      0.995      0.796
               Cognito          1          1          0          0          0          0
                Config          1          6          0          0          0          0
             Container          1          1      0.757          1      0.995      0.697
             Detective          1          1          0          0          0          0
        Direct Connect          4         11      0.872      0.818      0.821      0.543
          Distribution          2          2          0          0          0          0
          Docker Image          1          2          1          0     0.0396     0.0278
             Dynamo DB          8         19      0.842      0.579      0.741      0.587
                   EBS          3          4      0.449       0.25      0.134      0.067
                   EC2         13         40      0.647      0.367      0.386      0.283
                   EFS          5          5      0.155      0.124     0.0614     0.0491
      EFS Mount Target          4          9      0.472      0.401       0.41      0.306
                   ELB         10         13      0.447      0.154      0.368      0.276
                   EMR          1          1          0          0          0          0
         Edge Location          1          3          0          0          0          0
           ElastiCache          3          5      0.515      0.218      0.295      0.215
Elastic Container Service          1          2      0.853          1      0.995      0.895
        Elastic Search          1          1          1          0     0.0711     0.0426
Elemental MediaConvert          1          1      0.468          1      0.995      0.796
Elemental MediaPackage          1          1          0          0          0          0
                 Email          1          1          1          0          0          0
           EventBridge          1          5          1          0          0          0
      Firewall Manager          1          1          0          0          0          0
             Flow logs          1          4          0          0          0          0
               Glacier          1          1          0          0          0          0
                  Glue          1          2      0.806          1      0.995      0.801
             GuardDuty          1          5          1          0          0          0
                   IAM          2          9      0.247      0.111      0.109     0.0623
              IAM Role          2          7      0.436      0.286      0.153     0.0469
              IOT Core          1          1      0.732          1      0.995      0.895
       Inspector Agent          1          1          0          0          0          0
              Internet          7          8      0.345      0.265       0.22      0.174
      Internet Gateway          3          4          0          0          0          0
Key Management Service          2          3          0          0          0          0
  Kinesis Data Streams          2          4      0.716          1      0.945      0.754
                Lambda          4         10      0.643        0.8      0.649      0.542
                 Macie          2          4      0.607       0.25      0.272      0.218
             Memcached          1          2          0          0          0          0
         Mobile Client          1          4      0.923          1      0.995      0.871
           NAT Gateway          4          8          0          0          0          0
      Network Firewall          1          1          0          0          0          0
    Organization Trail          1          4          0          0          0          0
        Private Subnet          3         10          0          0      0.014      0.007
         Public Subnet          6         18      0.686      0.124      0.289      0.206
                   RDS          6         14      0.456       0.36       0.34      0.275
                 Redis          1          1      0.416          1      0.995      0.796
              Redshift          1          1          1          0      0.995      0.895
                Region          2          2          0          0          0          0
              Route 53          1          1          1          0          0          0
               Route53          9          9      0.414      0.316      0.182      0.147
                    S3         17         24      0.497      0.417      0.319      0.248
                   SDK          1          1      0.363          1      0.497      0.348
                   SES          2          2          0          0          0          0
                   SNS          3          3      0.606      0.667      0.672      0.605
                   SQS          2          2      0.402        0.5      0.502      0.452
             SSM Agent          1          1          0          0          0          0
        Secret Manager          1          1          1          0          0          0
        Security Group          1          1          0          0          0          0
          Security Hub          1          5          1          0          0          0
                Server          4         12      0.382      0.333      0.325      0.207
                Shield          1          1          1          0          0          0
               Sign-On          1          1          0          0          0          0
              Snowball          1          1          0          0          0          0
         Step Function          1          3       0.88          1      0.995      0.895
       Storage Gateway          1          1          0          0          0          0
       Systems Manager          1          2          1          0          0          0
                 Users         11         13        0.6      0.615      0.383      0.282
            VP Gateway          1          1       0.48      0.961      0.497      0.448
            VPC Router          2          6      0.629      0.667      0.696      0.584
        VPN Connection          1          1      0.867          1      0.995      0.597
                   WAF          1          1          0          0          0          0
           Web Clients          2          7      0.494      0.143      0.148      0.133
                   aws         11         13      0.726      0.538      0.623       0.45
Speed: 1.4ms preprocess, 24.4ms inference, 0.0ms loss, 0.9ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val2\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val2

🎯 Test Metrics (mean per class):
  Precision:    0.470
  Recall:       0.317
  mAP@0.5:      0.318
  mAP@0.5:0.95: 0.257

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 1 Dynamo DB, 5 Lambdas, 1 S3, 1 SNS, 2 Userss, 1 aws, 63.0ms
Speed: 2.5ms preprocess, 63.0ms inference, 2.5ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict\labels
✅ Detailed JSON saved to data\reports\yolo11s_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11s_custom_200\report.json
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'ACM', 1: 'ALB', 2: 'AMI', 3: 'API-Gateway', 4: 'Active Directory Service', 5: 'Airflow_', 6: 'Amplify', 7: 'Analytics Services', 8: 'AppFlow', 9: 'Appsync', 10: 'Athena', 11: 'Aurora', 12: 'Auto Scaling', 13: 'Auto Scaling Group', 14: 'Automated Tests', 15: 'Availability Zone', 16: 'Backup', 17: 'Build Environment', 18: 'CDN', 19: 'CUR', 20: 'Call Metrics', 21: 'Call Recordings', 22: 'Certificate Manager', 23: 'Client', 24: 'Cloud Connector', 25: 'Cloud Map', 26: 'Cloud Search', 27: 'Cloud Trail', 28: 'Cloud Watch', 29: 'CloudFormation Stack', 30: 'CloudHSM', 31: 'CloudWatch Alarm', 32: 'Cloudfront', 33: 'CodeBuild', 34: 'CodeCommit', 35: 'CodeDeploy', 36: 'CodePipeline', 37: 'Cognito', 38: 'Comprehend', 39: 'Config', 40: 'Connect', 41: 'Connect Contact Lens', 42: 'Container', 43: 'Control Tower', 44: 'Customer Gateway', 45: 'DSI', 46: 'Data Pipeline', 47: 'DataSync', 48: 'Deploy Stage', 49: 'Detective', 50: 'Direct Connect', 51: 'Distribution', 52: 'Docker Image', 53: 'Dynamo DB', 54: 'EBS', 55: 'EC2', 56: 'EFS', 57: 'EFS Mount Target', 58: 'EKS', 59: 'ELB', 60: 'EMR', 61: 'Edge Location', 62: 'ElastiCache', 63: 'Elastic Container Registry', 64: 'Elastic Container Service', 65: 'Elastic Search', 66: 'Elemental MediaConvert', 67: 'Elemental MediaPackage', 68: 'Email', 69: 'Endpoint', 70: 'Event Bus', 71: 'EventBridge', 72: 'Experiment Duration', 73: 'Experiments', 74: 'Fargate', 75: 'Fault Injection Simulator', 76: 'Firewall Manager', 77: 'Flask', 78: 'Flow logs', 79: 'GameLift', 80: 'Git', 81: 'Github', 82: 'Glacier', 83: 'Glue', 84: 'Glue DataBrew', 85: 'Grafana', 86: 'GuardDuty', 87: 'IAM', 88: 'IAM Role', 89: 'IOT Core', 90: 'Image', 91: 'Image Builder', 92: 'Ingress', 93: 'Inspector Agent', 94: 'Instances', 95: 'Internet', 96: 'Internet Gateway', 97: 'Jenkins', 98: 'Key Management Service', 99: 'Kibana', 100: 'Kinesis Data Streams', 101: 'Kubernetes', 102: 'Lambda', 103: 'Lex', 104: 'MQ', 105: 'Machine Learning', 106: 'Macie', 107: 'Marketplace', 108: 'Memcached', 109: 'Mobile Client', 110: 'Mongo DB', 111: 'MySQL', 112: 'NAT Gateway', 113: 'Neptune', 114: 'Network Adapter', 115: 'Network Firewall', 116: 'Notebook', 117: 'Order Controller', 118: 'Organization Trail', 119: 'Parameter Store', 120: 'Pinpoint', 121: 'PostgreSQL', 122: 'Private Link', 123: 'Private Subnet', 124: 'Prometheus', 125: 'Public Subnet', 126: 'Quarkus', 127: 'Quicksight', 128: 'RDS', 129: 'React', 130: 'Redis', 131: 'Redshift', 132: 'Region', 133: 'Rekognition', 134: 'Results', 135: 'Route 53', 136: 'Route53', 137: 'S3', 138: 'SAR', 139: 'SDK', 140: 'SES', 141: 'SNS', 142: 'SQS', 143: 'SSM Agent', 144: 'Sagemaker', 145: 'Secret Manager', 146: 'Security Group', 147: 'Security Hub', 148: 'Server', 149: 'Service Catalog', 150: 'Shield', 151: 'Sign-On', 152: 'Slack', 153: 'Snowball', 154: 'Stack', 155: 'Step Function', 156: 'Storage Gateway', 157: 'SwaggerHub', 158: 'Systems Manager', 159: 'TV', 160: 'Table', 161: 'Task Runner', 162: 'Terraform', 163: 'Text File', 164: 'Textract', 165: 'Transcribe', 166: 'Transfer Family', 167: 'Transit Gateway', 168: 'Translate', 169: 'Trusted Advisor', 170: 'Twilio', 171: 'Users', 172: 'VDA', 173: 'VP Gateway', 174: 'VPC Router', 175: 'VPN Connection', 176: 'WAF', 177: 'Web Clients', 178: 'Websites', 179: 'X-Ray', 180: 'aws', 181: 'cache Worker'}
obb: None
orig_img: array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [ 39,  34,  33],
        [ 62,  55,  52],
        [ 54,  45,  42]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 254],
        [235, 228, 225],
        [ 67,  58,  55]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 254],
        [255, 255, 252],
        [ 41,  32,  29]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 248],
        [255, 255, 249],
        [ 49,  43,  36]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 248],
        [247, 239, 232],
        [ 53,  47,  40]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [ 44,  36,  29],
        [ 90,  80,  73],
        [ 51,  43,  36]]], dtype=uint8)
orig_shape: (597, 744)
path: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_01.jpg'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict'
speed: {'preprocess': 2.53950001206249, 'inference': 63.011799938976765, 'postprocess': 2.5047999806702137}]
███████████████████████████████ 100% | 18.41/18.41 MB [01:29<00:00,  4.88s/MB]: 

Process finished with exit code 0
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

```
