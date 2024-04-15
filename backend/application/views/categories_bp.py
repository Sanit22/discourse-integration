import requests
from flask import Blueprint
from flask_restful import Api, Resource
from application.logger import logger
# from application.common_utils import (
#     token_required,
#     users_required,
# )
# from application.views.user_utils import UserUtils
from application.responses import *
from application.models import *
from application.globals import *

categories_bp = Blueprint("categories_bp", __name__)
categories_api = Api(categories_bp)

class GetAllCategories(Resource):
    # @token_required
    # @users_required(users=["student", "support", "admin"])
    def get(self):
        """
        Usage
        -----
        Get a list of all categories from discourse

        Returns
        -------
        List of Categories

        """

        url = DISCOURSE_DEFAULT_HOST + "/categories.json"
        res = requests.get(url)
        if res.status_code == 200:
            #print(res.text)
            return res.json()
        
        logger.error(
                "Failed to list categories from discourse"
            )
        raise InternalServerError(status_msg="Failed to list categories from discourse")
        

categories_api.add_resource(GetAllCategories, "/")
