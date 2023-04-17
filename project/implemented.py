from project.dao import DocumentDAO
from project.services import DocumentsService
from project.setup_db import db

document_dao = DocumentDAO(session=db.session)

document_service = DocumentsService(dao=document_dao)

