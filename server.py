import socket
import time

# AF_INET - тип адрессов с которыми будет работать сокет, IPv4,
# SOCK_STREAM - протокол по которому будет общаться сокет,
# TCP протокол, гарантированно доставляет данные, проверяет то ли дошло что нужно
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# отключить упоковывание данных в пакеты, потому что нам нужно частые отправки сообщений, а не отправка одни пакетом
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # отключаем алгоритм Нейгла
main_socket.bind(("localhost", 10000))  # 1 аргумент кортежа - IP, второе - порт, localhost - мой локальный адресс
main_socket.setblocking(False)  # непрерывная работа сервера, чтобы порт не останавливал программу в ожидании сообщения
main_socket.listen(5)  # режим прослушивания, 5 человек могут подключатся одновременно

print("Сокет создался")

players_sockets = []
while True:
    # проверка, ессть ли желающие войти в игру
    # принять новое подключение, возвращает новый сокет и адресс подключившегося игрока
    try:
        new_socket, address = main_socket.accept()
        print("Подключился ", address)
        new_socket.setblocking(False)
        players_sockets.append(new_socket)
    except BlockingIOError:
        print("Нет желающих войти в игру")

    time.sleep(1)

