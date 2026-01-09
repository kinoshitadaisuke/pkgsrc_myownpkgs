# $NetBSD$

DISTNAME=	rasterio-1.5.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=r/rasterio/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/rasterio/
COMMENT=	Rasterio reads and writes geospatial raster data
LICENSE=	modified-bsd

USE_LANGUAGES+=	c
USE_LANGUAGES+=	c++

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-cython>=3.1.0:../../devel/py-cython
DEPENDS+=	${PYPKGPREFIX}-affine>=0:../../pkgsrc_myownpkgs/py-affine
DEPENDS+=	${PYPKGPREFIX}-attrs>=0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-boto3>=0:../../net/py-boto3
DEPENDS+=	${PYPKGPREFIX}-click>=8.0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-click-plugins>=0:../../devel/py-click-plugins
DEPENDS+=	${PYPKGPREFIX}-cligj>=0:../../pkgsrc_myownpkgs/py-cligj
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-numpy>0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pyparsing>=0:../../devel/py-pyparsing

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} rio rio-${PYVERSSUFFIX} || ${TRUE}

# url2pkg-marker (please do not remove this line.)
.include "../../devel/py-cython/buildlink3.mk"
.include "../../geography/gdal-lib/buildlink3.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
