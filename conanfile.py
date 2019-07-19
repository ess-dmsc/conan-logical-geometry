from conans import ConanFile


class LogicalgeometryConan(ConanFile):
    name = "logical-geometry"
    version = "705ea61"
    license = "BSD 2-Clause"
    url = "https://github.com/ess-dmsc/conan-logical-geometry"
    description = "Classes for mapping pixelid <-> (x,y,z,p)"

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/logical-geometry.git")
        self.run("cd logical-geometry && git checkout 705ea61f4c613b441b4c6432afa4c5fb6a60487b")

    def package(self):
        self.copy("ESSGeometry.h", dst="include/logical_geometry", src="logical-geometry/source")
