# HzCheck  
HzCheck is a Python library that provides various tools for retrieving information about a network and its devices. It was created to help people get network information using Python.

I started this project just a week ago, and I've already added a bunch of useful functions that allow you to get information such as the WiFi name, the devices connected to the WiFi, the IP addresses of devices, and more.

## Installation  
To install HzCheck, simply use git:

***`git clone https://github.com/MucciDev/HzCheck.git`***

#### Note: You need to have git installed, otherwise you wont be able to install it.

## Usage  
Here's an example of how to use the library to get the WiFi name and the devices connected to it:

**`import HzCheck`**  
`wifi_name = HzCheck.getwifi()`  
`print(f'WiFi name: {wifi_name}')`  
`devices = HzCheck.getinfo()`  
`print(f'Connected devices: {devices}')`  

You can find more detailed documentation for each function in the library in the documentation file.

## Contributing  
If you'd like to contribute to the project, please feel free to open a pull request on GitHub.

## License  
This project is licensed under the MIT License - see the LICENSE file for details.

# HzCheck Documentation

## Functions
 
#### getwifi()
This function returns the name of the WiFi network that the device is connected to.

#### getinfo()
This function returns a list of the IP addresses of devices that are connected to the same WiFi network as the device running the library.

#### showinfo()
This function returns the IP address, MAC address, and hostname of a specific device on the network. The device_name parameter should be the hostname or IP address of the device.

#### ping(target, num_bytes)
This function sends num_bytes of data to the specified target IP address or domain name and returns True if the target responds, and False if it does not.

#### trc(target)
This function traces the route to the specified target IP address or domain name and returns a list of the IP addresses of the intermediate hops.

#### netscan()
This function scans for nearby WiFi networks and returns a list of the SSID (name) of the detected networks.

#### prtscan(ip_address)
Scans the specified IP address for open ports.

#### rvrshl(ip_address, port)
Establishes a reverse shell connection to the specified IP address and port.
