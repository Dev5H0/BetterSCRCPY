# NOT TESTED WITH LINUX OR MAC


# USB 
1. Look up how to enable developer mode on your type of phone. 
2. Go te developer settings. 
3. Enable "USB Debugging". 
4. Connect your phone to computer via USB cable. 
5. Run the ".exe" file 

# Wireless (Requires connecting via USB at least once.) 
1. Open your phone and go to settings. 
2. Go to "About Phone" and then "All Specs"/"Status". 
3. Here you should scroll until you see "IP address", and write down the four-part number there. 
4. Open the "config.ini" file, and replace the number after "DEVICE_IP=" with the number you just wrote down.  
5. Run the ".exe" file. 



# Developers
I calculate the "max_size" using the sum of all of the monitors' height and width divided by the double amount of montiors, divided by two.
By doing this, I can get an average size of the montiors

   res = 0
   for n in range(len(_monitors)): res += _monitors[n].width + _monitors[n].height
   res = round(round(res/(len(_monitors)*2)/2, -1))