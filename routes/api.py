# routes/api.py
from __future__ import annotations

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import traceback

from analysis import compute_basic_stats

api_bp = Blueprint("api", __name__)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ─────────────────── helpers ─────────────────── #

def ok(payload: dict, code: int = 200):
    return jsonify(payload), code

def err(message: str, code: int):
    return jsonify({"error": message}), code

def file_path_in_uploads(file_name: str) -> str:
    safe = secure_filename(file_name)
    return os.path.join(UPLOAD_DIR, safe)


# ─────────────────── health ─────────────────── #

@api_bp.get("/health")
def health():
    return ok({"status": "ok", "service": "e-soft-api", "step": "health"})


# ─────────────────── upload ─────────────────── #

@api_bp.post("/upload")
def upload_file():
    file = request.files.get("file")
    if file is None:
        return err("'file' is required", 400)

    if not file.filename:
        return err("empty filename", 400)

    path = file_path_in_uploads(file.filename)
    file.save(path)
    return ok({
        "message": "file uploaded",
        "file_id": 1,                 # упрощённо: заглушка
        "filename": file.filename,
        "path": path
    }, 201)


# ─────────────────── files listing ─────────────────── #

@api_bp.get("/files")
def list_files():
    try:
        items = []
        for name in sorted(os.listdir(UPLOAD_DIR)):
            full = os.path.join(UPLOAD_DIR, name)
            if os.path.isfile(full):
                st = os.stat(full)
                items.append({
                    "file_name": name,
                    "size": st.st_size,
                    "modified": int(st.st_mtime)
                })
        return ok({"files": items})
    except FileNotFoundError:
        return ok({"files": []})


# ─────────────────── analyze ─────────────────── #
# Теперь принимает {"file_name": "..."} вместо path

@api_bp.post("/analyze")
def analyze_file():
    if not request.is_json:
        return err("Content-Type must be application/json", 415)

    data = request.get_json(silent=True) or {}
    if "file_name" not in data:
        return err("field 'file_name' is required", 400)

    path = file_path_in_uploads(str(data["file_name"]))
    if not os.path.exists(path):
        return err(f"file '{data['file_name']}' not found", 404)

    try:
        stats = compute_basic_stats(path)
        return ok({
            "file_name": data["file_name"],
            "path": path,
            "stats": stats
        })
    except Exception:
        # аккуратно возвращаем стек в лог, а пользователю — 500
        traceback.print_exc()
        return err("failed to analyze file", 500)