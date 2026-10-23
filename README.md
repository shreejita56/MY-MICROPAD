# MY-MICROPAD

<img width="891" height="648" alt="Screenshot 2026-10-24 003302" src="https://github.com/user-attachments/assets/a60790ad-d761-4995-bbf2-87d18557bb76" />


So I made a custom 2x4 Micropad based on Xiao RP2040 and it has  a rotor encoder on top . We have used diodes to prevent ghosting , the Switches are hot-swappable and it has a compact design.

<br>
The PCB Design was made on Kicad. Here I used the SMD Footprint for the Xiao Rp2040 and Hot-Swappable Footprint for the Switches . The rotor encoder at the top of the matrix also works as a switch . So In total We can use this MicroPad for 9 different Shortcuts and the rotor encoder can be used as a Volume Controller.Also It has per switch LEDS as well <br>

We have also used a Diode with each Switch , So that we can prevent Ghosting. The PCB also have few connection holes which helps it to connect with the CASE Properly.
<br>
I have tried to make the PCB design as compact as I could <br>


<br>

Lastly I made the Firmware for the PCB which I wrote completely in C language .

### Features
- 2x4 Switch Design with rotor encoder on top
- Per switch LED and Diode for ghosting
- Compact Design
- Two layered Case with base (Structured at an angle )


## Schematics 
<img width="1181" height="486" alt="Screenshot 2026-10-23 232635" src="https://github.com/user-attachments/assets/e054334a-5c89-4db8-92ec-1de596256f58" />

## PCB 

<img width="802" height="642" alt="Screenshot 2026-10-24 000340" src="https://github.com/user-attachments/assets/1246a6bd-389c-42e5-a322-e1d94b5f8e6d" />
<img width="776" height="627" alt="Screenshot 2026-10-24 000209" src="https://github.com/user-attachments/assets/7ffe7f84-312f-469d-8b2b-f08de61afe01" />

## 3D Design 
<img width="891" height="648" alt="Screenshot 2026-10-24 003302" src="https://github.com/user-attachments/assets/ca8c7c67-c1cd-4870-b75b-f2a6facf0e49" />

<img width="658" height="527" alt="Screenshot 2026-10-24 003323" src="https://github.com/user-attachments/assets/90815bef-d5f2-4878-ab2e-c0efc4a85487" />












# Bill of Materials (BOM)

| Item | Quantity | Price (USD) | Source |
|---|---:|---:|---|
| PCB + Shipping (after coupons) | 1 | $15.47 | [JLCPCB](https://jlcpcb.com/) |
| Seeed Studio XIAO RP2040 + Shipping | 1 | $5.10 | [Robocraze](https://robocraze.com/products/seeed-studio-xiao-rp2040-development-board?variant=47742255562976&country=IN&currency=INR) |
| Blank DSA Keycaps (pack of 5) | 2 packs (10 keycaps) | $1.05 | [Meckeys](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank/blank-dsa-keycaps-1u/?attribute_pa_variations=off-white) |
| HMX Snowfall Tactile Switches (pack of 10) | 1 pack (10 switches) | $3.57 | [NeoMacro](https://neomacro.in/products/hmx-snowfall-tactile-switch?variant=50878813503766) |
| Kailh Hot-Swap Sockets (pack of 10) | 1 pack (10 sockets) | $0.78 | [Meckeys](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/kailh-hot-swap-socket/) |
| Meckeys Shipping | 1 | $1.10 | [Meckeys](https://meckeys.com/) |
| Diodes | 10 pieces | $0.00 | Already owned |
| Rotary Encoder | 1 | $0.00 | Already owned |
|**TOTAL**||| **$27.07**|

**Total project cost: $27.07 USD**
