import ipaddress
import socket
import tkinter as tk
import tkinter.font as tkFont

def ip_info(ip_entry, mask_entry, output_text):
    ip = ip_entry.get()
    mask = mask_entry.get()

    if not ip and not mask:
        hostname = socket.gethostname()    
        ip = socket.gethostbyname(hostname) + '/24'
    else:
        ip = ip + '/' + mask

    ip_interface = ipaddress.ip_interface(ip)
    network = ip_interface.network
    ip_address = ip_interface.ip

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, f'IP-адрес: {ip_address}\n')
    output_text.insert(tk.END, f'Маска: {network.netmask}\n')
    output_text.insert(tk.END, f'Сеть: {network.network_address}\n')
    output_text.insert(tk.END, f'Без маски: {network.broadcast_address}\n')
    output_text.insert(tk.END, f'С маской: {network.network_address} - {network.broadcast_address}\n')

    if isinstance(ip_address, ipaddress.IPv4Address):
        if (ip_address >= ipaddress.IPv4Address('0.0.0.0')) and (ip_address <= ipaddress.IPv4Address('127.0.0.0')):
            output_text.insert(tk.END, 'Класс A\n')
        elif (ip_address >= ipaddress.IPv4Address('128.0.0.0')) and (ip_address <= ipaddress.IPv4Address('191.255.0.0')):
            output_text.insert(tk.END, 'Класс B\n')
        elif (ip_address >= ipaddress.IPv4Address('192.0.0.0')) and (ip_address <= ipaddress.IPv4Address('223.255.255.0')):
            output_text.insert(tk.END, 'Класс C\n')
        elif (ip_address >= ipaddress.IPv4Address('224.0.0.0')) and (ip_address <= ipaddress.IPv4Address('239.0.0.0')):
            output_text.insert(tk.END, 'Класс D\n')
        elif (ip_address >= ipaddress.IPv4Address('240.0.0.0')) and (ip_address <= ipaddress.IPv4Address('255.0.0.0')):
            output_text.insert(tk.END, 'Класс E\n')
        else:
            output_text.insert(tk.END, 'Адрес виртуализации\n')
    else:
        output_text.insert(tk.END, 'Это IPv6 адрес\n')

def main():
    root = tk.Tk()
    root.geometry('1000x800')
    root.title('Информация о сети')

    custom_font = tkFont.Font(family = 'TkDefaultFont')

    ip_label = tk.Label(root, text = 'IP-адрес:', font = custom_font)
    ip_label.grid(row = 0, column = 0, sticky = 'w', padx = 20, pady = 20)

    ip_entry = tk.Entry(root, font=custom_font)
    ip_entry.grid(row = 0, column = 1, sticky = 'ew', padx = 20, pady = 20)

    mask_label = tk.Label(root, text = 'Маска:', font = custom_font)
    mask_label.grid(row = 1, column = 0, sticky = 'w', padx = 20, pady = 20)

    mask_entry = tk.Entry(root, font=custom_font)
    mask_entry.grid(row = 1, column = 1, sticky = 'ew', padx = 20, pady = 20)

    output_text = tk.Text(root, font=custom_font)
    output_text.grid(row = 2, column = 0, columnspan = 2, sticky = 'nsew', padx = 20, pady = 20)

    system_info_button = tk.Button(root, text = 'Вывод', command = lambda: ip_info(ip_entry, mask_entry, output_text), font=custom_font)
    system_info_button.grid(row = 3, column = 0, columnspan = 2, sticky = 'nsew', padx = 20, pady = 20)

    root.bind('<Return>', lambda event: ip_info(ip_entry, mask_entry, output_text))

    root.grid_rowconfigure(2, weight = 1)
    root.grid_columnconfigure(1, weight = 1)

    root.mainloop()

if __name__ == '__main__':
    main()
