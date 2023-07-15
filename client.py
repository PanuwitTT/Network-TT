import socket

def run_client():
    client_name = "missionimpossible"
    server_address = ('localhost',12347)

    # รับตัวเลขจากผู้ใช้ผ่านแป้นพิมพ์
    client_number = int(input("ป้อนตัวเลขระหว่าง 1 ถึง 100: "))

    # สร้างเชื่อมต่อและเชื่อมต่อกับเซิร์ฟเวอร์
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # ส่งชื่อและตัวเลขของไคลเอนต์ไปยังเซิร์ฟเวอร์
    client_message = client_name + ',' + str(client_number)
    client_socket.send(client_message.encode())

    # รับข้อความจากเซิร์ฟเวอร์
    server_message = client_socket.recv(1024).decode()
    server_name, server_number = server_message.split(',')
    server_number = int(server_number)

    # แสดงชื่อของไคลเอนต์และเซิร์ฟเวอร์, ตัวเลขของไคลเอนต์และเซิร์ฟเวอร์ และคำนวณผลรวม
    print("ชื่อไคลเอนต์:", client_name)
    print("ชื่อเซิร์ฟเวอร์:", server_name)
    print("ตัวเลขของไคลเอนต์:", client_number)
    print("ตัวเลขของเซิร์ฟเวอร์:", server_number)
    print("ผลรวมของตัวเลข:", client_number + server_number)

    client_socket.close()

if __name__ == '__main__':
    run_client()
