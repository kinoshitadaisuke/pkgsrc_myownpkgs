# $NetBSD$

DISTNAME=	osmnx-2.0.7
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/osmnx/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/osmnx/
COMMENT=	Download and visualize geospatial data from OpenStreetMap
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-uv-build>=0.9.11:../../devel/py-uv-build
DEPENDS+=	${PYPKGPREFIX}-geopandas>=1.0.1:../../pkgsrc_myownpkgs/py-geopandas
DEPENDS+=	${PYPKGPREFIX}-networkx>=2.5:../../math/py-networkx
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.22:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pandas>=1.4:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-requests>=2.27:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-shapely>=2.0:../../pkgsrc_myownpkgs/py-shapely
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-rasterio>=0:../../pkgsrc_myownpkgs/py-rasterio
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
