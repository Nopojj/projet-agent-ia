"""
JIRA Connector class for API interactions
"""
import requests
from requests.auth import HTTPBasicAuth

class JiraConnector:
    """Connect and interact with JIRA API"""
    
    def __init__(self, jira_url, email, api_token):
        """
        Initialize JIRA connector
        
        Args:
            jira_url: JIRA instance URL (e.g., https://your-domain.atlassian.net)
            email: User email
            api_token: API token
        """
        self.jira_url = jira_url.rstrip('/')
        self.email = email
        self.api_token = api_token
        self.auth = HTTPBasicAuth(email, api_token)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    
    def search_issues(self, jql, max_results=50):
        """
        Search issues using JQL
        
        Args:
            jql: JQL query string
            max_results: Maximum number of results
        
        Returns:
            List of issues
        """
        url = f"{self.jira_url}/rest/api/3/search"
        
        params = {
            'jql': jql,
            'maxResults': max_results
        }
        
        try:
            response = requests.get(
                url,
                headers=self.headers,
                auth=self.auth,
                params=params
            )
            response.raise_for_status()
            
            data = response.json()
            issues = []
            
            for issue in data.get('issues', []):
                issues.append({
                    'key': issue['key'],
                    'summary': issue['fields']['summary'],
                    'status': issue['fields']['status']['name'],
                    'priority': issue['fields'].get('priority', {}).get('name', 'None'),
                    'type': issue['fields']['issuetype']['name']
                })
            
            return issues
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching issues: {e}")
            return []
    
    def get_projects(self):
        """
        Get all projects
        
        Returns:
            List of projects
        """
        url = f"{self.jira_url}/rest/api/3/project"
        
        try:
            response = requests.get(
                url,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            
            projects = response.json()
            return [{'key': p['key'], 'name': p['name']} for p in projects]
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching projects: {e}")
            return []