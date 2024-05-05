# $NetBSD$

DISTNAME=	blosc2-2.6.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_PYPI:=b/blosc2/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/blosc2/
COMMENT=	Python wrapper for the C-Blosc2 library
LICENSE=	modified-bsd

USE_LANGUAGES+=	c
USE_LANGUAGES+=	c++

DEPENDS+=	cmake>=0:../../devel/cmake
DEPENDS+=	ninja-build>=0:../../devel/ninja-build
DEPENDS+=	${PYPKGPREFIX}-cython>=3:../../devel/py-cython
DEPENDS+=	${PYPKGPREFIX}-msgpack>=0:../../devel/py-msgpack
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-scikit-build>=0:../../devel/py-scikit-build
DEPENDS+=	${PYPKGPREFIX}-numexpr>=0:../../math/py-numexpr
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-cpuinfo>=0:../../sysutils/py-cpuinfo
DEPENDS+=	${PYPKGPREFIX}-ndindex>=0:../../pkgsrc_myownpkgs/py-ndindex

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
