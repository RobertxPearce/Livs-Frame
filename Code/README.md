# Code 💻

## loop_photos.py
Program to loop through a album of photos.
* To run use command: `python loop_photos.py`
* Update album shown edit: `directory_path = '../Photos/<Album Name>/'`
* Change duration of delay edit: `time.sleep(<TIME IN SECONDS>)`

## static_photo.py
Program to display a static photo.
* To run use command: `python static_photo.py`
* Update photo shown edit: `image_path = '../Photos/<Album Name>/<Photo>'`

## How to Use
1. **SSH into Pi**
2. **Move to Directory**
   ```bash
   cd /Desktop/livs-frame/Code
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
