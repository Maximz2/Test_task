from marshmallow import fields, Schema


class DocumentSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    id_document = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
