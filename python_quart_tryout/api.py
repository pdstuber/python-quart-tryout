from quart import jsonify,Blueprint

api = Blueprint('api', __name__)

@api.route("/api")
async def json():
    return jsonify({"hello": "world"})
