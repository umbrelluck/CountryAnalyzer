"""
Main module with GUI
IMPORTANT: run main_gui from with_GUI folder
"""
import gdeltAPI
import tkinter as tk
from tkinter import ttk
from stabilityWriter import stability
from helper import tone_chart, timeline_source_country, negative_news_count
import webbrowser

themes = ['kill', 'protest', 'political_turmoil', 'black_market', 'jihad', 'ceasefire', 'blockade',
          'treason', 'self_identified_atrocity', 'vandalize', 'crime_cartels', 'tax_cartels',
          'crime_illegal_drugs', 'extremism', 'political_prisoner', 'propaganda', 'scandal',
          'crime_common_robbery', 'violent_unrest', ]

LARGE_FONT = ('Verdana', 10)


class Main(tk.Tk):
    """
    Container for program windows
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().wm_title('CountryAnalyzer')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # container - is where all the windows will be located,
        # controller - is the Main class
        self.frames, self.country_name = {}, ''
        for F in (StartPage, IncorrectLocationPage, ResultPage):
            frame = F(container, self)
            self.frames[F] = frame
            self.frames[F].grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, container):
        """
        Shows new window
        :param container: class of the window (StartPage, IncorrectLocationPAge, ResultPage)
        :return: None
        """
        self.frames[container].tkraise()

    def resize(self, x, y):
        """
        Resize the window for better outlook, NotImplemented
        :param x:
        :param y:
        :return:
        """
        pass


class StartPage(tk.Frame):
    """
    Start page with basic information
    """

    def __init__(self, parent, controller):
        super().__init__(parent)

        input_label = tk.Label(self, text='Please enter your full country name here\n(United '
                                          'States not USA or US)', font=LARGE_FONT)
        input_label.grid(padx=3, rowspan=2)
        country_name = tk.StringVar(self)
        entry = ttk.Entry(self, textvariable=country_name)
        entry.grid(row=0, column=1, padx=3)

        startButton = ttk.Button(self, text='Check stability',
                                 command=lambda: self.check_stability(country_name, parent,
                                                                      controller))
        startButton.grid(columnspan=2, pady=25)

    def check_stability(self, input_text, parent, controller):
        """
        Gets the country name and starts analyzing
        :param input_text: listbox_text object
        :param parent: for further use, not implemented right now
        :param controller: Main instance
        :return:
        """
        country = input_text.get()
        controller.country_name = country
        if gdeltAPI.is_validLocation(country.lower()):
            self.result(controller)
        else:
            controller.show_frame(IncorrectLocationPage)

    def result(self, controller):
        """
        Shows result window
        :param controller: Main class instance
        :return: None
        """
        controller.frames[ResultPage].change(controller, search(controller.country_name))
        controller.show_frame(ResultPage)


class IncorrectLocationPage(tk.Frame):
    """
    The page with warnings about the input
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        text = 'We were unable to find such location\nPlease make sure your input is correct.\n' \
               'If everything seems OK, hit \'Ignore this check\' and try again'
        label = tk.Label(self, text=text, padx=10, pady=10, font=LARGE_FONT)
        label.grid(columnspan=2)
        ignore_button = ttk.Button(self, text='Ignore check',
                                   command=lambda: self.result(controller))
        back_button = ttk.Button(self, text='Back',
                                 command=lambda: controller.show_frame(StartPage))
        ignore_button.grid(row=1, column=0, pady=5)
        back_button.grid(row=1, column=1, pady=5)

    def result(self, controller):
        """
        Shows result window
        :param controller: Main class instance
        :return: None
        """
        controller.frames[ResultPage].change(controller, search(controller.country_name))
        controller.show_frame(ResultPage)


class ResultPage(tk.Frame):
    """Page with results of analysis"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.country_label = tk.Label(self,
                                      text='Country name: ' + controller.country_name + '\n' +
                                           'Status: ')
        ans_label = tk.Label(self, text='Would you like to get more detailed information?')
        self.country_label.grid(columnspan=2, pady=5)
        ans_label.grid(row=1, columnspan=2, pady=5)

        no_button = tk.Button(self, text='No', command=lambda: controller.show_frame(StartPage))
        yes_button = tk.Button(self, text='Yes',
                               command=lambda: self.detailed_search(controller.country_name))
        no_button.grid(row=2, column=0)
        yes_button.grid(row=2, column=1)

        back_button = ttk.Button(self, text='Back',
                                 command=lambda: self.to_main(controller))
        back_button.grid(row=10, columnspan=2, pady=5)

    def to_main(self, controller):
        """
        Returns to start page
        :param controller: Main class instance
        :return: ТЩту
        """
        try:
            self.frame.destroy()
        except:
            pass
        controller.show_frame(StartPage)

    def change(self, controller, text):
        """
        Sets the general results
        :param controller: ResultPage instance
        :param text: str
        :return: None
        """
        self.country_label[
            'text'] = 'Country name: ' + controller.country_name + '\n' + 'Status: ' + text

    def detailed_search(self, country_name):
        """
        Creates widget with detailed search results
        :param country_name: str
        :return: None
        """
        self.frame = tk.Frame(self)
        self.frame.grid(row=3, columnspan=2, pady=25)
        url = 'https://api.gdeltproject.org/api/v2/doc/doc?query=\"' + country_name + \
              '\"&mode=ToneChart'
        button_emotion = ttk.Button(self.frame, text='View emotions',
                                    command=lambda: self.url_open(url))
        url1 = 'https://api.gdeltproject.org/api/v2/doc/doc?query=\"' + country_name + \
               '\"&mode=WordCloudImageTags'
        button_cloud = ttk.Button(self.frame, text='View words cloud',
                                  command=lambda: self.url_open(url1))
        button_emotion.grid()
        button_cloud.grid(row=0, column=1)

        label_count = tk.Label(self.frame, text='We were able to find following information:')
        label_count.grid(row=1, columnspan=2)

        # scrol = scrl.ScrolledText()
        # scrol.grid(row=5)
        a, b = negative_news_count_output()
        lst_all = tk.Listbox(self.frame, width=50)
        for elem in a:
            lst_all.insert(tk.END, 'There are ' + str(a[elem]) + ' topics on ' + elem + ' category')
        lst_all.grid(row=2, columnspan=2)
        label_news = tk.Label(self.frame, text='And here are the news:')
        label_news.grid(row=3, columnspan=2)
        lst_unique = tk.Listbox(self.frame, width=100)
        for elem in b:
            try:
                lst_unique.insert(tk.END, elem[0])
            except:
                pass
        lst_unique.grid(row=4, columnspan=2)
        btn = tk.Button(self.frame, text="Visit site",
                        command=lambda: self.visit_news(lst_unique, b))
        # lst_unique.bind("<Double-Button-1>", self.visit_news(lst_unique, b))
        btn.grid(row=5, columnspan=2)

    def visit_news(self, listbox, lst):
        """
        Enables visiting selected website
        :param listbox: tk.listbox
        :param lst: list
        :return: None
        """
        tmp = listbox.get(listbox.curselection())
        if type(tmp) == str:
            for elem in lst:
                if elem[0] == tmp:
                    webbrowser.open_new_tab(elem[1])
                    break

    def url_open(self, url):
        """
        Opens url in default`s browser new tab
        :param url: str
        :return: None
        """
        webbrowser.open_new_tab(url)


def negative_news_count_output():
    """
    Nice print of negative_news_count
    """
    return negative_news_count(topics=themes)


def search(location):
    """
    General stability analysis
    :param location:
    :return:
    """
    neg, neu, pos = tone_chart(location)
    # print(neg, neu, pos)
    base = stability["interest"]
    interest = timeline_source_country(base=(base, 0.1))
    # print(interest)
    if (interest or stability['mood'][0] - neg > 0.3) or stability['mood'][0] - neg > 0.3:
        return 'your country seems to be unstable.'
    else:
        if abs(stability['mood'][0] - neg) < 0.1:
            return 'your county is stable with rather positive feedback.'
        else:
            return 'your county is stable with rather negative feedback.'


if __name__ == "__main__":
    app = Main()
    app.mainloop()
    # # print(stability)
