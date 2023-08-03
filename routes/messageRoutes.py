from flask import Blueprint
from controllers.messageController import index, create, message, edit, delete

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/')(index)
blueprint.route('/create/', methods=['GET', 'POST'])(create)
blueprint.route('/<int:id>/')(message)
blueprint.route('/<int:id>/edit/', methods=['GET', 'POST'])(edit)
blueprint.route('/<int:id>/delete/')(delete)