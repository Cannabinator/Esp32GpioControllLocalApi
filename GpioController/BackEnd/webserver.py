"""
Simple Web Server for ESP32-C6
Serves "Hello World" on a local web page
"""

import network
import socket
import time

# WiFi credentials - CHANGE THESE TO YOUR NETWORK
WIFI_SSID = "WLAN-426995"
WIFI_PASSWORD = "25988947440139653899"

def connect_wifi():
    """Connect to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        # Wait for connection
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            print('Connecting...', timeout)
            time.sleep(1)
            timeout -= 1
    
    if wlan.isconnected():
        print('WiFi connected!')
        print('IP address:', wlan.ifconfig()[0])
        return wlan.ifconfig()[0]
    else:
        print('WiFi connection failed!')
        return None

def load_frontend():
    """Load HTML content from frontend folder"""
    try:
        with open('GpioController/FrontEnd/index.html', 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading frontend: {e}")
        return "<h1>Error: Could not load frontend</h1>"

def create_web_server():
    """Create and start the web server"""
    html = load_frontend()
    
    # Create socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    
    print('Web server running on http://{}:80'.format(connect_wifi()))
    print('Press Ctrl+C to stop')
    
    while True:
        try:
            cl, addr = s.accept()
            print('Client connected from', addr)
            
            # Read request
            request = cl.recv(1024).decode('utf-8')
            print('Request:', request.split('\n')[0])
            
            # Send response
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html
            cl.send(response.encode('utf-8'))
            cl.close()
            
        except KeyboardInterrupt:
            print('\nShutting down web server...')
            s.close()
            break
        except Exception as e:
            print('Error:', e)
            try:
                cl.close()
            except:
                pass

# This module provides web server functionality
# Main execution is handled by main.py