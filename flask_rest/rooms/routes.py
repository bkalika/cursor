import json

from flask import request
from flask_restful import Resource

from rooms.parser import parser
from rooms.models import Room
from utils import read_data, write_data

json_file = 'rooms/rooms.json'
json_data = read_data(json_file)
rooms_data = json.load(open(json_file))


class Rooms(Resource):
    def get(self, status=None):
        if status is None:
            args = parser.parse_args(strict=True)
            if args.status is not None:
                info_room = []
                for room in json_data:
                    if room.get("status") == args.get("status"):
                        info_room.append(room)
                return info_room
            else:
                return json_data
        elif status:
            for room in json_data:
                if room.get("number") == status:
                    return room
            else:
                return "404 room not found"

    def post(self):
        data = request.json
        parser.parse_args(strict=True)
        for room in json_data:
            if room.get("number") == data["number"]:
                return "Room exist"
        else:
            rooms_data.append(Room(
                data["number"],
                data["level"],
                data["status"],
                data["price"],
            ).to_dict())
            write_data(rooms_data, json_file)
            return "Room added"

    def patch(self):
        data = request.json
        for room in rooms_data:
            if room.get("number") == data.get("number", 1):
                room.update(data)
        write_data(rooms_data, json_file)
        return "Room updated"

    def delete(self):
        data = request.json
        for room in range(len(rooms_data)):
            if rooms_data[room].get("number") == data.get("number"):
                del rooms_data[room]
                break
        else:
            return "Room not found"
        write_data(rooms_data, json_file)
        return "Room deleted"
