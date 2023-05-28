# $NetBSD$

DISTNAME=	sep-1.2.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sep/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/sep/
COMMENT=	Astronomical source extraction and photometry library
LICENSE=	gnu-lgpl-v3

USE_LANGUAGES+=	c c++

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
BUILD_DEPENDS+=	${PYPKGPREFIX}-cython>=0:../../devel/py-cython

DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy

# url2pkg-marker (please do not remove this line.)
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/extension.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
