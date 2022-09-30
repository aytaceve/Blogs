import json

import redis

redis = redis.Redis(host="localhost", port=6379, db=0)


# def set_names() -> None:
#     names = [
#         'John', 'Michael', 'Jim',
#     ]
#
#     redis.lpush("name", *names)
#
#
# def get_names() -> list:
#     names = redis.lrange("name", 0, -1)
#     names = [name.decode("utf-8") for name in names]
#     return names

#     return redis.lrange("name", 0, -1)


def main() -> None:
    money = [
        {
            'value': 500,
            'currency': 'USD',
        },
        {
            'value': 200,
            'currency': 'AZN',
        },
    ]

    money = json.dumps(money)

    redis.set("money", money)

    print(json.loads(redis.get("money")))


if __name__ == "__main__":
    print(main())

