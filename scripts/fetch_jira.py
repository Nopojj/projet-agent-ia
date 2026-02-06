"""
Fetch JIRA issues script
"""
import os
from scripts.jira_connector import JiraConnector

def fetch_issues(jira_url, email, api_token, project_key=None):
    """
    Fetch issues from JIRA
    
    Args:
        jira_url: JIRA instance URL
        email: User email
        api_token: API token
        project_key: Optional project key to filter
    
    Returns:
        List of issues
    """
    connector = JiraConnector(jira_url, email, api_token)
    
    if project_key:
        jql = f'project = {project_key}'
    else:
        jql = 'ORDER BY created DESC'
    
    issues = connector.search_issues(jql)
    
    print(f"✅ Fetched {len(issues)} issues")
    return issues

def main():
    """Main function"""
    # Get credentials from environment
    jira_url = os.getenv('JIRA_URL')
    email = os.getenv('JIRA_EMAIL')
    api_token = os.getenv('JIRA_API_TOKEN')
    
    if not all([jira_url, email, api_token]):
        print("❌ Error: Missing JIRA credentials in environment variables")
        print("Please set: JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN")
        return
    
    issues = fetch_issues(jira_url, email, api_token)
    
    # Display summary
    for issue in issues[:5]:  # Show first 5
        print(f"  - {issue['key']}: {issue['summary']}")

if __name__ == "__main__":
    main()