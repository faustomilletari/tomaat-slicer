import qt, ctk, slicer
import os
import uuid
import tempfile

def decorator(layout):
   pass

def collapsible_button(name):
    coll = ctk.ctkCollapsibleButton()
    coll.text = name
    return coll


def add_image(path):
    logo_label = qt.QLabel()
    logo_label.setAlignment(4)
    logo_pixmap = \
        qt.QPixmap(os.path.join(os.path.split(os.path.realpath(__file__))[0], path))
    logo_label.setPixmap(logo_pixmap)

    return logo_label, logo_pixmap


def add_textbox(default_text, select_function=None):
    text_box = qt.QLineEdit()
    text_box.text = default_text

    if select_function is not None:
        text_box.connect('textChanged(const QString &)', select_function)

    return text_box


def add_button(text, tooltip_text='', click_function=None, enabled=True):
    button = qt.QPushButton(text)
    button.toolTip = tooltip_text
    button.enabled = enabled
    button.connect('clicked(bool)', click_function)

    return button


def add_label(text):
    label = qt.QLabel()
    label.setText(text)

    return label


def volume_widget():
    input_selector = slicer.qMRMLNodeComboBox()


    return input_selector

class ScalarVolumeWidget(slicer.qMRMLNodeComboBox):
    def __init__(self, destination):
        super(ScalarVolumeWidget, self).__init__()

        self.destination = destination

        self.type = 'ScalarVolumeWidget'

        self.nodeTypes = ['vtkMRMLScalarVolumeNode']
        self.selectNodeUponCreation = True
        self.addEnabled = False
        self.removeEnabled = False
        self.noneEnabled = False
        self.showHidden = False
        self.showChildNodeTypes = False
        self.setMRMLScene(slicer.mrmlScene)
        self.setToolTip('Pick volume')


class SliderWidget(ctk.ctkSliderWidget):
    def __init__(self, minimum, maximum, destination):
        super(SliderWidget, self).__init__()

        self.minimum = minimum
        self.maximum = maximum
        self.destination = destination

        self.type = 'SliderWidget'

        self.value = float(maximum - minimum) / float(2)
        self.setToolTip('Set value')



