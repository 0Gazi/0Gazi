import netifaces

def get_wifi_ip_address():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface.startswith('wlan'):  # Wi-Fi arayüzünü seçin
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ip_address = addresses[netifaces.AF_INET][0]['addr']
                return ip_address

# ip = get_wifi_ip_address()
# if ip:
#     print("Wi-Fi IP adresiniz:", ip)
# else:
#     print("Wi-Fi bağlantısı bulunamadı veya IP adresi alınamadı.")
