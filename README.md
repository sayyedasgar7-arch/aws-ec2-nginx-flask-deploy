# AWS EC2 + Nginx + Flask Deployment

Deployed a Flask application on an AWS EC2 (Ubuntu) instance, using Nginx as a reverse proxy to serve the app over HTTP.

## What This Demonstrates
- Launching and configuring an AWS EC2 instance (Free Tier)
- Configuring Security Groups (inbound rules for SSH and HTTP)
- SSH access and Linux server administration
- Installing and configuring Nginx as a reverse proxy
- Deploying a Python Flask application on a cloud server
- Debugging connectivity issues (browser/network level)

## Architecture
Internet → Nginx (port 80) → Flask App (port 5000)

## Tech Stack
- AWS EC2 (Ubuntu 22.04)
- Nginx
- Python (Flask)
