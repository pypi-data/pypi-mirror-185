
import time
import logging
import numpy as np
from matplotlib.axes import Axes
from srsgui.task import Task

logger = logging.getLogger(__name__)


class TimePlot:
    def __init__(self, parent: Task, ax: Axes, plot_name='', data_names=('Y',), save_to_file=True):
        if not issubclass(type(parent), Task):
            raise TypeError('Invalid parent {} is not a Task subclass'.format(type(parent)))
        # if type(ax) is not Axes or AxesSubplot:
        #    raise TypeError('ax is not a Matplotlib Axes class, but "{}"'.format(type(ax)))

        self.type = self.__class__.__name__
        self.parent = parent
        self.ax = ax
        self.name = plot_name.strip()

        self.conversion_factor = 1
        self.unit = ''

        self.save_to_file = False
        if hasattr(self.parent, 'session_handler') and self.parent.session_handler:
            self.save_to_file = save_to_file
        else:
            logger.error('parent has no session_handler')

        self.data_keys = data_names


        self.data = {}
        self.lines = {}

        self.max_points_in_plot = 10000
        self._data_buffer_size = 1000000
        self.data_points = 0

        self.time = np.zeros(self._data_buffer_size)
        for key in self.data_keys:
            self.data[key] = np.zeros(self._data_buffer_size)
            self.lines[key], = self.ax.plot(self.time[:2], self.data[key][:2], label=key.split()[0])

        # significant digits in a number in text
        self.round_float_resolution = 4
        self.header_saved = False

        self.ax.set_title(self.name)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_xlim(0, 300)
        self.ax.legend()

        # Mark the time 0
        self.initial_time = time.time()

    def get_buffer_size(self):
        return self._data_buffer_size

    def set_buffer_size(self, size=10000000):
        self._data_buffer_size = size
        self.data_points = 0
        self.time = np.zeros(size)
        for key in self.data_keys:
            self.data[key] = np.zeros(size)

    def set_conversion_factor(self, factor=0.1, unit='fA'):
        old_factor = self.conversion_factor
        self.conversion_factor = factor
        self.unit = unit
        if self.parent:
            self.parent.add_details(' {:.4e} '.format(self.conversion_factor), 'Conversion factor')
            self.parent.add_details(' {} '.format(self.unit), 'Converted unit')

        factor_ratio = self.conversion_factor / old_factor
        bottom, top = self.ax.get_ylim()
        self.ax.set_ylim(bottom * factor_ratio, top * factor_ratio)
        self.ax.set_ylabel('Intensity ({})'.format(self.unit))

    def add_data(self, data_list=(0,), update_figure=False):
        self.time[self.data_points] = time.time() - self.initial_time
        for key, point in zip(self.data_keys, data_list):
            self.data[key][self.data_points] = point * self.conversion_factor
        self.data_points += 1

        x_min, x_max = self.ax.get_xlim()
        index_min = np.searchsorted(self.time[:self.data_points], x_min)
        index_max = np.searchsorted(self.time[:self.data_points], x_max)
        index_step = (index_max - index_min) // self.max_points_in_plot
        if index_step < 1:
            index_step = 1

        s = slice(index_min, index_max, index_step)
        for key in self.data_keys:
            self.lines[key].set_xdata(self.time[s])
            self.lines[key].set_ydata(self.data[key][s])
           
        if len(self.time) == 1:
            min_value = min(data_list)
            max_value = max(data_list)
            if min_value == 0 and max_value == 0:
                min_value = -1.0
                max_value = 1.0
            min_value *= self.conversion_factor
            max_value *= self.conversion_factor
            self.ax.set_ylim(min_value - abs(min_value)/2, max_value + abs(max_value)/2)
        if update_figure:
            self.parent.request_figure_update(self.ax.figure)
        self.save_data(data_list)

    def save_data(self, data_list):
        if not self.save_to_file:
            return
        if not self.header_saved:
            self.parent.session_handler.add_dict_to_file(self.name, self.get_plot_info())
            self.parent.create_table_in_file(self.name, 'Elapsed time', *self.data_keys)
            self.header_saved = True
        # write the spectrum in to the data file
        elapsed_time = self.round_float(time.time() - self.initial_time)
        # timestamp = datetime.now().strftime('%H:%M:%S')
        self.parent.add_to_table_in_file(self.name, elapsed_time, *map(self.round_float, data_list))

    def round_float(self, number):
        # set the resolution of the number with self.round_float_resolution
        fmt = '{{:.{}e}}'.format(self.round_float_resolution)
        return float(fmt.format(number))

    def get_plot_info(self):
        return {
            'type': self.type,
            'xunit': 's',
            'yunit': self.unit,
            'axes_title': self.ax.get_title(),
            'axes_xlabel': self.ax.get_xlabel(),
            'axes_ylabel': self.ax.get_ylabel(),
            'axes_xlim': self.ax.get_xlim(),
            'axes_ylim': self.ax.get_ylim(),
            'axes_xsclae': self.ax.get_xscale(),
            'axes_yscale': self.ax.get_yscale(),
        }

    def cleanup(self):
        pass
