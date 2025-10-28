from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, Body
from fastapi.responses import FileResponse
from datetime import datetime, timedelta, timezone
from typing import Annotated
from subprocess import Popen, PIPE
import os

HOME = os.getenv("HOME")
PJ_DIR = HOME+"/blblblweb"
APK_PATH = HOME+"blblblweb/app/build/outputs/apk/debug/app-debug.apk"

def exe(cmd: list|str, cwd: str|None = None):
    ps = Popen(
        cmd,
        cwd=cwd, text=True, stdout=PIPE, stderr=PIPE
    )
    return ps.communicate()


app = FastAPI()

@app.post("/cmd")
def exe_cmd(cmd: Annotated[str|dict, Body()], cwd: str|None = None):
    if isinstance(cmd, str):
        out, err = exe(cmd, cwd)
    else:
        out, err = exe(cmd['cmd'], cwd)
    return dict(output=out, error=err)


@app.get('/build')
def build():
    try:
        out, err = exe(['./gradlew', 'assembleDebug'], PJ_DIR)
        return dict(output=out, error=err)
    except Exception as e:
        if isinstance(e, PermissionError):
            exe(['setfacl', '-m', 'u::rwx', 'gradlew'], PJ_DIR)
            return dict(info="Please, Request again!")
        return dict(error=str(e))


@app.get('/getApp')
def get_app():
    if not os.path.exists(APK_PATH):
        raise HTTPException(400, "App haven't build yet.")
    return FileResponse(APK_PATH)

