import sys

import pyqtgraph as pg
from path_config import static_image_path, static_ui_path
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from sierpinski import SierpinskiTriangle


class SierpinskiTriangleWindow(QMainWindow,SierpinskiTriangle):

    def __init__(self):
        super().__init__()

        ui_file = static_ui_path("sierpinski_window.ui")
        uic.loadUi(ui_file,self)

        self.setWindowTitle("Sierpinski Triangle Emulator")

        self.graph_widget.setBackground('w')
        self.graph_widget.showGrid(x=True,y=True)

        self.step_at.setText("0")
        self.step_all.setText("0")

        self.generate_triangle_btn.clicked.connect(self.generate_valid_triangle)
        self.generate_starting_point_btn.clicked.connect(self.generate_random_point)
        self.generate_steps_btn.clicked.connect(self.generate_random_steps)
        self.generate_all_btn.clicked.connect(self.generate_all)

        self.run_chaos_btn.clicked.connect(self.run_chaos_game)



    def set_range(self):
        self.range = self.scale_num.value()

    def reset(self):
        self.scale_num.setValue(1)
        self.generate_valid_triangle()

    def generate_valid_triangle(self):
        self.set_range()
        self.point_a.setText(str(self.range))
        super().generate_valid_triangle()
        vertices = self.get_vertices()
        for index,point in enumerate([self.point_a,self.point_b,self.point_c]):
            point.setText(f"( {round(vertices[index][0],3)} , {round(vertices[index][1],3)} )")

    def generate_random_point(self):
        self.set_range()
        point = self.get_random_point()
        self.point_s_x.setValue(point[0])
        self.point_s_y.setValue(point[1])

    def generate_random_steps(self):
        self.num_steps.setValue(super().generate_random_steps())

    def generate_all(self):
        self.generate_valid_triangle()
        self.generate_random_point()
        self.generate_random_steps()

    def scatter_points(self,x_data,y_data,point_color="points"):
        color ={
            "triangle":pg.mkBrush(255, 0, 50),
            "start":pg.mkBrush(255, 139, 19),
            "points":pg.mkBrush(32, 82, 149, 120)
        }
        scatter = pg.ScatterPlotItem(size=10, brush=color[point_color])
        scatter.addPoints(x_data, y_data)
        return scatter

    def run_chaos_game(self):
        self.status_browser.clear()
        self.status_browser.append(("-"*10))
        self.status_browser.append(f"Running Chaos Game")
        starting_point=(self.point_s_x.value(),self.point_s_y.value())
        if self.is_inside_triangle(starting_point,self.get_vertices()):
            steps = self.num_steps.value()
            self.status_browser.append(f"Starting point - {starting_point} ")
            super().run_chaos_game(starting_point, steps)

            self.graph_widget.clear()
            self.graph_widget.addItem(
                self.scatter_points(
                    self.get_tri_point_x(),self.get_tri_point_y(),"triangle"))

            self.graph_widget.addItem(
                self.scatter_points(
                    [self.point_s_x.value()],[self.point_s_y.value()],"start"))

            self.graph_widget.addItem(
                self.scatter_points(
                    self.get_points_x(),self.get_points_y(),"points"))

            for step,point in enumerate(self.get_points()):
                self.status_browser.append(f"Step #{step+1} - {point}  ")

            self.step_at.setText("1")
            self.step_all.setText(str(self.num_steps.value()))
        else:
            self.status_browser.append(
                f"The Starting point {starting_point} is not inside of the triangle"
                )





app = QApplication(sys.argv)

sierpinski_window = SierpinskiTriangleWindow()
sierpinski_window.show()

try:
    app.exec()
except Exception as error:
    print("Exiting..")

app.exit()

