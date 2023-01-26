# Sierpinski Triangle

- Visualize the Sierpinski Triangle

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
Pre-condition: Must be inside of sierpinski_triangle module before running this
1. Run PyInstaller
- Option 1: Create `one file` exe ( Suggested)
    ```
    pyinstaller.exe --add-data "*.ico;."  --add-data "static/images/*.png;./static/images"  --add-data "static/images/*.jpg;./static/images"  --add-data "static/ui/*.ui;./static/ui" --onefile --windowed --icon=app.ico app.py
    ```
- Option 2:
    ```
    pyinstaller.exe --add-data "*.ico;."  --add-data "static/images/*.png;./static/images"  --add-data "static/images/*.jpg;./static/images"  --add-data "static/ui/*.ui;./static/ui" --windowed --icon=app.ico app.py
    ```