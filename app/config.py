import os
from dotenv import load_dotenv
 
load_dotenv()
 
# # Add these configurations to your Config class
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    # SQLite configuration (for development)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    #Product Config
    Lending_Products={
        "credit_decision_logik":{
            "Heading":"Credit Decisioning Logik",
            "TagLine":"Empowering Accurate Credit Decisions.",
        },
        "Borrower_qualification_logik": {
            "Heading":"Borrower Qualification Logik",
            "TagLine":"Evaluate with Precision, Approve with Confidence.",
        },
        "Bank_statement_visualizer_logik":{
            "Heading":"Bank Statement Visualizer Logik",
            "TagLine":"Simplify Statements, Amplify Insights.",
        },
 
        "Marketing_logik_dashboard":{
            "Heading":"Marketing Logik",
            "TagLine":"Target Smarter, Market Better.",
        },
        "cross_selling_logik_dashboard":{
            "Heading":"Cross Selling Logik",
            "TagLine":"Smart Suggestions for Bigger Opportunities",
        },
        "Borrower_lead_routing_logik_dashboard":{
            "Heading":"Borrower Lead Routing Logik",
            "TagLine":"Streamline Leads, Maximize Conversions.",
        },
        "Bad_debt_analyzer_logik_dashboard":{
            "Heading":"Bad Debt Analyzer Logik",
            "TagLine":"Turn Data Into Insights, Reduce Bad Debt Risks.",
        },
        "Compliance_logik_dashboard":{
            "Heading":"Compliance Logik",
            "TagLine":"Simplifying Regulatory Compliance for Modern Lending"
        }
    }
    


    # Existing configs...
    SF_CLIENT_ID = os.environ.get('SF_CLIENT_ID')
    SF_CLIENT_SECRET = os.environ.get('SF_CLIENT_SECRET')
    SF_DOMAIN = os.environ.get('SF_DOMAIN')  # Your Salesforce domain
 
    SALESFORCE_ORG = {
        "credit_decision_logik":{
            "SalesforceOrg" : "https://brave-hawk-6yrll5-dev-ed.trailblaze.lightning.force.com/lightning/o/Opportunity/list?filterName=NewThisWeek",
            "UserName"      : "rrr160701@gmail.com",
            "Password"      : "MRpark@123"
        },
        "Borrower_qualification_logik": {
            "SalesforceOrg" :"https://wise-goat-b6xnin-dev-ed.trailblaze.lightning.force.com/lightning/o/Lead/list?filterName=__Recent",
            "UserName"      : "ritik.raghuwanshi@wise-goat-b6xnin.com",
            "Password"      : "MRpark@123"
        },
        "Bank_statement_visualizer_logik":{
            "SalesforceOrg" : "",
            "UserName"      : "",
            "Password"      : ""
        },
        "Bank_statement_visualizer_logik_dashboard":{
            "SalesforceOrg" : "",
            "UserName"      : "",
            "Password"      : ""
        },
        "Marketing_logik_dashboard":{
            "SalesforceOrg" : "https://wise-goat-b6xnin-dev-ed.trailblaze.lightning.force.com/lightning/n/Marketing_Recommendations",
            "UserName"      : "ritik.raghuwanshi@wise-goat-b6xnin.com",
            "Password"      : "MRpark@123"
        },
        
        
        "cross_selling_logik_dashboard":{
            "SalesforceOrg" : "https://wise-goat-b6xnin-dev-ed.trailblaze.lightning.force.com/lightning/n/Cross_Selling_of_Loans",
            "UserName"      : "ritik.raghuwanshi@wise-goat-b6xnin.com",
            "Password"      : "MRpark@123"
        },
        "Borrower_lead_routing_logik_dashboard":{
            "SalesforceOrg" : "",
            "UserName"      : "",
            "Password"      : ""
        },
        "Bad_debt_analyzer_logik_dashboard":{
            "SalesforceOrg" : "",
            "UserName"      : "",
            "Password"      : ""
        },
        "Compliance_logik_dashboard":{
            "SalesforceOrg" : "https://wise-goat-b6xnin-dev-ed.trailblaze.lightning.force.com/lightning/o/Lead/list?filterName=__Recent",
            "UserName"      : "ritik.raghuwanshi@wise-goat-b6xnin.com",
            "Password"      : "MRpark@123"
        }
    }
    GITHUB_REPO = {
        "credit_decision_logik":{
            "Jupyter_code_approach1":"https://github.com/LendingLogik/Loan-Classification-Approch-1",
            "Jupyter_code_approach2":"https://github.com/LendingLogik/Loan-Classification-Approch-2",
            "Jupyter_code_approach3":"https://github.com/LendingLogik/Loan-Classification-Approch-3",
            "Fintech_loans_app"     : "https://github.com/LendingLogik/Fintech-loans-PHP-app",
            "Flynx_loans_app"       : "https://github.com/LendingLogik/Flynx-app",
            "Credit_decision_logik_SF_APP" : "https://github.com/LendingLogik/Credit-decision-logik-SF-app"
        },
        "Borrower_qualification_logik": {
            "Borrower_qualification_SF_APP" : "https://github.com/LendingLogik/Borrower-qualification-sf-app",
            "Borrower_qualification_logik"  : "https://github.com/LendingLogik/Borrower-qualification-logik",
            "Borrower_qualification_web_app" : "https://github.com/LendingLogik/Borrower-qualification-web-app"
        },
        "Bank_statement_visualizer_logik":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bank_statement_visualizer_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Marketing_logik_dashboard":"https://github.com/LendingLogik/Marketing-logik",
        "cross_selling_logik_dashboard":"https://github.com/LendingLogik/cross_selling-logik",
        "Borrower_lead_routing_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bad_debt_analyzer_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Compliance_logik_dashboard":"https://github.com/LendingLogik/compliance-logik-web-app"
    }
    VIDEO_TUTORIALS = {
        "credit_decision_logik":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/1%20Credit%20Decisioning%20Logik/Video%20demonstration?csf=1&web=1&e=DQuVJa",
        "Borrower_qualification_logik": "https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/2%20Borrower%20Qualification%20Logik/Video%20demonstration?csf=1&web=1&e=i7dQlh",
        "Bank_statement_visualizer_logik":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bank_statement_visualizer_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Marketing_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/5%20Marketing%20Logik/Video%20demonstration?csf=1&web=1&e=KDrjJg",
        "cross_selling_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/6%20Cross%20Selling%20Logik/Video%20Explaining%20the%20code?csf=1&web=1&e=lgMKz2",
        "Borrower_lead_routing_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bad_debt_analyzer_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/9%20Bad%20Debt%20Analyzer%20Logik/Video%20demonstration?csf=1&web=1&e=tOMaoE",
        "Compliance_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/11%20Compliance%20Logik/Video%20explaining%20the%20code?csf=1&web=1&e=4S0IMT"
    }
    
    VIDEO_DEMONSTRATION = { 
        "credit_decision_logik":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/1%20Credit%20Decisioning%20Logik/Video%20explaining%20the%20code?csf=1&web=1&e=5lv4le",
        "Borrower_qualification_logik": "https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/2%20Borrower%20Qualification%20Logik/Video%20explaining%20the%20code?csf=1&web=1&e=hHdVNV",
        "Bank_statement_visualizer_logik":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bank_statement_visualizer_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Marketing_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/5%20Marketing%20Logik/Video%20demonstration?csf=1&web=1&e=LkfC2o",
        "cross_selling_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/6%20Cross%20Selling%20Logik/Video%20demonstration?csf=1&web=1&e=CMrJHG",
        "Borrower_lead_routing_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bad_debt_analyzer_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/9%20Bad%20Debt%20Analyzer%20Logik/Video%20demonstration?csf=1&web=1&e=Y7PKWI",
        "Compliance_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/11%20Compliance%20Logik/Video%20demonstration?csf=1&web=1&e=JJSATw"
    }
 
    DOCUMENTATIONS = {
        "credit_decision_logik":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/1%20Credit%20Decisioning%20Logik/Documentation?csf=1&web=1&e=AL6sbb",
        "Borrower_qualification_logik": "https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/2%20Borrower%20Qualification%20Logik/Documentation?csf=1&web=1&e=SUMFk7",
        "Bank_statement_visualizer_logik":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bank_statement_visualizer_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Marketing_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/5%20Marketing%20Logik/Documentation?csf=1&web=1&e=S48BT4",
        "cross_selling_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/6%20Cross%20Selling%20Logik/Documentation?csf=1&web=1&e=6zt2Xr",
        "Borrower_lead_routing_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bad_debt_analyzer_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/9%20Bad%20Debt%20Analyzer%20Logik/Documentation?csf=1&web=1&e=OQTuH0",
        "Compliance_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/11%20Compliance%20Logik/Documentation?csf=1&web=1&e=Ou1E2a"
    }
 
    PRESENTATIONS = {
        "credit_decision_logik":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/1%20Credit%20Decisioning%20Logik/Power%20point%20presentation?csf=1&web=1&e=kSBjqR",
        "Borrower_qualification_logik": "https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/2%20Borrower%20Qualification%20Logik/Power%20point%20presentation?csf=1&web=1&e=tPssZQ",
        "Bank_statement_visualizer_logik":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bank_statement_visualizer_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Marketing_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/5%20Marketing%20Logik/Power%20point%20presentation?csf=1&web=1&e=MLBHQo",
        "cross_selling_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/6%20Cross%20Selling%20Logik/Power%20point%20presentation?csf=1&web=1&e=741rwB",
        "Borrower_lead_routing_logik_dashboard":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "Bad_debt_analyzer_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/9%20Bad%20Debt%20Analyzer%20Logik/Power%20point%20presentation?csf=1&web=1&e=v7PUUQ",
        "Compliance_logik_dashboard":"https://mindruby-my.sharepoint.com/:f:/r/personal/ritik_raghuwanshi_mindruby_com/Documents/Lendinglogik%20Products/11%20Compliance%20Logik/Power%20point%20presentation?csf=1&web=1&e=hLc87I"
    }

    devNoteBooks = {
        "credit_decision_logik"                     :   "/dev/notebook-explorer?path=notebooks/Credit_Decisioning_Logik",
        "Borrower_qualification_logik"              :   "/dev/notebook-explorer?path=notebooks/Borrower_Qualification_Logik",
        "Bank_statement_visualizer_logik"           :   "/dev/notebook-explorer?path=notebooks/",
        "Bank_statement_visualizer_logik_dashboard" :   "/dev/notebook-explorer?path=notebooks/",
        "Marketing_logik_dashboard"                 :   "/dev/notebook-explorer?path=notebooks/Marketing-logik",
        "cross_selling_logik_dashboard"             :   "/dev/notebook-explorer?path=notebooks/cross_selling-logik-master",
        "Borrower_lead_routing_logik_dashboard"     :   "/dev/notebook-explorer?path=notebooks/",
        "Bad_debt_analyzer_logik_dashboard"         :   "/dev/notebook-explorer?path=notebooks/",
        "Compliance_logik_dashboard"                :   "/dev/notebook-explorer?path=notebooks/"
    }
 
 
 
 
# Set the project root path
os.environ['PROJECT_ROOT'] = os.path.abspath(os.path.dirname(__file__))
 
 