# from app.models.user import User
from flask import Blueprint, render_template, send_from_directory, request, jsonify, redirect
import nbformat
from nbconvert import HTMLExporter
from simple_salesforce import Salesforce
import os
from ..config import Config

bp = Blueprint('dev_main', __name__)

def getcontextLinks(keyofContext):
    return {
        'salesforceOrg'     : Config.SALESFORCE_ORG[keyofContext],
        'githubRepo'        : Config.GITHUB_REPO[keyofContext],
        'videoTutorials'    : Config.VIDEO_TUTORIALS[keyofContext],
        'videoDemonstration': Config.VIDEO_DEMONSTRATION[keyofContext],
        'documentations'    : Config.DOCUMENTATIONS[keyofContext],
        'presentations'     : Config.PRESENTATIONS[keyofContext],
        'notebooks'         : Config.devNoteBooks[keyofContext]
    }


def getProductContext():
    return {
        "credit_decision_logik"          : Config.Lending_Products['credit_decision_logik'],
        "Borrower_qualification_logik"   : Config.Lending_Products['Borrower_qualification_logik'] ,
        "Bank_statement_visualizer_logik": Config.Lending_Products['Bank_statement_visualizer_logik'],
        "Marketing_logik_dashboard"      : Config.Lending_Products['Marketing_logik_dashboard']  ,
        "cross_selling_logik_dashboard"  : Config.Lending_Products['cross_selling_logik_dashboard'],
        "Borrower_lead_routing_logik_dashboard": Config.Lending_Products['Borrower_lead_routing_logik_dashboard'],
        "Bad_debt_analyzer_logik_dashboard": Config.Lending_Products['Bad_debt_analyzer_logik_dashboard'],
        "Compliance_logik_dashboard"     : Config.Lending_Products['Compliance_logik_dashboard'],
    }

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dev/Products')
def Products():
    context = getProductContext()
    context['IsDev'] = True
    context['Header'] = "Our Development Products"
    return render_template('products.html', context=context)

@bp.route('/dev/credit-decision-logik-dashboard')
def Credit_decision_logik_dashboard():
    context = getcontextLinks("credit_decision_logik")
    context['Header'] = 'Credit Decisioning Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/dev/Borrower-qualification-logik-dashboard')
def Borrower_qualification_logik_dashboard():
    context = getcontextLinks("Borrower_qualification_logik")
    context['Header'] = 'Borrower Qualification Logik'
    return render_template('product_dashboard.html', context=context)    

@bp.route('/dev/Bank-statement-visualizer-logik-dashboard')
def Bank_statement_visualizer_logik_dashboard():
    context = getcontextLinks("Bank_statement_visualizer_logik")
    context['Header'] = 'Bank Statement Visualizer Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/dev/Marketing-logik-dashboard')
def Marketing_logik_dashboard():
    context = getcontextLinks("Marketing_logik_dashboard")
    context['Header'] = 'Marketing Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/dev/cross-selling-logik-dashboard')
def cross_selling_logik_dashboard():
    context = getcontextLinks("cross_selling_logik_dashboard")
    context['Header'] = 'Cross Selling Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/dev/Borrower-lead-routing-logik-dashboard')
def Borrower_lead_routing_logik_dashboard():
    context = getcontextLinks("Borrower_lead_routing_logik_dashboard")
    context['Header'] = 'Borrower Lead Routing Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/dev/Bad-debt-analyzer-logik-dashboard')
def Bad_debt_analyzer_logik_dashboard():
    context = getcontextLinks("Bad_debt_analyzer_logik_dashboard")
    context['Header'] = 'Bad Debt Analyzer Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/dev/Compliance-logik-dashboard')
def Compliance_logik_dashboard():
    context = getcontextLinks("Compliance_logik_dashboard")
    context['Header'] = 'Compliance Logik'
    return render_template('product_dashboard.html', context=context)



@bp.route('/dev/notebook-explorer')
def notebook_explorer():
    # Access query parameters using request.args
    path = request.args.get('path', '')  # Default empty string if not provided
    # sort_by = request.args.get('sort', 'name')  # Default sort by name
    # filter_type = request.args.get('type', 'all')  # Default show all
    
    # base_path = os.path.join(os.getcwd(), 'notebooks', path)
    # items = []
    if path == "":
        path = "notebooks"



    project_root = os.environ.get('PROJECT_ROOT')
    notebooks_path = os.path.join(project_root, path)
    # notebooks_path = os.path.join(os.getcwd(), 'notebooks')  # Adjust path as needed
    
    # Get all files and folders in the notebooks directory
    items = []
    try:
        for item in os.listdir(notebooks_path):
            full_path = os.path.join(notebooks_path, item)
            items.append({
                'name': item,
                'type': 'folder' if os.path.isdir(full_path) else 'file',
                'path': full_path
            })
    except FileNotFoundError:
        items = []
    
    return render_template('notebook_explorer.html', items=items)


@bp.route('/dev/experiences')
def experiences():
    # Path to your Jupyter notebook
    fileName = request.args.get('fileName', '')  # Default empty string if not provided

    if fileName == "":
        fileName = "notebooks/experience_center.ipynb"
    
    project_root = os.environ.get('PROJECT_ROOT')
    notebook_path = os.path.join(project_root, fileName)

    # notebook_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'experience_center.ipynb')
    print("notebook path : ", notebook_path)
    # Read and convert the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
        
    # Convert to HTML
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'classic'
    notebook_html, _ = html_exporter.from_notebook_node(notebook_content)
    
    return render_template('experiences.html', notebook_content=notebook_html)

@bp.route('/dev/download-notebook')
def download_notebook():
    notebook_dir = os.path.join(os.path.dirname(__file__), '..', 'notebooks')
    return send_from_directory(notebook_dir, 'experience_center.ipynb')

