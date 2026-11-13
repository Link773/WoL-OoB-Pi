# WoL-OoB-Pi

This project involves using email to send a code from a particular email to a Raspberry Pi to turn on a computer from outside the network. This is a part of a greater project I had to be able to at least mostly securely access my desktop from an environment outside of the house, like at school where I cannot feasibly bring my desktop on a weekly basis.

Originally I believed the particular desktop did not have a Wake-On-LAN feature and actually was going to use the Raspberry Pi connected to the power switch connectors to communicate directly with the motherboard to turn on. However, It's rather difficult to safely manage a connection between the two devices as well as mount the raspberry pi in my metal case in such a way that would not be "jank" and unprofessional.

I have since determined my motherboard does have Wake-On-LAN capabilities strictly through the ethernet port, however not the built in Wifi antenna, so my current solution is to allow both devices their configured connections to the same network as well as an ethernet cable directly communicating between the two and using the Raspberry Pi to receive the out-of-band message via WiFi (as the setup in question is inconvenient for wired connection in the residence) and connect it directly to the desktop with an ethernet cable.


