# $NetBSD$

DISTNAME=	odrpack-0.2.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/odrpack/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/odrpack/
COMMENT=	Package for weighted orthogonal distance regression (ODR)
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_TOOLS+=	pkg-config
USE_LANGUAGES=	c c++ fortran

PKGCONFIG_OVERRIDE+=	extern/pybind11/tools/pybind11.pc.in

PYTHON_VERSIONS_INCOMPATIBLE=	27 37 38 39

DEPENDS+=	${PYPKGPREFIX}-numpy>=1.24:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=1.10:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-meson_python>=0.18.0:../../devel/py-meson_python
DEPENDS+=	${PYPKGPREFIX}-nanobind>=2.8.0:../../pkgsrc_myownpkgs/py-nanobind

TEST_DEPENDS+=	${PYPKGPREFIX}-test>=8.4.1:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-cov>=6.2.1:../../devel/py-test-cov

.include "../../devel/py-pybind11/buildlink3.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../devel/meson/build.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
