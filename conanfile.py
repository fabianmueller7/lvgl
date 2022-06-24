from conans ConanFile
from conan.tools.cmake import CMakeToolchian, CMake
from conan.tools.layout import cmake_layout

class LVGLConan(ConanFile):
    name = "lvgl"
    version = "0.1"

    #Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True,False], "fPIC": [True,False]}
    default_options = {"shared": False, "fPIC": True}

    #Sources are located in the sam place as this recipe, copy them to the recipe
    exports_sourcs = "CMakeLists.txt", "src/*"

    def config_options(self):
        if self.setting.os == "Windows"
            del self.options.fPIC
    
    def layout(self):
            cmake_layout(self)

    def generate(self)
        tc = CMakeToolchian(self)
        tc.generate() # creates conan_toolchain.cmake

    def build(self):
        cmake = CMake(self)
        cmake.configure() # same as cmake .
        cmake.build() # same as cmake --build

    def package(self):
        cmake = CMake(self)
        cmake.install() # same as cmake --install .

    def package_info(self):
        self.cpp_info.libs = ["lvgl"]

