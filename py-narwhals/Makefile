# $NetBSD$

DISTNAME=	narwhals-2.16.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=n/narwhals/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/narwhals/
COMMENT=	Lightweight compatibility layer between dataframe libraries
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 37 38

BUILD_DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=61:../../devel/py-setuptools

DEPENDS+=	${PYPKGPREFIX}-pandas>=1.1.3:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-modin>=0:../../pkgsrc_myownpkgs/py-modin
DEPENDS+=	${PYPKGPREFIX}-apache-arrow>=13.0.0:../../pkgsrc_myownpkgs/py-apache-arrow
DEPENDS+=	${PYPKGPREFIX}-pyspark>=3.5.0:../../pkgsrc_myownpkgs/py-pyspark
DEPENDS+=	${PYPKGPREFIX}-pyspark-connect>=3.5.0:../../pkgsrc_myownpkgs/py-pyspark-connect
DEPENDS+=	${PYPKGPREFIX}-duckdb>=1.1:../../databases/py-duckdb


.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
