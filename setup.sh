mkdir "$env:USERPROFILE\.streamlit" -Force

@"
[server]
port = 8501
enableCORS = false
headless = true
"@ | Out-File -Encoding UTF8 "$env:USERPROFILE\.streamlit\config.toml"
