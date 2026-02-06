"""
Tests unitaires pour les connecteurs
Démontre les bonnes pratiques de testing

Auteur: [Votre nom]
Date: 2026-02-06
"""

import pytest
from unittest.mock import Mock, patch
import sys
import os

# Ajouter le dossier scripts au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from jira_connector import JiraConnector  # type: ignore


class TestJiraConnector:
    """Tests pour le connecteur Jira"""
    
    def test_connector_initialization(self):
        """Test que le connecteur s'initialise correctement"""
        connector = JiraConnector(
            base_url="https://test.atlassian.net",
            email="test@example.com",
            api_token="fake-token"
        )
        
        assert connector.base_url == "https://test.atlassian.net"
        assert connector.email == "test@example.com"
        assert connector.requests_made == 0
    
    
    @patch('jira_connector.requests.Session.get')
    def test_connection_success(self, mock_get):
        """Test connexion réussie"""
        # Mock de la réponse API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'displayName': 'Test User',
            'emailAddress': 'test@example.com'
        }
        mock_get.return_value = mock_response
        
        # Test
        connector = JiraConnector("https://test.atlassian.net", "test@example.com", "token")
        result = connector.test_connection()
        
        assert result['displayName'] == 'Test User'
        assert connector.requests_made == 1
    
    
    @patch('jira_connector.requests.Session.get')
    def test_connection_unauthorized(self, mock_get):
        """Test erreur 401 (credentials invalides)"""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        connector = JiraConnector("https://test.atlassian.net", "test@example.com", "bad-token")
        
        with pytest.raises(ConnectionError, match="Authentication failed"):
            connector.test_connection()
    
    
    @patch('jira_connector.requests.Session.get')
    def test_get_projects(self, mock_get):
        """Test récupération de projets"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'key': 'DEMO', 'name': 'Demo Project'},
            {'key': 'TEST', 'name': 'Test Project'}
        ]
        mock_get.return_value = mock_response
        
        connector = JiraConnector("https://test.atlassian.net", "test@example.com", "token")
        projects = connector.get_projects()
        
        assert len(projects) == 2
        assert projects[0]['key'] == 'DEMO'
    
    
    def test_statistics(self):
        """Test calcul des statistiques"""
        connector = JiraConnector("https://test.atlassian.net", "test@example.com", "token")
        connector.requests_made = 10
        connector.errors_count = 2
        
        stats = connector.get_statistics()
        
        assert stats['requests_made'] == 10
        assert stats['errors_count'] == 2
        assert stats['success_rate'] == 80.0


if __name__ == "__main__":
    pytest.main([__file__, '-v'])