# tests/test_main.py
def test_upload_only_ops():
    response = client.post("/upload", headers=ops_headers, files=valid_docx)
    assert response.status_code == 200

def test_client_cannot_upload():
    response = client.post("/upload", headers=client_headers, files=valid_docx)
    assert response.status_code == 403

def test_download_secure_url():
    token = generate_encrypted_url(file_id=1)
    response = client.get(f"/download-file/{token}", headers=client_headers)
    assert response.status_code == 200
