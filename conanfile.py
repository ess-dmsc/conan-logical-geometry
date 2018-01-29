from conans import ConanFile


class LogicalgeometryConan(ConanFile):
    name = "logical-geometry"
    version = "09097f2"
    license = "BSD 2-Clause"
    url = "https://github.com/ess-dmsc/conan-logical-geometry"
    description = "Classes for mapping pixelid <-> (x,y,z,p)"

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/logical-geometry.git")
        self.run("cd logical-geometry && git checkout 09097f2bbb8b9adcd216d1048907535d80d9d478")

    def package(self):
        self.copy("ESSGeometry.h", dst="include", src="logical-geometry/cpp/src")
