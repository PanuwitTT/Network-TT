import socket

def run_server():
    server_name = "missionimpossible"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost',12347))
    server_socket.listen(1)
    print("เซิร์ฟเวอร์กำลังฟังการเชื่อมต่อ...")

    while True:
        client_socket, address = server_socket.accept()
        print("เชื่อมต่อกับไคลเอนต์:", address)

        # รับข้อความจากไคลเอนต์
        client_message = client_socket.recv(1024).decode()
        client_name, client_number = client_message.split(',')
        client_number = int(client_number)

        # แสดงชื่อไคลเอนต์และเซิร์ฟเวอร์
        print("ชื่อไคลเอนต์:", client_name)
        print("ชื่อเซิร์ฟเวอร์:", server_name)

        # เลือกตัวเลขของเซิร์ฟเวอร์และคำนวณผลรวม
        server_number = 42  # เลขตัวอย่างของเซิร์ฟเวอร์ คุณสามารถเปลี่ยนแปลงตัวเลขนี้ได้
        sum_of_numbers = client_number + server_number

        # แสดงตัวเลขของไคลเอนต์และเซิร์ฟเวอร์รวมกัน
        print("ตัวเลขของไคลเอนต์:", client_number)
        print("ตัวเลขของเซิร์ฟเวอร์:", server_number)
        print("ผลรวมของตัวเลข:", sum_of_numbers)

        # ส่งชื่อเซิร์ฟเวอร์และตัวเลขกลับไปยังไคลเอนต์
        server_message = server_name + ',' + str(server_number)
        client_socket.send(server_message.encode())

        client_socket.close()
        print("ปิดการเชื่อมต่อ.")

if __name__ == '__main__':
    run_server()
