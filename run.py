from project.config import DevelopmentConfig
from project.dao.models import Document
from project.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Document": Document
    }


app.debug = True


if __name__ == '__main__':
    app.run(host="localhost", port=9874)
