from flask import Flask, session, redirect, request, url_for, Blueprint, jsonify
from urllib.parse import quote
import os
from base64 import urlsafe_b64encode
import hashlib
import secrets
import requests


app = Blueprint('salesforce_r', __name__)

def generate_code_verifier():
    return secrets.token_urlsafe(96)

def generate_code_challenge(verifier):
    sha256 = hashlib.sha256(verifier.encode('utf-8')).digest()
    return urlsafe_b64encode(sha256).decode('utf-8').rstrip('=')

@app.route('/salesforce/token')
def get_salesforce_token():
    try:
        # Authentication parameters
        params = {
            'grant_type': 'password',
            'client_id': os.environ.get('SF_CLIENT_ID'),
            'client_secret': os.environ.get('SF_CLIENT_SECRET'),
            'username': "ritik.raghuwanshi@wise-goat-b6xnin.com",
            'password': "MRpark@123"  # Password + Security Token
        }

        # Make the token request
        response = requests.post(
            'https://login.salesforce.com/services/oauth2/token',
            params=params
        )

        # Check if request was successful
        response.raise_for_status()
        
        # Store token in session
        token_data = response.json()
        session['sf_access_token'] = token_data['access_token']
        session['sf_instance_url'] = token_data['instance_url']

        return jsonify({
            'success': True,
            'message': 'Authentication successful'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/salesforce/login')
def salesforce_login():
    params = {
        'response_type': 'code',
        'client_id': os.environ.get('SF_CLIENT_ID'),
        'redirect_uri': os.environ.get('SF_REDIRECT_URI'),
        'state': secrets.token_urlsafe(16),
        'scope': 'api refresh_token web openid'
    }
    SF_AUTH_URL = "https://wise-goat-b6xnin-dev-ed.trailblaze.lightning.force.com/services/oauth2/authorize"
    auth_url = f"{SF_AUTH_URL}?{'&'.join(f'{k}={quote(str(v))}' for k, v in params.items())}"
    return redirect(auth_url)

@app.route('/salesforce1/login1')
def salesforce_login1():
    try:
        # Generate PKCE values for security
        code_verifier = generate_code_verifier()
        code_challenge = generate_code_challenge(code_verifier)
        
        # Store code_verifier in session
        session['sf_code_verifier'] = code_verifier

        # Generate state parameter to prevent CSRF
        state = secrets.token_urlsafe(16)
        session['sf_state'] = state

        # Define OAuth parameters
        params = {
            'response_type': 'code',
            'client_id': os.environ.get('SF_CLIENT_ID'),
            'redirect_uri': "https://127.0.0.1/salesforce/callback",
            'state': state,
            'code_challenge': code_challenge,
            'code_challenge_method': 'S256',
            'scope': 'api refresh_token web openid profile email',
            'prompt': 'consent'  # Force consent screen
        }
        print("params : ", params)

        # Construct authorization URL
        base_url = os.environ.get('SF_AUTH_URL', 'https://login.salesforce.com/services/oauth2/authorize')
        auth_url = f"{base_url}?{'&'.join(f'{k}={quote(str(v))}' for k, v in params.items())}"
        
        print(f"Redirecting to Salesforce: {auth_url}")  # Debug print
        return redirect(auth_url)

    except Exception as e:
        return f"Error during SSO initialization: {str(e)}", 500
    
@app.route('/salesforce/callback')
def salesforce_callback():
    try:
         # Check for errors
        if 'error' in request.args:
            error_msg = f"Salesforce Error: {request.args.get('error')} - {request.args.get('error_description')}"
            print(error_msg)  # Debug print
            return error_msg, 400

        # Verify state parameter
        if request.args.get('state') != session.get('sf_state'):
            return 'Invalid state parameter', 400

        code = request.args.get('code')
        if not code:
            return 'Authorization code not received', 400

        # Exchange code for tokens
        token_response = exchange_code_for_token(code)
        
        # Store tokens in session
        session['sf_access_token'] = token_response['access_token']
        session['sf_instance_url'] = token_response['instance_url']

        # Redirect to Salesforce dashboard
        return redirect_to_salesforce_dashboard()

    except Exception as e:
        return f"Error during callback: {str(e)}", 500

def redirect_to_salesforce_dashboard():
    try:
        instance_url = session.get('sf_instance_url')
        access_token = session.get('sf_access_token')
        
        # Target the Lightning dashboard page
        dashboard_path = '/lightning/page/home'  # Or your specific dashboard URL
        
        # Construct frontdoor URL for SSO
        redirect_url = (
            f"{instance_url}/secur/frontdoor.jsp"
            f"?sid={access_token}"
            f"&retURL={quote(dashboard_path)}"
        )
        
        return redirect(redirect_url)

    except Exception as e:
        return f"Error during dashboard redirect: {str(e)}", 500

import requests
def exchange_code_for_token(code):
    
    # token_url = os.environ.get('SF_TOKEN_URL')
    token_url = os.environ.get('SF_TOKEN_URL', 'https://login.salesforce.com/services/oauth2/token')
    
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': os.environ.get('SF_CLIENT_ID'),
        'client_secret': os.environ.get('SF_CLIENT_SECRET'),
        'redirect_uri': os.environ.get('SF_REDIRECT_URI'),
        'code_verifier': session.get('sf_code_verifier')
    }
    
    response = requests.post(token_url, data=data)
    response.raise_for_status()
    return response.json()


@app.route('/dashboard')
def dashboard():
    if 'sf_access_token' not in session:
        return redirect(url_for('salesforce_login'))
        
    return f"""
    <h1>Successfully authenticated with Salesforce!</h1>
    <p>Instance URL: {session.get('sf_instance_url')}</p>
    <p>Access Token Available: {'Yes' if session.get('sf_access_token') else 'No'}</p>
    """
