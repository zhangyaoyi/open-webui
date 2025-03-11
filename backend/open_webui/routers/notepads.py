from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from pydantic import BaseModel
from open_webui.models.users import Users
from open_webui.models.notepad import Notepads

from open_webui.utils.auth import get_verified_user
from open_webui.constants import ERROR_MESSAGES
import logging

from open_webui.env import SRC_LOG_LEVELS

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

router = APIRouter()

############################
# GetNotepadContent
############################

@router.get("/{chat_id}")
async def get_notepad(chat_id: str, user=Depends(get_verified_user)):
    """Get notepad for a specific chat"""
    try:
        notepad = Notepads.get_notepad_by_chat_id(chat_id)
        return {"content": notepad.content if notepad else ""}
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MESSAGES.DEFAULT()
        )

############################
# SaveNotepad
############################

class NotepadForm(BaseModel):
    chat_id: str
    content: Optional[str] = None

@router.post("/save")
async def save_notepad(form_data: NotepadForm, user=Depends(get_verified_user)):
    """Save notepad for a specific chat"""
    try:
        Notepads.save_notepad(form_data.chat_id, form_data.content, user.id)
        return {"success": True}
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MESSAGES.DEFAULT()
        ) 