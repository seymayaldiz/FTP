import ftplib
f = ftplib.FTP("172.30.42.127")
try:
    f.login("ric", "12345")
    print(f.getwelcome())
    f.delete("myfile")
    print(f.dir())
    f.set_pasv(1)
    f.storbinary("STOR myfile ",open("myfile", "rb"))
    print(f.dir())
except Exception as e:
    print("Exception: ", e)
finally:
    f.close()