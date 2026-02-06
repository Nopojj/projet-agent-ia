import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Agent Dashboard - JIRA Integration",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Projet d'agent IA - Tableau de bord JIRA")

# Sidebar
with st.sidebar:
    st.header("⚙️ État du Projet")
    st.info("Phase: 🔨 Implémentation & Tests")
    
    # Project timeline
    st.subheader("📅 Timeline")
    progress_data = {
        "Phase": ["Planification", "Implémentation", "Tests", "Déploiement"],
        "Status": ["✅ Complété", "🔄 En cours", "🔄 En cours", "⏳ À venir"]
    }
    for phase, status in zip(progress_data["Phase"], progress_data["Status"]):
        st.write(f"**{phase}**: {status}")
    
    st.markdown("---")
    st.metric("Progression Globale", "60%", "↗️")

# Main content
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Issues Totales", "12", "+2 cette semaine")

with col2:
    st.metric("En Cours", "5", "+1")

with col3:
    st.metric("Terminées", "4", "+2")

with col4:
    st.metric("Tests", "3", "en cours")

st.markdown("---")

# Sample data
issues_data = pd.DataFrame({
    'Issue': ['DEMO-1', 'DEMO-2', 'DEMO-3', 'DEMO-4', 'DEMO-5', 'DEMO-6'],
    'Type': ['Feature', 'Bug', 'Feature', 'Test', 'Feature', 'Bug'],
    'Status': ['In Progress', 'Done', 'In Progress', 'Testing', 'To Do', 'Done'],
    'Priority': ['High', 'Medium', 'High', 'Medium', 'Low', 'High'],
    'Component': ['Backend', 'Frontend', 'API', 'Tests', 'Dashboard', 'Backend']
})

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Analyse JIRA", "🔄 CI/CD Pipeline", "📈 Progression"])

with tab1:
    st.subheader("📊 Analyse des Issues JIRA")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        # Status distribution
        st.markdown("##### Répartition par Statut")
        status_counts = issues_data['Status'].value_counts()
        fig_status = go.Figure(data=[go.Pie(
            labels=status_counts.index,
            values=status_counts.values,
            hole=0.4,
            marker_colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
        )])
        fig_status.update_layout(height=300, showlegend=True)
        st.plotly_chart(fig_status, use_container_width=True)
    
    with col_b:
        # Priority distribution
        st.markdown("##### Répartition par Priorité")
        priority_counts = issues_data['Priority'].value_counts()
        fig_priority = px.bar(
            x=priority_counts.index,
            y=priority_counts.values,
            labels={'x': 'Priorité', 'y': 'Nombre'},
            color=priority_counts.values,
            color_continuous_scale='Reds'
        )
        fig_priority.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_priority, use_container_width=True)
    
    # Issue type breakdown
    st.markdown("##### Types d'Issues")
    type_counts = issues_data.groupby(['Type', 'Status']).size().reset_index(name='Count')
    fig_types = px.bar(
        type_counts,
        x='Type',
        y='Count',
        color='Status',
        barmode='group',
        color_discrete_map={
            'Done': '#4ECDC4',
            'In Progress': '#FFD93D',
            'Testing': '#A8E6CF',
            'To Do': '#FFB6B9'
        }
    )
    st.plotly_chart(fig_types, use_container_width=True)
    
    # Data table
    st.markdown("##### Détails des Issues")
    st.dataframe(issues_data, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("🔄 Pipeline CI/CD GitHub")
    
    st.info("💡 **Comment visualiser**: Poussez le code sur GitHub → Actions → Voir le workflow")
    
    # Current pipeline stages
    st.markdown("#### Étapes Actuelles du Pipeline")
    
    pipeline_stages = [
        {"stage": "🧪 Test", "jobs": ["Tests unitaires", "Validation syntaxe"], "status": "✅ Success"},
        {"stage": "🔨 Build", "jobs": ["Installation dépendances", "Vérification imports"], "status": "✅ Success"}
    ]
    
    for stage_info in pipeline_stages:
        with st.expander(f"{stage_info['stage']} - {stage_info['status']}", expanded=True):
            for job in stage_info['jobs']:
                st.markdown(f"- ✓ {job}")
    
    # Future stage
    st.markdown("#### 🔮 Prochaine Étape")
    with st.expander("📦 Deploy (À venir)", expanded=False):
        st.write("Cette étape sera ajoutée après la phase de tests")
        st.write("- Déploiement automatique")
        st.write("- Vérification de santé")
    
    # Pipeline visualization
    st.markdown("#### Durée des Étapes")
    pipeline_duration = pd.DataFrame({
        'Stage': ['Test', 'Build'],
        'Durée (s)': [45, 30],
        'Status': ['Success', 'Success']
    })
    
    fig_pipeline = px.bar(
        pipeline_duration,
        x='Durée (s)',
        y='Stage',
        orientation='h',
        color='Status',
        title='Temps d\'exécution du Pipeline',
        color_discrete_map={'Success': '#4ECDC4'}
    )
    st.plotly_chart(fig_pipeline, use_container_width=True)

with tab3:
    st.subheader("📈 Progression du Projet")
    
    # Weekly progress
    weeks_data = pd.DataFrame({
        'Semaine': ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4'],
        'Issues Créées': [3, 4, 3, 2],
        'Issues Complétées': [0, 1, 2, 1],
        'Tests Ajoutés': [0, 1, 1, 1]
    })
    
    fig_progress = go.Figure()
    fig_progress.add_trace(go.Scatter(
        x=weeks_data['Semaine'],
        y=weeks_data['Issues Créées'],
        name='Créées',
        mode='lines+markers',
        line=dict(color='#FF6B6B', width=3)
    ))
    fig_progress.add_trace(go.Scatter(
        x=weeks_data['Semaine'],
        y=weeks_data['Issues Complétées'],
        name='Complétées',
        mode='lines+markers',
        line=dict(color='#4ECDC4', width=3)
    ))
    fig_progress.update_layout(
        title='Évolution Hebdomadaire',
        xaxis_title='Période',
        yaxis_title='Nombre d\'Issues',
        height=400
    )
    st.plotly_chart(fig_progress, use_container_width=True)
    
    # Component progress
    st.markdown("#### Progression par Composant")
    component_progress = pd.DataFrame({
        'Composant': ['Backend', 'Frontend', 'API', 'Tests', 'Dashboard'],
        'Complété': [70, 50, 60, 40, 65]
    })
    
    fig_components = px.bar(
        component_progress,
        x='Composant',
        y='Complété',
        color='Complété',
        color_continuous_scale='Viridis',
        labels={'Complété': 'Progression (%)'}
    )
    fig_components.update_layout(height=350)
    st.plotly_chart(fig_components, use_container_width=True)



st.caption(f"Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M')}")