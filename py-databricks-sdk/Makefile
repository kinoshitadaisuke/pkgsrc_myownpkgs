# $NetBSD$

DISTNAME=	databricks_sdk-0.87.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=d/databricks_sdk/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/databricks_sdk/
COMMENT=	Databricks SDK for Python
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none
USE_TOOLS+=	gmake

# build dependencies
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
# dependencies
DEPENDS+=	${PYPKGPREFIX}-requests>=2.28.1:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-google-auth>=2.0:../../security/py-google-auth
DEPENDS+=	${PYPKGPREFIX}-protobuf>=4.25.8:../../devel/py-protobuf

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
