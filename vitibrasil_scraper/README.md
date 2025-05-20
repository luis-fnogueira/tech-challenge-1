# Vitibrasil Scraper

Projeto desenvolvido para o curso de Engenharia de Machine Learning da FIAP. Esse projeto tem como finalidade buscar dados da Embrapa referentes à produção de vinhos e uvas no estado do Rio Grande do Sul e disponibilizá-los via uma API.

## Instalação

```bash
# Clonar o repositório
git clone https://github.com/seu_usuario/vitibrasil_scraper.git
cd vitibrasil_scraper

# Instalar dependências
pip install -r vitibrasil_scraper/requirements.txt
```

## Testes

Para executar os testes automatizados do projeto, você pode usar os seguintes comandos:

```bash
# Executar todos os testes
python -m unittest discover -s vitibrasil_scraper

# Executar testes específicos
python -m unittest vitibrasil_scraper.api.tests.test_routes
python -m unittest vitibrasil_scraper.scraper.tests.test_base
```

Os testes estão organizados em dois diretórios principais:
- `vitibrasil_scraper/api/tests/`: Testes relacionados à API Flask
- `vitibrasil_scraper/scraper/tests/`: Testes relacionados ao scraper de dados

## Uso

### Executar a API Flask

```bash
# Executar com configurações padrão
python vitibrasil_scraper/cli.py

# Executar no modo de debug
python vitibrasil_scraper/cli.py --debug

# Executar em um host e porta diferentes
python vitibrasil_scraper/cli.py --host 0.0.0.0 --port 8080
```

## Endpoints da API

- `GET /` - Informações da API
- `GET /api/production?year={year}` - Obter dados de produção de vinho para um ano específico
- `GET /api/processing?year={year}` - Obter dados de processamento de uvas para todas as categorias
- `GET /api/processing/{category}?year={year}` - Obter dados de processamento de uvas para uma categoria específica
- `GET /api/commercialization?year={year}` - Obter dados de comercialização de vinho para um ano específico 
- `GET /api/import?year={year}` - Obter dados de importação para todas as categorias
- `GET /api/import/{category}?year={year}` - Obter dados de importação para uma categoria específica
- `GET /api/export?year={year}` - Obter dados de exportação para todas as categorias
- `GET /api/export/{category}?year={year}` - Obter dados de exportação para uma categoria específica

### Categorias de uvas disponíveis

- `viniferas`: Variedades de uvas usadas para vinhos de alta qualidade (Vitis vinifera)
- `americanas`: Variedades de uvas americanas e híbridas 
- `mesa`: Uvas de mesa
- `sem_classificacao`: Variedades de uvas não classificadas

### Categorias de importação disponíveis

- `vinhos_mesa`: Vinhos de Mesa
- `espumantes`: Espumantes
- `uvas_frescas`: Uvas Frescas
- `uvas_passas`: Uvas Passas
- `suco_uva`: Suco de Uva

### Categorias de exportação disponíveis

- `vinhos_mesa`: Vinhos de Mesa
- `espumantes`: Espumantes
- `uvas_frescas`: Uvas Frescas
- `suco_uva`: Suco de Uva

## Exemplos de requests

Você pode fazer requests à API usando curl ou qualquer cliente HTTP:

```bash
# Obter informações da API
curl http://localhost:5000/

# Obter dados de produção de vinho para 2023
curl http://localhost:5000/api/production?year=2023

# Obter dados de processamento de uvas para viníferas em 2023
curl http://localhost:5000/api/processing/viniferas?year=2023

# Obter dados de comercialização de vinho para 2023
curl http://localhost:5000/api/commercialization?year=2023

# Obter dados de importação para vinhos de mesa em 2023
curl http://localhost:5000/api/import/vinhos_mesa?year=2023

# Obter dados de exportação para vinhos de mesa em 2023
curl http://localhost:5000/api/export/vinhos_mesa?year=2023
``` 