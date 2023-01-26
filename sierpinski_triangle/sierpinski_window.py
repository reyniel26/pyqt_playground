import os

import pandas as pd
import pyqtgraph as pg
from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog, QMainWindow

from .config import VERSION, static_image_path, static_ui_path
from .sierpinski import SierpinskiTriangle


class SierpinskiTriangleWindow(QMainWindow,SierpinskiTriangle):

    def __init__(self):
        super().__init__()

        ui_file = static_ui_path("sierpinski_window.ui")
        uic.loadUi(ui_file,self)

        self.setWindowTitle("Sierpinski Triangle Emulator")

        iconpath = static_image_path("Sierpinski_Triangle_Logo-nobg.png")

        if os.path.exists(iconpath):
            self.setWindowIcon(QIcon(iconpath))

        self.center_form()

        self.version_label.setText(VERSION)

        self.graph_widget.setBackground('w')
        self.graph_widget.showGrid(x=True,y=True)

        self.step_at.setText("0")
        self.step_all.setText("0")

        self.action_reset.triggered.connect(self.reset)
        self.action_generate_all.triggered.connect(self.generate_all)
        self.action_run_chaos.triggered.connect(self.run_chaos_game)
        self.action_export.triggered.connect(self.export_points)
        self.action_import.triggered.connect(self.import_points)

        self.generate_triangle_btn.clicked.connect(self.generate_valid_triangle)
        self.generate_starting_point_btn.clicked.connect(self.generate_random_point)
        self.generate_steps_btn.clicked.connect(self.generate_random_steps)
        self.generate_all_btn.clicked.connect(self.generate_all)

        self.run_chaos_btn.clicked.connect(self.run_chaos_game)

        self.start_btn.clicked.connect(self.start_step)
        self.end_btn.clicked.connect(self.end_step)
        self.prev_btn.clicked.connect(self.previous)
        self.next_btn.clicked.connect(self.next)


    def center_form(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_range(self):
        self.range = self.scale_num.value()

    def reset(self):
        self.scale_num.setValue(100)
        self.generate_valid_triangle()
        self.point_s_x.setValue(0)
        self.point_s_y.setValue(0)
        self.num_steps.setValue(0)
        self.status_browser.clear()
        self.step_at.setText("0")
        self.step_all.setText("0")
        self.graph_widget.clear()

    def export_points(self):
        self.status_browser.clear()
        self.status_browser.append("Exporting points")
        try:
            savefilename, _ = QFileDialog.getSaveFileName(
                self, "Save as",
                os.path.join("","sierpinski triangle points"),
                "Sheet data files (*.csv)"
            )

            points_x = self.get_tri_point_x()
            points_x.append(self.point_s_x.value())
            points_x.extend(self.get_points_x())

            points_y = self.get_tri_point_y()
            points_y.append(self.point_s_y.value())
            points_y.extend(self.get_points_y())

            label = ["a","b","c","starting_point"]
            label.extend([f"step#{step+1}" for step in range(len(self.get_points()))])
            points = {
                "label":label,
                "x":points_x,
                "y":points_y,

            }

            df = pd.DataFrame(points)

            if savefilename:
                df.to_csv(savefilename,index=False)
                self.status_browser.append(f"Points has been exported to:\n{savefilename}")
            else:
                self.status_browser.append("Canceled import")
        except:
            self.status_browser.append("Error occur")

    def import_points(self):
        self.status_browser.clear()
        self.status_browser.append("Importing points")
        try:
            # Import file
            filename, _ = QFileDialog.getOpenFileName(
                self,'Import points',"",'Sheet data files (*.csv)')
            if filename:
                # validate file
                df = pd.read_csv(filename)
                if not set(['x','y']).issubset(df.columns):
                    return False

                if df.shape[0] < 4:
                    return False
                df = df[["x","y"]]
                triangle = list(df.iloc[0:3].itertuples(index=False, name=None))
                starting_point = list(df.iloc[4])
                points = list(df.drop(df.iloc[[0,4]].index).itertuples(index=False, name=None))

                if not self.is_60_angle(triangle):
                    self.status_browser.append("The data has no valid triangle")
                    return False

                if not self.is_inside_triangle(starting_point,triangle):
                    self.status_browser.append(
                        "The staring point is not inside of triangle")
                    return False

                self.set_vertices(triangle)
                self.scale_num.setValue(triangle[2][0])
                self.show_triangle_coor()
                self.point_s_x.setValue(int(starting_point[0]))
                self.point_s_y.setValue(int(starting_point[1]))
                self.set_points(points)
                self.num_steps.setValue(len(points))
                self.run_chaos_game_step(len(points))

                # place values

        except Exception as e:
            self.status_browser.append("Error occur")
            print(f"Error: {e} Type: {type(e)}")

    def show_triangle_coor(self):
        vertices = self.get_vertices()
        for index,point in enumerate([self.point_a,self.point_b,self.point_c]):
            point.setText(f"( {round(vertices[index][0],3)} , {round(vertices[index][1],3)} )")

    def generate_valid_triangle(self):
        self.set_range()
        super().generate_valid_triangle()
        self.show_triangle_coor()

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
        self.step_at.setText("0")
        self.step_all.setText(str(self.num_steps.value()))

    def scatter_points(self,x_data,y_data,point_color="points"):
        color ={
            "triangle":pg.mkBrush(255, 0, 50),
            "start":pg.mkBrush(255, 139, 19),
            "points":pg.mkBrush(33, 150, 243, 120)
        }
        scatter = pg.ScatterPlotItem(size=10, brush=color[point_color])
        scatter.addPoints(x_data, y_data)
        return scatter

    def run_chaos_game_step(self,steps,is_step=True):
        """Run Chaos Game by steps"""

        self.status_browser.clear()
        self.status_browser.append(("-"*10))
        self.status_browser.append(f"Running Chaos Game")

        starting_point=(self.point_s_x.value(),self.point_s_y.value())
        if self.is_inside_triangle(starting_point,self.get_vertices()):
            self.status_browser.append(f"Starting point - {starting_point} ")

            if not is_step:
                super().run_chaos_game(starting_point, steps)

            if len(self.get_points())<=0:
                self.status_browser.append(f"**Run the Chaos Game first**")
                return False

            self.graph_widget.clear()
            self.graph_widget.addItem(
                self.scatter_points(
                    self.get_tri_point_x(),self.get_tri_point_y(),"triangle"))

            self.graph_widget.addItem(
                self.scatter_points(
                    [self.point_s_x.value()],[self.point_s_y.value()],"start"))

            self.graph_widget.addItem(
                self.scatter_points(
                    self.get_points_x(steps),self.get_points_y(steps),"points"))

            for step,point in enumerate(self.get_points(steps)):
                self.status_browser.append(f"Step #{step+1} - {point}  ")

            self.step_at.setText(str(steps))
            self.step_all.setText(str(self.num_steps.value()))
        else:
            self.status_browser.append(
                f"The Starting point {starting_point} is not inside of the triangle"
                )

    def run_chaos_game(self):
        """Re-run the chaos game"""
        steps = self.num_steps.value()
        self.run_chaos_game_step(steps,is_step=False)

    def start_step(self):
        self.run_chaos_game_step(0)

    def end_step(self):
        self.run_chaos_game_step(self.num_steps.value())

    def previous(self):
        steps = int(self.step_at.text())-1
        steps = steps if steps > 0 else 0
        self.run_chaos_game_step(steps)

    def next(self):
        steps = int(self.step_at.text())+1
        max_steps = self.num_steps.value()
        steps = steps if steps < max_steps else max_steps
        self.run_chaos_game_step(steps)