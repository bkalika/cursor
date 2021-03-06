import json

from flask import request
from flask_restful import Resource

from tenants.parser import parser
from tenants.models import Tenant
from utils import read_data, write_data

json_file = 'tenants/tenants.json'
json_data = read_data(json_file)
tenants_data = json.load(open(json_file))


class Tenants(Resource):
    def get(self, name=None):
        if name is None:
            args = parser.parse_args(strict=True)
            if args.name is not None:
                tenant_data = []
                for tenant in json_data:
                    if tenant.get("name") == args.get("name") or tenant.get("passport_id") == args.get("passport_id"):
                        tenant_data.append(tenant)
                return tenant_data
            else:
                return json_data
        elif name:
            for tenant in json_data:
                if tenant.get("name") == name or tenant.get("passport_id") == name:
                    return tenant
            else:
                return "404 tenant not found"

    def post(self):
        data = request.json
        parser.parse_args(strict=True)
        for tenant in json_data:
            if tenant.get("passport_id") == data["passport_id"]:
                return "Tenant already ordered room"
        else:
            tenants_data.append(Tenant(
                data["name"],
                data["passport_id"],
                data["age"],
                data["sex"],
                data["city"],
                data["street"],
                data["room_number"],
            ).to_dict())
            write_data(tenants_data, json_file)
            return "Tenant added"

    def patch(self):
        data = request.json
        for tenant in tenants_data:
            if tenant.get("name") == data.get("name"):
                tenant.update(data)
        write_data(tenants_data, json_file)
        return "Tenant updated"

    def delete(self):
        data = request.json
        for tenant in range(len(tenants_data)):
            if tenants_data[tenant].get("name") == data.get("name"):
                del tenants_data[tenant]
                break
        else:
            return "Tenant not found"
        write_data(tenants_data, json_file)
        return "Tenants deleted"
