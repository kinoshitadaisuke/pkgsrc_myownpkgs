# $NetBSD$

DISTNAME=	pygmt-0.17.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pygmt/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pygmt/
COMMENT=	Python interface for the Generic Mapping Tools
LICENSE=	modified-bsd

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=77:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=6.2:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-numpy>=2.0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pandas>=2.2:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-xarray>=2024.5:../../math/py-xarray
DEPENDS+=	${PYPKGPREFIX}-packaging>=0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-contextily>=0:../../pkgsrc_myownpkgs/py-contextily
DEPENDS+=	${PYPKGPREFIX}-geopandas>=0:../../pkgsrc_myownpkgs/py-geopandas
DEPENDS+=	${PYPKGPREFIX}-ipython>=0:../../devel/py-ipython
DEPENDS+=	${PYPKGPREFIX}-arrow>=0:../../time/py-arrow
DEPENDS+=	${PYPKGPREFIX}-rioxarray>=0:../../pkgsrc_myownpkgs/py-rioxarray

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
