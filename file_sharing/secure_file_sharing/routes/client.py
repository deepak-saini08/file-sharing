
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    user_db = create_user(user, role='client')
    verification_url = generate_encrypted_url(user_db.id)
    send_email(user.email, verification_url)
    return {"message": "Verify your email", "url": verification_url}


@router.get("/download-file/{token}")
def download(token: str, current_user: User = Depends(get_current_client_user)):
    file_id = decrypt_url(token)
    if not current_user.is_verified:
        raise HTTPException(status_code=403, detail="Email not verified.")
    return FileResponse(path=get_file_path(file_id))
