# $NetBSD$

DISTNAME=	astroscrappy-1.2.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/astroscrappy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/astroscrappy/
COMMENT=	Speedy Cosmic Ray Annihilation Package in Python
LICENSE=	modified-bsd

USE_LANGUAGES+=	c c++

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
BUILD_DEPENDS+=	${PYPKGPREFIX}-extension-helpers>=0:../../devel/py-extension-helpers
BUILD_DEPENDS+=	${PYPKGPREFIX}-cython>=0.29.21:../../devel/py-cython

DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-astropy>=0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-sphinx-astropy>=0:../../textproc/py-sphinx-astropy

TEST_DEPENDS+	${PYPKGPREFIX}-test-astropy>=0:../../pkgsrc_myownpkgs/py-test-astropy
TEST_DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy

# url2pkg-marker (please do not remove this line.)
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
