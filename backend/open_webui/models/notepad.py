import logging
from typing import Optional
import time

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, String, Text, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from open_webui.internal.db import Base, get_db
from open_webui.env import SRC_LOG_LEVELS

####################
# Notepad DB Schema
####################

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

class Notepad(Base):
    __tablename__ = "notepad"

    chat_id = Column(String, primary_key=True)
    content = Column(Text, nullable=True)
    user_id = Column(String)

    created_at = Column(BigInteger)
    updated_at = Column(BigInteger)

####################
# Models
####################

class NotepadModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    chat_id: str
    content: Optional[str] = None
    user_id: str
    created_at: int
    updated_at: int

####################
# Table Operations
####################

class NotepadTable:
    def get_notepad_by_chat_id(self, chat_id: str) -> Optional[NotepadModel]:
        """Get notepad by chat ID."""
        try:
            with get_db() as db:
                notepad = db.query(Notepad).filter(
                    Notepad.chat_id == chat_id
                ).first()
                return NotepadModel.model_validate(notepad) if notepad else None
        except Exception:
            log.exception("Failed to get notepad")
            return None

    def save_notepad(self, chat_id: str, content: str, user_id: str) -> Optional[NotepadModel]:
        """Save or update notepad content."""
        try:
            with get_db() as db:
                notepad = db.query(Notepad).filter(
                    Notepad.chat_id == chat_id
                ).first()
                
                current_time = int(time.time())
                
                if notepad:
                    notepad.content = content
                    notepad.updated_at = current_time
                else:
                    notepad = Notepad(
                        chat_id=chat_id,
                        content=content,
                        user_id=user_id,
                        created_at=current_time,
                        updated_at=current_time
                    )
                    db.add(notepad)
                
                db.commit()
                db.refresh(notepad)
                return NotepadModel.model_validate(notepad)
        except Exception:
            log.exception("Failed to save notepad")
            return None

    def delete_notepad_by_chat_id(self, chat_id: str) -> bool:
        """Delete notepad content by chat ID."""
        try:
            with get_db() as db:
                db.query(Notepad).filter_by(chat_id=chat_id).delete()
                db.commit()
                return True
        except Exception:
            log.exception("Failed to delete notepad")
            return False

    def delete_notepads_by_user_id(self, user_id: str) -> bool:
        """Delete all notepads for a user."""
        try:
            with get_db() as db:
                db.query(Notepad).filter_by(user_id=user_id).delete()
                db.commit()
                return True
        except Exception:
            log.exception("Failed to delete user's notepads")
            return False

    def get_notepads_by_user_id(self, user_id: str) -> list[NotepadModel]:
        """Get all notepads for a user."""
        try:
            with get_db() as db:
                contents = db.query(Notepad).filter_by(user_id=user_id).all()
                return [NotepadModel.model_validate(content) for content in contents]
        except Exception:
            log.exception("Failed to get user's notepads")
            return []

Notepads = NotepadTable() 