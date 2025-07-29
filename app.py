from flask import Flask, request, jsonify
from minio import Minio
from flask import send_file
import os

app = Flask(__name__)

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "minio:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")
BUCKET_NAME = "flask-bucket"

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Create bucket if it doesn't exist
if not client.bucket_exists(BUCKET_NAME):
    client.make_bucket(BUCKET_NAME)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    client.fput_object(BUCKET_NAME, filename, filename)
    os.remove(filename)
    return jsonify({"message": f"{filename} uploaded to S3 bucket!"})

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    local_file = f"/tmp/{filename}"
    try:
        client.fget_object(BUCKET_NAME, filename, local_file)
        return send_file(local_file, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)