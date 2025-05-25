# SalesOps Manager – Start.io 2025

Mini-app Streamlit pour piloter la prospection, le suivi des consultants, et la gestion des candidats en ESN.

## Installation

1. Clone le dépôt ou dézippe le dossier
2. Place ton fichier `credentials.json` dans le dossier racine
3. Exécute :

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Connexion Google Sheets

Le fichier est connecté à ce Google Sheet :  
https://docs.google.com/spreadsheets/d/1fFjvk0X6vvvM7ZEBfF03yGpNEQhzL1IkM2YrAxJCc70

## Modules couverts

- 📊 Dashboard
- 🧲 Prospection
- 🧠 Consultants
- 👤 Candidats

secrets.TOML : 

[credentials]
type = "service_account"
project_id = "salesops-manager-2025"
private_key_id = "adfde3a893336e60741b07948fabaafe1a00a4e0"
private_key = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/eia/fLOWiHav
HTup7SPG2oNi8TQ9yZ4E5z6ulks51ipdPLO+Iyok87Q0MN7nbpMnte4PCCsid59r
Xacbo+ox51+rVpCeIghnThIaT0mv1xbVBBkK0AEw/0uJpK+rsYcDWv6QWYlEDTux
t9ioZjs0tv6qAW/gjY0V2hZFZj6KnMzHkxT54v0oI4HHDGG80huLPY52uf1awHDN
rGhorpcFAOQXE/mXzJAAlEWmLldDQKO7lz8LDK8GPkWqo91HSt0F3yDgs0dUbqxc
m2RoKxyP8lSsqfG10/PinHKdjAqM824aAOYBNsjAOWQTp/21pLDqcmO1kXSBVdpC
UDAkZUslAgMBAAECggEABBxG+Dlg3ujaKLpuXwQnHK+4MB0ey4k2e9+S+DzyK5TK
grHjkep4q5WELJnCpJPlGpjpAWEpETnon8L6QWQXNPcMJEYkH71dg+3E5il3zJnk
WECKfYbufA90SazR1CmElD748Hfp0HPz0+JoByj+OUV6oLwcDSx1oclY97amaJyn
kjwxprQ8RP34Sa4PnIAX9G93LXl+1YgrZOuCt2RMmZ3EtTVyi+Pfy8hsclCn1Tyz
mRark/fVLoZnBIw/laagrN9YXaME/WmEOQFvFCU4ZupL6uojGGuXO7U3Y/nOxceA
wvCQ24FKE2sFBAGaBo/vWFhAdTz4qG3hVo+azWtBgQKBgQDvuAscbagqPL6RZpa7
T/T2zFoRAZ6zQ+YiBfde8AvipwXM+WCwX1rTF81GjfIgWXfrYRb46NdWvDxqraYq
2S2GstRSwWyejuqIAu9OhUx3nJv/kb94psx9hVFZ58+daU+Z0lbeBnYDPBfGmfA/
5d8Adjk7g2h83N7o9PW3A76O0QKBgQDMe1XujvWpvAppoIcLkyEnpEQUwmtBiDbb
3XV0/Os/hcibkXCxLjfkCGYR9xRRVmDuSvcdgCrda4YAn3mRkvQdMs+fzlqurXIN
fWYyY6TsaqhteEXGg3DSFFiQYrSGxRdL+H3fIFTsnDvmhK9TMU+XvLeoBqIsPMUR
Fd2PoDdUFQKBgCw1LqdheZ/AcAx0dNu6VRymdv2n5NJ+dRRVMVdqwWZdEu7IFpKw
IxnGy+51AvAAT+Myln/0wLGYKTQrLfe88W5j0FAqp5NeG9ZVZDiA0KdGVGZ/RGZF
rHSBf40q+Ni4sRtW9PohCuZx0JipjurZw5RcORXGmCBewyUG98F2iU/hAoGAKfGG
n+d9JrLmo+IEsXAdlecQ+/0hSRDqx9C2XiffDWmgy6BasE1ds42xei/nYAPK4DZK
WCfJIyACHbCYnC67mh2pDwuh+EClq3S0eNONqdz67XGFRoIBq2X3AK7uftKAw9mV
4CXepaYqd09yMytjOym/tlyd+VsBxU5p4yMnFj0CgYEA68twQ0z7Ww6+DuYPYSln
bkA8xyfRI+ErQ25C55F9/4A+NXRfKfl9dZvpX1T0ibyRg0fTdBodS/tOr0VTvMdv
VMTfO0kUhcY/7EBnzeFuKlBUeSW5/G/WPp9dY57FmHYPXobm43NKkZBDYeuE1MFI
2wqu6LCGB4UCRDA1O0nDo6E=
-----END PRIVATE KEY-----"""
client_email = "salesopsmanager@salesops-manager-2025.iam.gserviceaccount.com"
client_id = "102093674790966447137"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/salesopsmanager@salesops-manager-2025.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
