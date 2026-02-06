"""
Utility functions for the AI Agent Dashboard project
"""

def format_jira_data(data):
    """Format JIRA data for display"""
    if not data:
        return []
    return data

def validate_config(config):
    """Validate configuration settings"""
    required_keys = ['jira_url', 'jira_email', 'jira_token']
    return all(key in config for key in required_keys)

def get_mock_data():
    """Return mock data for demo purposes"""
    return [
        {
            "key": "DEMO-1",
            "summary": "Implement authentication",
            "status": "In Progress",
            "priority": "High",
            "type": "Feature"
        },
        {
            "key": "DEMO-2",
            "summary": "Create dashboard",
            "status": "Done",
            "priority": "Medium",
            "type": "Feature"
        },
        {
            "key": "DEMO-3",
            "summary": "Add CI/CD pipeline",
            "status": "To Do",
            "priority": "High",
            "type": "Feature"
        },
        {
            "key": "DEMO-4",
            "summary": "Fix login bug",
            "status": "Done",
            "priority": "High",
            "type": "Bug"
        },
        {
            "key": "DEMO-5",
            "summary": "Add unit tests",
            "status": "Testing",
            "priority": "Medium",
            "type": "Test"
        },
        {
            "key": "DEMO-6",
            "summary": "Update documentation",
            "status": "To Do",
            "priority": "Low",
            "type": "Feature"
        }
    ]