# ESP32-C6 GPIO Controller

A modular web-based GPIO controller for ESP32-C6 microcontroller.

## Project Structure

```
esp/
├── main.py                           # Main application entry point
├── GpioController/
│   ├── BackEnd/
│   │   └── webserver.py             # Web server and network handling
│   └── FrontEnd/
│       └── index.html               # Web interface (HTML/CSS/JS)
├── .vscode/                         # VS Code settings
├── .micropico                       # MicroPico configuration
└── esp                              # Shell script for development
```

## How to Run

### Method 1: Complete Project Upload (Recommended)
Use the automated upload script to deploy your entire project:

```bash
# Upload the complete project structure
./upload_project.sh

# After upload, run the application
./esp run main.py
```

**What the upload script does:**
- ✅ Activates virtual environment automatically
- ✅ Checks ESP32 connection
- ✅ Creates proper directory structure on ESP32
- ✅ Uploads only project files (not development tools)
- ✅ Verifies successful upload
- ✅ Optional cleanup of old files

### Method 2: Using MicroPico (Good for Development)
1. Open VS Code in this folder
2. Upload files individually using MicroPico:
   - Upload `main.py`
   - Upload `GpioController/BackEnd/webserver.py`
   - Upload `GpioController/FrontEnd/index.html`
3. Run `main.py` using MicroPico
4. Access the web interface at the displayed IP address

### Method 3: Manual Command Line Upload
```bash
# Create directory structure
./esp exec "import os; os.mkdir('GpioController')"
./esp exec "import os; os.mkdir('GpioController/BackEnd')"
./esp exec "import os; os.mkdir('GpioController/FrontEnd')"

# Upload files
./esp upload main.py
./esp upload GpioController/BackEnd/webserver.py GpioController/BackEnd/webserver.py
./esp upload GpioController/FrontEnd/index.html GpioController/FrontEnd/index.html

# Run application
./esp run main.py
```

### Method 4: Quick Development Workflow
```bash
# For rapid testing during development
./esp update main.py  # Upload and run main.py only
```

**Note:** Method 4 only works if the GpioController folder structure already exists on the ESP32.

## Architecture

### Backend (`GpioController/BackEnd/`)
- **webserver.py**: Handles WiFi connection, HTTP server, and will handle GPIO control

### Frontend (`GpioController/FrontEnd/`)
- **index.html**: Web interface with controls for GPIO pins

### Main Application (`main.py`)
- Orchestrates backend and frontend
- Provides clean startup sequence
- Handles application lifecycle

## Development Workflow

1. **Frontend Development**: Edit `GpioController/FrontEnd/index.html`
2. **Backend Development**: Edit `GpioController/BackEnd/webserver.py` 
3. **Test Changes**: Upload and run `main.py`

## Next Steps

To add GPIO control functionality:

1. **Research GPIO control** in MicroPython (`machine.Pin`)
2. **Add URL routing** to webserver.py for handling `/gpio/pin/action` requests
3. **Implement GPIO functions** in backend
4. **Connect frontend buttons** to backend API endpoints

## Configuration

- WiFi credentials are in `GpioController/BackEnd/webserver.py`
- GPIO pin mappings can be customized in the frontend HTML
- MicroPico settings are in `.vscode/settings.json`

## Upload Script Usage

### Basic Usage
```bash
./upload_project.sh
```

### Script Features
- **Connection Check**: Automatically verifies ESP32 is connected
- **Smart Upload**: Only uploads project files, not development tools
- **Directory Creation**: Creates proper folder structure on ESP32
- **Cleanup Option**: Optionally removes old project files before upload
- **Verification**: Lists uploaded files to confirm success
- **Color Output**: Easy-to-read colored status messages

### Files Uploaded by Script
```
ESP32:/
├── main.py                           # Main application
└── GpioController/
    ├── BackEnd/
    │   └── webserver.py             # Web server module
    └── FrontEnd/
        └── index.html               # Web interface
```

### Troubleshooting Upload Script

**Error: "ESP32 not connected or not accessible"**
- Check USB connection
- Verify ESP32 is powered on
- Check if another program is using the serial port
- Try: `ls -la /dev/ttyACM*` to see available devices
- Add user to dialout group: `sudo usermod -a -G dialout $USER`

**Error: "Permission denied"**
- Make script executable: `chmod +x upload_project.sh`
- Check serial port permissions: `sudo chmod 666 /dev/ttyACM0`

**Error: "Failed to upload file"**
- ESP32 might be running code that blocks file operations
- Try resetting ESP32: `./esp reset`
- Try stopping running code: Press Ctrl+C in MicroPico vREPL

**Script says "File not found"**
- Ensure you're running the script from the esp/ directory
- Check that all project files exist in the correct locations