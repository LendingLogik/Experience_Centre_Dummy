# from app.models.user import User
from flask import Blueprint, render_template, send_from_directory, request, jsonify, redirect
import nbformat
from nbconvert import HTMLExporter
from simple_salesforce import Salesforce
import os
from ..config import Config

bp = Blueprint('main', __name__)

def getcontextLinks(keyofContext):
    return {
        'salesforceOrg': Config.SALESFORCE_ORG[keyofContext],
        'videoDemonstration': Config.VIDEO_DEMONSTRATION[keyofContext],
        'presentations': Config.PRESENTATIONS[keyofContext],
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

@bp.route('/Products')
def Products():
    context = getProductContext()
    context['Header'] = "Our Products"
    return render_template('products.html', context=context)

@bp.route('/credit-decision-logik-dashboard')
def Credit_decision_logik_dashboard():
    context = getcontextLinks("credit_decision_logik")
    context['Header'] = 'Credit Decisioning Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/Borrower-qualification-logik-dashboard')
def Borrower_qualification_logik_dashboard():
    context = getcontextLinks("Borrower_qualification_logik")
    context['Header'] = 'Borrower Qualification Logik'
    return render_template('product_dashboard.html', context=context)    

@bp.route('/Bank-statement-visualizer-logik-dashboard')
def Bank_statement_visualizer_logik_dashboard():
    context = getcontextLinks("Bank_statement_visualizer_logik")
    context['Header'] = 'Bank Statement Visualizer Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/Marketing-logik-dashboard')
def Marketing_logik_dashboard():
    context = getcontextLinks("Marketing_logik_dashboard")
    context['Header'] = 'Marketing Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/cross-selling-logik-dashboard')
def cross_selling_logik_dashboard():
    context = getcontextLinks("cross_selling_logik_dashboard")
    context['Header'] = 'Cross Selling Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/Borrower-lead-routing-logik-dashboard')
def Borrower_lead_routing_logik_dashboard():
    context = getcontextLinks("Borrower_lead_routing_logik_dashboard")
    context['Header'] = 'Borrower Lead Routing Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/Bad-debt-analyzer-logik-dashboard')
def Bad_debt_analyzer_logik_dashboard():
    context = getcontextLinks("Bad_debt_analyzer_logik_dashboard")
    context['Header'] = 'Bad Debt Analyzer Logik'
    return render_template('product_dashboard.html', context=context)

@bp.route('/Compliance-logik-dashboard')
def Compliance_logik_dashboard():
    context = getcontextLinks("Compliance_logik_dashboard")
    context['Header'] = 'Compliance Logik'
    return render_template('product_dashboard.html', context=context)
