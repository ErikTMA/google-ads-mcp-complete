#!/usr/bin/env python3
"""
Google Ads OAuth2 Token Generator
Generates refresh token for Google Ads MCP server configuration
"""

import json
import sys
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

# Google Ads OAuth scope
SCOPES = ['https://www.googleapis.com/auth/adwords']

def main():
    print("=" * 70)
    print("🔐 Google Ads OAuth2 Token Generator")
    print("=" * 70)
    print()

    # Prompt for client secrets file location
    print("Where is your OAuth client secrets JSON file?")
    print("(Press Enter for default: ./client_secret_google_ads.json)")
    client_secret_input = input("Path: ").strip()

    if not client_secret_input:
        client_secret_path = Path("./client_secret_google_ads.json")
    else:
        client_secret_path = Path(client_secret_input)

    if not client_secret_path.exists():
        print(f"❌ Error: {client_secret_path} not found")
        print(f"   Please ensure your OAuth credentials are at the correct location")
        sys.exit(1)

    print()
    print(f"📂 Using credentials from: {client_secret_path}")
    print()
    print("⏳ Opening browser for authentication...")
    print()
    print("👉 In the browser:")
    print("   1. Sign in with your Google account")
    print("   2. Review permissions (Google Ads API access)")
    print("   3. Click 'Allow' to grant access")
    print()

    try:
        # Run OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(
            str(client_secret_path),
            scopes=SCOPES
        )

        # This will open the browser automatically
        creds = flow.run_local_server(port=0)

        print()
        print("=" * 70)
        print("✅ SUCCESS! Authentication Complete")
        print("=" * 70)
        print()

        # Load client secrets to get client_id and client_secret
        with open(client_secret_path) as f:
            client_data = json.load(f)
            client_id = client_data['installed']['client_id']
            client_secret = client_data['installed']['client_secret']

        print("📋 Google Ads MCP Server Configuration")
        print("=" * 70)
        print()
        print("Add these to your .mcp.json under 'google-ads' → 'env':")
        print()
        print(f"GOOGLE_ADS_CLIENT_ID: {client_id}")
        print(f"GOOGLE_ADS_CLIENT_SECRET: {client_secret}")
        print(f"GOOGLE_ADS_REFRESH_TOKEN: {creds.refresh_token}")
        print()
        print("=" * 70)
        print("🎉 All Done! Copy the values above to .mcp.json")
        print()

    except Exception as e:
        print()
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
