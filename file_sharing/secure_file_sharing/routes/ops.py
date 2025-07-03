
@router.post("/upload")
async def upload_file(file: UploadFile, current_user: User = Depends(get_current_ops_user)):
    if not file.filename.endswith(('.pptx', '.docx', '.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    path = save_file(file)
    return {"message": "File uploaded", "path": path}
