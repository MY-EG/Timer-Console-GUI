# TimeTaskMaster
## Description
This Python script provides a countdown timer with customizable actions to perform after the countdown finishes. It allows users to specify the countdown duration and select from a list of actions to execute, such as shutting down the PC, sending notifications, playing music, and more.

## Features
- Countdown timer with hours, minutes, and seconds inputs.
- Flexible action selection after countdown completion.
- Actions include shutting down, restarting the PC, sending notifications, playing music, opening files/links, running custom commands, etc.
- Customizable notification messages and icons.
- Ability to hide the console window during countdown execution.

## Dependencies
- **os**: For system operations like hiding the console window, shutting down, and restarting the PC.
- **time**: For time-related functions and delays.
- **datetime**: For timedelta calculation and formatting.
- **pygame**: For playing music files.
- **webbrowser**: For opening links in the default web browser.
- **plyer**: For sending desktop notifications.
- **tkinter**: For file dialogs to select files/links.
- **win32gui, win32con**: For hiding the console window on Windows systems.

## Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies using pip:
    ```
    pip install pygame
    pip install pygame plyer
    pip install win32gui
    pip install win32con
    ```
4. Run the script:
    ```
    python timer.py
    ```

## Usage
1. Run the script and follow the prompts to set the countdown time and select actions.
2. Optionally, choose to hide the console window during countdown execution.
3. After the countdown finishes, the selected action will be executed automatically.

## Screenshots
![image](https://github.com/MYounesEG/TimeTaskMaster/assets/158834031/228359d3-4833-47d2-9e47-b323a99adf7b)
![image](https://github.com/MYounesEG/TimeTaskMaster/assets/158834031/ce559c6c-75f5-42b9-a187-dbd596a6c5d1)
![image](https://github.com/MYounesEG/TimeTaskMaster/assets/158834031/1929411f-7195-4728-ae02-71a0b205d385)
![image](https://github.com/MYounesEG/TimeTaskMaster/assets/158834031/c7e8aa46-824d-4414-9456-394fda1de1ef)
![image](https://github.com/MYounesEG/TimeTaskMaster/assets/158834031/5cfd8bd6-aeaa-47e4-acda-cb85d42536fe)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
