import paho.mqtt.publish as publish

msgs = \
[
    {
        'topic':"/fish_db/Feed",
        'payload':"9876"
    },

    (
        "/fish_db/Oxygen",
        "1235", 0, False
    )
]
publish.multiple(msgs, hostname="175.121.249.37", port= 8137)
#Topic 에 문자값 multiple 1, multiple 2를 발행한다.