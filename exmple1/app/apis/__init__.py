from flask_restful import Api

from app.apis.goods_api import GoodsResource, SingleGoodsResource

api=Api()

def init_api(app):
    api.init_app((app))

api.add_resource(GoodsResource,'/goods')
api.add_resource(SingleGoodsResource,'/goods/<int:id>/',endpoint="single_goods")