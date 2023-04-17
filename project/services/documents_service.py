from project.dao import DocumentDAO
from project.exceptions import ItemNotFound
from project.schemas.document import DocumentSchema
from project.services.base import BaseService


class DocumentsService(BaseService):
    def __init__(self, dao: DocumentDAO):
        self.dao = dao

    def create(self, document_data):
        return self.dao.create(document_data)

    # def update(self, id_document, name, description):
    #     self.dao.update(id_document, name, description)

    # def delete(self, uid: int):
    #     return DocumentSchema().dump(self.dao.delete(uid))

    def get_all_documents(self):
        documents = self.dao.get_all()
        return DocumentSchema(many=True).dump(documents)

    def get_item_by_id(self, pk):
        document = self.dao.get_by_id(pk)
        if not document:
            raise ItemNotFound
        return DocumentSchema().dump(document)

    def get_all_by_id(self, pk):
        documents = self.dao.get_all_by_id(pk)
        return DocumentSchema(many=True).dump(documents)
