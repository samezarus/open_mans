from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QSlider,
    QTabWidget,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QCheckBox,
    QTextEdit,
    QToolButton,
    QFileDialog,
)

from PyQt5.QtGui import QPixmap, QDesktopServices
from PyQt5.QtCore import QSize, QThreadPool, Qt, QUrl

from PIL.ImageQt import ImageQt
from constants import (
    LCM_DEFAULT_MODEL,
    LCM_DEFAULT_MODEL_OPENVINO,
    APP_NAME,
    APP_VERSION,
)
from frontend.gui.image_generator_worker import ImageGeneratorWorker
from app_settings import AppSettings
from paths import FastStableDiffusionPaths
from frontend.utils import is_reshape_required
from context import Context
from models.interface_types import InterfaceType
from constants import DEVICE
from frontend.utils import enable_openvino_controls


class MainWindow(QMainWindow):
    def __init__(self, config: AppSettings):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setFixedSize(QSize(600, 620))
        self.init_ui()
        self.pipeline = None
        self.threadpool = QThreadPool()
        self.config = config
        self.device = "cpu"
        self.previous_width = 0
        self.previous_height = 0
        self.previous_model = ""
        self.previous_num_of_images = 0
        self.context = Context(InterfaceType.GUI)
        self.init_ui_values()
        self.gen_images = []
        self.image_index = 0
        print(f"Output path : {  self.config.settings.results_path}")

    def init_ui_values(self):
        self.lcm_model.setEnabled(
            not self.config.settings.lcm_diffusion_setting.use_openvino
        )
        self.guidance.setValue(
            int(self.config.settings.lcm_diffusion_setting.guidance_scale * 10)
        )
        self.seed_value.setEnabled(self.config.settings.lcm_diffusion_setting.use_seed)
        self.safety_checker.setChecked(
            self.config.settings.lcm_diffusion_setting.use_safety_checker
        )
        self.use_openvino_check.setChecked(
            self.config.settings.lcm_diffusion_setting.use_openvino
        )
        self.width.setCurrentText(
            str(self.config.settings.lcm_diffusion_setting.image_width)
        )
        self.height.setCurrentText(
            str(self.config.settings.lcm_diffusion_setting.image_height)
        )
        self.inference_steps.setValue(
            int(self.config.settings.lcm_diffusion_setting.inference_steps)
        )
        self.seed_check.setChecked(self.config.settings.lcm_diffusion_setting.use_seed)
        self.seed_value.setText(str(self.config.settings.lcm_diffusion_setting.seed))
        self.use_local_model_folder.setChecked(
            self.config.settings.lcm_diffusion_setting.use_offline_model
        )
        self.results_path.setText(self.config.settings.results_path)
        self.num_images.setValue(
            self.config.settings.lcm_diffusion_setting.number_of_images
        )

    def init_ui(self):
        self.create_main_tab()
        self.create_settings_tab()
        self.create_about_tab()
        self.show()

    def create_main_tab(self):
        self.img = QLabel("<<Image>>")
        self.img.setAlignment(Qt.AlignCenter)
        self.img.setFixedSize(QSize(512, 512))

        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText("A fantasy landscape")
        self.prompt.setAcceptRichText(False)
        self.generate = QPushButton("Generate")
        self.generate.clicked.connect(self.text_to_image)
        self.prompt.setFixedHeight(35)
        self.browse_results = QPushButton("...")
        self.browse_results.setFixedWidth(30)
        self.browse_results.clicked.connect(self.on_open_results_folder)
        self.browse_results.setToolTip("Open output folder")

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.prompt)
        hlayout.addWidget(self.generate)
        hlayout.addWidget(self.browse_results)

        self.previous_img_btn = QToolButton()
        self.previous_img_btn.setText("<")
        self.previous_img_btn.clicked.connect(self.on_show_previous_image)
        self.next_img_btn = QToolButton()
        self.next_img_btn.setText(">")
        self.next_img_btn.clicked.connect(self.on_show_next_image)
        hlayout_nav = QHBoxLayout()
        hlayout_nav.addWidget(self.previous_img_btn)
        hlayout_nav.addWidget(self.img)
        hlayout_nav.addWidget(self.next_img_btn)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout_nav)
        vlayout.addLayout(hlayout)

        self.tab_widget = QTabWidget(self)
        self.tab_main = QWidget()
        self.tab_settings = QWidget()
        self.tab_about = QWidget()
        self.tab_main.setLayout(vlayout)

        self.tab_widget.addTab(self.tab_main, "Text to Image")
        self.tab_widget.addTab(self.tab_settings, "Settings")
        self.tab_widget.addTab(self.tab_about, "About")

        self.setCentralWidget(self.tab_widget)
        self.use_seed = False

    def create_settings_tab(self):
        model_hlayout = QHBoxLayout()
        self.lcm_model_label = QLabel("Latent Consistency Model:")
        self.lcm_model = QLineEdit(LCM_DEFAULT_MODEL)
        model_hlayout.addWidget(self.lcm_model_label)
        model_hlayout.addWidget(self.lcm_model)

        self.inference_steps_value = QLabel("Number of inference steps: 4")
        self.inference_steps = QSlider(orientation=Qt.Orientation.Horizontal)
        self.inference_steps.setMaximum(25)
        self.inference_steps.setMinimum(1)
        self.inference_steps.setValue(4)
        self.inference_steps.valueChanged.connect(self.update_steps_label)

        self.num_images_value = QLabel("Number of images: 1")
        self.num_images = QSlider(orientation=Qt.Orientation.Horizontal)
        self.num_images.setMaximum(100)
        self.num_images.setMinimum(1)
        self.num_images.setValue(1)
        self.num_images.valueChanged.connect(self.update_num_images_label)

        self.guidance_value = QLabel("Guidance scale: 8")
        self.guidance = QSlider(orientation=Qt.Orientation.Horizontal)
        self.guidance.setMaximum(200)
        self.guidance.setMinimum(10)
        self.guidance.setValue(80)
        self.guidance.valueChanged.connect(self.update_guidance_label)

        self.width_value = QLabel("Width :")
        self.width = QComboBox(self)
        self.width.addItem("256")
        self.width.addItem("512")
        self.width.addItem("768")
        self.width.setCurrentText("512")
        self.width.currentIndexChanged.connect(self.on_width_changed)

        self.height_value = QLabel("Height :")
        self.height = QComboBox(self)
        self.height.addItem("256")
        self.height.addItem("512")
        self.height.addItem("768")
        self.height.setCurrentText("512")
        self.height.currentIndexChanged.connect(self.on_height_changed)

        self.seed_check = QCheckBox("Use seed")
        self.seed_value = QLineEdit()
        self.seed_value.setInputMask("9999999999")
        self.seed_value.setText("123123")
        self.seed_check.stateChanged.connect(self.seed_changed)

        self.safety_checker = QCheckBox("Use safety checker")
        self.safety_checker.setChecked(True)
        self.safety_checker.stateChanged.connect(self.use_safety_checker_changed)

        self.use_openvino_check = QCheckBox("Use OpenVINO")
        self.use_openvino_check.setChecked(False)
        self.use_local_model_folder = QCheckBox(
            "Use locally cached model or downloaded model folder(offline)"
        )
        self.use_openvino_check.setEnabled(enable_openvino_controls())
        self.use_local_model_folder.setChecked(False)
        self.use_local_model_folder.stateChanged.connect(self.use_offline_model_changed)
        self.use_openvino_check.stateChanged.connect(self.use_openvino_changed)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.seed_check)
        hlayout.addWidget(self.seed_value)
        hspacer = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        slider_hspacer = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.results_path_label = QLabel("Output path:")
        self.results_path = QLineEdit()
        self.results_path.textChanged.connect(self.on_path_changed)
        self.browse_folder_btn = QToolButton()
        self.browse_folder_btn.setText("...")
        self.browse_folder_btn.clicked.connect(self.on_browse_folder)

        self.reset = QPushButton("Reset All")
        self.reset.clicked.connect(self.reset_all_settings)

        vlayout = QVBoxLayout()
        vspacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vlayout.addItem(hspacer)
        vlayout.addLayout(model_hlayout)
        vlayout.addWidget(self.use_local_model_folder)
        vlayout.addItem(slider_hspacer)
        vlayout.addWidget(self.inference_steps_value)
        vlayout.addWidget(self.inference_steps)
        vlayout.addWidget(self.num_images_value)
        vlayout.addWidget(self.num_images)
        vlayout.addWidget(self.width_value)
        vlayout.addWidget(self.width)
        vlayout.addWidget(self.height_value)
        vlayout.addWidget(self.height)
        vlayout.addWidget(self.guidance_value)
        vlayout.addWidget(self.guidance)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.safety_checker)
        vlayout.addWidget(self.use_openvino_check)
        vlayout.addWidget(self.results_path_label)
        hlayout_path = QHBoxLayout()
        hlayout_path.addWidget(self.results_path)
        hlayout_path.addWidget(self.browse_folder_btn)
        vlayout.addLayout(hlayout_path)
        self.tab_settings.setLayout(vlayout)
        hlayout_reset = QHBoxLayout()
        hspacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hlayout_reset.addItem(hspacer)
        hlayout_reset.addWidget(self.reset)
        vlayout.addLayout(hlayout_reset)
        vlayout.addItem(vspacer)

    def create_about_tab(self):
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(
            f"""<h1>FastSD CPU {APP_VERSION}</h1> 
               <h3>(c)2023 - Rupesh Sreeraman</h3>
                <h3>Faster stable diffusion on CPU</h3>
                 <h3>Based on Latent Consistency Models</h3>
                <h3>GitHub : https://github.com/rupeshs/fastsdcpu/</h3>"""
        )

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.label)
        self.tab_about.setLayout(vlayout)

    def on_show_next_image(self):
        if self.image_index != len(self.gen_images) - 1 and len(self.gen_images) > 0:
            self.previous_img_btn.setEnabled(True)
            self.image_index += 1
            self.img.setPixmap(self.gen_images[self.image_index])
            if self.image_index == len(self.gen_images) - 1:
                self.next_img_btn.setEnabled(False)

    def on_open_results_folder(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.config.settings.results_path))

    def on_show_previous_image(self):
        if self.image_index != 0:
            self.next_img_btn.setEnabled(True)
            self.image_index -= 1
            self.img.setPixmap(self.gen_images[self.image_index])
            if self.image_index == 0:
                self.previous_img_btn.setEnabled(False)

    def on_path_changed(self, text):
        self.config.settings.results_path = text

    def on_browse_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        folder_path = QFileDialog.getExistingDirectory(
            self, "Select a Folder", "", options=options
        )

        if folder_path:
            self.config.settings.results_path = folder_path
            self.results_path.setText(folder_path)

    def on_width_changed(self, index):
        width_txt = self.width.itemText(index)
        self.config.settings.lcm_diffusion_setting.image_width = int(width_txt)

    def on_height_changed(self, index):
        height_txt = self.height.itemText(index)
        self.config.settings.lcm_diffusion_setting.image_height = int(height_txt)

    def use_openvino_changed(self, state):
        if state == 2:
            self.lcm_model.setEnabled(False)
            self.config.settings.lcm_diffusion_setting.use_openvino = True
        else:
            self.config.settings.lcm_diffusion_setting.use_openvino = False

    def use_offline_model_changed(self, state):
        if state == 2:
            self.config.settings.lcm_diffusion_setting.use_offline_model = True
        else:
            self.config.settings.lcm_diffusion_setting.use_offline_model = False

    def use_safety_checker_changed(self, state):
        if state == 2:
            self.config.settings.lcm_diffusion_setting.use_safety_checker = True
        else:
            self.config.settings.lcm_diffusion_setting.use_safety_checker = False

    def update_steps_label(self, value):
        self.inference_steps_value.setText(f"Number of inference steps: {value}")
        self.config.settings.lcm_diffusion_setting.inference_steps = value

    def update_num_images_label(self, value):
        self.num_images_value.setText(f"Number of images: {value}")
        self.config.settings.lcm_diffusion_setting.number_of_images = value

    def update_guidance_label(self, value):
        val = round(int(value) / 10, 1)
        self.guidance_value.setText(f"Guidance scale: {val}")
        self.config.settings.lcm_diffusion_setting.guidance_scale = val

    def seed_changed(self, state):
        if state == 2:
            self.seed_value.setEnabled(True)
            self.config.settings.lcm_diffusion_setting.use_seed = True
        else:
            self.seed_value.setEnabled(False)
            self.config.settings.lcm_diffusion_setting.use_seed = False

    def get_seed_value(self) -> int:
        use_seed = self.config.settings.lcm_diffusion_setting.use_seed
        seed_value = int(self.seed_value.text()) if use_seed else -1
        return seed_value

    def generate_image(self):
        self.config.settings.lcm_diffusion_setting.seed = self.get_seed_value()
        self.config.settings.lcm_diffusion_setting.prompt = self.prompt.toPlainText()

        if self.config.settings.lcm_diffusion_setting.use_openvino:
            model_id = LCM_DEFAULT_MODEL_OPENVINO
        else:
            model_id = self.lcm_model.text()

        self.config.settings.lcm_diffusion_setting.lcm_model_id = model_id

        reshape_required = False
        if self.config.settings.lcm_diffusion_setting.use_openvino:
            # Detect dimension change
            reshape_required = is_reshape_required(
                self.previous_width,
                self.config.settings.lcm_diffusion_setting.image_width,
                self.previous_height,
                self.config.settings.lcm_diffusion_setting.image_height,
                self.previous_model,
                model_id,
                self.previous_num_of_images,
                self.config.settings.lcm_diffusion_setting.number_of_images,
            )

        images = self.context.generate_text_to_image(
            self.config.settings,
            reshape_required,
            DEVICE,
        )
        self.image_index = 0
        self.gen_images = []
        for img in images:
            im = ImageQt(img).copy()
            pixmap = QPixmap.fromImage(im)
            self.gen_images.append(pixmap)

        if len(self.gen_images) > 1:
            self.next_img_btn.setEnabled(True)
            self.previous_img_btn.setEnabled(False)
        else:
            self.next_img_btn.setEnabled(False)
            self.previous_img_btn.setEnabled(False)

        self.img.setPixmap(self.gen_images[0])

        self.previous_width = self.config.settings.lcm_diffusion_setting.image_width
        self.previous_height = self.config.settings.lcm_diffusion_setting.image_height
        self.previous_model = model_id
        self.previous_num_of_images = (
            self.config.settings.lcm_diffusion_setting.number_of_images
        )

    def text_to_image(self):
        self.img.setText("Please wait...")
        worker = ImageGeneratorWorker(self.generate_image)
        self.threadpool.start(worker)

    def closeEvent(self, event):
        self.config.settings.lcm_diffusion_setting.seed = self.get_seed_value()
        print(self.config.settings.lcm_diffusion_setting)
        print("Saving settings")
        self.config.save()

    def reset_all_settings(self):
        self.use_local_model_folder.setChecked(False)
        self.width.setCurrentText("512")
        self.height.setCurrentText("512")
        self.inference_steps.setValue(4)
        self.guidance.setValue(80)
        self.use_openvino_check.setChecked(False)
        self.seed_check.setChecked(False)
        self.safety_checker.setChecked(True)
        self.results_path.setText(FastStableDiffusionPaths().get_results_path())
