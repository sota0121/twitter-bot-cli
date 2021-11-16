# twitter bot

## Features

- Post tweet regularly
  - posting messages are in `tweets_list.json` (save in Cloud Storage)
  - **Future** : use tweets list in `spreadsheet`


## Infrastructure

- Google Cloud Functions


## Deployment

### 1. Make `.env.yaml`

Copy and create `.env.yaml` from `.env-template.yaml`, in root directory.

```bash
cp .env-template.yaml .env.yaml
```

And then set the values below:

```yaml
consumer_key: "twitter-consumer-key"
consumer_secret: "twitter-consumer-secret"
access_token: "twitter-access-token"
access_secret: "twitter-access-secret"
gs_type: "service_account"
gs_project_id: "Google Spreadsheet Project ID"
gs_private_key_id: "Google Spreadsheet Private key id"
# \nもそのまま設定したいのでシングルクォート
gs_private_key: 'Google Spreadsheet Private key'
gs_client_email: "Google Spreadsheet Service Account Email"
gs_client_id: "Google Spreadsheet Client ID"
gs_auth_uri: "Google Spreadsheet Auth URI"
gs_token_uri: "Google Spreadsheet Token URI"
gs_auth_provider_x509_cert_url: "Google Spreadsheet provider cert uri"
gs_client_x509_cert_url: "Google Spreadsheet client cert uri"
```

### 2. Execute shell script

Execute `deploy-function.sh` to deploy `main.py` as Google Cloud Functions' instance.

```bash
chmod ./deploy-function.sh
source ./deploy-function.sh
```
