# $NetBSD$

DISTNAME=	contextily-1.7.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=c/contextily/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/contextily/
COMMENT=	Python package to retrieve tile maps from the internet
LICENSE=	modified-bsd

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-mercantile>=0:../../pkgsrc_myownpkgs/py-mercantile
DEPENDS+=	${PYPKGPREFIX}-numpy>0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-Pillow>=0:../../graphics/py-Pillow
DEPENDS+=	${PYPKGPREFIX}-rasterio>=0:../../pkgsrc_myownpkgs/py-rasterio
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-geopy>=0:../../pkgsrc_myownpkgs/py-geopy
DEPENDS+=	${PYPKGPREFIX}-joblib>=0:../../devel/py-joblib
DEPENDS+=	${PYPKGPREFIX}-xyzservices>=0:../../pkgsrc_myownpkgs/py-xyzservices

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
