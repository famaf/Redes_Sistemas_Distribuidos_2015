# 200...:HTTP => SERVER
# 192...:PUERTO => CLIENTE
[
    {'src': '192.168.1.3:38774', 'ack': False, 'dst': '200.16.17.104:http', 'syn': True, 'rst': False, 'fin': False},
    {'src': '192.168.1.3:38774', 'ack': False, 'dst': '200.16.17.104:http', 'syn': False, 'rst': True, 'fin': False},
    {'src': '192.168.1.3:38774', 'ack': False, 'dst': '200.16.17.104:http', 'syn': True, 'rst': False, 'fin': False},
    {'src': '200.16.17.104:http', 'ack': False, 'dst': '192.168.1.3:38774', 'syn': True, 'rst': False, 'fin': False},
    {'src': '192.168.1.3:38774', 'ack': True, 'dst': '200.16.17.104:http', 'syn': False, 'rst': False, 'fin': False},
    {'src': '192.168.1.3:38774', 'ack': False, 'dst': '200.16.17.104:http', 'syn': False, 'rst': False, 'fin': True},
    {'src': '192.168.1.3:38774', 'ack': False, 'dst': '200.16.17.104:http', 'syn': False, 'rst': False, 'fin': False},
    {'src': '200.16.17.104:http', 'ack': False, 'dst': '192.168.1.3:38774', 'syn': False, 'rst': False, 'fin': True},
    {'src': '192.168.1.3:38774', 'ack': True, 'dst': '200.16.17.104:http', 'syn': False, 'rst': False, 'fin': False}
]