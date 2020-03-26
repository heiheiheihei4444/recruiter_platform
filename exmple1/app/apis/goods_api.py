# coding=utf-8
from flask import request
from flask_restful import Resource, abort, fields, marshal_with, reqparse

from app.models import Goods

goods_fields={
    "id":fields.Integer,
    "g_name":fields.String,
    "g_price":fields.Integer,
    "uri":fields.Url('single_goods',absolute=True)
}
single_goods_fields={
    "data":fields.Nested(goods_fields),
    "status":fields.Integer,
    "msg":fields.String,
}

multi_goods_fieds={
    "status":fields.Integer,
    "msg":fields.String,
    "data":fields.List(fields.Nested(goods_fields))
}

parser=reqparse.RequestParser()
parser.add_argument("g_name",type=str,help="please input g_name")
parser.add_argument("g_price")
parser.add_argument("sex",action='append')
parser.add_argument("HOST",dest='host',location='headers')

class GoodsResource(Resource):
    @marshal_with(multi_goods_fieds)
    def get(self):
        args = parser.parse_args()
        print(args.get('host'))
        goods_List=Goods.query.all()


        data={
            "status":200,
            "msg":"ok",
            "data":goods_List
        }
        return data

    @marshal_with(single_goods_fields)
    def post(self):
        # g_name=request.form.get('g_name')
        # g_price=request.form.get('g_price')
        args=parser.parse_args()
        g_name=args.get('g_name')
        g_price=args.get('g_price')

        goods=Goods()
        goods.g_name=g_name
        goods.g_price=g_price
        if not goods.save() :
            abort(404)



        data={
            "msg":"create success",
                 "status":201,
                "data":goods

            }
        return data

class SingleGoodsResource(Resource):
    @marshal_with(single_goods_fields)
    def get(self,id):
        goods=Goods.query.get(id)
        data={
            "status":200,
            "msg":"ok",
            "data":goods
        }
        return data
    def delete(self,id):
        goods=Goods.query.get(id)
        if not goods:
            abort(404)
        if not goods.delete():
            abort(404)
        data={
            "msg":"delete success",
            "status":204
        }
        return data
