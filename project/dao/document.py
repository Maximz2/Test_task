from sqlalchemy import desc
from sqlalchemy.orm.scoping import scoped_session
from project.dao.models import Document


class DocumentDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    # Запрос всех документов
    def get_all(self):
        return self._db_session.query(Document).order_by(Document.id_document).all()

    # Запрос последней версии документа по id_document
    def get_by_id(self, pk):
        return self._db_session.query(Document).filter(Document.id_document == pk).order_by(desc(Document.id)).first()

    # Запрос всех версий документа по id_document
    def get_all_by_id(self, pk):
        return self._db_session.query(Document).filter(Document.id_document == pk).all()

    # Создание записи о документе
    def create(self, document_data):
        document = Document(**document_data)
        if document.name == '' and document.description == '':
            document.name = "Deleted"
        self._db_session.add(document)
        self._db_session.commit()
        return document

    # def delete(self, uid: int):
    #     deleted_rows = self._db_session.query(Document).filter(Document.id == uid).delete()
    #     if deleted_rows != 1:
    #         return None, 404
    #     self._db_session.commit()
    #     return None, 200

    # def update(self, id_document, name=None, description=None, document_data=None):
    #     document = Document(**document_data)
    #     if name:
    #         document.name = name
    #     if description:
    #         document.description = description
    #     self._db_session.commit()
