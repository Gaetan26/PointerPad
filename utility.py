

# trouver l'adresse ip du pc dans le reseau local
# ...
def get_local_ip() -> str | None:
    
    import socket
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as test_socket:
        try:
            test_socket.connect(("8.8.8.8", 80))
            local_ip = test_socket.getsockname()[0]
       
        except Exception:
            local_ip = None
    
    return local_ip



# generer et sauvegarder un qrcode
# ...
def create_transparent_qrimage(qrimage_data:object, qrimage_dir:str) -> tuple[bool, str]:

    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import CircleModuleDrawer


    qrimage = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10, 
        border=4
    )
    
    qrimage.add_data(qrimage_data)
    qrimage.make(fit=True)
    
    qrimage = qrimage.make_image(
        image_factory=StyledPilImage, 
        module_drawer=CircleModuleDrawer(),
    ).save(qrimage_dir)

    return True, qrimage_dir