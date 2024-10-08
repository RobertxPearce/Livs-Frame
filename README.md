### HAPPY BIRTHDAY LIV!

## How to Use
1. **SSH into Pi**
   ```bash
   ssh user@piframe
   ```
3. **Move to Directory**
   ```bash
   cd /Desktop/Livs-Frame/Code
   ```
4. **Run the Program**
   ```bash
   python3 image_static.py
   ```
   ```bash
   python3 image_loop.py
   ```
5. **Run Loop in Background**
   ```bash
   nohup python3 image_loop.py &
   ```
6. **To Kill Program**
    ```bash
    ps aus | grep image_loop.py
    ```
    ```bash
    kill <PID>
    ```

## Files
### Code
* Directory for custom code to operate display.
### Photos
* Photo albums I made for display.
  * `Jiji`: Photos you sent me of Jiji :).
  * `Ghibli`: *Aesthetic* Ghibli art.
  * `Anime`: Cool anime photos and covers.
  * `Cats`: Crazy *aesthetic* photos of cats.
  * `Halloween`: Halloween themed photos because its october.
### Resources
* Resources from Pimoroni and Thingiverse.
  * `Inky Impression 7.3`: Directory for Inky Impression display resources.
      * `inky-main`: Pimoroni libraires, tools, and example code.
      * `Schematics`: Schematics for the display
      * `Drawing`: Drawing of the display for dimensions.
  * `Cases`: 3D print files for display case.

## Build Process

### Tech Assembly 🔧
* Components
  * Inky Impression 7.3" (7 colour ePaper/E Ink HAT) by Pimoroni
  * Raspberry Pi Zero 2 W WH
  * 32gb Micro SD Card (Headless Pi OS)

### Code 💻

* `loop_photos.py`: Program to loop through a collection of photos.


* `static_photo.py`: Program to display a static photo.




