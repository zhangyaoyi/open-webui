import logging
from typing import Optional
import time

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, String, Text, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from open_webui.internal.db import Base, get_db
from open_webui.env import SRC_LOG_LEVELS

####################
# Editor DB Schema
####################

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

class EditorContent(Base):
    __tablename__ = "editor_content"

    chat_id = Column(String, primary_key=True)
    content = Column(Text, nullable=True)
    user_id = Column(String)

    created_at = Column(BigInteger)
    updated_at = Column(BigInteger)

####################
# Models
####################

class EditorModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    chat_id: str
    content: Optional[str] = None
    user_id: str
    created_at: int
    updated_at: int

####################
# Forms
####################

class EditorContentForm(BaseModel):
    content: str

####################
# Table Operations
####################

class EditorTable:
    def get_content_by_chat_id(self, chat_id: str) -> Optional[EditorModel]:
        """Get editor content by chat ID."""
        try:
            with get_db() as db:
                editor_content = db.query(EditorContents).filter(
                    EditorContents.chat_id == chat_id
                ).first()
                return EditorModel.model_validate(editor_content) if editor_content else None
        except Exception:
            log.exception("Failed to get editor content")
            return None

    def save_content(self, chat_id: str, content: str, user_id: str) -> Optional[EditorModel]:
        """Save or update editor content."""
        try:
            with get_db() as db:
                editor_content = db.query(EditorContents).filter(
                    EditorContents.chat_id == chat_id
                ).first()
                
                current_time = int(time.time())
                
                if editor_content:
                    editor_content.content = content
                    editor_content.updated_at = current_time
                else:
                    editor_content = EditorContents(
                        chat_id=chat_id,
                        content=content,
                        user_id=user_id,
                        created_at=current_time,
                        updated_at=current_time
                    )
                    db.add(editor_content)
                
                db.commit()
                db.refresh(editor_content)
                return EditorModel.model_validate(editor_content)
        except Exception:
            log.exception("Failed to save editor content")
            return None

    def delete_content_by_chat_id(self, chat_id: str) -> bool:
        """Delete editor content by chat ID."""
        try:
            with get_db() as db:
                db.query(EditorContents).filter_by(chat_id=chat_id).delete()
                db.commit()
                return True
        except Exception:
            log.exception("Failed to delete editor content")
            return False

    def delete_contents_by_user_id(self, user_id: str) -> bool:
        """Delete all editor contents for a user."""
        try:
            with get_db() as db:
                db.query(EditorContents).filter_by(user_id=user_id).delete()
                db.commit()
                return True
        except Exception:
            log.exception("Failed to delete user's editor contents")
            return False

    def get_contents_by_user_id(self, user_id: str) -> list[EditorModel]:
        """Get all editor contents for a user."""
        try:
            with get_db() as db:
                contents = db.query(EditorContents).filter_by(user_id=user_id).all()
                return [EditorModel.model_validate(content) for content in contents]
        except Exception:
            log.exception("Failed to get user's editor contents")
            return []

Editor = EditorTable() 