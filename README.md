# Network-TT
ในกรณีนี้คุณควรรันโปรแกรมเซิร์ฟเวอร์ก่อนแล้วจึงรันโปรแกรมไคลเอนต์ เพราะโปรแกรมเซิร์ฟเวอร์จะต้องเริ่มต้นให้พร้อมให้บริการและรอรับการเชื่อมต่อจากไคลเอนต์

ดังนั้น ตามลำดับขั้นตอนดังนี้:

รันโปรแกรมเซิร์ฟเวอร์: เปิดหน้าต่างคอมมานด์ไลน์ (หรือเทอร์มินอล) แล้วเปลี่ยนไปยังไดเรกทอรีที่มีไฟล์โปรแกรมเซิร์ฟเวอร์ (server.py) แล้วใช้คำสั่ง python server.py เพื่อเริ่มต้นเซิร์ฟเวอร์

รันโปรแกรมไคลเอนต์: เปิดหน้าต่างคอมมานด์ไลน์ (หรือเทอร์มินอล) แล้วเปลี่ยนไปยังไดเรกทอรีที่มีไฟล์โปรแกรมไคลเอนต์ (client.py) แล้วใช้คำสั่ง python client.py เพื่อรันโปรแกรมไคลเอนต์

โปรแกรมเซิร์ฟเวอร์จะเริ่มต้นฟังการเชื่อมต่อและรอรับข้อมูลจากไคลเอนต์ ในขณะที่โปรแกรมไคลเอนต์จะให้คุณป้อนตัวเลขและส่งข้อมูลไปยังเซิร์ฟเวอร์ เมื่อเซิร์ฟเวอร์ได้รับข้อมูลแล้ว โปรแกรมจะแสดงผลลัพธ์ที่ไคลเอนต์และทำงานเสร็จสิ้น
