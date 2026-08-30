# 🚀 AWS EC2 Deployment with Nginx Reverse Proxy

> **A Python Flask application deployed on AWS EC2 with Nginx configured as a reverse proxy.**

This project demonstrates my foundational understanding of **cloud deployment, Security Groups, and reverse proxy setup** — the first step before moving to production-grade tooling like Gunicorn and systemd.

---

## 🌐 Live Project

🔗 **GitHub:** `github.com/sayyedasgar7-arch/aws-ec2-nginx-flask-deploy`

📸 **Deployment Screenshot:**
*Add live browser screenshot here.*

---

## 🏗️ Architecture

```text
        🌍 Internet
             │
             ▼
      ┌─────────────┐
      │    Nginx     │  ← Port 80 (public)
      │ (reverse     │
      │  proxy)      │
      └──────┬───────┘
             │ HTTP (localhost:5000)
             ▼
      ┌─────────────┐
      │  Flask App   │
      │ (dev server) │
      └─────────────┘
```

### Request Flow

**Browser → Nginx (port 80) → Flask App (port 5000) → Response**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| ☁️ AWS EC2 | Cloud compute instance |
| 🐧 Ubuntu | Server operating system |
| 🐍 Flask | Web application |
| 🌐 Nginx | Reverse proxy |
| 🔥 AWS Security Groups | Network access control |

---

## 🎯 What This Project Demonstrates

- Launching and configuring an AWS EC2 instance (Free Tier)
- Configuring **Security Groups** for controlled inbound access (SSH + HTTP)
- Connecting to the server via SSH
- Installing and configuring **Nginx** as a reverse proxy
- Routing public traffic (port 80) to a Flask app running on port 5000
- Debugging a real connectivity issue caused by a browser-level (not server-level) restriction

---

## 🚀 Deployment Process

### 1️⃣ Launch EC2 Instance

Ubuntu, `t2.micro`, Security Group allowing SSH (22) and HTTP (80).

### 2️⃣ Connect via SSH

```bash
ssh -i my-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

### 3️⃣ Install Nginx and Python

```bash
sudo apt update
sudo apt install nginx python3-pip python3-venv -y
```

### 4️⃣ Set Up Flask App

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
flask run --host=0.0.0.0 --port=5000
```

### 5️⃣ Configure Nginx as Reverse Proxy

```nginx
location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

```bash
sudo systemctl restart nginx
```

### 6️⃣ Access the App

```text
http://YOUR_EC2_PUBLIC_IP
```

---

## 📁 Project Structure

```text
aws-ec2-nginx-flask-deploy/
│
├── app.py
└── README.md
```

---

## 🔍 Real Debugging Story

While testing, the site returned `ERR_CONNECTION_TIMED_OUT` in one browser (Brave) but worked instantly in Microsoft Edge — despite Nginx running correctly (`curl http://localhost` succeeded on the server). Root cause: the browser's built-in Shields feature was interfering with the HTTP connection, not an AWS or Nginx misconfiguration. This reinforced the importance of isolating **client-side vs server-side** issues when debugging.

---

## 🧠 Key Learnings

- Security Groups must explicitly allow both SSH (administration) and HTTP (public access)
- `curl http://localhost` from inside the server is a fast way to confirm whether an issue is server-side or network/client-side
- Not every "connection failed" error means the server is broken

---

## 🔮 Future Improvements

- [ ] Replace Flask dev server with Gunicorn (see related project)
- [ ] Restrict SSH access to a specific IP instead of `0.0.0.0/0`
- [ ] Add HTTPS
- [ ] Automate this setup with Terraform

---

## 💼 DevOps Skills Demonstrated

```text
AWS
├── EC2
└── Security Groups

Web Server
└── Nginx Reverse Proxy

Troubleshooting
└── Client vs Server-Side Debugging
```

---

## 👨‍💻 About Me

**Sayed Asgar** — DevOps / Cloud Engineering Enthusiast

🔗 **LinkedIn:** `linkedin.com/in/sayed-asgar-devops`
🐙 **GitHub:** `github.com/sayyedasgar7-arch`

---

### 📌 Project Status

**Status:** 🟢 Completed | **Stack:** Flask + Nginx | **Type:** Cloud Deployment Basics
