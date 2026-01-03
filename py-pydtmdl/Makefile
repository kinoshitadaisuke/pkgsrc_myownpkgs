# $NetBSD$

DISTNAME=	pydtmdl-0.0.9
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pydtmdl/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pydtmdl/
COMMENT=	Python library to download DTM data from various providers
LICENSE=	gnu-gpl-v3

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=42:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-rasterio>=0:../../pkgsrc_myownpkgs/py-rasterio
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-pydantic>=0:../../devel/py-pydantic
DEPENDS+=	${PYPKGPREFIX}-tqdm>=0:../../misc/py-tqdm
DEPENDS+=	${PYPKGPREFIX}-osmnx>=0:../../pkgsrc_myownpkgs/py-osmnx
DEPENDS+=	${PYPKGPREFIX}-owslib>=0:../../geography/py-owslib

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
