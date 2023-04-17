from flask import request, render_template
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.implemented import document_service

documents_ns = Namespace("documents")


@documents_ns.route("/create")
class DoccreateView(Resource):
    def post(self):
        req_json = request.json
        document_service.create(req_json)
        return "", 201


@documents_ns.route("/")
class DocumentsView(Resource):
    @documents_ns.response(200, "OK")
    def get(self):
        all_documents = document_service.get_all_documents()
        return render_template('documents.html', items=all_documents)


@documents_ns.route("/<int:document_id>")
class DocumentView(Resource):
    @documents_ns.response(200, "OK")
    @documents_ns.response(404, "Document not found")
    def get(self, document_id: int):
        try:
            document = document_service.get_item_by_id(document_id)
            return render_template('document.html', name=document['name'], description=document['description'])
        except ItemNotFound:
            abort(404, message="Document not found")

    def put(self, document_id: int):
        req_json = request.json
        req_json["id_document"] = document_id
        document_service.create(req_json)
        return "", 204

    def delete(self, document_id: int):
        req_json = {}
        req_json["id_document"] = document_id
        req_json["name"] = ''
        req_json["description"] = ''
        document_service.create(req_json)
        return "", 204


@documents_ns.route("/documents/<int:document_id>")
class DocumentsView(Resource):
    @documents_ns.response(200, "OK")
    @documents_ns.response(404, "Document not found")
    def get(self, document_id: int):
        try:
            items = document_service.get_all_by_id(document_id)
            return render_template('documents.html', items=items)
        except ItemNotFound:
            abort(404, message="Document not found")
