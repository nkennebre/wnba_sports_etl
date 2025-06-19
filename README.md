# WNBA Sports ETL 🏀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)


**Work In Progress 🚧**

A production-ready data engineering pipeline for processing, transforming, and analyzing women's sports data — starting with WNBA team stats and game logs.

---

## Project Goals

- Build end-to-end ETL pipelines for women's sports data
- Develop clean, analytics-ready datasets for underserved sports domains
- Engineer features to support predictive modeling and advanced analysis
- Contribute to the visibility of women's sports in the data community

---

## Current Focus

- WNBA team stats (2015–2024) — ETL pipeline in progress
- Feature engineering and data validation
- Future roadmap: PWHL data exploration + ML pipeline development

---

## Project Structure

sports_etl_project/
├── data/                 # Raw and processed data  
├── notebooks/            # EDA and analysis notebooks  
├── scripts/              # CLI scripts for running the ETL  
├── sports_etl/           # Core ETL and utils modules  
│   ├── etl/  
│   ├── utils/  
├── tests/                # Unit tests  
├── README.md  
├── pyproject.toml  
└── .gitignore  

---

## How to Run

1️⃣ Install dependencies:

```bash
poetry install
```

2️⃣ Activate virtual environment:

```bash
poetry shell
```

3️⃣ Example usage in a notebook:

```
from sports_etl.etl.extract import load_team_stats
from sports_etl.etl.transform import transform_team_stats
from sports_etl.etl.load import save_to_csv, save_to_sqlite
```


## Credits
## Credits

- Primary WNBA Game Logs dataset (2015–2024): [My Kaggle dataset](https://www.kaggle.com/datasets/natoshakennebrew/wnba-gamelogs-2015-2024)
- Additional WNBA team stats reference: [WNBA Team Stats by Evan Gower](https://www.kaggle.com/datasets/evangower/wnba-team-stats)

Project by Maxine Kennebrew  
**“Beast on the ice, stat nerd in the lab.”**

🚀 Part of the PlayHer.ai initiative — building open, analytics-first tools to elevate women’s sports.

*Building on open data sources to help grow a stronger community of women's sports analytics practitioners.*