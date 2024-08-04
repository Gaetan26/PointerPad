

import utility, multiprocessing
from desktopapp import app
from webserver import server



def main():
    
    local_ip = utility.get_local_ip()

    if local_ip is not None:
        server_host, server_port = local_ip, 47586
        server_addr = f"http://{server_host}:{server_port}"
        qrimage_dir = "temp/qrimage.png"
        
        utility.create_transparent_qrimage(server_addr, qrimage_dir)

        server_process = multiprocessing.Process(
            target=server.run_server,
            kwargs={ 'debug':True, 'host':server_host, 'port':server_port }
        )
        server_process.start()
        
        app.run_app("server_launched", qrimage_dir=qrimage_dir)
        server_process.join()

    else:
        app.run_app("network_error")



if __name__ == "__main__":
    main()