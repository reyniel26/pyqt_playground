# Sierpinski Triangle

- Visualize the Sierpinski Triangle

![Sierpinski_Triangle_Logo-nobg](https://user-images.githubusercontent.com/58727783/214821362-799efcb6-45c5-4b74-b36d-999a62ae0727.png)

I just see this in TikTok and I want to try it. So that I research, and created a desktop app that will emulate Sierpinski Triangle.

The Chaos Game

1. Take three points in a plane to form a triangle.
2. Randomly select any point inside the triangle and consider that your current position.
3. Randomly select any one of the three vertex points.
4. Move half the distance from your current position to the selected vertex.
5. Plot the current position.
6. Repeat from step 3.

- [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
- [Chaos Game](https://www.pythoninformer.com/generative-art/iterated-function-systems/chaos-game/)
- [How To Determine if a Point Is in a 2D Triangle](https://www.baeldung.com/cs/check-if-point-is-in-2d-triangle)
- [Applying the midpoint formula to find the midpoint between two points](https://youtu.be/6mx8HIf3oUk?t=74)

## Create Installer
Pre-condition: Must sure all required dependencies are installed.

1. Run PyInstaller
- Option 1: Create `one file` exe ( Suggested)
    ```
    pyinstaller.exe --add-data "sierpinski_triangle/*.py;./sierpinski_triangle/" --add-data "sierpinski_triangle/*.ico;."  --add-data "sierpinski_triangle/static/images/*.png;./static/images" --add-data "sierpinski_triangle/static/ui/*.ui;./static/ui" --onefile --windowed --icon=sierpinski_triangle/app.ico sierpinski_app.py
    ```
- Option 2:
    ```
    pyinstaller.exe --add-data "sierpinski_triangle/*.py;./sierpinski_triangle/" --add-data "sierpinski_triangle/*.ico;."  --add-data "sierpinski_triangle/static/images/*.png;./static/images" --add-data "sierpinski_triangle/static/ui/*.ui;./static/ui" --windowed --icon=sierpinski_triangle/app.ico sierpinski_app.py
    ```


2. Run Inno Setup
    - Compile the sierpinsi_installer_builder.iss using Inno Setup
