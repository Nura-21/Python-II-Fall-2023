
import customtkinter as tk
import messages as msg
import methods as m
import re
from CTkMessagebox import CTkMessagebox
from functools import partial
from vector import Vector
from config import config


tk.set_appearance_mode(config['window']['mode'])
tk.set_default_color_theme(config['window']['theme'])
tk.set_widget_scaling(config['window']['scale'])
tk.set_window_scaling(config['window']['scale'])


class Window(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config['window']['title'])
        self.geometry(config['window']['size'])
        self.grid_columnconfigure(0, weight=1)

        self.methods = [
            m.ADD,
            m.SUB,
            m.MUL,
            m.MAGNITUDE,
            m.DISTANCE,
            m.DOT,
            m.CROSS,
            m.NORMALIZE,
            m.LAGR,
            m.L_DEP,
            m.L_COMB,
            m.L_REG,
            m.GS]

        self.has_input = False
        self.has_second_input = False
        self.has_second_input_created = False
        self.has_coeffs_input = False
        self.has_result = False

        self.create_vector_input()

    def show_error(self, e):
        CTkMessagebox(
            title="Error", message=e, icon="cancel")

    def show_info(self, i):
        CTkMessagebox(title="Info", message=i)

    def show_success(self, s):
        CTkMessagebox(title='Success', message=s,
                      icon="check")

    def destroy_result(self):
        if self.has_result == True:
            self.has_result = False

    def destroy_second_input(self):
        if self.has_second_input == True:
            self.has_second_input = False
            self.second_input_frame.destroy()
        if self.has_second_input_created == True:
            self.has_second_input_created = False
            self.second_input_frame.destroy()

    def destroy_coeffs_input(self):
        if self.has_coeffs_input == True:
            self.has_coeffs_input = False
            self.coeffs_input_frame.destroy()

    def show_result(self, result=None):
        try:
            self.result_frame = tk.CTkFrame(self)
            self.result_frame.grid(row=5, column=0, pady=10)

            line_result_label = tk.CTkLabel(
                self.result_frame, text='Result: ')
            line_result_label.grid(row=0, column=0, padx=10)

            line_result = tk.CTkEntry(self.result_frame)
            line_result.grid(row=0, column=1)
            line_result.insert(0, result)
            line_result.configure(state='readonly')

            copy_result_btn = tk.CTkButton(
                self.result_frame, text='Copy', width=40, command=partial(
                    self.copy, result))
            copy_result_btn.grid(row=0, column=2)
            self.has_result = True
        except Exception as e:
            self.show_error(e)

    def copy(self, text=None):
        try:
            if text != None:
                self.clipboard_clear()
                self.clipboard_append(text)
                self.show_success(msg.SUCCESS)
        except Exception as e:
            self.show_error(e)

    def create_vector_input(self):
        if self.has_result == True:
            self.destroy_result()
        self.input_frame = tk.CTkFrame(self)
        self.input_frame.grid(row=0, column=0, pady=20)

        vector_input_label = tk.CTkLabel(
            self.input_frame, text="Vector value (ex: [1,2,3]):")
        vector_input_label.grid(row=0, column=0, padx=10, pady=10)

        self.vector_input = tk.CTkEntry(self.input_frame)
        self.vector_input.grid(row=0, column=1, padx=10)

        set_vector_value_btn = tk.CTkButton(
            self.input_frame, text='Set', command=self.set_vector_value)
        set_vector_value_btn.grid(row=1, columnspan=2, pady=(0, 10))

    def create_second_vector_input(self, method):
        self.destroy_result()
        self.second_input_frame = tk.CTkFrame(self)
        self.second_input_frame.grid(row=1, column=0, pady=20)

        vector_input_label = tk.CTkLabel(
            self.second_input_frame, text="Second vector (ex: [4,5,6]):")
        vector_input_label.grid(row=0, column=0, padx=10, pady=10)

        self.second_vector_input = tk.CTkEntry(self.second_input_frame)
        self.second_vector_input.grid(row=0, column=1, padx=10)

        self.set_second_vector_value_btn = tk.CTkButton(
            self.second_input_frame, text='Set second', command=partial(self.set_second_vector_value, method))
        self.set_second_vector_value_btn.grid(
            row=1, columnspan=2, pady=(0, 10))
        self.has_second_input_created = True

    def create_coeffs_input(self, method):
        self.destroy_result()
        self.coeffs_input_frame = tk.CTkFrame(self)
        self.coeffs_input_frame.grid(row=2, column=0, pady=10)

        coeffs_label = tk.CTkLabel(
            self.coeffs_input_frame, text='Coeffs (ex "1,2"):')
        coeffs_label.grid(row=0, column=0, padx=10)

        self.coeffs_input = tk.CTkEntry(self.coeffs_input_frame)
        self.coeffs_input.grid(row=0, column=1)

        set_coeffs_btn = tk.CTkButton(
            self.coeffs_input_frame, text='Set coeffs', width=40, command=partial(self.set_coeffs, method))
        set_coeffs_btn.grid(row=0, column=2, )

    def set_coeffs(self, method):
        try:
            coeffs_value = self.coeffs_input.get().strip().split(',')
            if len(coeffs_value) != 2:
                raise Exception(msg.EMPTY_INPUT_OR_WRONG_FORMAT)
            self.coeffs = [float(i) for i in coeffs_value]
            self.has_coeffs_input = True
            self.pick_method(method)
        except Exception as e:
            self.show_error(e)

    def set_vector_value(self):
        try:
            self.destroy_result()
            self.destroy_second_input()
            self.destroy_coeffs_input()
            vector_value = self.vector_input.get().strip()
            if len(vector_value) == 0 or re.search('\[[0-9,]+\]', vector_value) == None:
                raise Exception(msg.EMPTY_INPUT_OR_WRONG_FORMAT)
            vector_list = [int(i) for i in vector_value.replace(
                '[', '').replace(']', '').split(',')]
            self.vector = Vector(vector_list)
            self.has_input = True
            self.create_method_select()
        except Exception as e:
            self.show_error(e)

    def set_second_vector_value(self, method):
        try:
            vector_value = self.second_vector_input.get().strip()
            if len(vector_value) == 0 or re.search('\[[0-9,]+\]', vector_value) == None:
                raise Exception(msg.EMPTY_INPUT_OR_WRONG_FORMAT)
            vector_list = [int(i) for i in vector_value.replace(
                '[', '').replace(']', '').split(',')]
            self.vector_2 = Vector(vector_list)
            self.has_second_input = True
            self.pick_method(method)
        except Exception as e:
            self.show_error(e)

    def create_method_select(self):
        self.method_frame = tk.CTkFrame(self)
        self.method_frame.grid(row=3, column=0, pady=20)

        option_value = tk.StringVar(self.method_frame)

        method_label = tk.CTkLabel(
            self.method_frame, text="Method:")
        method_label.grid(row=0, column=0, padx=20)

        method_menu = tk.CTkOptionMenu(
            self.method_frame, variable=option_value, values=self.methods, command=self.pick_method)
        method_menu.grid(row=0, column=1)

    def pick_method(self, method=None):
        try:
            if method == None:
                self.destroy_result()
                self.destroy_second_input()
                self.destroy_coeffs_input()
                raise Exception(msg.METHOD_NOT_PICKED)
            result = None
            if self.has_result == True:
                self.result_frame.destroy()
            if self.has_second_input == True:
                self.set_second_vector_value_btn.configure(
                    command=partial(self.set_second_vector_value, method))
            if method == m.ADD:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector + self.vector_2
                else:
                    self.create_second_vector_input(method)
            if method == m.SUB:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector - self.vector_2
                else:
                    self.create_second_vector_input(method)
            if method == m.MUL:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector * self.vector_2
                else:
                    self.create_second_vector_input(method)
            if method == m.MAGNITUDE:
                self.destroy_second_input()
                self.destroy_coeffs_input()
                result = self.vector.magnitude()
            if method == m.DISTANCE:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.distance(self.vector_2)
                else:
                    self.create_second_vector_input(method)
            if method == m.DOT:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.dot(self.vector.v, self.vector_2.v)
                else:
                    self.create_second_vector_input(method)
            if method == m.CROSS:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.cross(self.vector_2)
                else:
                    self.create_second_vector_input(method)
            if method == m.NORMALIZE:
                self.destroy_coeffs_input()
                self.destroy_second_input()
                result = self.vector.normalize(self.vector.v)
            if method == m.LAGR:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.lagrange(
                        self.vector.v.tolist(), self.vector_2.v.tolist())
                else:
                    self.create_second_vector_input(method)
            if method == m.L_DEP:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.l_dependence(
                        [self.vector.v.tolist(), self.vector_2.v.tolist()])
                else:
                    self.create_second_vector_input(method)
            if method == m.L_COMB:
                if self.has_second_input == True:
                    if self.has_coeffs_input == True:
                        result = self.vector.l_combination(
                            [self.vector.v, self.vector_2.v], self.coeffs)
                    else:
                        self.create_coeffs_input(method)
                else:
                    self.create_second_vector_input(method)
            if method == m.L_REG:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.l_regression(
                        self.vector.v.tolist(), self.vector_2.v.tolist())
                else:
                    self.create_second_vector_input(method)
            if method == m.GS:
                self.destroy_coeffs_input()
                if self.has_second_input == True:
                    result = self.vector.gs(
                        [self.vector.v.tolist(), self.vector_2.v.tolist()])
                else:
                    self.create_second_vector_input(method)
            if result != None:
                self.show_result(result)
        except Exception as e:
            self.show_error(e)

    def test(self):
        try:
            vector = Vector([1, 2, 3])
            vector_2 = Vector([4, 5, 6])
            print(f'Vector_1: {vector}, Vector_2: {vector_2}')
            print('Basic operations')
            print(f'Add: {vector + vector_2}')
            print(f'Sub: {vector - vector_2}')
            print(f'Multiplication: {vector * vector_2}')
            print(f'Scalar multiplication: {vector * 2}')
            print(f'Distance: {vector.distance(vector_2)}')
            print(f'Magnitude (Vector_1): {vector.magnitude()}')
            print(f'Magnitude (Vector_2): {vector_2.magnitude()}')
            print(f'Dot product: {vector.dot(vector.v, vector_2.v)}')
            print(f'Cross product: {vector.cross(vector_2)}')
            print(f'Normalization (Vector_1): {vector.normalize(vector.v)}')
            print(
                f'Normalization (Vector_2): {vector_2.normalize(vector_2.v)}')
            print(
                f'Lagrange Interpolation (y point): {vector.lagrange(vector.v, vector_2.v)}')
            print(
                f'Linear Dependence: {vector.l_dependence([vector.v.tolist(), vector_2.v.tolist()])}')
            print(
                f'Linear Combination (coeffs: "1,2"): {vector.l_combination([vector.v, vector_2.v], [1,2])}')
            print(
                f'Linear Regression: {vector.l_regression(vector.v.tolist(), vector_2.v.tolist())}')
            print(
                f'Gram-Schmidt: {vector.gs([vector.v.tolist(), vector_2.v.tolist()])}')

        except Exception as e:
            self.show_error(e)


if __name__ == "__main__":
    app = Window()
    app.mainloop()
