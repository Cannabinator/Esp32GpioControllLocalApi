"""
Main Application Entry Point
ESP32-C6 GPIO Controller

This file orchestrates the frontend and backend components.
"""

# Import backend modules
from GpioController.BackEnd.webserver import connect_wifi, create_web_server

def main():
    """Main application entry point"""
    print("=" * 50)
    print("ESP32-C6 GPIO Controller Starting...")
    print("=" * 50)
    
    # Step 1: Connect to WiFi
    print("Step 1: Connecting to WiFi...")
    ip = connect_wifi()
    
    if not ip:
        print("❌ Failed to connect to WiFi!")
        print("Cannot start application without network connection.")
        return
    
    print(f"✅ WiFi connected! IP: {ip}")
    
    # Step 2: Start Web Server
    print("Step 2: Starting web server...")
    print(f"🌐 Web interface available at: http://{ip}")
    print("📱 Open this URL in your browser to control GPIO pins")
    print("\nPress Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        create_web_server()
    except KeyboardInterrupt:
        print("\n" + "=" * 50)
        print("Application stopped by user")
        print("=" * 50)
    except Exception as e:
        print(f"\n❌ Application error: {e}")

if __name__ == "__main__":
    main()