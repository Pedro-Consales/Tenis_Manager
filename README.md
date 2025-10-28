# 🎾 Tenis_Manager

> Sistema de gerenciamento para quadras de tênis - Desenvolvido como projeto acadêmico na PUC-Rio

## 📋 Sobre o Projeto

Sistema web desenvolvido em django para auxílio de um gerente da quadras de tênis de um clube esportivo no Rio de Janeiro

### ✨ Funcionalidades Principais
- [ ] Cadastro de jogadores
- [ ] Reserva de quadras
- [ ] Controle de horários
- [ ] [Adicione suas funcionalidades aqui]

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8+ instalado
- pip (gerenciador de pacotes do Python)

### 1️⃣ Instalação das Dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Executar o Servidor
```bash
python manage.py runserver
```

### 3️⃣ Acessar o Sistema
Abra seu navegador e acesse: `http://localhost:8000`

## 📁 Estrutura do Projeto

```
Tenis_Manager/
├── 📄 manage.py                 # Script principal do Django (como um "botão de ligar")
├── 📄 requirements.txt          # Lista de bibliotecas necessárias (como uma "lista de compras")
├── 📄 db.sqlite3                # Banco de dados (onde ficam guardados os dados)
├── 📂 tenis_prjct/              # Pasta principal do projeto (o "cérebro" do sistema)
│   ├── 📄 settings.py           # Configurações gerais (como um "painel de controle")
│   ├── 📄 urls.py               # Rotas principais (como um "mapa de navegação")
│   └── 📄 wsgi.py               # Configuração do servidor web
├── 📂 mainapp_tenis/            # Pasta com as funcionalidades (como "departamentos")
│   │── 📄 urls.py               # Rotas específicas desta funcionalidade
│   ├── 📄 models.py             # Define como os dados são organizados
│   ├── 📂 quadras/              # Modulo para gerenciar quadras
│   │   ├── 📄 views_quadras.py  # Lógica de negócio
│   │   └── 📄 admin.py          # Interface de administração
│   ├── 📂 socios/               # Modulo para gerenciar jogadores
│   ├── 📄 views_socios.py       # Lógica de negócio
│   └── 📂 reservas/             # Modulo para gerenciar reservas
├── 📂 templates/                # Páginas HTML (a "cara" do sistema)
├── 📂 static/                   # Arquivos CSS, JS, imagens (o "visual")
└── 📂 media/                    # Uploads de usuários (fotos, documentos)
```

## 🧩 Responsabilidades dos Arquivos

### 🎯 Arquivos Principais
| Arquivo | O que faz | Analogia |
|---------|-----------|----------|
| `manage.py` | Executa comandos do Django | Como um controle remoto do sistema |
| `settings.py` | Configurações do projeto | Painel de controle de um carro |
| `urls.py` | Define as rotas/caminhos | GPS que direciona para onde ir |
| `models.py` | Estrutura dos dados | Planta baixa de como organizar as informações |
| `views.py` | Lógica de cada página | Chef que processa os pedidos |
| `templates/` | Interface visual | Vitrines de uma loja |

### 📱 Modulos (Funcionalidades)
- **quadras/**: Tudo relacionado às quadras de tênis
- **jogadores/**: Cadastro e gerenciamento de jogadores  
- **reservas/**: Sistema de reservas e agendamentos
- **[adicione seus apps aqui]**

## 🛠️ Tecnologias Utilizadas e Não Utlizadads
- **Django**: Framework web Python
- **SQLite**: NÃO vamos utilizar banco de dados (requisito da disciplina)
- **HTML/CSS/JavaScript**: Interface do usuário (Tailwind/Bootstrap)
- **Tailwind/Bootstrap**: Framework CSS (se estiver usando)

## 👨‍💻 Desenvolvido por
Pedro Consales Margaronis - Estudante de Ciência da Computação - PUC-Rio
Julia Pareto - Estudante de Ciência da Computação - PUC-Rio
Lucas Thurler - Estudante de Ciência da Computação - PUC-Rio


## 📝 Comandos Úteis

```bash
# Criar migrações (quando alterar models.py que não será utilizado)
python manage.py makemigrations

# Aplicar migrações no banco (também não será utilizado)
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Acessar shell do Django
python manage.py shell
```

## 🎓 Aprendizados
[Compartilhe aqui o que você aprendeu desenvolvendo este projeto]

---
**📚 Projeto desenvolvido como parte dos estudos em Ciência da Computação na PUC-Rio**











# 🗂️ Guia da Estrutura Django - Tenis_Manager

## 🏗️ Analogia Geral: Django como um Prédio Comercial

Imagine o Django como um **prédio comercial** onde cada andar tem uma função específica:

### 🏢 Estrutura do "Prédio" Django

```
🏢 Tenis_Manager (O Prédio)
├── 🚪 manage.py (Portaria Principal)
├── 📋 requirements.txt (Lista de Fornecedores)
├── 🗄️ db.sqlite3 (Arquivo Central)
│
├── 🏛️ tenis_prjct/ (Administração do Prédio)
│   ├── ⚙️ settings.py (Regulamento Interno)
│   ├── 🗺️ urls.py (Mapa de Localização)
│   └── 🔌 wsgi.py (Sistema Elétrico)
│
├── 🏬 mainapp_tenis/ (Lojas/Departamentos)
│   ├── 🎾 quadras/ (Loja de Equipamentos -> Módulos)
│   ├── 👥 socios/ (Recepção/Cadastro -> Módulos)
│   └── 📅 reservas/ (Central de Agendamentos -> Módulos)
│
├── 🖼️ templates/ (Vitrines e Decoração)
├── 🎨 static/ (Material de Marketing)
└── 📁 media/ (Depósito de Documentos)
```

## 📝 Detalhamento de Cada Arquivo

### 🚪 manage.py - A Portaria
**O que faz**: É o ponto de entrada do sistema
**Analogia**: Como um porteiro que:
- Liga e desliga o sistema (`runserver`)
- Organiza o banco de dados (`migrate`)
- Cria novos usuários administrativos (`createsuperuser`)

### ⚙️ settings.py - O Regulamento Interno
**O que faz**: Define todas as configurações do projeto
**Analogia**: Como o regulamento de um condomínio que define:
- Quais apps estão "autorizados" a funcionar
- Configurações de segurança
- Onde ficam os arquivos
- Configurações do banco de dados

**Principais seções**:
```python
# Lista de "inquilinos" autorizados
INSTALLED_APPS = [
    'django.contrib.admin',
    'mainapp_tenis' #Só teremos um app com várias pastas, módulos.
]

# "Endereço" do banco de dados
DATABASES = {...}

# Configurações de segurança
SECRET_KEY = 'sua-chave-secreta'
```

### 🗺️ urls.py - O Mapa de Localização
**O que faz**: Define para onde cada URL deve levar (Cada url chama uma função da view que executa algo no sistema )
**Analogia**: Como um mapa de shopping que mostra:
- `/admin/` → Vai para a administração 
- `/quadras/` → Vai para a seção de quadras
- `/jogadores/` → Vai para a recepção

**Estrutura típica (urls.py) da pasta tenis_prjct**:
```python
urlpatterns = [
    path('admin/', admin.site.urls),  # Administração
    path('app/', include('mainapp_tenis')),  # App quadras
]
```

## 🏬 Estrutura de um App

Cada app é como uma **loja especializada** no shopping:

### 📊 models.py - A Planta do Estoque
**O que faz**: Define como os dados são organizados
**Analogia**: Como fichas de cadastro que definem:
- Quais informações guardar sobre cada jogador
- Como uma quadra deve ser cadastrada
- Relacionamentos entre os dados

**Exemplo prático (NÃO IREMOS UTILIZAR)**:
```python
class Jogador(models.Model):
    nome = models.CharField(max_length=100)  # Nome na ficha
    email = models.EmailField()              # Contato
    nivel = models.CharField(max_length=20)  # Iniciante/Intermediário/Avançado
```

### 🎭 views.py - Os Vendedores/Atendentes
**O que faz**: Processa as solicitações dos usuários
**Analogia**: Como vendedores que:
- Recebem o pedido do cliente
- Buscam as informações necessárias
- Preparam a resposta
- Entregam o resultado

**Exemplo prático**:
```python
def listar_quadras(request):
    # 1. Cliente pede para ver quadras
    # 2. Vendedor busca no estoque (banco de dados)
    quadras = Quadra.objects.all()
    # 3. Prepara a apresentação (template)
    # 4. Entrega para o cliente
    return render(request, 'quadras/lista.html', {'quadras': quadras})
    #nesse caso retorna um html, mas pode simplemente retornar uma repsosta qualquer ou executar algo internamente
```

### 🗺️ urls.py (do app) - Guia Interno da Loja
**O que faz**: Define as rotas específicas daquele app
**Analogia**: Como placas internas de uma loja:
- `lista/` → Mostra todas as quadras
- `nova/` → Formulário para cadastrar quadra
- `editar/1(id)/` → Editar quadra específica

### 🖼️ templates/ - As Vitrines
**O que faz**: Define como as páginas aparecem para o usuário
**Analogia**: Como vitrines que mostram os produtos de forma atrativa
- `lista.html` → Vitrine com todas as quadras
- `detalhes.html` → Folheto detalhado de uma quadra

## 🎨 Pastas de Recursos

### 🎨 static/ - Material de Marketing
**O que contém**:
- `css/` → Estilos visuais (cores, fontes) TAILWIND FAZ O CSS NO PRÓPRIO HTML
- `js/` → Interatividade (botões, animações) SEM USO NO NOSSO SISTEMA!
- `img/` → Imagens fixas do site

### 📁 media/ - Depósito de Documentos
**O que contém**:
- Fotos enviadas pelos usuários
- Documentos anexados
- Qualquer arquivo "dinâmico"

## 🔄 Fluxo de uma Requisição

**Como funciona quando alguém acessa seu site**:

1. **🚪 Portaria (manage.py)**: Recebe a visita
2. **🗺️ Mapa Principal (urls.py)**: "Você quer ir onde?"
3. **🏬 Loja Específica (app/urls.py)**: "Que seção da nossa loja?"
4. **🎭 Atendente (views.py)**: Processa o pedido
5. **📊 Estoque (models.py)**: Busca os dados necessários
6. **🖼️ Vitrine (template)**: Apresenta o resultado
7. **🚪 Entrega**: Usuário recebe a página pronta


## 💡 Dicas Práticas

1. **Sempre comece pelos models**: Defina primeiro como seus dados serão organizados (Não vamos utilizar)
2. **URLs são hierárquicas**: Do geral para o específico
3. **Templates podem ser reutilizados**: Como peças de LEGO
4. **Cada app deve ter uma responsabilidade clara**: Um Módulo = uma funcionalidade

---
