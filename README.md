# Flask + MinIO (S3 Simulation) with Docker Compose

A **Flask web app** that demonstrates **cloud storage handling** using **MinIO (S3-compatible storage)**.  
Files can be **uploaded and downloaded** via API endpoints, all running in **multi-container Docker Compose**.

---

## 🚀 Features

- Upload files to S3-like storage using `/upload` endpoint
- Download files with `/download/<filename>` endpoint
- MinIO provides **AWS S3 API compatibility**
- Multi-container setup: Flask + MinIO
- Secure local testing for cloud storage handling

---

### Clone Repository

```bash
git clone git@github.com:alphatushar/flask-minIO-app.git
cd flask-minIO-app
```

---

### Services
- Flask Web App → http://127.0.0.1:5000	
- MinIO Storage → http://127.0.0.1:9000
- MinIO Console → http://127.0.0.1:9001
- Login → minioadmin / minioadmin

---

### Examples
![screenshot 1](example/Screenshot%201.png)
![screenshot 1](example/Screenshot%202.png)
![screenshot 1](example/Screenshot%203.png)
![screenshot 1](example/Screenshot%204.png)

---

### Author

Tushar Sharma