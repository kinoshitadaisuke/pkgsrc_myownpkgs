# $NetBSD$

DISTNAME=	rioxarray-0.20.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=r/rioxarray/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/rioxarray/
COMMENT=	Geospatial xarray extension powered by rasterio
LICENSE=	apache-2.0

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-packaging>=0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-rasterio>=1.4.3:../../pkgsrc_myownpkgs/py-rasterio
DEPENDS+=	${PYPKGPREFIX}-xarray>=2024.7.0:../../math/py-xarray
DEPENDS+=	${PYPKGPREFIX}-proj>=3.3:../../geography/py-proj
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
