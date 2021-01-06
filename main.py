import socket




if __name__ == "__main__":
    ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1
    ipv4_socket.bind(("127.0.0.1", 8000) )                          # 2
    ipv4_socket.listen(4)   
    
    resp_page = ""
    resp_status_OK = "HTTP/1.1 200 OK\r\n\r\n"
    resp_status_404 = "HTTP/1.1 404 NOT_FOUND\r\n\r\n"                                        # 3
    global filename

    print("Servidor inicializado com sucesso...\n\n")

    while True:
        (io_socket, addr) = ipv4_socket.accept()    # 4
        data_stream = io_socket.recv(1024)          # 5
        data_string = data_stream.decode("utf-8")   # 6

        

        

        print("nova requisicao vinda do cliente {}\n------\n\n".format(addr))   # 7
        print("http: \n" + data_string)                                                      # 8

        request_lines = data_string.splitlines()                    # 9


        # Firefox: as vezes o navegador envia um request vazio, este if é para checar se é um request que não vai quebrar o app
        if len(request_lines) > 4:
            request = request_lines[0].split(" ")[1]                    # 10

        print("req = {}".format(request))

        




        if request == "/":      # 11
            filename = open("index.html") 
            resp_page = filename.read()

            resp = resp_status_OK + resp_page   # 12
            io_socket.send(resp.encode("utf-8"))    # 13

            filename.close()

        elif request == "/article":     # 14
            filename = open("article.html")
            resp_page = filename.read()

            resp = resp_status_OK + resp_page
            io_socket.send(resp.encode("utf-8"))

            filename.close()

        

        elif request.split(".")[1] == "png":    # 15
            
            try:
                filename = open("images" + request, "rb")
                img = filename.read()

                resp = resp_status_OK.encode("utf-8") + img
                io_socket.send(resp)
            except:

                resp = resp_status_404.encode("utf-8") + "nao encontrado".encode("utf-8")
                io_socket.send(resp)
                
            finally:
                filename.close()

        elif request == "/style.css":       # 16
            filename = open("style.css")
            resp_page = filename.read()

            resp = resp_status_OK + resp_page

            io_socket.send(resp.encode("utf-8"))

            filename.close()


        else:
            resp_page = "<h2>Página nao encontrada!<br>Page not found!</h2>"

            resp = resp_status_404 + resp_page      # 17
            io_socket.send(resp.encode("utf-8"))
            
        
        io_socket.close()                       # 18








