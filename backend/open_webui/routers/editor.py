from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from pydantic import BaseModel
from open_webui.models.users import Users
from open_webui.models.editor import EditorContents
from open_webui.utils.auth import get_verified_user
from open_webui.constants import ERROR_MESSAGES
import logging

from open_webui.env import SRC_LOG_LEVELS

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

router = APIRouter()

class EditorContent(BaseModel):
    chatId: str
    content: Optional[str] = None

############################
# GetEditorContent
############################

@router.get("/{chatId}")
async def get_editor_content(chatId: str, user=Depends(get_verified_user)):
    """Get editor content for a specific chat"""
    try:
        editor_content = EditorContents.get_content_by_chat_id(chatId)
        return {"content": editor_content.content if editor_content else ""}
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MESSAGES.DEFAULT()
        )

############################
# SaveEditorContent
############################

@router.post("/save")
async def save_editor_content(content: EditorContent, user=Depends(get_verified_user)):
    """Save editor content for a specific chat"""
    try:
        EditorContents.save_content(content.chatId, content.content, user.id)
        return {"success": True}
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MESSAGES.DEFAULT()
        ) 