#Функция для извлечения IP адресов с кодом ошибок 4хх и 5хх
def extract_error_ips(log_entries):
    error_ips = []

    for entry in log_entries:
        parts = entry.split()

        if len(parts) >= 4 and parts[-2][0] in ['4', '5']:
            ip_address = parts[0]
            error_ips.append(ip_address)


    return error_ips

log_entries = [
    "192.168.1.1 - GET /home 200 1.2s",
    "192.168.1.2 - POST /login 404 0.8s",
    "192.168.1.3 - GET /profile 500 2.1s",
    "192.168.1.4 - GET /about 200 0.5s",
    "192.168.1.5 - POST /submit 403 1.5s"
]

result = extract_error_ips(log_entries)
print(result)
