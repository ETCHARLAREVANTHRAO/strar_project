import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np


global val1
global val2
global val3
global val4
global bar_graph
global pie_graph
global line2


class Pedictor:

    def create_graphs(self):
        val1, val2 = [i for i in entry1.get().split(" ")]
        val3 = [i for i in entry2.get().split(" ")]
        val4 = [int(i) for i in entry3.get().split(" ")]

        data1 = {val1 : val3, val2: val4}
        df1 = DataFrame(data1, columns=[val1, val2])
        df2 = DataFrame(data1, columns=[val1, val2])
        #print(val1, val2, val3)
        #print(data1)
        #print(df1)

        figure1 = plt.Figure(figsize=(4, 3), dpi=100)
        axis = figure1.add_subplot(111)
        axis.set_title(val1 +" vs "+ val2)
        self.bar_graph  = FigureCanvasTkAgg(figure1, window)
        self.bar_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[[val1, val2]].groupby(val1).sum()
        df1.plot(kind='bar', legend=True, ax=axis)

        figure2 = plt.Figure(figsize=(4, 3), dpi=100)
        axis = figure2.add_subplot(111)
        axis.set_title(val1 + " vs " + val2)
        self.line2 = FigureCanvasTkAgg(figure2, window)
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[[val1, val2]].groupby(val1).sum()
        df2.plot(kind='line', legend=True, ax=axis)

        figure3 = plt.Figure(figsize=(4, 3), dpi=100)
        axis3 = figure3.add_subplot(111)
        axis3.pie(val4,labels= val3,shadow=True)
        self.pie_graph = FigureCanvasTkAgg(figure3, window)
        self.pie_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        axis3.legend(val2)
        axis3.set_xlabel(val1)
        axis3.set_title(val1 + " vs "+ val2)

    def clear_graph(self):
        self.bar_graph.get_tk_widget().pack_forget()
        self.line2.get_tk_widget().pack_forget()
        self.pie_graph.get_tk_widget().pack_forget()

    def predict_graph(self):
        val1, val2 = [i for i in entry1.get().split(" ")]
        val3 = [int(i) for i in entry2.get().split(" ")]
        val4 = [int(i) for i in entry3.get().split(" ")]
        val5 = [int(i) for i in entry4.get().split(" ")]
        X = np.array(val3).reshape((-1, 1))
        y = np.array(val4)

        model = LinearRegression()
        model.fit(X, y)
        future_arr1 = np.array(val5).reshape((-1,1))
        future_arr2 = model.predict(future_arr1)

        result_label.config(text="Predicted future are: " + str(future_arr2))
        plt.scatter(X, y)
        plt.plot(X, model.predict(X), color='red')
        plt.title('Linear Regression')
        plt.xlabel("Array1")
        plt.ylabel('Aray2')
        plt.show()


if __name__ == '__main__':
    window = tk.Tk()
    obj = Pedictor()
    canvas1 = tk.Canvas(window, width=800, height=300, bg="white")
    canvas1.pack()
    label1 = tk.Label(window, text='S.T.A.R.K Graph Predector')
    label1.config(font=('Times', 18))
    canvas1.create_window(400, 50, window=label1)

    label2 = tk.Label(window, text='Graph Name')
    label2.config(font=('Times', 14))
    canvas1.create_window(200, 100, window=label2)

    entry1 = tk.Entry(window)
    canvas1.create_window(400, 100, window=entry1)

    label2 = tk.Label(window, text='X-axis')
    label2.config(font=('Times', 14))
    canvas1.create_window(200, 120, window=label2)

    entry2 = tk.Entry(window)
    canvas1.create_window(400, 120, window=entry2)

    label2 = tk.Label(window, text='Y-axis')
    label2.config(font=('Times', 14))
    canvas1.create_window(200, 140, window=label2)

    entry3 = tk.Entry(window)
    canvas1.create_window(400, 140, window=entry3)

    label3 = tk.Label(window, text= "Future values")
    label3.config(font=('Times', 14))
    canvas1.create_window(200, 160, window= label3)

    entry4 = tk.Entry(window)
    canvas1.create_window(400, 160, window=entry4)



    button1 = tk.Button(window, text='Show Graph', bg='green',command=obj.create_graphs,font=('Times', 10, 'bold'))
    canvas1.create_window(100, 200, window=button1)

    button2 = tk.Button(window, text='Predict Graph', bg='green', command=obj.predict_graph, font=('Times', 10, 'bold'))
    canvas1.create_window(300, 200, window=button2)

    button3 = tk.Button(window, text='Clear Graph', bg='green',command=obj.clear_graph, font=('Times', 10, 'bold'))
    canvas1.create_window(500, 200, window=button3)

    button4 = tk.Button(window, text='Exit GUI', bg='green', command=window.destroy, font=('Times', 10, 'bold'))
    canvas1.create_window(700, 200, window=button4)

    result_label =tk.Label(window, text="")
    result_label.pack()

    window.mainloop()



'''data1 = {val1: val3, val2: val4}
        df1 = DataFrame(data1, columns=[val1, val2])
        Y_train = df1[val2]
        X_train = df1[val1]
        X_train = sm.add_constant(X_train)
        model = sm.OLS(Y_train, X_train)
        results = model.fit()

        future_pred= range(5, 10, 50)
        X_pred = pd.DataFrame(data = future_pred,columns=val3)
        X_pred = sm.add_constant(X_pred)
        prediction = model.predict(results.params, X_pred)

        plt.figure()
        plt.plot(X_train[val2], model.predict(results.params), '-r', label= 'Linear Model')
        plt.plot(X_pred[val2], prediction, '--r', label = 'Linear Prediction')
        plt.scatter(df1[val2], df1[val1], label= 'data')
        plt.xlabel(val2)
        plt.ylabel(val1)
        plt.legend()
        plt.show()'''