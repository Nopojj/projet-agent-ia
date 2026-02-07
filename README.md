# 🤖 AI Agent Project - DevOps & Integrations

> Système automatisé d'extraction et d'analyse de données de projets avec Intelligence Artificielle

![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Pipeline](https://img.shields.io/badge/CI%2FCD-GitLab-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 📊 Aperçu du Dashboard

![Dashboard Preview](screenshots/dashboard_preview.png)

## 🎯 Objectif

Automatiser l'extraction, le traitement et l'analyse des données de gestion de projets depuis **Jira**, **Azure DevOps** et **GitHub** pour alimenter un agent IA intelligent.

## ✨ Fonctionnalités

- 🔄 **Extraction automatique** des données via APIs REST
- 🤖 **Pipeline CI/CD GitLab** avec 4 stages (Validate, Fetch, Process, Export)
- 📊 **Dashboard Streamlit** interactif avec graphiques Plotly
- 🧪 **Mode DEMO** fonctionnel sans credentials
- ✅ **Tests automatisés** avec pytest
- 📁 **Export JSON** standardisé pour l'agent IA
- 🔐 **Sécurité** : credentials dans variables d'environnement

## 🚀 Quick Start

### Mode DEMO (sans credentials)
```bash
# Clone
git clone https://github.com/Nopojj/projet-agent-ia.git
cd projet-agent-ia

# Installation
pip install -r requirements.txt

# Génération données DEMO
python scripts/demo_mode.py

# Lancement dashboard
cd Dashboard
streamlit run app.py
```

Le dashboard s'ouvre à `http://localhost:8501`

### Mode Production (avec credentials Jira)
```bash
# Configuration
cp .env.example .env
# Éditer .env avec vos tokens

# Extraction
python scripts/fetch_jira.py

# Dashboard
cd Dashboard
streamlit run app.py
```

## 🏗️ Architecture
```
APIs (Jira/Azure/GitHub)
        ↓
GitLab CI/CD Pipeline
        ↓
Connecteurs Python
        ↓
Export JSON
        ↓
Agent IA (LangChain)
        ↓
Dashboard Streamlit
```

## 📁 Structure
```
projet-agent-ia/
├── Dashboard/          # Application Streamlit
├── scripts/            # Connecteurs API
├── tests/              # Tests unitaires
├── data/               # Données exportées (gitignored)
├── .gitlab-ci.yml      # Pipeline CI/CD
└── README.md
```

## 🧪 Tests
```bash
pytest tests/ -v
```

## 🔧 Technologies

- **Python 3.10+**
- **Streamlit** - Dashboard
- **Plotly** - Graphiques
- **Requests** - API calls
- **GitLab CI/CD** - Automatisation
- **pytest** - Tests

## 👥 Équipe

- **DevOps & Integrations** - Pipeline, APIs, Infrastructure
- **AI Agent** - LangChain, Analyse
- **Dashboard** - Visualisation
- **Data Collection** - Extraction, Processing

## 📝 Documentation

 Architecture détaillée
- [Pipeline Guide](.gitlab-ci.yml) - Configuration CI/CD

## 📄 License

Projet académique - AI Agent Project 2026

---

**Status** : ✅ Production Ready (Mode DEMO)  
**Version** : 1.0.0  
**Dernière mise à jour** : 2026-02-07