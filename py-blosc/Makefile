# $NetBSD$

DISTNAME=	blosc-1.11.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=b/blosc/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/blosc/
COMMENT=	Python wrapper for the extremely fast Blosc compression library
LICENSE=	modified-bsd

USE_LANGUAGES+=	c
USE_LANGUAGES+=	c++

USE_TOOLS+=	cmake
USE_TOOLS+=	ninja

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-scikit-build>=0.11.1:../../devel/py-scikit-build
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
DEPENDS+=	cmake>=3.14.0:../../devel/cmake
DEPENDS+=	ninja-build>=0:../../devel/ninja-build
DEPENDS+=	${PYPKGPREFIX}-cpuinfo>=9.0.0:../../sysutils/py-cpuinfo
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.16:../../math/py-numpy

MAKE_ENV+=USE_SYSTEM_BLOSC=1
MAKE_ENV+=Blosc_ROOT=${BUILDLINK_PREFIX.blosc}
PYSETUPARGS+=	-DCMAKE_SKIP_RPATH:BOOL=YES

# url2pkg-marker (please do not remove this line.)
.include "../../devel/blosc/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../math/py-numpy/buildlink3.mk"
#.include "../../devel/cmake/build.mk"
.include "../../mk/bsd.pkg.mk"
